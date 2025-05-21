from django.shortcuts import render
from django.template import loader
from django.db import transaction
from .models import Account

	
# Create your views here.

def transfer(sender, receiver, amount):
    if amount <= 0:
        raise ValueError("Transfer amount must be more than 0")

    with transaction.atomic():
        acc1 = Account.objects.select_for_update().get(iban=sender)
        acc2 = Account.objects.select_for_update().get(iban=receiver)

        if acc1.balance < amount:
            raise ValueError("Sender does not have enough balance")

        if acc1 != acc2:
            acc1.balance -= amount
            acc2.balance += amount

            acc1.save()
            acc2.save()

def homePageView(request):
    if request.method == 'POST':
        sender = request.POST.get('from')
        receiver = request.POST.get('to')
        amount = request.POST.get('amount')

        try:
            if not amount:
                raise ValueError("Amount is required")

            amount = int(amount)

            transfer(sender, receiver, amount)

        except ValueError as e:
            accounts = Account.objects.all()
            context = {'accounts': accounts, 'error': str(e)}
            return render(request, 'pages/index.html', context)

    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, 'pages/index.html', context)



