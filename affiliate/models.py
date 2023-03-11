from django.db import models
import uuid
from property.models import User, Agent

# Create your models here.


class Affiliate(models.Model):
    AFFILIATE_STATUS = [
        ('POSTED', 'Posted'),
        ('SEEN', 'Seen'),
        ('FORWARDED', 'Forwarded'),
        ('CONVERTED', 'Converted'),
        ('CANCELLED', 'Cancelled'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aff_name = models.CharField(max_length=250)
    aff_email = models.EmailField(max_length=250)
    aff_phone = models.CharField(max_length=12)
    aff_subject = models.CharField(max_length=500)
    aff_details = models.CharField(max_length=1250)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=AFFILIATE_STATUS, default="POSTED")

    def __str__(self):
        return "{}-{}".format(self.user, self.aff_name)
