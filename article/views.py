from django.shortcuts import render, redirect, get_object_or_404
from article.models import Article,Comment #從 articel/models.py 匯入 Article 這個class model
from article.forms import ArticleForm #
from django.contrib import messages # INSTALLED_APPS 裡的 django.contrib.message 訊息框架
from django.db.models.query_utils import Q #Django 用來處理搜尋
# Create your views here.
def article(request):
    '''
    render the article page
    '''
    articles={article:Comment.objects.filter(article=article) for article in Article.objects.all()} #取出所有文章資料

    context={'articles':articles}
    return render(request, 'article/article.html',context)

def articleCreate(request):
    '''
    Create a new article instance
    1. If method is GET, render an empty form
    2.  如果是POST請求，表示使用者新增完畢並送出表單，系統驗證資料是否正確，如果資料錯誤
        就回覆錯誤訊息，否則就將資料存入資料庫，最後轉到文章列表頁面
    '''
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'articleForm':ArticleForm()})
    articleForm = ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    articleForm.save()
    messages.success(request,'文章已新增')
    return redirect('article:article')

def articleRead(request, articleId):
    '''
    Read
    '''
    article = get_object_or_404(Article, id=articleId)
    context = {
        'article': article,
        'comment': Comment.objects.filter(article=article)
    }

    return render(request, 'article/articleRead.html', context)

def articleUpdate(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm =  ArticleForm(instance=article)
        return render(request, template, {'articleForm':articleForm})
    #POST
    articleForm = ArticleForm(request.POST, instance=article)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    
    articleForm.save()
    messages.success(request, '文章已修改')
    return redirect('article:articleRead', articleId=articleId)

def articleDelete(request, articleId):
    if request.method == 'GET':
        return render('article:article')
    #POST
    article = get_object_or_404(Article, id=articleId)
    article.delete()
    messages.success(request, '文章已刪除')
    return redirect('article:article')

def articleSearch(request):
    searchTerm = request.GET.get('searchTerm')
    articles = Article.objects.filter(Q(title__icontains=searchTerm) | Q(content__icontains=searchTerm))
    context = {'articles':articles, 'searchTerm':searchTerm}
    return render(request, 'article/articleSearch.html', context)