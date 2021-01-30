from django.urls import path
from home import views

urlpatterns =[
    path("", views.home, name="home"),
    path('<int:id>/', views.detail),
    path('<int:id>/', views.category)
]