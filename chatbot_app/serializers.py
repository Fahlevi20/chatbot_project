from rest_framework import serializers
from .models import Customer

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id","nama", "nomor_telepon","email","alamat"]


        