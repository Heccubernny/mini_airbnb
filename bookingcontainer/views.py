from datetime import datetime

from bookingcontainer.models import (Contact, Room, RoomBooking, RoomImage,
                                     RoomReview)
from bookingcontainer.serializers import (ContactSerializer,
                                          RoomBookingSerializer,
                                          RoomImageSerializer,
                                          RoomReviewSerializer, RoomSerializer)
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

# Create your views here.

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer



class RoomBookingViewSet(viewsets.ModelViewSet):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer

    def get(self, request, *args, **kwargs):
        roombooking = RoomBooking.objects.get(id=kwargs['id'])
        serializer = RoomBookingSerializer(roombooking)
        return Response(serializer.data)

    def create(self, validated_data):
        roombooking = RoomBooking(validated_data)
        roombooking.save()
        return roombooking

    def update(self, instance, validated_data):
        instance.room = validated_data.get('room', instance.room)
        instance.booking = validated_data.get('booking', instance.booking)
        instance.save()
        return instance

    def delete(self, request, *args, **kwargs):
        roombooking = RoomBooking.objects.get(id=kwargs['id'])
        roombooking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(["POST"])
    def book(self, request, *args, **kwargs):
        if request.method == 'POST':

            booker_user_id = request.data.get('booker_user_id')
            room_number = request.data.get('room_number')
            room_booking_checkin_date = request.data.get('room_booking_checkin_date')
            room_booking_checkout_date = request.data.get('room_booking_checkout_date')
            request.session['room_booking_checkin_date'] = room_booking_checkin_date
            request.session['room_booking_checkout_date'] = room_booking_checkout_date
            room_booking_checkin_date = datetime.strptime(room_booking_checkin_date, '%d-%m-%y').date()
            room_booking_checkout_date = datetime.strptime(room_booking_checkout_date, '%d-%m-%y').date()
            no_of_days = (room_booking_checkout_date - room_booking_checkin_date).days
            room = Room.objects.get(room_number=room_number)
            room_amount = request.data.get('room_amount')
            room_type = request.data.get('room_type')
            room_booking_created_at = request.data.get('room_booking_created_at')
            room_booking_updated_at = request.data.get('room_booking_updated_at')
            room_booking_deleted_at = request.data.get('room_booking_deleted_at')
            data = Room.objects.filter(room_is_available = True, no_of_days_advance__gte = no_of_days, room_booking_checkin_date__lte = room_booking_checkin_date, room_number=room_number)
            request.session['no_of_days'] = no_of_days

            if data:
                data = RoomBooking.objects.create(room=room, booker_user_id=booker_user_id, room_booking_checkin_date=room_booking_checkin_date, room_booking_checkout_date=room_booking_checkout_date, room_amount=room_amount, room_type=room_type, room_booking_created_at=room_booking_created_at, room_booking_updated_at=room_booking_updated_at, room_booking_deleted_at=room_booking_deleted_at)
                return Response({'message': 'Room booked successfully', 'data': data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Room not available'}, status=status.HTTP_400_BAD_REQUEST)

        data.save()
            # return Response({'message': 'Room booked successfully'})
        return Response(data, status=status.HTTP_201_CREATED)

    def delete_room(self, request, *args, **kwargs):
        data = Room.objects.get(id=kwargs['id'])
        room_manager = data.room_manager.email
        if room_manager == request.user.email:
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You are not authorized to delete this room'}, status=status.HTTP_400_BAD_REQUEST)


    def cancel_room_booking(self, request, *args, **kwargs):
        if request.method == 'POST':
            room_booking_id = request.data.get('room_booking_id')
            room_booking_deleted_at = request.data.get('room_booking_deleted_at')
            data = RoomBooking.objects.filter(room_booking_id=room_booking_id)
            room = data.room_number
            room.room_is_available = True
            room.save()
            if data:
                data = RoomBooking.objects.update(room_booking_deleted_at=room_booking_deleted_at)
                return Response({'message': 'Room cancelled successfully', 'data': data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Room not available'}, status=status.HTTP_400_BAD_REQUEST)


            data.delete()

            return Response(status=status.HTTP_201_CREATED)

    def checkin(self, request, *args, **kwargs):
        if request.method == 'POST':
            room_booking_id = request.data.get('room_booking_id')
            room_booking_checkin_date = request.data.get('room_booking_checkin_date')
            data = RoomBooking.objects.filter(room_booking_id=room_booking_id)
            if data:
                data = RoomBooking.objects.update(room_booking_checkin_date=room_booking_checkin_date)
                return Response({'message': 'Room checked in successfully', 'data': data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Room not available'}, status=status.HTTP_400_BAD_REQUEST)

            data.save()
            return Response(status=status.HTTP_201_CREATED)

    def checkout(self, request, *args, **kwargs):
        if request.method == 'POST':
            room_booking_id = request.data.get('room_booking_id')
            room_booking_checkout_date = request.data.get('room_booking_checkout_date')
            data = RoomBooking.objects.filter(room_booking_id=room_booking_id)
            if data:
                data = RoomBooking.objects.update(room_booking_checkout_date=room_booking_checkout_date)
                return Response({'message': 'Room checked out successfully', 'data': data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Room not available'}, status=status.HTTP_400_BAD_REQUEST)

            data.save()
            return Response(status=status.HTTP_201_CREATED)

    def book_now(self, request, *args, **kwargs):
        if request.session.get("username", None) and request.session.get("type", None) == 'user':
            if request.session.get("no_of_days", 1):
                no_of_days = request.session['no_of_days']
                room_booking_checkin_date = request.session['room_booking_checkin_date']
                room_booking_checkout_date = request.session['room_booking_checkout_date']
                request.session['room_number'] = id
                data=Room.objects.get(room_no=id)
                bill=data.price*int(no_of_days)
                request.session['bill']=bill
                room_manager = data.room_manager.email
                data = Rooms.objects.filter(room_is_available = True, no_of_days_advance__gte = no_of_days, room_booking_checkin_date__lte = room_booking_checkin_date, room_number=id, room_booking_checkout_date__gte = room_booking_checkout_date, data = data, bill = bill, room_manager = room_manager)
                request.session['no_of_days'] = no_of_days
                if data:
                    return Response({'message': 'Room booked successfully', 'data': data}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Room not available'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Room not available'}, status=status.HTTP_400_BAD_REQUEST)

    def booking_history(self, request, *args, **kwargs):
        if request.method == 'GET':
            booker_user_id = request.data.get('booker_user_id')
            data = RoomBooking.objects.filter(booker_user_id=booker_user_id)
            if data:
                return Response({'message': 'Room booking history', 'data': data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No bookings found'}, status=status.HTTP_400_BAD_REQUEST)

            data.save()
            return Response(status=status.HTTP_201_CREATED)

    def booking_confirmation(self, request, *args, **kwargs):
        room_number = request.session['room_number']
        room_booking_checkin_date = request.session['room_booking_checkin_date']
        room_booking_checkout_date = request.session['room_booking_checkout_date']
        username = request.session['username']
        user_id = User.objects.get(username=username)
        room = Rooms.objects.get(room_number=room_number)
        room_type = room.room_type
        room_amount = room.room_amount
        amount_per_day = room_amount * request.session['no_of_days']
        amount = request.session['bill']
        room_booking_checkin_date = datetime.strptime(room_booking_checkin_date, '%Y-%m-%d').date()
        room_booking_checkout_date = datetime.strptime(room_booking_checkout_date, '%Y-%m-%d').date()
        data = RoomBooking.objects.create(booker_user_id=user_id, room_number=room_number, room_type=room_type, room_booking_checkin_date=room_booking_checkin_date, room_booking_checkout_date=room_booking_checkout_date, room_booking_amount=amount, room_booking_amount_per_day=amount_per_day)
        data.save()
        room.room_is_available = False
        room.save()

        del request.session['room_number']
        del request.session['room_booking_checkin_date']
        del request.session['room_booking_checkout_date']
        del request.session['no_of_days']
        del request.session['bill']

        messages.info(request, 'Room booked successfully')


        return Response({'message': 'Room booked successfully', 'data': data}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        roombooking = RoomBooking.objects.all()
        serializer = RoomBookingSerializer(roombooking, many=True)
        return Response(serializer.data)




class RoomReviewViewSet(viewsets.ModelViewSet):
    queryset = RoomReview.objects.all()
    serializer_class = RoomReviewSerializer


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


    def contact(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        if request.method == 'GET':
            return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        else:
            username = request.POST['username']
            email = request.POST['email']
            message = request.POST['message']
            contact = Contact(username=username, email=email, message=message)
            contact.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post', 'get'], url_path='contact', url_name='contact', name='contact')
    def get(self, request, *args, **kwargs):
        contact = Contact.objects.filter()
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
