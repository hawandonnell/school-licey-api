from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status


class PostView(views.APIView):

	# Get all instances
	def get(self, request, format=None):
		queryset = Post.objects.all().order_by('-updated_at')
		serializer = PostSerializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	# Create instance
	def put(self, request, format=None):
		post = Post(title=request.data.get('title'), text=request.data.get('text'), post_type=request.data.get('post_type'))
		post.save()
		serializer = PostSerializer(post)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostPKView(views.APIView):

	# Delete existing instance
	def delete(self, request, format=None, pk=None):
		queryset = Post.objects.get(pk=pk).delete()
		serializer = PostSerializer(queryset)
		return Response(serializer.data, status=status.HTTP_200_OK)

	# Change existing instance
	def post(self, request, format=None, pk=None):
		post = Post.objects.get(pk=pk)
		post.title = request.data.get('title')
		post.text = request.data.get('text')
		post.post_type = request.data.get('post_type')
		post.save()
		serializer = PostSerializer(post)
		return Response(serializer.data, status=status.HTTP_200_OK)