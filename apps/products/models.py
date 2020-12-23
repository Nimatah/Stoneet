from django.db import models

from mptt.models import MPTTModel, TreeManager, TreeForeignKey

from apps.core.models import TimestampedModel, BaseMedia
from apps.users.models import User


class AttributeManager(models.Manager):

    pass


class CategoryManager(TreeManager):

    def get_root(self):
        return self.filter(mptt_level=0)

    def get_leaf(self):
        return self.filter(children__isnull=True)


class ProductManager(models.Manager):
    pass


class VariantManager(models.Manager):
    pass


class Attribute(TimestampedModel):
    TYPE_BOOL = 'bool'
    TYPE_STR = 'str'
    TYPE_INT = 'int'
    TYPE_FLOAT = 'float'
    TYPE_IMAGE = 'image'
    TYPE_DROPDOWN = 'dropdown'

    _TYPE_CHOICES = (
        (TYPE_BOOL, 'Boolean',),
        (TYPE_STR, 'String',),
        (TYPE_INT, 'Integer',),
        (TYPE_FLOAT, 'Float',),
        (TYPE_IMAGE, 'Image',),
        (TYPE_DROPDOWN, 'Dropdown',),
    )

    PRODUCT_TYPE_CONSTANT = "Product"
    PRODUCT_TYPE_VARIANT = "Variant"

    _PRODUCT_TYPE = (
        (PRODUCT_TYPE_CONSTANT, "Product",),
        (PRODUCT_TYPE_VARIANT, "Variant",),
    )

    title = models.CharField(max_length=255)
    value_type = models.CharField(max_length=255, choices=_TYPE_CHOICES)
    options = models.TextField(null=True, blank=True)
    unit = models.CharField(max_length=255, blank=True)
    is_required = models.BooleanField(default=False)
    view_in_product_page = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)

    objects = AttributeManager()

    def __str__(self) -> str:
        return self.title

    @property
    def dropdown(self):
        return self.options.split("|")

    def is_valid(self, value) -> bool:
        if self.value_type == Attribute.TYPE_BOOL:
            return self.__validate_boolean(value)
        elif self.value_type == Attribute.TYPE_INT:
            return self.__validate_int(value)
        elif self.value_type == Attribute.TYPE_FLOAT:
            return self.__validate_float(value)
        elif self.value_type == Attribute.TYPE_DROPDOWN:
            return self.__validate_dropdown(value)
        else:
            return True

    @staticmethod
    def __validate_boolean(value) -> bool:
        return value.lower() in ('true', 'false',)

    @staticmethod
    def __validate_int(value) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def __validate_float(value) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    def __validate_dropdown(self, value) -> bool:
        return value in self.options.split('|')


class AttributeMedia(BaseMedia):

    product_attribute = models.ForeignKey('ProductAttribute', on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='attributes')

    def __str__(self) -> str:
        return f'{self.product_attribute} -> {self.type} | {self.file}'


class Category(MPTTModel):
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    attributes = models.ManyToManyField(Attribute, related_name='categories', blank=True)
    is_active = models.BooleanField(default=True)
    commission = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CategoryManager()

    class MPTTMeta:
        level_attr = 'mptt_level'

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title

    def to_dict_hierarchy(self):
        return {
            'id': self.id,
            'title': self.title,
            'commission': f'{self.commission:.2f}%',
            'children': [c.to_dict_hierarchy() for c in self.children.all()]
        }


class ProductAttribute(models.Model):
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE, related_name='product_attributes')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='attributes')
    value_bool = models.BooleanField(null=True, blank=True)
    value_string = models.CharField(max_length=255, null=True, blank=True)
    value_int = models.IntegerField(null=True, blank=True)
    value_float = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.attribute} -> {self.value}'

    @property
    def value(self):
        if self.attribute.value_type == self.attribute.TYPE_BOOL:
            return self.value_bool
        elif self.attribute.value_type == self.attribute.TYPE_STR:
            return self.value_string
        elif self.attribute.value_type == self.attribute.TYPE_INT:
            return self.value_int
        elif self.attribute.value_type == self.attribute.TYPE_FLOAT:
            return self.value_float
        elif self.attribute.value_type == self.attribute.TYPE_DROPDOWN:
            return self.value_string
        elif self.attribute.value_type == self.attribute.TYPE_IMAGE:
            return self.media
        else:
            raise ValueError("could not find a value type")

    @value.setter
    def value(self, value):
        if self.attribute.is_valid(value):
            if self.attribute.value_type == self.attribute.TYPE_BOOL:
                if isinstance(value, str):
                    value = True if value == 'true' else False
                self.value_bool = value
            elif self.attribute.value_type == self.attribute.TYPE_STR:
                self.value_string = value
            elif self.attribute.value_type == self.attribute.TYPE_INT:
                self.value_int = value
            elif self.attribute.value_type == self.attribute.TYPE_FLOAT:
                self.value_float = value
            elif self.attribute.value_type == self.attribute.TYPE_DROPDOWN:
                self.value_string = value
            elif self.attribute.value_type == self.attribute.TYPE_IMAGE:
                # Uses AttributeMedia file handler
                pass
            else:
                raise ValueError("could not find a value type")
        else:
            raise ValueError("invalid value")


class Product(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self) -> str:
        return self.title


class ProductMedia(BaseMedia):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='products')
    # is_primary = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.product} -> {self.type} | {self.file}'
