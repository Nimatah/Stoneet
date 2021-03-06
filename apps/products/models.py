from typing import Union, List, Dict, Any

from django.db import models
from mptt.models import MPTTModel, TreeManager, TreeForeignKey

from apps.core import SPLIT
from apps.core.models import TimestampedModel, BaseMedia
from apps.core.utils import get_file_path
from apps.users.models import User, Mine


def get_product_file_path(instance, filename):
    return get_file_path('products', filename)


class AttributeManager(models.Manager):

    def get_by_input_field(self):
        return self.filter(value_type__in=['int', 'dropdown', 'str', 'float', 'range', 'multiple'])

    def get_by_image_field(self):
        return self.filter(value_type='image')

    def get_by_bool_field(self):
        return self.filter(value_type='bool')


class CategoryManager(TreeManager):

    def get_root(self):
        return self.filter(mptt_level=0)

    def get_leaf(self):
        return self.filter(children__isnull=True)


class ProductAttributeManager(models.Manager):

    def get_ordinary(self):
        return self.filter(attribute__is_special=False)

    def get_special(self):
        return self.filter(attribute__is_special=True)


class ProductQueryset(models.QuerySet):

    def accepted(self) -> 'ProductQueryset':
        return self.filter(state=Product.STATE_ACCEPTED)

    def rejected(self) -> 'ProductQueryset':
        return self.filter(state=Product.STATE_REJECTED)

    def pending(self) -> 'ProductQueryset':
        return self.filter(state=Product.STATE_PENDING)


class ProductManager(models.Manager):

    def get_queryset(self) -> 'ProductQueryset':
        return ProductQueryset(model=self.model, using=self.db)

    def get_by_user(self, user: User) -> 'ProductQueryset':
        return self.filter(user=user)


class ProductMediaManager(models.Manager):

    def get_primary(self):
        return self.get(is_primary=True)

    def get_additional(self):
        return self.filter(is_primary=False)


class ProductHistoryManager(models.Manager):
    pass


class Attribute(TimestampedModel):

    ID_PRICE = 1
    ID_ANALYZE = 2
    ID_SKU = 4
    ID_SAMPLE = 5
    ID_PAYMENT_TYPE = 9
    ID_CARAT_FROM = 12
    ID_CARAT_TO = 13
    ID_GRAIN_FROM = 14
    ID_GRAIN_TO = 15
    ID_DELIVERY_TYPE = 16
    ID_AVAILABLE_DEPO = 17
    ID_MIN_ORDER = 18

    TYPE_BOOL = 'bool'
    TYPE_STR = 'str'
    TYPE_INT = 'int'
    TYPE_FLOAT = 'float'
    TYPE_IMAGE = 'image'
    TYPE_DROPDOWN = 'dropdown'
    TYPE_RANGE = 'range'
    TYPE_MULTIPLE = 'multiple'

    RANGE_FROM = 'from'
    RANGE_TO = 'to'

    _TYPE_CHOICES = (
        (TYPE_BOOL, 'Boolean',),
        (TYPE_STR, 'String',),
        (TYPE_INT, 'Integer',),
        (TYPE_FLOAT, 'Float',),
        (TYPE_IMAGE, 'Image',),
        (TYPE_DROPDOWN, 'Dropdown',),
        (TYPE_RANGE, 'Range',),
        (TYPE_MULTIPLE, 'Multiple Choice',),
    )

    _RANGE_CHOICES = (
        (RANGE_FROM, '????????????',),
        (RANGE_TO, '??????????????',),
    )

    WEIGHT_KG = 'kg'
    WEIGHT_TON = 'ton'
    WEIGHT_MM = 'mm'
    WEIGHT_CM = 'cm'

    PAYMENT_CASH = 'cash'
    PAYMENT_MONTHLY_BEFORE = 'monthly_before'
    PAYMENT_MONTHLY_AFTER = 'monthly_after'

    PAYMENT_MAP = {
        PAYMENT_CASH: '???????????? ??????',
        PAYMENT_MONTHLY_BEFORE: '?????????? ???????? ??????????',
        PAYMENT_MONTHLY_AFTER: '???????????? ??????????',
    }

    PAYMENT_REVERSE_MAP = {
        '???????????? ??????': PAYMENT_CASH,
        '?????????? ???????? ??????????': PAYMENT_MONTHLY_BEFORE,
        '???????????? ??????????': PAYMENT_MONTHLY_AFTER,
    }

    title = models.CharField(max_length=255)
    value_type = models.CharField(max_length=255, choices=_TYPE_CHOICES)
    options = models.TextField(null=True, blank=True)
    unit = models.CharField(max_length=255, blank=True)
    range_type = models.CharField(max_length=255, choices=_RANGE_CHOICES, null=True, blank=True)
    order = models.IntegerField(default=10)
    has_weight = models.BooleanField(default=False)
    has_child_value = models.BooleanField(default=False)
    is_required = models.BooleanField(default=False)
    view_in_product_page = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)

    objects = AttributeManager()

    def __str__(self) -> str:
        return self.title

    @property
    def dropdown(self):
        return self.options.split(SPLIT)

    @property
    def choices(self):
        return self.options.split(SPLIT)

    def is_valid(self, value) -> bool:
        if self.value_type == Attribute.TYPE_BOOL:
            return self.__validate_boolean(value)
        elif self.value_type == Attribute.TYPE_INT:
            return self.__validate_int(value)
        elif self.value_type == Attribute.TYPE_FLOAT:
            return self.__validate_float(value)
        elif self.value_type == Attribute.TYPE_DROPDOWN:
            return self.__validate_dropdown(value)
        elif self.value_type == Attribute.TYPE_RANGE:
            return self.__validate_range(value)
        elif self.value_type == Attribute.TYPE_MULTIPLE:
            return self.__validate_multiple(value)
        else:
            return True

    @staticmethod
    def __validate_boolean(value: str) -> bool:
        return value.lower() in ('true', 'false',)

    @staticmethod
    def __validate_int(value: int) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def __validate_float(value: float) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def __validate_range(value: int) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False

    def __validate_multiple(self, value: str) -> bool:
        return all([i in self.options.split(SPLIT) for i in value.split(SPLIT)])

    def __validate_dropdown(self, value: str) -> bool:
        return value in self.options.split(SPLIT)


