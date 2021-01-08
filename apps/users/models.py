from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from apps.core.models import TimestampedModel, BaseMedia


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


class MediaManager(models.Manager):
    pass


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
        (LEGAL_INDIVIDUAL, "Individual",),
        (LEGAL_LEGAL, "Legal",),
    )

    STATE_DRAFT = "draft"
    STATE_PENDING = "pending"
    STATE_ACCEPTED = "accepted"
    STATE_REJECTED = "rejected"

    _STATE_CHOICES = (
        (STATE_DRAFT, "Draft",),  # Can edit
        (STATE_PENDING, "Waiting For Confirm",),  # Can't edit
        (STATE_ACCEPTED, "Confirmed",),
        (STATE_REJECTED, "Rejected",),  # Rejection details box
    )

    username = models.CharField(db_index=True, max_length=255, unique=True)
    full_name = models.CharField(max_length=255, default="Admin")
    phone_number = models.CharField(db_index=True, max_length=20, default="0999xxxxxxx")
    mobile_number = models.CharField(db_index=True, max_length=20, default="021xxxxxxxx")
    fax_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(db_index=True, max_length=255, unique=True, null=True, blank=True)
    id_code = models.CharField(db_index=True, max_length=50, default="xxxxxxxxxx")
    region = models.CharField(max_length=255, default="tehran")
    address = models.TextField(default="tehran")
    postal_code = models.CharField(max_length=15, default="1231231231")
    use_type = models.CharField(max_length=20, choices=_TYPE_CHOICES, default="buyer")
    legal_type = models.CharField(max_length=20, choices=_LEGAL_CHOICES, default="individual")
    state = models.CharField(max_length=20, choices=_STATE_CHOICES, default=STATE_PENDING)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self) -> str:
        return self.username

    def get_full_name(self) -> str:
        return self.full_name

    def get_short_name(self) -> str:
        return self.full_name

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
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='users')

    def __str__(self) -> str:
        return f'{self.user} -> {self.type} | {self.file}'
