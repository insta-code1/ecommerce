from django.conf import settings
from django.db import models

# Create your models here


class UserCheckout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True) #not required
    email = models.EmailField()
   # merchant_id

    def __unicode__(self):
        return self.email


#class Order(models.Models):
    #cart
    #usercheckout --> required
    #shipping address
    #billing address
    #shipping total price
    #order (cart total + shipping)
    #order_id --> custom id
