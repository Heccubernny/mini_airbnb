from bookingcontainer.models import (Contact, Room, RoomBooking, RoomImage,
                                     RoomReview)
from rest_framework import serializers, status
from rest_framework.response import Response


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ('contact_deleted_at',)

    def get(self, request, *args, **kwargs):
        contact = Contact.objects.get(id=kwargs['id'])
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def create(self, validated_data):
        contact = Contact(**validated_data)
        contact.save()
        return contact

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance

    def delete(self, request, *args, **kwargs):
        contact = Contact.objects.get(id=kwargs['id'])
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        instance.delete()
    def perform_list(self, queryset):
        queryset.all()
    def perform_retrieve(self, instance):
        instance


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'

    def get(self, request, *args, **kwargs):
        roomimage = RoomImage.objects.get(id=kwargs['id'])
        serializer = RoomImageSerializer(roomimage)
        return Response(serializer.data)

    def create(self, validated_data):
        roomimage = RoomImage(**validated_data)
        roomimage.save()
        return roomimage

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    def delete(self, request, *args, **kwargs):
        roomimage = RoomImage.objects.get(id=kwargs['id'])
        roomimage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        instance.delete()
    def perform_list(self, queryset):
        queryset.all()
    def perform_retrieve(self, instance):
        instance


class RoomReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReview
        fields = '__all__'

    def get(self, request, *args, **kwargs):
        roomreview = RoomReview.objects.get(id=kwargs['id'])
        serializer = RoomReviewSerializer(roomreview)
        return Response(serializer.data)

    def create(self, validated_data):
        roomreview = RoomReview(**validated_data)
        roomreview.save()
        return roomreview

    def update(self, instance, validated_data):
        instance.review = validated_data.get('review', instance.review)
        instance.save()
        return instance

    def delete(self, request, *args, **kwargs):
        roomreview = RoomReview.objects.get(id=kwargs['id'])
        roomreview.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        instance.delete()
    def perform_list(self, queryset):
        queryset.all()
    def perform_retrieve(self, instance):
        instance


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def get(self, request, *args, **kwargs):
        room = Room.objects.get(id=kwargs['id'])
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def create(self, validated_data):
        room = Room(**validated_data)
        room.save()
        return room

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    def delete(self, request, *args, **kwargs):
        room = Room.objects.get(id=kwargs['id'])
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        instance.delete()
    def perform_list(self, queryset):
        queryset.all()
    def perform_retrieve(self, instance):
        instance


class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBooking
        exclude = ('room_booking_deleted_at',)

    def get(self, request, *args, **kwargs):
        roombooking = RoomBooking.objects.get(id=kwargs['id'])
        serializer = RoomBookingSerializer(roombooking)
        return Response(serializer.data)

    def create(self, validated_data):
        roombooking = RoomBooking(**validated_data)
        roombooking.save()
        return roombooking

    def update(self, instance, validated_data):
        instance.check_in = validated_data.get('check_in', instance.check_in)
        instance.check_out = validated_data.get('check_out', instance.check_out)
        instance.save()
        return instance

    def delete(self, request, *args, **kwargs):
        roombooking = RoomBooking.objects.get(id=kwargs['id'])
        roombooking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
    def perform_destroy(self, instance):
        instance.delete()
    def perform_list(self, queryset):
        queryset.all()
    def perform_retrieve(self, instance):
        instance
