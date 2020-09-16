from django.db import models

# Create your models here.
class DjangoHowToPost(models.Model):
    heading = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200,blank=True)
    description = models.TextField(default='Here description will be placed !')
    def __str__(self):
        return self.short_name
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    page_views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    
class IpTracker(models.Model):
    ip = models.GenericIPAddressField()
    time = models.IntegerField()
    print(time)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.ip