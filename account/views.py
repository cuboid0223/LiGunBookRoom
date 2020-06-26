from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from account.forms import UserForm
from django.contrib.auth import authenticate #會員登入
from django.contrib.auth import login as auth_login #會員登入 #因為稱登入函式為login故將 Django 函式改名
from django.contrib.auth import logout as auth_logout #會員登出 #因為稱登出函式為logout 故將 Django 函式改名
from django.contrib.auth.decorators import login_required  # 未登入者存取限制

def register(request): #會員註冊
    template = 'account/register.html'
    if request.method == 'GET':
        return render(request, template, {'userForm':UserForm()})
    
    #POST
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, template, {'userForm':userForm})

    userForm.save()
    messages.success(request, '歡迎註冊')
    return redirect('main:main')

def login(request): #會員登入
    '''
    login existing users
    '''
    template = 'account/login.html'
    #GET
    if request.method == 'GET':
        return render (request, template, {'nextURL':request.GET.get('next')})

    #POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        messages.error(request, '請填資料')
        return render(request, template)
    
    user = authenticate(username=username, password=password)
    if not user:
        messages.error(request, '登入失敗')
        return render(request, template)
    
    #login success
    auth_login(request, user)
    nextURL = request.POST.get('nextURL')
    if nextURL:
        return redirect(nextURL)
    messages.success(request, '登入成功')
    return redirect('main:main')

@login_required
def logout(request): #會員登出
    auth_logout(request)
    messages.success(request, '您已登出')
    return redirect('main:main')


