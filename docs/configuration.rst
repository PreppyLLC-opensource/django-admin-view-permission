Configuration
=============

The admin view permission provides one setting that you can add in your project's
settings module to customize its behavior.

ADMIN_VIEW_PERMISSION_MODELS
----------------------------

This setting defines which models you want to be added the view permission. If
you don't specify this setting then the view permission will be applied to all
the models.

Example
~~~~~~~
::

     ADMIN_VIEW_PERMISSION_MODELS = [
         'auth.User',
         ...
     ]

ADMIN_VIEW_PERMISSION_EXCLUDE_MODELS
------------------------------------

You can also use another setting in which you can provide models which
you want to be excluded from the view permission. The view permission will be
applied to all the models except those listed in this list.

Example
~~~~~~~
::

    ADMIN_VIEW_PERMISSION_EXCLUDE_MODELS = [
        'auth.User',
        ...
    ]

:warning: You can't use both settings at the same time.
