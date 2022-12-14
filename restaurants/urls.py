from django.urls import path

from . import views

app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/<int:restaurant_id>/', views.detail, name='detail'),
    path('restaurant/<int:restaurant_id>/comment', views.comment, name='comment'),
]
