from django import forms
from .models import Photo, Wallet

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'situation']

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['money']