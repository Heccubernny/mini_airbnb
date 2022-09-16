from django.db import models
from PIL import Image

# Create your models here.
GENDER_LIST = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHER'),
)

class User(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.TextField()
    phone_number = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_LIST)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_booking = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    class Meta:
        db_table = 'users'
        ordering = ['-id']


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Customer: {self.user.username}"


    class Meta:
        db_table = 'user_tokens'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class RoomManager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_LIST)
    address = models.TextField()
    state = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Manager: {self.first_name} {self.last_name}"

    class Meta:
        db_table = 'room_managers'
        ordering = ['-id']
