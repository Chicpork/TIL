from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Giftcard, CrawlerProcess
from multiprocessing import Process
import giftcard.giftcard_crawler as giftcard_crawler
import json
import psutil
import os
import logging

# make logger
with open("logging.json", "r") as f:
    config = json.load(f)

logging.config.dictConfig(config)
logger = logging.getLogger("views")

# Create your views here.
class giftCardView(View):
    template_name = 'giftcard_list.html'

    def get(self, request, *args, **kwargs):
        if request.META['CONTENT_TYPE'] == "application/json":
            data = json.loads(request.body)
            keyword = data['keyword']
            min_price = data['min_price']
            max_price = data['max_price']
        else:
            keyword = request.GET.get('keyword')
            min_price = request.GET.get('min_price')
            max_price = request.GET.get('max_price')
        
        if keyword is None or min_price is None or max_price is None:
            return HttpResponse(status=400)
        
        crawler_process_info = CrawlerProcess.objects.latest('id')

        logger.info(crawler_process_info.is_run)
        logger.info(crawler_process_info.server_pid)
        logger.info(crawler_process_info.crawler_pid)
        is_run = False
        if crawler_process_info.is_run:
            if crawler_process_info.server_pid == os.getpid(): # 현재 서버 pid와 같은지
                logger.info(psutil.pid_exists(crawler_process_info.crawler_pid))
                if psutil.pid_exists(crawler_process_info.crawler_pid): # crawler pid가 존재하는지
                    crawler_process = psutil.Process(crawler_process_info.crawler_pid)
                    logger.info(crawler_process.name())
                    logger.info(crawler_process.ppid())
                    if crawler_process.name().find("python") >= 0: # crawler pid가 python 이름을 가지는지
                        if crawler_process.ppid() == os.getpid():
                            # Already running scraping process
                            is_run = True
        
        if is_run == False:
            processes = CrawlerProcess.objects.filter(server_pid=os.getpid(), is_run=True)
            for process in processes:
                if psutil.pid_exists(process.crawler_pid):
                    if psutil.Process(process.crawler_pid).name().find("python") > 0 and psutil.Process(process.crawler_pid).ppid() is os.getpid():
                        psutil.Process(process.crawler_pid).kill()
                        process.is_run = False
                        process.save()
        
            gc = giftcard_crawler.GiftcardCrawler()
            p = Process(target=gc.crawling, args=(keyword, min_price, max_price))
            p.start()
            CrawlerProcess.objects.create(server_pid=os.getpid()
                                        , crawler_pid=p.pid
                                        , is_run=True
                                        , args=(keyword, min_price, max_price))

        return render(request, 'giftcard_list.html')
    
    # def get(self, request, *args, **kwargs):
    #     giftcards = Giftcard.objects.filter(date=timezone.now().strftime('%Y%m%d')).order_by('price')
    #     return render(request, 'giftcard_list.html', {'giftcards' : giftcards})
    
    # def post(self, request, *args, **kwargs):
    #     if request.META['CONTENT_TYPE'] == "application/json":
    #         data = json.loads(request.body)
    #         keyword = data['keyword']
    #         min_price = data['min_price']
    #         max_price = data['max_price']
    #     else:
    #         keyword = request.POST['keyword']
    #         min_price = request.POST['min_price']
    #         max_price = request.POST['max_price']
        
    #     crawler_process_info = CrawlerProcess.objects.latest('id')

    #     is_run = False
    #     if crawler_process_info.server_pid is os.getpid(): # 현재 서버 pid와 같은지
    #         if psutil.pid_exists(crawler_process_info.crawler_pid): # crawler pid가 존재하는지
    #             crawler_process = psutil.Process(crawler_process_info.crawler_pid)
    #             if crawler_process.name().find("python") > 0: # crawler pid가 python 이름을 가지는지
    #                 if crawler_process.ppid() is os.getpid():
    #                     # Already running scraping process
    #                     is_run = True
        
    #     if not is_run:
    #         processes = CrawlerProcess.objects.filter(server_pid=os.getpid(), is_run=True)
    #         for process in processes:
    #             if psutil.pid_exists(process.crawler_pid):
    #                 if psutil.Process(process.crawler_pid).name().find("python") > 0 and psutil.Process(process.crawler_pid).ppid() is os.getpid():
    #                     psutil.Process(process.crawler_pid).kill()
    #                     process.is_run = False
    #                     process.save()
        
    #         gc = giftcard_crawler.GiftcardCrawler()
    #         p = Process(target=gc.crawling, args=(keyword, min_price, max_price))
    #         p.start()
    #         CrawlerProcess.objects.create(server_pid=os.getpid()
    #                                     , crawler_pid=p.pid
    #                                     , is_run=True
    #                                     , args=(keyword, min_price, max_price))

    #     return HttpResponse(status=200)