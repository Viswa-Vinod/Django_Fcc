from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    # django also generates an auto-id field
    title       = models.CharField(max_length=120)  #max_length is required
    description = models.TextField(blank=True, null=True) # blank renders the field as a required field
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField()
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):   # check list.html to see how this is used
        return  reverse("products:product-detail", kwargs={"id": self.id})# this is the recommended way
        # return f"/products/{self.id}" - not recommended to do it this way because you are hard-coding /products in there
