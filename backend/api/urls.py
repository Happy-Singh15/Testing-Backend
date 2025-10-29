from django.urls import path

from . import views

urlpatterns=[
    path('url/',views.url_list_create_view),
    path('exercise/',views.exercise_list_create_view)
]