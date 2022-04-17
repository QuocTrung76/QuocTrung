from django.urls import path

from . import views
app_name='polls'
urlpatterns = [
        #path('', views.IndexView.as_view(), name='index'),
        #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        #path('<int:question_id>/vote/', views.vote, name='vote'),
        path('', views.question_list, name='question'),
        path('<int:pk>/', views.question_detail, name='detail'),
        #path('<int:question_id>/vote/', views.vote, name='vote'),
        path('questions/<int:question_id>/', views.question_detail_view, name='question_detail_view'),
        path('questions/<int:question_id>/choices/', views.choices_view, name='choices_view'),
        path('questions/<int:question_id>/vote/', views.vote_view, name='vote_view'),
        path('questions/<int:question_id>/result/', views.question_result_view, name='question_result_view')
]
