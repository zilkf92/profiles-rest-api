from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

# Router is a class provided by Django rest_framework to generate the
# different routes that are available for the view set
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
router.register('RequestData', views.RequestDataViewSet)

urlpatterns = [
    # as_view is the standard function to convert APIView class
    # to be rendered by url
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    
    # Generates a list of URLs that are required
    # for all of the functions that are added to the viewset
    # which can be passed in to using path and include function
    path('', include(router.urls))
]
