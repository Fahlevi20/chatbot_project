from django.shortcuts import render
from .forms import CustomerForm
from django.http import JsonResponse

# Create your views here.
def chatbot_input(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return JsonResponse("")