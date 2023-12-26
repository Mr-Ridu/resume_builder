from django import forms
from .models import Resume,Education,experiance,certification,awards


class basicforms(forms.ModelForm):
    class Meta:
        model  = Resume
        fields = '__all__'

class educationform(forms.ModelForm):
    class Meta:
        model  = Education
        fields = '__all__'
        exclude = ['resume']

class experianceform(forms.ModelForm):
    class Meta:
        model  = experiance
        fields = '__all__'
        exclude = ['resume']

class certificateform(forms.ModelForm):
    class Meta:
        model  = certification
        fields = '__all__'
        exclude = ['resume']

class awardsform(forms.ModelForm):
    class Meta:
        model  = awards
        fields = '__all__'
        exclude = ['resume']