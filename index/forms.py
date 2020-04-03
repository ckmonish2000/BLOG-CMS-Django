from django import forms


class mainform(forms.Form):
    title=forms.CharField(max_length=200)
    body=forms.CharField(max_length=800)
    link=forms.CharField(max_length=600)
    file=forms.FileField()