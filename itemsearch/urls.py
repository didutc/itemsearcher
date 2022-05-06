"""itemsearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('sports/', views.sports, name='sports'),
    path('food/', views.food, name='food'),
    path('cloth/', views.cloth, name='cloth'),
    path('fasioncloth/', views.fasioncloth, name='fasioncloth'),
    path('fasionitem/', views.fasionitem, name='fasionitem'),
    path('digital/', views.digital, name='digital'),
    path('living/', views.living, name='living'),
    path('interior/', views.interior, name='interior'),
    path('baby/', views.baby, name='baby'),
    path('cosmetics/', views.cosmetics, name='cosmetics'),
    path('post/', views.post, name='post'),
    path('transe/', views.transe, name='transe'),


]
