from django.db import models
from django.forms.fields import MultipleChoiceField

# Create your models here.

# Create a minimalistic model to store various data records of the user

class UserStatSub(models.Model):
  """ Keep the model simple, accept username and IM services """

  uname = models.CharField(max_length=200)

  # Choice of IM Service for the user
  IM_SERVICE_CHOICE = (
      ('GTALK', "Google Talk"),
      ('MSN', "Microsoft Network"),
      ('FB', "FACEBOOK"),
  )
  im_services = models.CharField(max_length=3, choices=IM_SERVICE_CHOICE)
