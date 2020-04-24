from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('publish', views.publish, name='publish'),
    path('publications', views.index_test, name='index_test'),
    path('publications/<int:number>', views.index_tests),
    path('comment', views.comment),
]
