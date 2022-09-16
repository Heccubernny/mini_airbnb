# # from django.urls import path
# # from rest_framework import routers
# # from usercontainer.views import GoogleLogin

# # , RoomImageViewSet, RoomReviewViewSet, RoomBookingViewSet, RoomBookingReviewViewSet

# # router = routers.DefaultRouter()

# # router.register('logout', UserViewSet.logout, 'logout')
# urlpatterns = [
#     # path('', include(router.urls)),
#     # path('log', GoogleLogin.as_view(), name='google_login')
#     # path('room/<int:room_id>/booking/', RoomBookingViewSet.as_view({'post': 'create'}), name='room_booking'),
#     # path('room/<int:room_id>/booking/<int:booking_id>/', RoomBookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='room_booking'),
#     # path('room/<int:room_id>/booking/<int:booking_id>/review/', RoomBookingReviewViewSet.as_view({'post': 'create'}), name='room_booking_review'),
#     # path('room/<int:room_id>/booking/<int:booking_id>/review/<int:review_id>/', RoomBookingReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='room_booking_review'),
#     # path('room/<int:room_id>/review/', RoomReviewViewSet.as_view({'post': 'create'}), name='room_review'),
#     # path('room/<int:room_id>/review/<int:review_id>/', RoomReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='room_review'),
#     # path('room/<int:room_id>/image/', RoomImageViewSet.as_view({'post': 'create'}), name='room_image'),
#     # path('room/<int:room_id>/image/<int:image_id>/', RoomImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='room_image'),

# ]

from bookingcontainer.views import ContactViewSet, RoomBookingViewSet
from django.urls import include, path
from rest_framework import routers

# , RoomImageViewSet, RoomReviewViewSet, RoomBookingViewSet, RoomBookingReviewViewSet

router = routers.DefaultRouter()

router.register('contact', ContactViewSet, 'contact'),
router.register('roombooking', RoomBookingViewSet, 'roombooking'),
urlpatterns = [
    path('', include(router.urls)),
]
