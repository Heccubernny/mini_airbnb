
from django.db import models
from usercontainer.models import RoomManager, User

ROOM_TYPES = (
    ('Single', 'Single'),
    ('Double', 'Double'),
    ('Triple', 'Triple'),
    ('Quad', 'Quad'),
    ('Queen', 'Queen'),
    ('King', 'King'),
    ('Twin', 'Twin'),
    ('Double-Double', 'Double-Double'),
    ('Studio', 'Studio'),
    ('Suite', 'Suite'),
    ('Other', 'Other'),
)

# Create your models here.

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=100, default='Room')
    room_description = models.CharField(max_length=500, default='Room Description')
    room_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    room_number = models.CharField(max_length=100, default='Room Number')
    room_type = models.CharField(max_length=100, choices=ROOM_TYPES)
    no_of_days_advance=models.IntegerField(null = True)
    room_city = models.CharField(max_length=100, default='Room City')
    room_state = models.CharField(max_length=100, default='Room State')
    room_zipcode = models.CharField(max_length=100, default='Room Zipcode')
    # room_country = models.CharField(max_length=100, default='Room Country')
    room_latitude = models.DecimalField(max_digits=10, decimal_places=6, default=0.000000)
    room_longitude = models.DecimalField(max_digits=10, decimal_places=6, default=0.000000)
    room_manager = models.ForeignKey(RoomManager, on_delete=models.CASCADE)
    room_image = models.FileField(upload_to='room_images')
    room_rating = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    room_review_count = models.IntegerField(default=0)
    room_is_available = models.BooleanField(default=True)
    room_created_at = models.DateTimeField(auto_now_add=True)
    room_updated_at = models.DateTimeField(auto_now=True)
    room_deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.room_name

    class Meta:
        db_table = 'rooms'
        ordering = ['-room_id']


class RoomImage(models.Model):
    room_image_id = models.AutoField(primary_key=True)
    room_image = models.FileField(upload_to='room_images')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image_created_at = models.DateTimeField(auto_now_add=True)
    room_image_updated_at = models.DateTimeField(auto_now=True)
    room_image_deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.room_image_id} - {self.room_image}'

    class Meta:
        db_table = 'room_images'
        ordering = ['-room_image_id']


class RoomReview(models.Model):
    room_review_id = models.AutoField(primary_key=True)
    room_review = models.CharField(max_length=500, default='Room Review')
    room_review_rating = models.DecimalField(max_digits=1, decimal_places=1, default=0.00)
    room_review_created_at = models.DateTimeField(auto_now_add=True)
    room_review_updated_at = models.DateTimeField(auto_now=True)
    room_review_deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'room_reviews'
        ordering = ['-room_review_id']


class RoomBooking(models.Model):
    booker_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_number = models.ForeignKey(Room, verbose_name=("Room Name"), related_name='room_number+', on_delete=models.CASCADE)
    room_booking_checkin_date = models.DateField(null = False, auto_now_add=True)
    room_booking_checkout_date = models.DateField(null=False,  auto_now=True)
    room_amount = models.PositiveIntegerField(default=1, null=True, blank=True, verbose_name=("Number of Rooms"), help_text=("Number of Rooms"))
    room_type = models.CharField(max_length=100, choices=ROOM_TYPES)
    room_booking_created_at = models.DateTimeField(auto_now_add=True)
    room_booking_updated_at = models.DateTimeField(auto_now=True)
    room_booking_deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.room_number} - {self.room_booking_checkin_date} - {self.room_booking_checkout_date}"


    # @property
    # def room_booking_checkin_date(self):
    #     return self.room_booking_checkin_date.strftime("%d/%m/%Y")

    # @property
    # def room_booking_checkout_date(self):
    #     return self.room_booking_checkout_date.strftime("%d/%m/%Y")

    @property
    def is_overdue(self):
        return self.room_booking_checkout_date < timezone.now().date()

    class Meta:
        db_table = 'room_bookings'
        ordering = ['-room_booking_created_at']


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100, default='Contact Name')
    contact_email = models.CharField(max_length=100, default='Contact Email')
    contact_message = models.CharField(max_length=500, default='Contact Message')
    contact_created_at = models.DateTimeField(auto_now_add=True)
    contact_updated_at = models.DateTimeField(auto_now=True)
    contact_deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.contact_name

    def __unicode__(self):
        return self.contact_name

    class Meta:
        db_table = 'contacts'
        ordering = ['-contact_id']
