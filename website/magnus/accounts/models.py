from django.db import models

# Create your models here.
class Register(models.Model):
    user_full_name = models.CharField(max_length = 100)
    user_email = models.TextField()
    user_password = models.TextField()
    user_gender = models.CharField()
    user_address = models.TextField()
    user_phone = models.IntegerField()
    user_dob = models.DateField()
    user_aadhaar = models.IntegerField()
    user_aadhar_photo  = models.ImageField(upload_to = 'user_aadhaar_photo')
    user_photo  = models.ImageField(upload_to = 'user_photos')