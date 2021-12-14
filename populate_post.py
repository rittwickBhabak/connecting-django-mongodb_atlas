import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') 

import django 
django.setup() 

from myapp.models import Post 
from faker import Faker 
import random 

fakegen = Faker() 

def populate(N=5):

    for entry in range(N):
        print(f'Populating {entry}th post...')
        title = fakegen.sentence().title().replace('.', '')
        text = [fakegen.sentence() for i in range(random.randint(20,40))]

        # New entry 
        Post.objects.create(title=title, text=' '.join(text))



if __name__ == "__main__":
    print('Populating...')
    populate(80)
    print('Complete!')   