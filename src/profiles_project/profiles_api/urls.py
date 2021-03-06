from django.urls import path,include
from .views import HeloApViews
from rest_framework.routers import DefaultRouter
from . import views 

router=DefaultRouter()
router.register('hello-viewset',views.HeloViewSet,base_name="hello-viewset")
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
router.register('login',views.LoginViewSet,base_name="login")
urlpatterns = [
    path('',HeloApViews.as_view(),name='test-view'),
    path('',include(router.urls)),

]
