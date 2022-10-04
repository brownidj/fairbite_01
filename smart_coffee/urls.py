from django.urls import path

from smart_coffee import views

urlpatterns = [
    path('simple_view', views.simple_view, name='simple_view')
]
