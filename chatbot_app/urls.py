from django.urls import path
from . import views
urlpatterns=[
    path('chatbot/input/', views.chatbot_input, name="chatbot_input"),
    path('chatbot/input/serializer', views.chatbot_serializer, name="chatbot_serializer"),
    path('chatbot/get/', views.get_data, name="chatbot_get_data"),


]