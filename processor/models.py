from django.db import models

# Create your models here.
class Pizza(models.Model):
    user_id = models.BigIntegerField()
    size = models.CharField(max_length=200, blank=True, null=True)
    payment_type = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.size,
                              self.payment_type)