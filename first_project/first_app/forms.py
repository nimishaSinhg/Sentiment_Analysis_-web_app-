from django import forms
from models import csvfiles

class csvfiles(forms.ModelForm):   
    class Meta:      
      model = csvfiles        
      fields = ( 'file_input',)