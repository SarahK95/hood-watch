
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    username = models.ForeignKey(User,  on_delete=models.CASCADE)
    bio = models.TextField(blank= True)
    email = models.EmailField()
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Hood (models.Model):
    hood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Occupants_count = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        
    # def __str__(self):
    #     return self.hood_name
    
    # def create_hood(self):
    #     self.save
    
    # def 
            
    
 
    
