from django.db import models

# Create your models here.
class Tag(models.Model):
	"""Basic tagging feature"""
	name = models.CharField(_('name'), max_length=50, unique=True, db_index=True, validator_list=[isTag])
	slug = models.SlugField(prepopulate_from=("name",))
	
	class Meta:
        ordering = ('name',)
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

	class Admin:
		pass

    def __unicode__(self):
        return self.name