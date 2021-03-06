import uuid
from datetime import datetime, timedelta
from typing import Optional

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from persiantools.jdatetime import JalaliDate

from apps.core.models import TimestampedModel, BaseMedia
from apps.core.utils import get_file_path


def get_user_file_path(instance, filename):
    return get_file_path('users', filename)


class MineManager(models.Manager):
    pass


class AddressManager(models.Manager):
    pass


class UserQuerySet(models.QuerySet):

    def sellers(self) -> 'UserQuerySet':
        return self.filter(use_type=User.TYPE_SELLER)

    def buyers(self) -> 'UserQuerySet':
        return self.filter(use_type=User.TYPE_BUYER)

    def logistics(self) -> 'UserQuerySet':
        return self.filter(use_type=User.TYPE_LOGISTIC)

    def admins(self) -> 'UserQuerySet':
        return self.filter(use_type=User.TYPE_ADMIN)

    def sellers_pending(self) -> 'UserQuerySet':
        return self.sellers().filter(state=User.STATE_PENDING)

    def sellers_accepted(self) -> 'UserQuerySet':
        return self.sellers().filter(state=User.STATE_ACCEPTED)

    def sellers_rejected(self) -> 'UserQuerySet':
        return self.sellers().filter(state=User.STATE_REJECTED)

    def sellers_banned(self) -> 'UserQuerySet':
        return self.sellers().filter(state=User.STATE_BANNED)

    def buyers_pending(self) -> 'UserQuerySet':
        return self.buyers().filter(state=User.STATE_PENDING)

    def buyers_accepted(self) -> 'UserQuerySet':
        return self.buyers().filter(state=User.STATE_ACCEPTED)

    def buyers_rejected(self) -> 'UserQuerySet':
        return self.buyers().filter(state=User.STATE_REJECTED)

    def buyers_banned(self) -> 'UserQuerySet':
        return self.buyers().filter(state=User.STATE_BANNED)

    def logistics_pending(self) -> 'UserQuerySet':
        return self.logistics().filter(state=User.STATE_PENDING)

    def logistics_accepted(self) -> 'UserQuerySet':
        return self.logistics().filter(state=User.STATE_ACCEPTED)

    def logistics_rejected(self) -> 'UserQuerySet':
        return self.logistics().filter(state=User.STATE_REJECTED)

    def logistics_banned(self) -> 'UserQuerySet':
        return self.logistics().filter(state=User.STATE_BANNED)


class UserManager(BaseUserManager):

    def get_queryset(self) -> 'UserQuerySet':
        return UserQuerySet(model=self.model, using=self.db)

    def get_by_token(self, token) -> Optional['User']:
        try:
            return self.get(password_reset_token=token, password_reset_expiration__lte=datetime.now())
        except User.DoesNotExist:
            return None

    @staticmethod
    def __validate_username(username: str):
        if username is None:
            raise TypeError('Users must have a username.')

    @staticmethod
    def __validate_password(password: str):
        if password is None:
            raise TypeError('Users must have a password.')

    def create_user(self, username: str, password: str = None, **kwargs):
        self.__validate_username(username)
        self.__validate_password(password)
        username = username.lower()
        user = self.model(
            username=username,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username: str, password: str):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def find_by_email_or_phone_number(self, email: str, mobile_number: str) -> 'User':
        return self.filter(Q(email=email) | Q(mobile_number=mobile_number)).first()

    def find_by_email(self, email: str) -> 'User':
        try:
            return self.get(email=email)
        except User.DoesNotExist:
            return None


class MediaManager(models.Manager):
    pass


class ProfileManager(models.Manager):
    pass


class Mine(models.Model):

    REGION_NORTH = 'north'
    REGION_SOUTH = 'south'
    REGION_EAST = 'east'
    REGION_WEST = 'west'

    _REGION_CHOICES = (
        (REGION_NORTH, '????????',),
        (REGION_SOUTH, '????????',),
        (REGION_EAST, '??????',),
        (REGION_WEST, '??????',),
    )

    title = models.CharField(max_length=255)
    region = models.ForeignKey('locations.Region', on_delete=models.CASCADE)
    address = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='mines')
    road_name = models.CharField(max_length=255, blank=True)
    location_in_region = models.CharField(max_length=255, choices=_REGION_CHOICES)
    distance_to_road = models.IntegerField()
    proper_road = models.BooleanField()
    load_tools = models.BooleanField()

    objects = MineManager()

    def __str__(self):
        return f'{self.user} -> {self.title}'


