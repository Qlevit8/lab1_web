from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Invalid email")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='Джон')
    surname = models.CharField(max_length=255, blank=True, default='Доу')
    date_of_birth = models.DateField(null=True, blank=True, default='21.01.2000')
    GENDER_CHOICES = [
        ('Чоловік', 'Чоловік'),
        ('Жінка', 'Жінка')
    ]
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, default='Чоловік')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"
        swappable = 'AUTH_USER_MODEL'


class Species(models.Model):
    species_name = models.CharField(max_length=255, verbose_name='Назва виду')
    species_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')

    def __str__(self):
        return self.species_name

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Види"


class Pet(models.Model):
    MALE = 'Чоловіча'
    FEMALE = 'Жіноча'
    SEX_CHOICES = [
        (MALE, 'Чоловіча'),
        (FEMALE, 'Жіноча'),
    ]

    pet_name = models.CharField(max_length=255, verbose_name='Ім`я тварини')
    pet_age = models.IntegerField(verbose_name='Вік тварини')
    pet_species = models.ForeignKey(Species, on_delete=models.CASCADE)
    pet_sex = models.CharField(max_length=8, choices=SEX_CHOICES, verbose_name='Стать тварини')
    pet_weight = models.FloatField(verbose_name='Вага тварини')

    def __str__(self):
        return self.pet_name

    class Meta:
        verbose_name = "Тварина"
        verbose_name_plural = "Тварини"


