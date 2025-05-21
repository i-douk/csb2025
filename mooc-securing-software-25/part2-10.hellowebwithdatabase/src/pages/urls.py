from django.urls import path

from .views import homePageView ,dbMessageView

urlpatterns = [
    path('', dbMessageView, name='home')
]
