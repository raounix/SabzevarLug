from django.contrib import admin
from .models import Tag,Author,News,Images,Images_Info,Calendar,Event
# Register your models here.
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(News)
admin.site.register(Calendar)
admin.site.register(Event)
class PostImageAdmin(admin.StackedInline):
    model = Images
 
@admin.register(Images_Info)
class ImageAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Images_Info
 
