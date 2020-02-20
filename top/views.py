from django.shortcuts import render, redirect
from .models import Photo, Wallet
from .forms import PhotoForm

# Create your views here.
def index(request):
    return render(request, 'top/index.html')

def wallet(request):
    last_wallet = Wallet.objects.last()
    context = {'last_wallet':last_wallet}
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