from django.db import models
from django.contrib.auth.models import User

# Product class
class Product(models.Model):
    # title
    title = models.CharField(max_length = 255)
    # url
    url = models.TextField()
    # pub_date
    pub_date = models.DateTimeField()
    # votes_total
    votes_total = models.IntegerField(default=1)
    # image
    image = models.ImageField(upload_to = 'images/')
    # icon
    icon = models.ImageField(upload_to = 'images/')
    # body
    body = models.TextField()
    # hunter (person who submitted or found the product)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    # function that will allow the admin page to display each blog title
    def __str__(self):
        return self.title

    # function that will return certain portion of the body
    def summary(self):
        return self.body[:100]+"..."

    # customize publishing dates
    # pub_date_pretty
    def pub_date_neat(self):
        return self.pub_date.strftime('%B %e, %Y')
