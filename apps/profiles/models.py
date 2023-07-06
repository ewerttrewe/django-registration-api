from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    NONE = "None", _("None")


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), default='/default.png')
    gender = models.CharField(verbose_name=_("Gender"), max_length=50, choices=Gender.choices, default=Gender.NONE)
    role = models.TextField(verbose_name=_("Role"), max_length=100, default='employee')
    description = models.TextField(verbose_name=_("Description"), default="Say something about yourself!" ,max_length=200)
    
    def get_role(self):
        return f'Position: {self.role}'

    def __str__(self):
        return f"{self.user.username}'s Profile"
    


