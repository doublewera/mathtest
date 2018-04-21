from django.urls import path

from . import views

app_name = 'ariphmetics'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_count>', views.index, name='index'),
    path('answer_list', views.answer_list),
    path('user_list', views.user_list),
    path('solve/', views.solve, name='solve'),
]
