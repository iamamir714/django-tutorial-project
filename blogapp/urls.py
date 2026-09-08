from django.urls import path
from blogapp.views import *

app_name = 'blogapp'

urlpatterns = [
    path('', blog_view, name = 'index'),
    path('<int:pid>', blog_single, name = 'single'),
    path('category/<str:cat_name>', blog_view, name = 'category'),
    path('author/<str:author_username>', blog_view, name = 'author'),
    path('test', test, name='test')
]
