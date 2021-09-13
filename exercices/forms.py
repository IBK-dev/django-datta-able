from django import forms
from .models import Exercices

class exercicesForm(forms.ModelForm):
    class Meta:
      model = Exercices
      fields = '__all__'