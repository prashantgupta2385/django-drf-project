from django.db import models
from helper.models import Trackingmodel
from authentication.models import User

class Todo(Trackingmodel):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    is_complete=models.BooleanField(default=False)
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title