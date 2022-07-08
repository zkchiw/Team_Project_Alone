from datetime import datetime
from django.db import models

class Cal(models.Model):
    time = models.CharField(max_length=10)
    gudan1 = models.CharField(max_length=15)
    gudan2 = models.CharField(max_length=15)
    regdate = models.TextField()
    class Meta :
        db_table : 'Cal'