from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class': 'form-control'}), label='')
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class': 'form-control'}), label='')
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder':'Email', 'class': 'form-control'}), label='')
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder':'Phone', 'class': 'form-control'}), label='')
    address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Address', 'class': 'form-control'}), label='')
    city = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'City', 'class': 'form-control'}), label='')
    
    class Meta:
        model = Record
        exclude = ("user",)