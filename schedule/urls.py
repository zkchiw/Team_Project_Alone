from django.urls import path
from schedule import views

urlpatterns = [
    path('', views.ScheduleView.as_view(), name='schedule'),
    path('july_all', views.JulyView.as_view(), name='july'),
    path('july_02', views.JulyView02.as_view(), name='july'),
    path('july_03', views.JulyView03.as_view(), name='july'),
    path('july_05', views.JulyView05.as_view(), name='july'),
    path('july_06', views.JulyView06.as_view(), name='july'),
    path('july_08', views.JulyView08.as_view(), name='july'),
    path('july_09', views.JulyView09.as_view(), name='july'),
    path('july_10', views.JulyView10.as_view(), name='july'),
    path('july_16', views.JulyView16.as_view(), name='july'),
    path('july_30', views.JulyView30.as_view(), name='july'),
    path('july_31', views.JulyView31.as_view(), name='july'),
]