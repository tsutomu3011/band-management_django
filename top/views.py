from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'top/index.html')

def wallet(request):
  return render(request, 'top/wallet.html')

def photo(request):
  return render(request, 'top/photo.html')

