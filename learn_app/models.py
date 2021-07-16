from django.db import models
import re 
# Create your models here.

class DullAPI(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    @property
    def is_name_valid(self):
        return bool(re.search("[A-Za-z]{2,50}\s[A-Za-z]{2,50}", self.name))
    


    def __str__(self):
        return self.name

class BlockList(models.Model):

    ip_address = models.TextField()

    def __str__(self):
        return self.ip_address
