import uuid
from django.db import models


# Create your models here.
class FirstModel(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=128,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
class Author(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=128,blank=False,null=False)
    age=models.IntegerField()

class Publisher(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=128,blank=False,null=False)    
class Book(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=128,blank=False,null=False)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="book_author")
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE,related_name='books',null=True)
    
