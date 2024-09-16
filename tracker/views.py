from django.shortcuts import render,redirect
from .models import *
from django.db.models import Sum
# Create your views here.
def index(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        current_balance , _ = CurrentBalance.objects.get_or_create(id=1)
        
        if float(amount)<0:
            expense_type = 'DEBIT'
        else:
            expense_type = 'CREDIT'

        tracking_history = TrackingHistory.objects.create(
            expense_type = expense_type,
            amount =amount,
            description = description,
            current_balance = current_balance
        )

        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()
        return redirect('/')
    
    income = 0
    expense = 0

    # This process is going to take a lot of time so its better to use aggregate function
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == "CREDIT":
            income += tracking_history.amount
        else:
            expense += tracking_history.amount
    
    current_balance , _ = CurrentBalance.objects.get_or_create(id=1)
    context = {'transactions':TrackingHistory.objects.all(), 'current_balance':current_balance,'income':income,'expense':expense}
    return render(request,'index.html',context)

def delete_transaction(request,id):
    tracking_history = TrackingHistory.objects.filter(id=id)
    if tracking_history.exists():
        current_balance , _ = CurrentBalance.objects.get_or_create(id=1)
        tracking_history = tracking_history[0]
        current_balance.current_balance -= tracking_history.amount
        current_balance.save()

    tracking_history.delete()
    return redirect('/')
