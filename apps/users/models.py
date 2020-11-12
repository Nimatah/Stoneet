from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from apps.core.models import TimestampedModel


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


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):

    TYPE_SELLER = "seller"
    TYPE_LOGISTIC = "logistic"
    TYPE_BUYER = "buyer"

    TYPE_CHOICES = (
        (TYPE_SELLER, "Seller",),
        (TYPE_LOGISTIC, "Logistic",),
        (TYPE_BUYER, "Buyer",),
    )

    LEGAL_INDIVIDUAL = "individual"
    LEGAL_LEGAL = "legal"

    LEGAL_CHOICES = (
        (LEGAL_INDIVIDUAL, "Individual",),
        (LEGAL_LEGAL, "Legal",),
    )

    STATE_PENDING = "pending"
    STATE_ACCEPTED = "accepted"
    STATE_REJECTED = "rejected"

    STATE_CHOICES = (
        (STATE_PENDING, "Pending",),
        (STATE_ACCEPTED, "Accepted",),
        (STATE_REJECTED, "Rejected",),
    )

    username = models.CharField(db_index=True, max_length=255, unique=True)
    name = models.CharField(max_length=255, default="Admin")
    phone_number = models.CharField(db_index=True, max_length=20, default="0999xxxxxxx")
    mobile_number = models.CharField(db_index=True, max_length=20, default="021xxxxxxxx")
    fax_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(db_index=True, max_length=255, unique=True, null=True, blank=True)
    id_code = models.CharField(db_index=True, max_length=50, default="xxxxxxxxxx")
    region = models.CharField(max_length=255, default="tehran")
    address = models.TextField(default="tehran")
    postal_code = models.CharField(max_length=15, default="1231231231")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="buyer")
    legal_type = models.CharField(max_length=20, choices=LEGAL_CHOICES, default="individual")
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default=STATE_PENDING)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self) -> str:
        return self.username

    def get_full_name(self) -> str:
        return self.name

    def get_short_name(self) -> str:
        return self.name

    def is_buyer(self) -> bool:
        return self.type == self.TYPE_BUYER

    def is_seller(self) -> bool:
        return self.type == self.TYPE_SELLER

    def is_logistic(self) -> bool:
        return self.type == self.TYPE_LOGISTIC

    def is_individual(self) -> bool:
        return self.legal_type == self.LEGAL_INDIVIDUAL

    def is_legal(self) -> bool:
        return self.legal_type == self.LEGAL_LEGAL

    def is_pending(self) -> bool:
        return self.state == self.STATE_PENDING

    def is_accepted(self) -> bool:
        return self.state == self.STATE_ACCEPTED

    def is_rejected(self) -> bool:
        return self.state == self.STATE_REJECTED
