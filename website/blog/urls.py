from django.urls import path

from . import views

app_names = 'blog'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name = 'detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name= 'vote'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]