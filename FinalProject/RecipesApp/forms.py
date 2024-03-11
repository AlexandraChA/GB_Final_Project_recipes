from django import forms


class RecipeForm(forms.Form):
    name = forms.CharField(max_length=100)
    desc =  forms.CharField(max_length=200)
    steps = forms.CharField(max_length=200)
    time_minutes = forms.IntegerField()
    photo = forms.ImageField(required = False)
    author = forms.CharField(max_length=100)