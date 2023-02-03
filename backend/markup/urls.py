from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('markup/', GetMarkUp.as_view(), name='add_markup'),

    path('history', HistoryMarkUp.as_view(), name='history'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

]