from django.contrib import admin
from .models import Movies, MyCategory,MyLanguges,BookMovie
# Register your models here.

admin.site.register(MyCategory)
admin.site.register(MyLanguges)
admin.site.register(Movies)
admin.site.register(BookMovie)
