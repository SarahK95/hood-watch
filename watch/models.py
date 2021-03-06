import datetime as dt
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
    image = models.ImageField(upload_to='image/')
    
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
        self.save()
    
    @classmethod
    def delete_business(cls, business_name):
        cls.objects.filter(business_name=business_name).delete()
    
    @classmethod
    def find_business(cls, search_term):
        business = cls.cls.objects.filter(business_name__icontains = search_term)
        return business
    
    
    def update_business(self, business_name):
        self.business_name = business_name
        self.save()
        
class Healthdepts(models.Model):
    healthdepts = models.CharField(max_length=100)
    
    def __str__(self):
        return self.healthdepts
    
    def save_healthdepts(self):
        self.save()   
    
    
    @classmethod
    def delete_healthdepts(cls, healthdepts):
        cls.objects.filter(healthdepts=healthdepts).delete()
        
class Health(models.Model):
    logos = models.ImageField(upload_to='logos/')
    health_hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    health_name =models.CharField(max_length=100)
    emails = models.EmailField()
    contacts = models.IntegerField()
    addy =models.CharField(max_length=100)
    # healthdepts = models.ManyToManyField(healthdepts)

    def __str__(self):
        return self.health_name        
        
class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='image/')
    post = models.TextField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    hood= models.ForeignKey(Hood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title

    @classmethod
    def search_post(cls,search_term):
        posts = cls.objects.filter(title__icontains = search_term)
        return posts
    
class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)            

class Police(models.Model):
    police_hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    police_name =models.CharField(max_length=100)
    pemail = models.EmailField()
    pcontact = models.IntegerField()
    paddress =models.CharField(max_length=100)

    def __str__(self):
        return self.police_name

