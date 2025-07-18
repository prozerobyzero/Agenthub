
from django.urls import path
from . import views

urlpatterns = [
    path('scraped/', views.scraped, name='scraped'),
    path('add_scrape/', views.add_scrape, name='add_scrape'),
]
