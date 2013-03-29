===========================
    django-uwsgi-admin
===========================

Fork of https://github.com/unbit/uwsgi_django with better integration, packaging fixed etc etc ...

Installation
============

``pip install django-wsgi-admin`` and add ``uwsgi_admin`` to ``INSTALLED_APPS``. Thats it !

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
