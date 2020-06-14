from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main(request):
    '''
    Render the main page
    '''
    html = '''
    <!doctype html>
    <html>
    <head>
    <title>my blog</title>
    <meta charset = "utf-8">
    </head>
    <body>
    <p>this is a html Hello World!</p>
    </body>
    </html>
    '''
    return HttpResponse(html)