class Address(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='addresses')
    receiver_name = models.CharField(max_length=255)
    region = models.ForeignKey('locations.Region', on_delete=models.CASCADE)
    address = models.TextField()
    postal_code = models.CharField(max_length=255)

    objects = AddressManager()

    def __str__(self) -> str:
        return f'{self.user} -> address: {self.receiver_name}'


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    TYPE_SELLER = "seller"
    TYPE_LOGISTIC = "logistic"
    TYPE_BUYER = "buyer"
    TYPE_ADMIN = "admin"
    TYPE_SUPER_USER = "superuser"

    _TYPE_CHOICES = (
        (TYPE_SELLER, "Seller",),
        (TYPE_LOGISTIC, "Logistic",),
        (TYPE_BUYER, "Buyer",),
        (TYPE_ADMIN, "Admin",),
        (TYPE_SUPER_USER, "Super User"),
    )

    LEGAL_INDIVIDUAL = "individual"
    LEGAL_LEGAL = "legal"

    _LEGAL_CHOICES = (
        (LEGAL_INDIVIDUAL, "??????????",),
        (LEGAL_LEGAL, "??????????",),
    )

    STATE_PENDING = "pending"
    STATE_ACCEPTED = "accepted"
    STATE_REJECTED = "rejected"
    STATE_BANNED = "banned"

    STATE_CHOICES = (
        (STATE_PENDING, "???? ???????????? ??????????",),  # Can't edit
        (STATE_ACCEPTED, "?????????? ??????",),
        (STATE_REJECTED, "???? ??????",),  # Rejection details box
        (STATE_BANNED, "?????????? ??????",),
    )

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, max_length=255, unique=True, null=True, blank=True)
    mobile_number = models.CharField(db_index=True, max_length=20, default="021xxxxxxxx")
    use_type = models.CharField(max_length=20, choices=_TYPE_CHOICES, default="buyer")
    legal_type = models.CharField(max_length=20, choices=_LEGAL_CHOICES, default="individual")
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default=STATE_PENDING)
    rejection_reason = models.TextField(blank=True)
    password_reset_token = models.UUIDField(default=None, null=True, blank=True)
    password_reset_expiration = models.DateTimeField(default=None, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self) -> str:
        return self.email or self.username

    def get_full_name(self) -> str:
        return self.username

    def get_short_name(self) -> str:
        return self.username

    def get_email(self) -> str:
        return self.email or ''

    @property
    def is_buyer(self) -> bool:
        return self.use_type == self.TYPE_BUYER

    @property
    def is_seller(self) -> bool:
        return self.use_type == self.TYPE_SELLER

    @property
    def is_logistic(self) -> bool:
        return self.use_type == self.TYPE_LOGISTIC

    @property
    def is_admin(self) -> bool:
        return self.use_type == self.TYPE_ADMIN

    @property
    def is_individual(self) -> bool:
        return self.legal_type == self.LEGAL_INDIVIDUAL

    @property
    def is_legal(self) -> bool:
        return self.legal_type == self.LEGAL_LEGAL

    @property
    def is_pending(self) -> bool:
        return self.state == self.STATE_PENDING

    @property
    def is_accepted(self) -> bool:
        return self.state == self.STATE_ACCEPTED

    @property
    def is_rejected(self) -> bool:
        return self.state == self.STATE_REJECTED

    @property
    def is_male(self) -> bool:
        return self.profile.gender == Profile.GENDER_MALE

    @property
    def is_female(self) -> bool:
        return self.profile.gender == Profile.GENDER_FEMALE

    def get_image_id_card_front(self):
        return self.media.filter(title=UserMedia.name_map['image_id_card_front']).first()

    def get_image_id_card_back(self):
        return self.media.filter(title=UserMedia.name_map['image_id_card_back']).first()

    def get_image_company_registration(self):
        return self.media.filter(title=UserMedia.name_map['image_company_registration']).first()

    def get_image_company_added_value_certificate(self):
        return self.media.filter(title=UserMedia.name_map['image_company_added_value_certificate']).first()

    def get_image_company_latest_newspaper(self):
        return self.media.filter(title=UserMedia.name_map['image_company_latest_newspaper']).first()

    def get_image_company_tax_on_added_value_certificate(self):
        return self.media.filter(title=UserMedia.name_map['image_company_tax_on_added_value_certificate']).first()

    def get_image_company_signature_copyright_certificate(self):
        return self.media.filter(title=UserMedia.name_map['image_company_signature_copyright_certificate']).first()

    def get_image_company_license(self):
        return self.media.filter(title=UserMedia.name_map['image_company_license']).first()

    def get_password_reset_token(self):
        if not self.password_reset_token:
            token = uuid.uuid4()
            self.password_reset_token = token
            self.password_reset_expiration = datetime.now() + timedelta(days=1)
        else:
            token = self.password_reset_token
            self.password_reset_expiration = datetime.now() + timedelta(days=1)
        return token


