from django import forms
from delivery.models import Deliverymodel
class deliveryform(forms.ModelForm):
    class Meta:
        model = Deliverymodel
        fields = '__all__'
        widgets = {
            'username':forms.TextInput(attrs={'readonly':'readonly'})
        }