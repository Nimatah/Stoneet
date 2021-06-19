from django.db import models
from django.core.cache import cache

from mptt.models import MPTTModel, TreeManager, TreeForeignKey


class RegionManager(TreeManager):

    def get_root(self):
        return self.filter(mptt_level=0)

    def get_leaf(self):
        return self.filter(children__isnull=True)

    def to_context(self):
        key = "location_context"
        timeout = 30 * 24 * 60 * 60
        cached_results = cache.get(key)
        if cached_results:
            return cached_results
        results = [r.to_dict_hierarchy() for r in self.get_root().prefetch_related('children')]
        cache.set(key, results, timeout)
        return results


class Region(MPTTModel):
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RegionManager()

    class MPTTMeta:
        level_attr = 'mptt_level'

    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self) -> str:
        return self.title

    def to_dict_hierarchy(self):
        return {
            'id': self.id,
            'title': self.title,
            'children': [c.to_dict_hierarchy() for c in self.children.all()]
        }

