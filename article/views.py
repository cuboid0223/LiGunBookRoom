from django.shortcuts import render, redirect, get_object_or_404
from article.models import Article,Comment #從 articel/models.py 匯入 Article 這個class model
from article.forms import ArticleForm #
from django.contrib import messages # INSTALLED_APPS 裡的 django.contrib.message 訊息框架
from django.db.models.query_utils import Q #Django 用來處理搜尋
from django.contrib.auth.decorators import login_required #未登入者存取限制
from main.views import admin_required

 # Create your views here.
def article(request):
    '''
    render the article page
    '''
    articles={article:Comment.objects.filter(article=article) for article in Article.objects.all()} #取出所有文章資料

    context={'articles':articles}
    return render(request, 'article/article.html',context)

@admin_required
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


@admin_required
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


@admin_required
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

@login_required
def articleLike(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    if request.user not in article.likes.all():
        article.likes.add(request.user)
    else:#收回愛心
        article.likes.remove(request.user)
    #return articleRead(request, articleId)
    return redirect('article:article')


@login_required
def commentCreate(request, articleId):
    if request.method == 'GET':
        return render(request, articleId)
    #POST
    comment = request.POST.get('comment')
    if comment:
        comment = comment.strip()
    if not comment:
        return redirect('article:articleRead', articleId=articleId)
    
    article = get_object_or_404(Article, id=articleId)
    Comment.objects.create(article=article, user=request.user, content=comment)
    #return redirect('article:articleRead', articleId=articleId)
    return redirect('article:article')


@login_required
def commentUpdate(request, commentId):
    commentToUpdate = get_object_or_404(Comment, id=commentId)
    article = get_object_or_404(Article, id=commentToUpdate.article.id)
    if request.method == 'GET':
        return article(request, article.id)
    #POST
    if commentToUpdate.user != request.user:
        messages.error(request, '你當你阿泓喔？') 
        # return redirect('article:articleRead', articleId=article.id)
        return redirect('article:article')
    comment = request.POST.get('comment', '').strip()
    if not comment:
        commentToUpdate.delete()
    else:
        commentToUpdate.content = comment
        commentToUpdate.save()
    return redirect('article:article')


@login_required
def commentDelete(request, commentId):
    comment=get_object_or_404(Comment, id=commentId)
    article=get_object_or_404(Article, id=comment.article.id)
    if request.method == 'GET':
        return articleRead(request, article.id)
    if comment.user != request.user:
        messages.error(request, '無刪除權限')
        # return redirect('article:articleRead', articleId=article.id)
        return redirect('article:article')
    comment.delete()
    # return redirect('article:articleRead', articleId=article.id)
    return redirect('article:article')
