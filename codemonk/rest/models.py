from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom user manager for handling user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, dob, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, dob=dob)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, dob, password=None):
        user = self.create_user(email, name, dob, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'dob']

    def __str__(self):
        return self.email

# Model representing a word
class Word(models.Model):
    word = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.word

# Model representing a paragraph
class Paragraph(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    words = models.ManyToManyField(Word)  # Many-to-many relationship with words

    def __str__(self):
        return f'{self.id}'

# Model representing the mapping between words and paragraphs
class WordToParagraphMapping(models.Model):
    word = models.CharField(max_length=255)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
