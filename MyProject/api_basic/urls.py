from django.urls import path
from .views import NewsP, Contact, Home

urlpatterns = [
    path('news', NewsP, name='news'),
    path('', Home, name='home'),
    path('Contact', Contact, name='contact'),
]