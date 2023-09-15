from django.db import models

# Create your models here.
class Orders(models.Model):
    oid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    price = models.FloatField()
    mail = models.EmailField()
    addr = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.fname}'