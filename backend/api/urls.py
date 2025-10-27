from django.urls import path

from . import views

urlpatterns=[
    path('',views.url_list_create_view)
]