from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
import uuid



class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have provided an invalid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField( primary_key = True, unique=True,
         default = uuid.uuid4,  editable = False)
    email = models.EmailField(blank=True, default='', unique=True)
    fname = models.CharField(max_length=255, blank=True, default='')
    lname =  models.CharField(max_length=255, blank=True, default='')
    phone = models.CharField(max_length=12, blank=True, default='')
    profile_pic = models.ImageField(blank=True,upload_to="ids/")
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone','fname','lname']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.fname+" "+self.lname
    
    def get_short_name(self):
        return self.lname
    def __str__(self) -> str:
        return self.email