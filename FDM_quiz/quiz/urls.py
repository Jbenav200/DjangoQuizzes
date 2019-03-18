from django.conf.urls import url
from .views import MainPage

urlpatterns = [
    url(r'^$', MainPage.as_view(), name='index'),
]
