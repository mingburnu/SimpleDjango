"""SimpleDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

from trips.views import hello_world, home, post_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello_world),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
    url(r'^$', login_required(home, login_url='login'), name='home'),
    url(r'^post/(?P<pk>\d+)/$', login_required(post_detail, login_url='login'), name='post_detail'),
    url(r'^api/', include('trips.urls')),
]
