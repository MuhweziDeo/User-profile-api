from django.urls import path,include
from .views import HeloApViews
from rest_framework.routers import DefaultRouter
from . import views 

router=DefaultRouter()
router.register('hello-viewset',views.HeloViewSet,base_name="hello-viewset")
urlpatterns = [
    path('',HeloApViews.as_view(),name='test-view'),
    path('',include(router.urls))
]
