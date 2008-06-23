from django.db import models

# Create your models here.
class Tag(models.Model):
	"""Basic tagging feature"""
	name = models.CharField(max_length=50, unique=True, db_index=True)
	slug = models.SlugField(prepopulate_from=("name",))
	
	class Meta:
		ordering = ('name',)
		verbose_name = ('tag')
		verbose_name_plural = ('tags')

	class Admin:
		pass
		
	def __unicode__(self):
		return self.name