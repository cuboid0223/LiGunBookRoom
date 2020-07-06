from django import forms
from account.models import User


from django.core.files.images import get_image_dimensions#使用者頭像


class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    password = forms.CharField(label='密碼', widget=forms.PasswordInput)
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput)
    fullname = forms.CharField(label='姓名', max_length=128)
    website = forms.URLField(label='個人網址', max_length=128, required=False)
    address = forms.CharField(label='住址', max_length=128, required=False)# required=False 表示非必填選項欄
    avater = forms.ImageField(label='頭貼', required=False)  # 使用者頭像
    class Meta:
        model = User
        fields = '__all__'
    
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

    def clean_avatar(self):  # 使用者頭像
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar


    
