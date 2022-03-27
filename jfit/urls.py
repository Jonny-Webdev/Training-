from django.urls import path
from .views import HomeView

app_name = "jfit"
urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('<str:alert_msg>', HomeView.as_view(), name="home"),
]
