from django.urls import path
from . import views
urlpatterns = [
    # path('january', views.january),
    # path('february', views.february),
    # path('march', views.march),
    # path('april', views.april),
    path('', views.index, name="index"),
    path('<int:month>', views.monthly_challenges_by_num),
    path('<str:month>', views.monthly_challenge, name="month-challenge")

]
