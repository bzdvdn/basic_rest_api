# generic
from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostAPIView(generics.ListAPIView): # DetailView CreateView FormView
	lookup_field 		= 'pk'
	serializer_class	= BlogPostSerializer

	#queryset			= BlogPost.objects.all()

	def get_queryset(self):
		return BlogPost.objects.all()

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		return 


	# def get_object(self):
	# 	pk = self.kwargs.get("pk")
	# 	return BlogPost.objects.all()



class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
	lookup_field 		= 'pk'
	serializer_class	= BlogPostSerializer

	#queryset			= BlogPost.objects.all()

	def get_queryset(self):
		return BlogPost.objects.all()

	# def get_object(self):
	# 	pk = self.kwargs.get("pk")
	# 	return BlogPost.objects.all()
