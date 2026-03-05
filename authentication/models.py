from django.db import models

from django.db import models

from django.utils import timezone

from django.contrib.auth.hashers import make_password



gender_choices = [
    ('Male','MALE'),
    ('Female','FEMALE'),
    ('Other','OTHER')
]

class Register(models.Model):
    name = models.CharField(max_length=40)
    phone_no = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=400)
    gender = models.CharField(max_length=10,choices=gender_choices)
    registered_timestamp = models.DateTimeField(default=timezone.now)

    def set_password(self,raw_password):
        self.password = make_password(raw_password)


    def check_password(self,raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password,self.password)
