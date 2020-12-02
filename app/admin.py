from django.contrib import admin
from .models import Post,Tag,Author,News,Images,Images_Info
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(News)


class PostImageAdmin(admin.StackedInline):
    model = Images
 
@admin.register(Images_Info)
class ImageAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Images_Info
 
