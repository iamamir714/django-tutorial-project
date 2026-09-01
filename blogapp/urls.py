from django.urls import path
from blogapp.views import *

app_name = 'blogapp'

urlpatterns = [
    path('', blog_view, name = 'index'),
    path('single', blog_single, name = 'single'),
    path('test', test, name='test')
]
