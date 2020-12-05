from django.db import models

# Create your models here.
Statuses = ( 
    ("d", "Draft"), 
    ("p","Publish"),
   
) 
class Author(models.Model):
    Author = models.CharField(max_length=50)

    def __str__(self):
        return (self.Author)


class Tag(models.Model):
    tag = models.CharField(max_length=20)


    def __str__(self):
        return (self.tag)


class Post(models.Model):
    
    Title = models.CharField(max_length=40)
    Slug = models.SlugField(unique=True)
    Brief = models.TextField(max_length=100)
    MainText=models.TextField()
    PostTag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='app/static/img/post'  , null=True)
    Status=models.CharField(max_length=20,choices=Statuses,default='p')

    


    class Meta:
        ordering = ['-date',]
    


    def __str__(self):
        return (self.Title)


class News(models.Model):
    
    Title = models.CharField(max_length=40)
    Slug = models.SlugField(unique=True)
    Brief = models.TextField(max_length=100)
    MainText=models.TextField()
    
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='app/static/img/post'  , null=True , default='app/static/img/post/default_news.jpg')
    Status=models.CharField(max_length=20,choices=Statuses,default='p')

    


    class Meta:
        ordering = ['-date',]
    


    def __str__(self):
        return (self.Title)


class Images_Info(models.Model):
    Title=models.CharField(max_length=50)
    Slug = models.SlugField(unique=True,blank=True)
    image = models.FileField(upload_to = 'app/static/img/meet',blank=True)

class Images(models.Model):
    image_rel = models.ForeignKey(Images_Info, default=None, on_delete=models.CASCADE)
    images_url = models.FileField(upload_to = 'app/static/img/meet',blank=True)

    def __str__(self):
        return self.image_rel.Title

class Calendar(models.Model):
    Title = models.CharField(max_length=50)
    MainText = models.TextField()

    def __str__(self):
        return self.Title

class Event(models.Model):
    Title = models.CharField(max_length=40)
    Slug = models.SlugField(unique=True)
    Brief = models.TextField(max_length=100)
    MainText=models.TextField()
    
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='app/static/img/events'  , null=True , default='app/static/img/events/default_news.jpg')
    Status=models.CharField(max_length=20,choices=Statuses,default='p')

    


    class Meta:
        ordering = ['-date',]
    


    def __str__(self):
        return (self.Title)