from django.contrib import admin
from advance_serilize.models import FirstModel,Author,Publisher,Book
# Register your models here.
admin.site.register(FirstModel)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)