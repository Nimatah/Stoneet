from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from apps.core.models import TimestampedModel, BaseMedia


class MineManager(models.Manager):
    pass


class UserManager(BaseUserManager):

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


class MediaManager(models.Manager):
    pass


class ProfileManager(models.Manager):
    pass


class Mine(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey('locations.Region', on_delete=models.CASCADE)
    address = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    road_name = models.CharField(max_length=255, blank=True)
    distance_to_road = models.IntegerField()
    proper_road = models.BooleanField()
    load_tools = models.BooleanField()

    objects = MineManager()

    def __str__(self):
        return f'{self.user} -> {self.title}'


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
        (LEGAL_INDIVIDUAL, "حقیقی",),
        (LEGAL_LEGAL, "حقوقی",),
    )

    STATE_PENDING = "pending"
    STATE_ACCEPTED = "accepted"
    STATE_REJECTED = "rejected"
    STATE_BANNED = "banned"

    _STATE_CHOICES = (
        (STATE_PENDING, "در حال بررسی",),  # Can't edit
        (STATE_ACCEPTED, "تایید شده",),
        (STATE_REJECTED, "رد شده",),  # Rejection details box
        (STATE_BANNED, "مسدود شده",),
    )

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, max_length=255, unique=True, null=True, blank=True)
    mobile_number = models.CharField(db_index=True, max_length=20, default="021xxxxxxxx")
    use_type = models.CharField(max_length=20, choices=_TYPE_CHOICES, default="buyer")
    legal_type = models.CharField(max_length=20, choices=_LEGAL_CHOICES, default="individual")
    state = models.CharField(max_length=20, choices=_STATE_CHOICES, default=STATE_PENDING)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self) -> str:
        return self.email or self.mobile_number

    def get_full_name(self) -> str:
        return self.username

    def get_short_name(self) -> str:
        return self.username

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


class UserMedia(BaseMedia):
    STATE_PENDING = "pending"
    STATE_ACCEPTED = "accepted"
    STATE_REJECTED = "rejected"

    _STATE_CHOICES = (
        (STATE_PENDING, "در حال بررسی",),  # Can't edit
        (STATE_ACCEPTED, "تایید شده",),
        (STATE_REJECTED, "رد شده",),
    )

    name_map = {
        'image_id_card_front': 'روی کارت ملی',
        'image_id_card_back': 'پشت کارت کلی',
        'image_company_registration': 'گواهی ثبت شرکت',
        'image_company_added_value_certificate': 'گواهی ارزش افزوده',
        'image_company_public_certificate': 'آخرین به روز رسانی روزنامه رسمی',
        'image_company_tax_on_added_value_certificate': 'گواهی مالیات بر ارزش افزوده',
        'image_company_signature_copyright_certificate': 'شناسنامه ملی کپی رایت امضا',
    }

    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='media')
    title = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, choices=_STATE_CHOICES, default=STATE_PENDING)
    file = models.FileField(upload_to='users')

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
        (COMPANY_TYPE_AM, 'عام'),
        (COMPANY_TYPE_KHAS, 'خاص',),
        (COMPANY_TYPE_MASOULIAT_MAHDOOD, 'مسئولیت محدود',),
        (COMPANY_TYPE_TAAVONI, 'تعاونی',),
    )

    _GENDER_CHOICES = (
        (GENDER_MALE, 'مرد',),
        (GENDER_FEMALE, 'زن',),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, choices=_GENDER_CHOICES, blank=True)
    id_code = models.CharField(max_length=255, blank=True)
    national_code = models.CharField(max_length=255, blank=True)

    address = models.TextField(blank=True)
    postal_code = models.CharField(max_length=15, blank=True)
    region = models.ForeignKey('locations.Region', on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    bank_account_name = models.CharField(max_length=255, blank=True)
    bank_sheba_number = models.CharField(max_length=255, blank=True)

    company_name = models.CharField(max_length=255, blank=True)
    company_type = models.CharField(max_length=255, choices=_COMPANY_CHOICES, blank=True)
    company_register_code = models.CharField(max_length=255, blank=True)
    company_national_code = models.CharField(max_length=255, blank=True)
    company_finance_code = models.CharField(max_length=255, blank=True)
    company_print_signature_right = models.CharField(max_length=255, blank=True)

    company_license_type = models.CharField(max_length=255, blank=True)
    company_license_code = models.CharField(max_length=255, blank=True)
    company_license_start = models.DateField(null=True, blank=True)
    company_license_end = models.DateField(null=True, blank=True)
    company_ceo_name = models.CharField(max_length=255, blank=True)
    company_ceo_id_code = models.CharField(max_length=255, blank=True)
    company_ceo_national_code = models.CharField(max_length=255, blank=True)

    objects = ProfileManager()

    def __str__(self):
        return f'{self.user.username} Profile'
