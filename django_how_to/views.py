from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse 
from .models import *
import time,random
# Create your views here.
def index(request): 
    data = DjangoHowToPost.objects.all()
    return fetchpost(request,'Home')
    # return render(request, 'django-how-to/django-how-to.html', {'posts':data})


def fetchpost(request,url):  
    data = DjangoHowToPost.objects.all()
    page_info = data.get(url=url) 
    previous_item = data.filter(id=page_info.id-1).first()
    next_item = data.filter(id=page_info.id+1).first()
    pages = DjangoHowToPost.objects.all().exclude(url=url).exclude(url='Home')
    related_articles = random.sample(list(pages), len(pages)) 
    length1 = int((70*len(pages))/100) 
    if len(pages)<=10:length1=len(pages) 
    context = {
        'posts':data,
        'previous': previous_item,
        'next':next_item,
        'page_title':page_info.short_name,
        'article_heading': page_info.heading,
        'app_name': 'Django How To', 
        'related_articles':related_articles[:length1],
        'bottom_articles':related_articles[length1:]
    }
    return render(request, f'django-how-to/{url}/{url}.html', context)

 
 
 


def stateanalyzer(ip,title, limit):  
    # This will delete extra records who have passed their restricting time limit
    z = [x.delete() for x in IpTracker.objects.all() if (time.time()-x.time)>=limit]
    # This will prohibit duplication of records having same IP with same POST.
    if IpTracker.objects.filter(ip=ip,post=Post.objects.get(title=title)):
        pass
    # This will create record of new visitor and will not peroform checking.
    elif not IpTracker.objects.filter(ip=ip,post=Post.objects.get(title=title)):
        IpTracker(ip=ip,time=time.time(),post=Post.objects.get(title=title)).save()
        return True
    # This section will check either visitor is visiting page frequently within time limit or not.
    located_ip = IpTracker.objects.get(ip=ip,post=Post.objects.get(title=title))
    submit_time = IpTracker.objects.get(ip=ip,post__title=title).time 
    currnt_time = time.time()
    difference = currnt_time-submit_time
    if difference>limit:
        located_ip.time=time.time()
        located_ip.save()
        return True
    else:
        return False 
 
def testfetchpostusingip(request,ip,title):   
    posts = Post.objects.all()  
    requested_post = Post.objects.get(title=title)  
    if stateanalyzer(ip,title, 30):
        requested_post.page_views = requested_post.page_views + 1
        requested_post.save()
    context = {
        'posts':posts, 
        'requested_post': requested_post,
    } 
    return JsonResponse({'title':requested_post.title, 'views':requested_post.page_views})