class AttributeMedia(BaseMedia):
    product_attribute = models.ForeignKey('ProductAttribute', on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to=get_product_file_path)

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
            'commission': f'{self.commission:.2f}%' if self.parent is None else f'{self.parent.commission:.2f}%',
            'children': [c.to_dict_hierarchy() for c in self.children.all()]
        }


class ProductAttribute(models.Model):

    _WEIGHT_UNIT_CHOICES = (
        (Attribute.WEIGHT_KG, '??????????????',),
        (Attribute.WEIGHT_TON, '????',),
        (Attribute.WEIGHT_MM, '?????????????????',),
        (Attribute.WEIGHT_CM, '???????????????????',),
    )

    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE, related_name='product_attributes')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='attributes')
    value_bool = models.BooleanField(null=True, blank=True)
    value_string = models.CharField(max_length=255, null=True, blank=True)
    value_int = models.IntegerField(null=True, blank=True)
    value_float = models.FloatField(null=True, blank=True)
    weight_unit = models.CharField(max_length=255, choices=_WEIGHT_UNIT_CHOICES, blank=True)
    child_value = models.FloatField(null=True, blank=True)

    objects = ProductAttributeManager()

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
        elif self.attribute.value_type == self.attribute.TYPE_RANGE:
            return self.value_int
        elif self.attribute.value_type == self.attribute.TYPE_MULTIPLE:
            return self.value_string.split(SPLIT)
        elif self.attribute.value_type == self.attribute.TYPE_IMAGE:
            try:
                return self.media.first().file
            except AttributeMedia.DoesNotExist:
                return None
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
            elif self.attribute.value_type == self.attribute.TYPE_RANGE:
                self.value_int = value
            elif self.attribute.value_type == self.attribute.TYPE_MULTIPLE:
                self.value_string = value
            elif self.attribute.value_type == self.attribute.TYPE_IMAGE:
                # Uses AttributeMedia file handler
                pass
            else:
                raise ValueError("could not find a value type")
        else:
            raise ValueError("invalid value")


