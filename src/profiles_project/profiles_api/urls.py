from django.urls import path
from .views import HeloApViews

urlpatterns = [
    path('',HeloApViews.as_view(),name='test-view')
]
