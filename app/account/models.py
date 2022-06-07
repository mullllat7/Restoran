from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.db import models

class UserManager(BaseUserManager):
    def _create(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email не может быть пустым')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    # name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    def generate_activation_code(self):
        from django.utils.crypto import get_random_string

        code = get_random_string(8)
        self.activation_code = code
        self.save()
        return code
    @staticmethod
    def send_activation_mail(email, code):
        message = f'Ваш код активации: {code}'
        send_mail('Активация аккаунта',
                  message, 'test@gmail.com',
                  [email])


class InfoUser(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='info_user')
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/user_image', blank=True, null=True)

    def __str__(self):
        return f'{self.name}-{self.surname}'

    class Meta:
        verbose_name = 'Info user'
        verbose_name_plural = 'Info users'
