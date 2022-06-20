from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class HoodTestClass(TestCase):
    def setUp(self):
        self.Kahawa = Hood(hood_name='Buru')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kahawa,Hood))


    def test_save_method(self):
        self.Kahawa.save_neighbourhood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Kahawa.delete_neighbourhood('Buru')
        hood = Hood.objects.all()
        self.assertTrue(len(hood)==0)
        
    def tearDown(self):
            Hood.objects.all().delete()    

class HealthDeptsTestClass(TestCase):
    def setUp(self):
        self.Dentist = Healthdepts(Health='Dentist')

    def test_instance(self):
        self.assertTrue(isinstance(self.Dentist,Healthdepts))


    def test_save_method(self):
        self.Dentist.save_healthdepts()
        health = Healthdepts.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Dentist.delete_healthdepts('Dentist')
        health = Healthdepts.objects.all()
        self.assertTrue(len(health)==0)
        
    def tearDown(self):
        Healthdepts.objects.all().delete()    
        
class BusinessTestClass(TestCase):
    def setUp(self):
        self.Dentist = Business(Health='Fashion')

    def test_instance(self):
        self.assertTrue(isinstance(self.Dentist,Business))

    def test_save_method(self):
        self.Fashion.save_business()
        biz = Business.objects.all()
        self.assertTrue(len(biz)>0)

    def test_delete_method(self):
        self.Fashion.delete_business('Fashion')
        biz = Business.objects.all()
        self.assertTrue(len(biz)==0) 
        
    def tearDown(self):
        Business.objects.all().delete()           