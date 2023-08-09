from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import string
import random
from django.utils.text import slugify

# for unique slug 
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, null=True, blank=True,unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"slug": self.slug})       
