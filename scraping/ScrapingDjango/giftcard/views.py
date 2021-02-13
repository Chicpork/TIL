from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Giftcard, CrawlerProcess
from multiprocessing import Process
import giftcard.giftcard_crawler as giftcard_crawler
import json
import psutil
import os
import logging

# make logger
# with open("logging.json", "r") as f:
#     config = json.load(f)

# logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

# Create your views here.
class giftCardView(View):
    template_name = 'giftcard_list.html'

    def get(self, request, *args, **kwargs):
        giftcards = Giftcard.objects.filter(date=timezone.localtime().strftime('%Y%m%d')).order_by('price')
        return render(request, 'giftcard_list.html', {'giftcards' : giftcards})

    def post(self, request, *args, **kwargs):
        if request.META['CONTENT_TYPE'] == "application/json":
            data = json.loads(request.body)
            keyword = data['keyword']
            min_price = data['min_price']
            max_price = data['max_price']
        else:
            keyword = request.POST.get('keyword')
            min_price = request.POST.get('min_price')
            max_price = request.POST.get('max_price')
        
        if keyword is None or min_price is None or max_price is None:
            return HttpResponse(status=400)
        
        crawler_process_infos = CrawlerProcess.objects.filter(server_pid=os.getpid(), is_run=True, args=(keyword, min_price, max_price))

        is_run = False
        if crawler_process_infos is not None and len(crawler_process_infos) > 0:
            for crawler_process_info in crawler_process_infos:
                if psutil.pid_exists(crawler_process_info.crawler_pid): # crawler pid가 존재하는지
                    crawler_process = psutil.Process(crawler_process_info.crawler_pid)
                    if crawler_process.name().find("python") >= 0: # crawler pid가 python 이름을 가지는지
                        if crawler_process.ppid() == os.getpid():
                            # Already running scraping process
                            is_run = True
                            logger.info(crawler_process.connections())
                            logger.info(crawler_process.cmdline())
                            logger.info(crawler_process.name())
            
        if is_run == False:
            processes = CrawlerProcess.objects.filter(is_run=True)
            for process in processes:
                # 현 서버의 프로세스 아니면
                if process.server_pid != os.getpid():
                    if psutil.pid_exists(process.crawler_pid):
                        psutil.Process(process.crawler_pid).kill()
                    process.is_run = False
                    process.save()
                    
                    # # 현재 존재하는 프로세스인 경우
                    # if psutil.pid_exists(process.crawler_pid):
                    #     # 이전에 실행되던 프로세스의 경우
                    #     if psutil.Process(process.crawler_pid).name().find("python") > 0 and psutil.Process(process.crawler_pid).ppid() is os.getpid():
                    #         psutil.Process(process.crawler_pid).kill()
                    #         process.is_run = False
                    #         process.save()
                    
        
            p = Process(target=giftcard_crawler.GiftcardCrawler(60, 5).crawling, args=(keyword, min_price, max_price), daemon=True, name="crawler")
            p.start()
            CrawlerProcess.objects.create(server_pid=os.getpid()
                                        , crawler_pid=p.pid
                                        , is_run=True
                                        , args=(keyword, min_price, max_price))
            logger.info("process added [" + keyword + ", " + min_price + ", " + max_price + "]")

        return HttpResponseRedirect(self.request.path_info)
    
class ProcessView(View):
    def get(self, request, *args, **kwargs):
        crawler_process_info = CrawlerProcess.objects.filter(is_run=True).order_by('created_date')
        
        return render(request, 'process_list.html', context={"processes":crawler_process_info})
    
    def post(self, request, *args, **kwargs):
        return render(request, 'process_list.html')