from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.get_json_data, name='index'),

]