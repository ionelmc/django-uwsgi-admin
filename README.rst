===========================
    django-uwsgi-admin
===========================

Fork of https://github.com/unbit/uwsgi_django with better integration, packaging fixed etc etc ...

Installation
============

Run ``pip install django-uwsgi-admin2`` and add ``uwsgi_admin`` to ``INSTALLED_APPS``. Thats it !

.. note:: You can also run ``pip install "django-uwsgi-admin2[uwsgi]"`` - `uwsgi` is not a mandatory dependency.


Bonus: debug_toolbar uWSGIDebugPanel
====================================

Just add ``'uwsgi_admin.panels.uWSGIDebugPanel'`` to your ``DEBUG_TOOLBAR_PANELS``.

Eg::

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
        'uwsgi_admin.panels.uWSGIDebugPanel',
    )

Obligatory screenshots
======================


Admin
-----

.. image:: https://raw.github.com/ionelmc/django-uwsgi-admin/master/docs/uWSGI-Stats.jpeg

Debug Toolbar
-------------

.. image:: https://raw.github.com/ionelmc/django-uwsgi-admin/master/docs/uWSGI-Stats-debug-panel.jpeg
