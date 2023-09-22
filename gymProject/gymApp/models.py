from django.db import models


# Create your models here.




class gymPlans(models.Model):
    name= models.CharField(max_length=100)
    amount =models.IntegerField()
    duration = models.TextField()
    class Meta:
        verbose_name_plural ="gym Plans"

        
class gym(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    number = models.IntegerField()
    subscription= models.ForeignKey(gymPlans,on_delete=models.CASCADE,default=3)

class gymAdmin(models.Model):
    username= models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    active =models.BooleanField()


class trainer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    address = models.TextField()
    number = models.IntegerField()

class bookSlots(models.Model):
    date = models.DateTimeField()
    member =models.ForeignKey(gym,on_delete=models.CASCADE)
    trainer= models.ForeignKey(trainer,on_delete=models.CASCADE)
    plans= models.ForeignKey(gymPlans,on_delete=models.CASCADE,default=3)

