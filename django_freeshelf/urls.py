"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books import views as books_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path ('', books_views.book_list, name='book_list'),
    path('accounts/', include('registration.backends.simple.urls')),
    
    #path ('geners/<slug:slug>)
]


## create some books (Urls =blank/null=) make books, 
# add URLS in book description once book detail page is made 

## get books displayed with all data

## order books recently added to the top

## create bookdetail 

## make sure urls are in working order/ set up html real good


## check phone for exapmle code pics for log in/registration



