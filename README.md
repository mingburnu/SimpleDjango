# SimpleDjango

> pip install ipython

> pip install djangorestframework

> mkdir templates

> python manage.py startapp trips

<a href="https://github.com/mingburnu/SimpleDjango/blob/master/SimpleDjango/settings.py">edit /SimpleDjango/settings.py</a>

    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            ...
        },
    ]

    INSTALLED_APPS = [
        ...
        'trips',
	    'rest_framework',
    ]
    
    LOGIN_REDIRECT_URL = '/'


<a href="https://github.com/mingburnu/SimpleDjango/blob/master/trips/models.py">edit /SimpleDjango/trips/models.py</a>

    from django.db import models
    
    class Post(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField(blank=True)
        photo = models.URLField(blank=True)
        location = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


<a href="https://github.com/mingburnu/SimpleDjango/blob/master/trips/PostSerializer.py">edit SimpleDjango/trips/PostSerializer.py</a>

<a href="https://github.com/mingburnu/SimpleDjango/blob/master/trips/admin.py">edit /SimpleDjango/trips/admin.py</a>
   
    admin.site.register(Post)


> python manage.py makemigrations<br>
> python manage.py migrate<br>

> python manage.py createsuperuser

> python manage.py shell

> from trips.models import Post<br>
> Post.objects.create(title='My First Trip', content='肚子好餓，吃什麼好呢?', location='台北火車站')<br>
> Post.objects.create(title='My Second Trip', content='去散散步吧', location='大安森林公園')<br>
> Post.objects.create(title='Django 大冒險', content='從靜態到動態', location='台北市大安區復興南路一段293號')<br>
> Post.objects.create(title='My Tainan Trip', content='府城之旅', location='台南火車站')<br>
> Post.objects.all()<br>
> Post.objects.filter(id=1).update(photo='http://images.undiff.net/articles/2015/2015-07-25/_Featured.jpg')<br>
> Post.objects.filter(id=2).update(photo='http://pic.pimg.tw/dinosaurs/1386222553-3967104467.jpg')<br>
> Post.objects.filter(id=3).update(photo='http://www.yolks.ca/wp-content/uploads/2015/03/slider2.jpg')<br>
> Post.objects.filter(id=4).update(photo='https://i.ytimg.com/vi/B4y9BvPIyr0/maxresdefault.jpg')<br>
> Post.objects.get(pk=1)<br>
> Post.objects.filter(location__contains='台北')<br> 
> posts = Post.objects.filter(title__contains='Trip')<br>
> posts<br>
> posts[0].location<br>
> posts[1].location<br>
> posts.update(location='象山親山步道')<br>
> posts.delete()<br>

<a href="https://github.com/mingburnu/SimpleDjango/blob/master/trips/views.py">edit SimpleDjango/trips/views.py</a>

<a href="https://github.com/mingburnu/SimpleDjango/blob/master/trips/urls.py">edit SimpleDjango/trips/urls.py</a>

<a href="https://github.com/mingburnu/SimpleDjango/blob/master/SimpleDjango/urls.py">edit SimpleDjango/urls.py</a>

<a href="https://github.com/mingburnu/SimpleDjango/tree/master/templates">edit SimpleDjango/templates/xxxx.html</a>

<a href="http://127.0.0.1:8000">127.0.0.1:8000</a><br>
<a href="http://127.0.0.1:8000/api">127.0.0.1:8000/api</a>

### REFERECE
<a href="https://www.gitbook.com/book/djangogirlstaipei/django-girls-taipei-tutorial/details">Django Girls 學習指南</a><br>
<a href="https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html">How to Use Django's Built-in Login System</a><br>
<a href="http://getalusmind.blogspot.tw/2016/05/django-rest-framework-restful-api.html">django-rest-framework 十分鐘架一個簡單的 restful api</a><br>
<a href="https://eureka.ykyuen.info/2015/04/07/django-rest-framework-setting-permissions/">DJANGO REST FRAMEWORK – SETTING PERMISSIONS</a><br>
