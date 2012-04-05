from django.db import models
from django.forms.fields import MultipleChoiceField

# Create your models here.

# Create a minimalistic model to store various data records of the user

IM_SERVICE_CHOICE = (
    ('GTALK', "Google Talk"),
    ('MSN', "Microsoft Network"),
    ('FB', "FACEBOOK"),
)
IM_SERVICE_NICK = map(lambda x: x[0], IM_SERVICE_CHOICE)

class UserStatSub(models.Model):
  """ Keep the model simple, accept username and IM services """

  uname = models.CharField(max_length=200)

  # Choice of IM Service for the user
  im_services = models.CharField(max_length=3, choices=IM_SERVICE_CHOICE)
  time_of_sum = models.DateTimeField(auto_now=True, auto_now_add=True)
