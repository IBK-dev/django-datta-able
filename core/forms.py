from django import forms  
from société.models import société  
class sociétéForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  
