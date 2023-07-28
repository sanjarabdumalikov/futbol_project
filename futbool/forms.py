
from django import  forms
from .models import Place
class FootballForms(forms.ModelForm):
      name_uz = forms.CharField()
      name_en = forms.CharField()



      class Meta:
         model =Place
         exclude=['name',]
