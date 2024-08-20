from django.urls import path

from . import views

urlpatterns = [
    path("quiz/", views.generate_artwork_questions, name="quiz"),
    path("search/<str:query>/", views.artwork_by_query, name="artist")
]