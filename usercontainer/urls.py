from django.urls import include, path
from rest_framework import routers
from usercontainer.views import  RoomManagerViewSet, UserViewSet

# , RoomImageViewSet, RoomReviewViewSet, RoomBookingViewSet, RoomBookingReviewViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet, 'users')
router.register('roommanagers', RoomManagerViewSet, 'roommanagers')
urlpatterns = [
    path('', include(router.urls)),
]