class Product(TimestampedModel):

    STATE_PENDING = 'pending'
    STATE_ACCEPTED = 'accepted'
    STATE_REJECTED = 'rejected'

    _STATE_CHOICES = (
        (STATE_PENDING, '???? ???????????? ??????????',),
        (STATE_ACCEPTED, '?????????? ??????',),
        (STATE_REJECTED, '???? ??????',),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=255, choices=_STATE_CHOICES, default=STATE_PENDING)
    title = models.CharField(max_length=255)
    mine = models.ForeignKey(Mine, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    reject_reason = models.TextField(blank=True)

    objects = ProductManager()

    def __str__(self) -> str:
        return self.title

    def get_price(self) -> Union[ProductAttribute, None]:
        try:
            return self.attributes.get(attribute_id=Attribute.ID_PRICE)
        except ProductAttribute.DoesNotExist:
            return None

    def get_sku(self) -> Union[ProductAttribute, None]:
        try:
            return self.attributes.get(attribute_id=Attribute.ID_SKU)
        except ProductAttribute.DoesNotExist:
            return None

    def get_analyze(self) -> Union[ProductAttribute, None]:
        try:
            return self.attributes.get(attribute_id=Attribute.ID_ANALYZE)
        except ProductAttribute.DoesNotExist:
            return None

    def get_min_caret(self):
        return self.attributes.get(attribute_id=Attribute.ID_CARAT_FROM)

    def get_max_caret(self):
        return self.attributes.get(attribute_id=Attribute.ID_CARAT_TO)

    def get_caret(self) -> str:
        caret_from = self.attributes.get(attribute_id=Attribute.ID_CARAT_FROM)
        caret_to = self.attributes.get(attribute_id=Attribute.ID_CARAT_TO)
        caret = f'{caret_from.value} ???? {caret_to.value} %' if caret_from.value != caret_to.value else f'{caret_from.value} %'
        return caret

    def get_min_grain(self):
        return self.attributes.get(attribute_id=Attribute.ID_GRAIN_FROM)

    def get_max_grain(self):
        return self.attributes.get(attribute_id=Attribute.ID_GRAIN_TO)

    def get_grain_weight(self):
        return self.get_max_grain().weight_unit or self.get_min_grain().weight_unit

    def get_size(self) -> str:
        size_from = self.attributes.get(attribute_id=Attribute.ID_GRAIN_FROM)
        size_to = self.attributes.get(attribute_id=Attribute.ID_GRAIN_TO)
        size = f'{size_from.value} ???? {size_to.value} {size_to.get_weight_unit_display()}' if size_from.value != size_to.value else f'{size_from.value} {size_to.get_weight_unit_display()}'
        return size

    def get_payment_type(self) -> List[str]:
        return self.attributes.get(attribute_id=Attribute.ID_PAYMENT_TYPE).value

    def get_payment_type_object(self):
        return self.attributes.get(attribute_id=Attribute.ID_PAYMENT_TYPE)

    def get_delivery_object(self):
        return self.attributes.get(attribute_id=Attribute.ID_DELIVERY_TYPE)

    def get_delivery_type(self):
        attribute = self.attributes.get(attribute_id=Attribute.ID_DELIVERY_TYPE)
        return f'{attribute.value} {attribute.child_value} {attribute.get_weight_unit_display()}'

    def get_commission(self) -> float:
        return self.category.commission if self.category.parent is None else self.category.parent.commission

    def get_sample(self):
        try:
            sample = self.attributes.get(attribute_id=Attribute.ID_SAMPLE)
            return f'{sample.value} ??????????????'
        except:
            return '??????????'

    def get_sample_object(self):
        try:
            return self.attributes.get(attribute_id=Attribute.ID_SAMPLE)
        except Attribute.DoesNotExist:
            return None

    def has_sample(self):
        return self.attributes.filter(attribute_id=Attribute.ID_SAMPLE).exists()

    def get_available_depo(self):
        return self.attributes.filter(attribute_id=Attribute.ID_AVAILABLE_DEPO).first()

    def get_min_order(self):
        return self.attributes.filter(attribute_id=Attribute.ID_MIN_ORDER).first()

    def to_dict(self) -> Dict[str, Any]:
        return {
            'user_id': self.user_id,
            'state': self.state,
            'title': self.title,
            'mine_id': self.mine_id,
            'description': self.description,
            'category': self.category_id,
            'is_active': self.is_active,
            'attributes': {i.attribute.title: i.value for i in self.attributes.prefetch_related('attribute').all()}
        }


class ProductMedia(BaseMedia):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to=get_product_file_path)
    is_primary = models.BooleanField(default=False)

    objects = ProductMediaManager()

    def __str__(self) -> str:
        return f'{self.product} -> {self.type} | {self.file}'
