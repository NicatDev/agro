from django import forms
from .models import Message

class Messageform(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'
    
        
    def __init__(self,*args,**kvargs):
        super(Messageform,self).__init__(*args,**kvargs)
    