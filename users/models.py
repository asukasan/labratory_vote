from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from labs.models import Laboratory


class CustomUserManager(UserManager):
    use_in_migrations = True

    def create_user(self, num, password=None):
        """Creates a user profile object."""

        if not num:
            raise ValueError('Users must have an number.')

        user = self.model(num=num)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, num, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(num=num, password=password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル."""

    num = models.IntegerField(_('学籍番号'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_of_birth = models.DateTimeField(_('date joined'), default=timezone.now)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'num'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __repr__(self):
        return str(self.num)

    def __str__(self):
        return str(self.num) 

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    belongs1 = models.ForeignKey(Laboratory, verbose_name='第一希望', on_delete=models.CASCADE, related_name='belongs1', help_text='第二希望と第三希望と違うものを入れてください')
    belongs2 = models.ForeignKey(Laboratory, verbose_name='第二希望', on_delete=models.CASCADE, related_name='belongs2', help_text='第一希望と第三希望と違うものを入れてください')
    belongs3 = models.ForeignKey(Laboratory, verbose_name='第三希望', on_delete=models.CASCADE, related_name='belongs3', help_text='第一希望と第二希望と違うものを入れてください')
    rank = models.IntegerField(verbose_name='順位')

    def __str__(self):
        return str(self.user.num)



class Inquiry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(_('テキスト'))
    def __str__(self):
        return str(self.user.num)