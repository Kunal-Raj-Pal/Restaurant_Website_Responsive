from django.db import models

# Create your models here.


class AddMenu(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item
    

class BookSeatData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    nop = models.IntegerField()
 
    def __str__(self):
        return self.name
    

class FeedbackOrContactData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    feed = models.TextField()
 
    def __str__(self):
        return self.name
    