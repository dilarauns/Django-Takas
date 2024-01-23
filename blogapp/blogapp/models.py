from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    repassword = models.CharField(max_length=50)
    urun_adi = models.CharField(max_length=100)
    sehir = models.CharField(max_length=50)
    universite = models.CharField(max_length=100)
    gorsel = models.ImageField(upload_to='urun_gorselleri/', blank=True, null=True) 
    
    def __str__(self):
        return f"{self.firstname}\t{self.lastname}\t{self.email}\t{self.username}\t{self.password}\t{self.repassword}\t{self.urun_adi}\t{self.sehir}\t{self.universite}\t{self.gorsel}"

    