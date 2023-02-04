from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add_markup/', GetMarkUp.as_view(), name='add_markup'),
    path('lookmap/', LookMap.as_view(), name='look_map'),
    path('lookmap/map_folium/', Map.as_view(), name='map_folium'),
    path('add_markup/map_start/', StartMap.as_view(), name='map_start'),

    path('history', HistoryMarkUp.as_view(), name='history'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('contact/', Contact.as_view(), name='contact'),

]
