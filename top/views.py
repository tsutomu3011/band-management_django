from django.shortcuts import render, redirect
from .models import Photo, Wallet
from .forms import PhotoForm, WalletForm

# Create your views here.
def index(request):
    return render(request, 'top/index.html')

def wallet(request):
    if request.method == "POST":
        send_money = request.POST
        total_wallet = Wallet.objects.last().money + int(send_money['money'])
        Wallet.objects.create(money=total_wallet)
        return redirect('top:wallet')
    else:
        wallet_bar = 0
        wallet_deficit_bar = 0
        # if Wallet.objects.last().money >= 0:
        #     wallet_bar = Wallet.objects.last().money
        # else:
        #     wallet_deficit_bar = Wallet.objects.last().money * -1
        last_wallet = Wallet.objects.last()
        form = WalletForm()
        context = {'last_wallet':last_wallet, 'form':form, 'wallet_bar':wallet_bar, 'wallet_deficit_bar':wallet_deficit_bar}
        return render(request, 'top/wallet.html', context)

def photo(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('top:photo')
    else:
        form = PhotoForm()
        photos = Photo.objects.all()
        context = {'photos':photos, 'form':form}
        return render(request, 'top/photo.html', context)