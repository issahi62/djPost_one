from django.db import models
from django.conf import settings 

USER = settings.AUTH_USER_MODEL

class Post(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey('Author', related_name='author', on_delete=models.CASCADE)
    image = models.ImageField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Author(models.Model):
	user = models.ForeignKey(USER, on_delete = models.CASCADE)
	email = models.EmailField()
	contact = models.IntegerField()# '+233'


	def __str__(self): 
		return self.user.username
    
	
		
    
