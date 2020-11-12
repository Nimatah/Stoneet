from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from apps.users.models import User


class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification."
    )

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = auth_forms.ReadOnlyPasswordHashField(
        label=("Password",),
        help_text="Raw passwords are not stored, so there is no way to see this "
                  "user's password, but you can change the password using "
                  "<a href=\"../password\">this form</a>."
    )

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial["password"]


class UserLoginForm(AuthenticationForm):

    def clean_username(self):
        username = self.cleaned_data['username'].lower().strip()
        return username


class UserRegisterForm(forms.ModelForm):
    ERROR_MESSAGES = {
        'password_mismatch': "رمز عبور وارد شده با تکرار رمز عبور مغایرت دارد",
    }

    TYPE_CHOICES = (
        (User.TYPE_BUYER, 'خریدار',),
        (User.TYPE_SELLER, 'فروشنده',),
        (User.TYPE_LOGISTIC, 'باربری',),
    )

    LEGAL_CHOICES = (
        (User.LEGAL_INDIVIDUAL, 'حقیقی',),
        (User.LEGAL_LEGAL, 'حقوقی',),
    )

    LOCATION_CHOICES = (
        ('tehran', 'تهران',),
        ('not-tehran', 'شهرستان',),
    )

    use_type = forms.ChoiceField(label="User Type", choices=TYPE_CHOICES, required=True)
    legal_type = forms.ChoiceField(label="Legal Type", choices=LEGAL_CHOICES, required=True)
    username = forms.CharField(min_length=4, max_length=255, required=False)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput, required=True)
    full_name = forms.CharField(label="Full Name", required=True)
    id_code = forms.CharField(label="ID Code", required=True)
    phone_number = forms.CharField(label="Phone Number", required=True)
    mobile_number = forms.CharField(label="Mobile Number", required=False)
    fax_number = forms.CharField(label="Fax Number", required=False)
    email = forms.EmailField(label="Email", required=False)
    region = forms.ChoiceField(label="Region", choices=LOCATION_CHOICES, required=True)
    address = forms.CharField(label="Address", required=True)
    postal_code = forms.CharField(label="Postal Code", required=True)

    class Meta:
        model = User
        fields = ('use_type', 'legal_type', 'username', 'full_name', 'id_code', 'phone_number', 'password1',
                  'password2', 'mobile_number', 'fax_number', 'email', 'region', 'address', 'postal_code',)

    def clean_email(self):
        email = self.cleaned_data.get('email').lower().strip()
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.ERROR_MESSAGES['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
