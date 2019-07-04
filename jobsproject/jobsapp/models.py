from django.db import models

# Create your models here.
class Hydjobsinfo(models.Model):
    Date =models.DateField()
    Company = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    Eligibility = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Email = models.EmailField()
    PhoneNumber = models.IntegerField()

class Delhijobsinfo(models.Model):
    Date =models.DateField()
    Company = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    Eligibility = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Email = models.EmailField()
    PhoneNumber = models.IntegerField()

class Punejobsinfo(models.Model):
    Date =models.DateField()
    Company = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    Eligibility = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Email = models.EmailField()
    PhoneNumber = models.IntegerField()

class Noidajobsinfo(models.Model):
    Date =models.DateField()
    Company = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    Eligibility = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Email = models.EmailField()
    PhoneNumber = models.IntegerField()