from django.db import models

# Create your models here.
class Customer(models.Model):
    nama = models.CharField(max, length=100)
    nomor_telepon = models.CharField(max,length=100)
    email = models.EmailField()
    alamat = models.TextField()

    def __str__(self):
        return self.nama
