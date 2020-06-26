from populate import base
from account.models import User




def populate():
    User.objects.all().delete()
    User.objects.create_superuser(username='AHong', password='2288037yyy', email=None, fullName='阿泓')
    print('Creating admin account.....')
    print('done')

if __name__=='__main__':
    populate()