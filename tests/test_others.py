from __future__ import unicode_literals

from django.apps import apps
from django.conf import UserSettingsHolder, settings
from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.core.signals import setting_changed
from django.test import SimpleTestCase, override_settings

from admin_view_permission.admin import AdminViewPermissionModelAdmin


class TestTestAppModelAdminOverride(SimpleTestCase):

    def test_testapp_modeladmin_override_1(self):
        for model in admin.site._registry:
            assert isinstance(admin.site._registry[model],
                              AdminViewPermissionModelAdmin)
            assert isinstance(admin.site._registry[model], admin.ModelAdmin)


# noinspection PyPep8Naming
class reload_apps(override_settings):

    def enable(self):
        override = UserSettingsHolder(settings._wrapped)
        for key, new_value in self.options.items():
            setattr(override, key, new_value)
        self.wrapped = settings._wrapped
        settings._wrapped = override
        for key, new_value in self.options.items():
            setting_changed.send(sender=settings._wrapped.__class__,
                                 setting=key, value=new_value, enter=True)
        if 'INSTALLED_APPS' in self.options:
            try:
                apps.set_installed_apps(self.options['INSTALLED_APPS'])
            except Exception:
                apps.unset_installed_apps()
                raise


class TestImproperlyConfigured(SimpleTestCase):

    def test_improperly_configured(self):
        try:
            with reload_apps(ADMIN_VIEW_PERMISSION_MODELS=[],
                             ADMIN_VIEW_PERMISSION_EXCLUDE_MODELS=[],
                             INSTALLED_APPS=['admin_view_permission']):
                pass
        except ImproperlyConfigured:
            pass
        else:
            raise AssertionError
