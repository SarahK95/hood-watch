
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hood (models.Model):
    hood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Occupants_count = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.hood_name
    
    def create_hood(self):
        self.save
    
    @classmethod
    def delete_hood(cls, hood_name):
        cls.objects.filter(hood_name=hood_name).delete()
    
    @classmethod
    def find_hood(cls, search_term):
        hoods = cls.cls.objects.filter(hood_name__icontains = search_term)
        return hoods
    
    
    def update_hood(self, hood_name):
        self.hood_name = hood_name
        self.save()
                
        
        
class Profile(models.Model):
    name = models.CharField(max_length=100)
    username = models.ForeignKey(User,  on_delete=models.CASCADE)
    bio = models.TextField(blank= True)
    email = models.EmailField()
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Business(models.Model):
    description = models.TextField(blank= True)
    hoody = models.ForeignKey(Hood,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    business_name =models.CharField(max_length=100)
    business_email = models.EmailField()
    contact = models.IntegerField()
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.business_name
    
    def create_business(self):
        self.save
    
    @classmethod
    def delete_business(cls, business_name):
        cls.objects.filter(business_name=business_name).delete()
    
    # @classmethod
    # def find_business(cls, search_term):
    #     business = cls.cls.objects.filter(business_name__icontains = search_term)
    #     return business
    
    
    # def update_business(self, business_name):
    #     self.business_name = business_name
    #     self.save()
    
 
    
