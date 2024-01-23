from django.db import models
import os

class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    repassword = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.firstname}\t{self.lastname}\t{self.email}\t{self.username}\t{self.password}\t{self.repassword}"
    
class Product(models.Model):
    
    urun_adi = models.CharField(max_length=100, null=True)
    urun_kategori = models.CharField(max_length=100, null=True)
    urun_aciklamasi = models.CharField(max_length=250, null=True)
    urun_durum = models.CharField(max_length=250, null=True)
    urun_mekani = models.CharField(max_length=200, null=True)
    sehir = models.CharField(max_length=50, null=True)
    universite = models.CharField(max_length=100)
    gorsel = models.ImageField(upload_to='blog/static/image/urun_gorselleri', blank=True, null=True)
    karsi_takas = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f"{self.urun_adi}\t{self.urun_kategori}\t{self.urun_aciklamasi}\t{self.urun_durum}\t{self.urun_mekani}\t{self.sehir}\t{self.universite}\t{self.gorsel}\t{self.karsi_takas}"   
# Create your models here.
#yukaridaki gibi bir veri kumesi olusturduktan sonra pyhton manage.py makemigrations yaparak
#migrations dosyasini initial ettik 0001 dosyasi icerisnde gelen bilgiler onemli