from django.urls import path
from .views import (
    HomeView,
    ItemDetailView,
    search
)

app_name = 'main'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', search, name='search'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]