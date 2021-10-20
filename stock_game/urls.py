from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="news"),
    path("stock_game", view=views.stock_game, name="game")
]
