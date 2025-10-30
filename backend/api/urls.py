from django.urls import path

from . import views

urlpatterns=[
    path('exercise/',views.exercise_list_view),
    path('search/',views.search_api_view)
]