class UserMedia(BaseMedia):
    STATE_PENDING = "pending"
    STATE_ACCEPTED = "accepted"
    STATE_REJECTED = "rejected"

    _STATE_CHOICES = (
        (STATE_PENDING, "???? ???????????? ??????????",),  # Can't edit
        (STATE_ACCEPTED, "?????????? ??????",),
        (STATE_REJECTED, "???? ??????",),
    )

    name_map = {
        'image_id_card_front': '?????? ???????? ??????',
        'image_id_card_back': '?????? ???????? ??????',
        'image_company_registration': '?????????? ?????? ????????',
        'image_company_added_value_certificate': '?????????? ???????? ????????????',
        'image_company_latest_newspaper': '?????????? ???? ?????? ?????????? ?????????????? ????????',
        'image_company_tax_on_added_value_certificate': '?????????? ???????????? ???? ???????? ????????????',
        'image_company_signature_copyright_certificate': '???????????????? ?????? ?????? ???????? ????????',
        'image_company_license': '???????????? ????????????'
    }

    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='media')
    title = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, choices=_STATE_CHOICES, default=STATE_PENDING)
    file = models.FileField(upload_to=get_user_file_path)

    def __str__(self) -> str:
        return f'{self.user} -> {self.type} | {self.file}'


class Profile(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    COMPANY_TYPE_AM = 'am'
    COMPANY_TYPE_KHAS = 'khas'
    COMPANY_TYPE_MASOULIAT_MAHDOOD = 'masouliat_mahdood'
    COMPANY_TYPE_TAAVONI = 'taavoni'

    _COMPANY_CHOICES = (
        (COMPANY_TYPE_AM, '??????'),
        (COMPANY_TYPE_KHAS, '??????',),
        (COMPANY_TYPE_MASOULIAT_MAHDOOD, '?????????????? ??????????',),
        (COMPANY_TYPE_TAAVONI, '????????????',),
    )

    _GENDER_CHOICES = (
        (GENDER_MALE, '??????',),
        (GENDER_FEMALE, '????',),
    )

    COMPANY_LICENSE_TYPE_CITY = 'city'
    COMPANY_LICENSE_TYPE_PROVINCE = 'province'
    COMPANY_LICENSE_TYPE_COUNTRY = 'country'
    COMPANY_LICENSE_TYPE_INTERNATIONAL = 'international'

    COMPANY_LICENSE_TYPE_CHOICES = (
        (COMPANY_LICENSE_TYPE_CITY, '?????? ?? ?????? ????????',),
        (COMPANY_LICENSE_TYPE_PROVINCE, '?????? ?? ?????? ????????????',),
        (COMPANY_LICENSE_TYPE_COUNTRY, '?????? ?? ?????? ????????????',),
        (COMPANY_LICENSE_TYPE_INTERNATIONAL, '?????? ?? ?????? ?????????????????????',)
    )

    COMPANY_BRANCH_TYPE_CENTRAL = 'central'
    COMPANY_BRANCH_TYPE_BRANCH = 'branch'

    COMPANY_BRANCH_TYPE_CHOICES = (
        (COMPANY_BRANCH_TYPE_CENTRAL, '???????? ????????',),
        (COMPANY_BRANCH_TYPE_BRANCH, '?????????????? ????????',),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, choices=_GENDER_CHOICES, blank=True)
    id_code = models.CharField(max_length=255, blank=True)
    national_code = models.CharField(max_length=255, blank=True)

    address = models.TextField(blank=True)
    postal_code = models.CharField(max_length=15, blank=True)
    region = models.ForeignKey('locations.Region', on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    bank_account_name = models.CharField(max_length=255, blank=True)
    bank_account_number = models.CharField(max_length=255, blank=True)
    bank_sheba_number = models.CharField(max_length=255, blank=True)

    company_name = models.CharField(max_length=255, blank=True)
    company_type = models.CharField(max_length=255, choices=_COMPANY_CHOICES, null=True, blank=True)
    company_register_code = models.CharField(max_length=255, blank=True)
    company_national_code = models.CharField(max_length=255, blank=True)
    company_finance_code = models.CharField(max_length=255, blank=True)
    company_print_signature_right = models.CharField(max_length=255, blank=True)

    company_license_type = models.CharField(max_length=255, blank=True, choices=COMPANY_LICENSE_TYPE_CHOICES)
    company_license_code = models.CharField(max_length=255, blank=True)
    company_license_start = models.DateField(null=True, blank=True)
    company_license_end = models.DateField(null=True, blank=True)
    company_ceo_name = models.CharField(max_length=255, blank=True)
    company_ceo_id_code = models.CharField(max_length=255, blank=True)
    company_ceo_national_code = models.CharField(max_length=255, blank=True)
    company_branch_type = models.CharField(max_length=255, blank=True, choices=COMPANY_BRANCH_TYPE_CHOICES)

    objects = ProfileManager()

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_full_name(self):
        return self.company_name or f'{self.first_name} {self.last_name}'

    def get_national_code(self):
        return self.national_code or self.company_finance_code

    def get_persian_birthday(self):
        if not self.birthday:
            return ''
        return JalaliDate.to_jalali(self.birthday)

    def get_persian_company_license_start(self):
        if not self.company_license_start:
            return ''
        return JalaliDate.to_jalali(self.company_license_start)

    def get_persian_company_license_end(self):
        if not self.company_license_end:
            return ''
        return JalaliDate.to_jalali(self.company_license_end)

    def get_province(self):
        return self.region.parent

    def get_city(self):
        return self.region

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_name = self.get_full_name()
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )
