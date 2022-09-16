from django.contrib import admin
# Register your models here.
from usercontainer.models import RoomManager, User

# , Room, RoomImage, RoomReview, RoomBooking, RoomBookingReview

admin.site.register((User, RoomManager))
