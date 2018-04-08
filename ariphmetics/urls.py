from django.urls import path

from . import views

app_name = 'ariphmetics'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_count>', views.index, name='index'),
    path('solve/', views.solve, name='solve'),
]
