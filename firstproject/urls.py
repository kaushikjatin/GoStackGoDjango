from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path("stock_game/", include('stock_game.urls'))
]
