from django.shortcuts import render

# Create your views here.
def article(request):
    '''
    render the article page
    '''
    return render(request, 'article/article.html')