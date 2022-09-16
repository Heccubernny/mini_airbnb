from bookingcontainer.models import (Contact, Room, RoomBooking, RoomImage,
                                     RoomReview)
from django.contrib import admin

# Register your models here.
admin.site.register((RoomReview, RoomBooking, Contact))


class RoomImageAdmine(admin.StackedInline):
    model = RoomImage
    extra = 1

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageAdmine]
    list_display = ('room_number', 'room_type', 'room_price', 'room_description', 'room_created_at', 'room_updated_at', 'room_deleted_at')
    list_filter = ('room_type', 'room_price')
    search_fields = ('room_number', 'room_type', 'room_price', 'room_description', 'room_created_at', 'room_updated_at', 'room_deleted_at')
    list_per_page = 10

    class Meta:
        model = Room


@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    list_display = ('room_image', 'room', 'room_image_created_at', 'room_image_updated_at', 'room_image_deleted_at')
    list_filter = ('room_image', 'room')
    search_fields = ('room_image', 'room', 'room_image_created_at', 'room_image_updated_at', 'room_image_deleted_at')
    list_per_page = 10

    class Meta:
        model = RoomImage
