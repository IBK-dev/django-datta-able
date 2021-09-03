from django import forms  
from app.models import société  
class sociétéForm(forms.ModelForm):  
    class Meta:  
        model = société  
        fields = "__all__"  
