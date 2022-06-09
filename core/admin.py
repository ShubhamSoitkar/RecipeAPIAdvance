'''
Django admin customization
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

class UserAdmin(BaseUserAdmin):
    '''Define the admin pages for users.'''
    ordering = ['id']
    list_display = ['email','name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields':('last_login',)}),
    )
    readonly_fields = ['last_login']

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':(
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )

admin.site.register(models.User, UserAdmin)



'''
Meaning of gettext_lazy _   -->

if you do change the language of Django and you want to change it for everywhere in your project,

then you can do it in the configuration and it means any way you use this translation shortcut here,

it's going to automatically translate the text, which is really useful and this is just best practice.

We're not actually going to be implementing any translation in our code, but it's always best practice


-->'classes':('wide',)
classes is a way that you can assign custom Css classes in the Django (its optional)
'''