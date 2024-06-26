from django.db import models # type: ignore

# Create your models here.
class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age  = models.IntegerField(default=18)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField()


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    car_speed = models.IntegerField(default=50)


    def __str__(self) -> str:
        return self.car_name