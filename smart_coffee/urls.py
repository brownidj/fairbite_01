from django.urls import path

from smart_coffee import views

urlpatterns = [
    path("", views.example_view),
    # path('<int:num_page>', views.num_page_view, name='num_page_view'),
    # path('<str:page>', views.page_view, name='page_view')
]
