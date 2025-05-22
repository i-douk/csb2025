from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required
def addView(request):
    if request.method == 'POST':
        try:
            iban = request.POST.get('iban')
            if not iban:
                return JsonResponse({'error': 'IBAN is required'}, status=400)
            
            if Account.objects.filter(owner=request.user, iban=iban).exists():
                return JsonResponse({'error': 'IBAN already exists'}, status=400)
            
            Account.objects.create(owner=request.user, iban=iban)
            return redirect('/')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    

@login_required
def homePageView(request):

	logged = request.user
	accounts = Account.objects.filter(owner=logged)
	print(logged)
	return render(request, 'pages/index.html',{"accounts": accounts})
