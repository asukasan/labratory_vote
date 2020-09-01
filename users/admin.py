from django.contrib import admin
from .models import Laboratory
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser, Profile, Inquiry
from django.utils.translation import ugettext_lazy as _

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('num',)

@admin.register(CustomUser)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('num', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_of_birth')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('num', 'password1', 'password2'),
        }),
    )

    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('num', 'is_staff')
    list_filter = ('is_admin', 'is_superuser', 'is_active', 'groups')
    search_fields = ('num',)
    ordering = ('num',)



admin.site.register(Profile)
admin.site.register(Inquiry)

