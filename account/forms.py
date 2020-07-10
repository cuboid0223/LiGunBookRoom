from django import forms
from account.models import User




class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號', widget=forms.TextInput(attrs={'class': 'userForm'}))
    password = forms.CharField(label='密碼', widget=forms.PasswordInput and forms.TextInput(attrs={'class': 'userForm'}))
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput and forms.TextInput(attrs={'class': 'userForm'}))
    fullName = forms.CharField(label='暱稱', max_length=8, widget=forms.TextInput(attrs={'class': 'userForm'}))
    website = forms.URLField(label='個人網址', max_length=128, required=False, widget=forms.TextInput(attrs={'class': 'userForm'}))
    address = forms.CharField(label='住址', max_length=128, required=False, widget=forms.TextInput(attrs={'class': 'userForm'}))# required=False 表示非必填選項欄
    class Meta:
        model = User
        fields = ['username','password','password2','fullName']
        widgets = {
            # 加入css 配合 widget=forms.TextInput(attrs={'class': 'userForm'})
            'userForm': forms.TextInput(attrs={'class': 'userForm'}),
        }
    
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return password2

    def save(self):
        user = super().save(commit=False)
        user.set_password(user.password)
        user.save()
        return user

    
    
