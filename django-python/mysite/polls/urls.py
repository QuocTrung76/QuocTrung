from django.urls import path

from . import views
from . import apiviews
app_name='polls'
urlpatterns = [
        #path('', views.IndexView.as_view(), name='index'),
        #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        #path('<int:question_id>/vote/', views.vote, name='vote'),
        path('', views.question_list, name='question'),
        path('<int:pk>/', views.question_detail, name='detail'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
        path('detail/<int:question_id>/', views.DetailView.as_view(), name='detail'),
        path('question/', apiviews.question_view, name='question_view'),
]
