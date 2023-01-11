from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=False)
    phone = models.IntegerField()
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=1500)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    agency = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=500)
    description = models.CharField(max_length=5000)
    facebook = models.CharField(max_length=1000, blank=True)
    instagram = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(blank=False, upload_to="agent_profile_img")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=150)
    agency_tagline = models.CharField(max_length=500)
    agency_phone = models.CharField(max_length=12)
    agency_email = models.EmailField(max_length=500)
    agency_description = models.CharField(max_length=5000)
    agency_facebook = models.CharField(max_length=1000, blank=True)
    agency_instagram = models.CharField(max_length=1000, blank=True)
    agency_image = models.ImageField(
        blank=False, upload_to="agency_profile_img")
    agency_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agency_name


class Property(models.Model):
    agency_name = models.ForeignKey(Agency, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    property_type = models.CharField(max_length=100)
    property_size = models.CharField(max_length=100)
    property_status = models.CharField(max_length=100)
    property_price = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    main_pic = models.ImageField(upload_to="main_property_img")
    pic_02 = models.ImageField(upload_to="property_img_02")
    pic_03 = models.ImageField(upload_to="property_img_03")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ForgotPassword(models.Model):
    email = models.CharField(max_length=100)
    auth_token = models.CharField(max_length=100)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Schedule(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    message = models.CharField(max_length=1000)
    property_title = models.CharField(max_length=500)
    agency_name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MapLocater(models.Model):
    ip = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} "
