from django.conf import settings
from django.db import models
from django.utils import timezone


# following will give all blogpost of the first user
# from dhango.contrib.auth import get_user_model
# User = get_user_model()
# j = User.objects.first() 
# j.blogpost_set_all() -> blogpost_set = queryset

# from blog.models import BlogPost
# qs = BlogPost.objects.filter(user__id = 1)

# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(published_date__lte = now)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()



class BlogPost(models.Model):
    # id = models.IntegerField() # pk
    # on_delete=models.CASCADE
    
    user = models.ForeignKey(User, default=1, null=True,  on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/', blank=True, null=True)#Pillow is library allows to use ImageField
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True) # hello world -> hello-world
    content = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        # - To get most recent first
        ordering = ['-published_date', '-updated', '-timestamp' ]

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

