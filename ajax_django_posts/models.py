from django.db import models 
# Create your models here.
class DjangoAjaxPosts(models.Model):
    heading = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200,)
    description = models.TextField(default='Here description will be placed !')
    def __str__(self):
        return self.short_name
    def get_absolute_url(self):
        return f'/{self.url}/'
 
