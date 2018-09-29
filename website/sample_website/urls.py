from django.conf.urls import url, include
from .views import home

urlpatterns = [
    #url(r'', home),
    url(r'home$', home)  # any string that ends with home

]
