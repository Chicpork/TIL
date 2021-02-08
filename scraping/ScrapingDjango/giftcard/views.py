from django.views.generic import View
from django.shortcuts import render
from .models import Giftcard
from django.utils import timezone

# Create your views here.
class giftCardView(View):
    template_name = 'giftcard_list.html'

    def get(self, request, *args, **kwargs):
        giftcards = Giftcard.objects.filter(date=timezone.now().strftime('%Y%m%d')).order_by('price')
        return render(request, 'giftcard_list.html', {'giftcards' : giftcards})

# def giftcard_list(request):
#     giftcards = Giftcard.objects.filter(date=timezone.now().strftime('%Y%m%d')).order_by('date')
#     return render(request, 'giftcard_list.html', {'giftcards' : giftcards}) 