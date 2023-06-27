from django import forms
from .models import Contact

class ContactForm(forms.Form):
    first_name = forms.CharField(label="Ім'я",widget=forms.TextInput(attrs={"placeholder":"Ім'я","required":True,'class':'form-control'}),error_messages={"required":"Ім'я не може бути порожнім"})
    last_name = forms.CharField(label="Прізвище",widget=forms.TextInput(attrs={"placeholder":"Прізвище","required":True,'class':'form-control'}),error_messages={"required":"Прізвище не може бути порожнім"})
    email = forms.EmailField(label="E-mail",widget=forms.EmailInput(attrs={"required":True,"Placeholder":"E-mail",'class':'form-control'}),error_messages={'required':'Поля електронної пошти не повинні бути порожніми'})
    message = forms.CharField(min_length=20,label="Повідомлення", widget=forms.Textarea(attrs={'placeholder': 'Ваше повідомлення','class':'form-control'}))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']

