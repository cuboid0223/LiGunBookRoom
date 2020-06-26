from populate import base
from article.models import Article, Comment
from account.models import User

titles = ['如何像電腦科學家一樣思考','10分鐘內學好python','簡單學習Django']
comments = ['文章真棒', '並不認同你的觀點', '借分享', '學好一個程式語言或框架並不容易']


def populate():
   
    Article.objects.all().delete()
    Comment.objects.all().delete()
    admin = User.objects.get(is_superuser=True) 
    for title in titles:
        article = Article()
        article.title = title
        for j in range(20):
            article.content += title + '\n'
        article.save()
        for comment in comments:
            Comment.objects.create(article=article,content=comment, user=admin)
    print('done')
    print('populating articles and comments...')

if __name__=='__main__':
    populate()
