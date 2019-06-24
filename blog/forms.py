from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog # 블로그 모델
        # 필드 종류 = {"name", "leader", "create_date", "location", "introduce"}
        fields = '___all__'
        exclude = ['pub_date'] # name 필드 사용 안함

        widgets = {'title' : forms.TextInput(attrs={'class' : 'form-control'})},
        'body' : forms.Textarea(attrs={'class' : 'form-control'}),