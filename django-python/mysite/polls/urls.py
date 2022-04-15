from django.urls import path
from . import apiviews

from . import views
app_name='polls'
urlpatterns = [
        #path('', views.IndexView.as_view(), name='index'),
        #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        #path('<int:question_id>/vote/', views.vote, name='vote'),
        path('', views.index, name='index'),
        path('question/', apiviews.questions_view, name='questions_view'),
]
