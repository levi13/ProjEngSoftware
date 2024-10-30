from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'hora', 'descricao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }
