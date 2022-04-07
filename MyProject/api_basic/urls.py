from django.urls import path
from .views import NewsP, Contact, Home, Newsdate

urlpatterns = [
    path('news', NewsP, name='news'),
    path('', Home, name='home'),
    path('Contact', Contact, name='contact'),
    path('newsdate/<int:year>', Newsdate, name='newsdate'),
]