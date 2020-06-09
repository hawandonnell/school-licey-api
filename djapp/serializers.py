from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = [ 'title', 'text', 'post_type', 'created_at', 'updated_at' ]