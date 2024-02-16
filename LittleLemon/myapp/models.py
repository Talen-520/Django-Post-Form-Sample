from django.db import models

# Create your models here.
class UserComments(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    comment = models.CharField(max_length = 1000)
    #comment = models.CharField(max_length = 1000,blank = True) #optional field 
    def __str__(self):
        # This will display the first name and last name in the admin
        return f"{self.first_name} {self.last_name}"