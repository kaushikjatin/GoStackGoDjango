from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="news"),
    path('calculation', views.calculation, name="calculation"),
    path("stock_game", view=views.stock_game, name="game"),
    path("predict",view=views.predict,name='predict')

]
