from rest_framework import serializers
from advance_serilize.models import Author, Publisher,Book

class CreateFirstSerializer(serializers.Serializer):
    title=serializers.CharField()

    def validate(self, attrs):
        if attrs.get('title') and len(attrs.get('title'))>20:
            raise serializers.ValidationError('title is too long')
        return attrs
    def to_representation(self,data):
        representation=super().to_representation(data)

        title_value=data.get('title',None)
        if title_value:
            representation['title2']=f"custom {title_value}"
        return representation

class AuthorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model=Author  
        fields='__all__'  
class BookModelSerializer(serializers.ModelSerializer):
    author=AuthorModelSerializer(read_only=True)
    class Meta:
        model=Book   
        fields=('uuid','title','author') 
class PublisherModelSerializer(serializers.ModelSerializer):
    books=BookModelSerializer(many=True, read_only=True)
    class Meta:
        model=Publisher
        fields=('uuid','name','books')
