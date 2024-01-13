from django.urls import path
from .views import calculate_premium

urlpatterns = [
    path('calculate/', calculate_premium, name='calculate_premium'),

]