from django.urls import path
from .views import function_view, ClassBasedView

urlpatterns = [
    path('function/', function_view, name='function_view'),
    path('class/', ClassBasedView.as_view(), name='class_view'),
]
