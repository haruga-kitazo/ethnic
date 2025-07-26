from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .models import Restaurant

def index(request):
    restaurants = Restaurant.objects.all()  # 全店舗データを取得
    return render(request, 'ethnic/index.html', {'restaurants': restaurants})
