from django.shortcuts import render
from .forms import CustomerForm
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializers
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

@csrf_exempt
@api_view(["POST"])
# Create your views here.
def chatbot_input(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return JsonResponse({"success": True, "message": "Data customer berhasil disimpan"})
        
        return JsonResponse({"success": False, "message": "Validasi form gagal", "errors": form.errors})
    else:
        form = CustomerForm()
        return render(request,"input_form.html", {"form": form})

@csrf_exempt
@api_view(["POST"])    
def chatbot_serializer(request):
    if request.method == "POST":
        serializer = CustomerSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "message":"data customer berhasil disimpan"})
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def get_data(request):
    if request.method == "GET":
        customers=Customer.objects.all()
        serializer = CustomerSerializers(customers, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)