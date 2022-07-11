from django.urls import path
from home import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('test/', views.TestView.as_view(), name='test'),
]