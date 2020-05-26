from django.db import models

# Create your models here.
Statuses = ( 
    ("d", "Draft"), 
    ("p","Publish"),
   
) 

class Tag(models.Model):
    tag = models.CharField(max_length=20)


    def __str__(self):
        return (self.tag)


class Post(models.Model):
    Title = models.CharField(max_length=40)
    Brief = models.TextField(max_length=100)

    MainText=models.TextField()
    PostTag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    Status=models.CharField(max_length=20,choices=Statuses,default='p')


    def __str__(self):
        return (self.Title)

