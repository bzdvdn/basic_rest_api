from rest_framework import serializers

from postings.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer): # forms.ModelForm
	class Meta:
		model = BlogPost
		fields = [
			'pk',
			'user',
			'title',
			'content',
			'timestamp'
		]
		read_only_fields = ['user']
	# converts to JSON
	# validations for data passed

	def validate_titel(self, value):
		qs = BlogPost.objets.filter(title__iexact=value)
		if self.instance:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise serializers.validationsError("The title must be unique")
		return value