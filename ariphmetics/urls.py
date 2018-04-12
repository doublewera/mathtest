from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'ariphmetics'
urlpatterns = [
    path('', views.index, name='index'),
    path('user_list', views.user_list),
    # path('user_list.css', )
    path('<int:question_count>', views.index, name='index'),
    path('solve/', views.solve, name='solve'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
