from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    desription = models.TextField(blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    slug = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def get_absolute_url(self):
        parents = self.get_all_parents()
        return '/%s/' % ('/'.join([p.slug for p in parents]))
        
    def get_all_parents(self):
        "Gets all parents going up the parent tree until a page with no parent, including itself."
        parents = []
        category = self
        while True:
            parents.insert(0, page)
            category = category.parent
            if not category:
                break
        return parents

    def get_children(self):
        "Gets children of current category, no grandchildren."
        return Category.objects.filter(parent=self.id)

    def get_all_siblings(self):
        "Gets siblings of current category only, no children of siblings."
        return Category.objects.filter(parent=self.category)
        #return "/%i/" % (self.slug)