from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    icon = models.ImageField(upload_to='images/')
    url = models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]  # self is use when inside a class and the function wants to use the value of the class


