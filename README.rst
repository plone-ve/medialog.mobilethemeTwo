=======================
medialog.mobilethemeTwo
=======================


Introduction
============

``medialog.mobilethemeTwo`` is an installable Plone Mobile Theme developed by 
`Grieg Medialog AS`_ using the **theming** and **packaging** features available 
in `plone.app.theming`_, `plone.app.themingplugins`_ and `zettwerk.mobiletheming`_ packages.

.. image:: https://github.com/espenmn/medialog.mobilethemeTwo/raw/master/medialog/mobilethemeTwo/static/preview.png
  :alt: medialog.mobilethemeTwo Mobile Theme
  :align: center


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/espenmn/medialog.mobilethemeTwo/raw/master/screenshot0.png
  :alt: medialog.mobilethemeTwo theme Demo at Computer device
  :align: center

A demo using the ``medialog.mobilethemeTwo`` add-on as a reduced view for Mobile device look like the following:

.. image:: https://github.com/espenmn/medialog.mobilethemeTwo/raw/master/screenshot1.png
  :alt: medialog.mobilethemeTwo theme Demo at Mobile device
  :align: center


Features
========

- It's an Mobile Theme with responsive design support.
- It's an installable Plone Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- It's uses ``plone.app.themingplugins`` package to override templates.
- Also it's a simple Diazo package (Zip file).


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming``, ``plone.app.themingplugins`` and ``zettwerk.mobiletheming`` packages (*will be installed as a dependencies of this package*)


Installation
============


Zip file
--------

If you are an end user, you might enjoy installation via zip file import.

1. Download a `zip file <https://github.com/espenmn/medialog.mobilethemeTwo/raw/master/medialog.mobilethemeTwo.zip>`_.
2. Import the theme from the Diazo theme control panel.

Enabling the theme
^^^^^^^^^^^^^^^^^^

Select and enable the theme from the Diazo control panel. That's it!


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``medialog.mobilethemeTwo`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        medialog.mobilethemeTwo


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'medialog.mobilethemeTwo',
    ],


Usage
=====

A theme intended for use with mobile theming control panel (``zettwerk.mobiletheming``).

You probably want to use the theme like this:

- install ``zettwerk.mobiletheming`` package

- install ``medialog.mobilethemeTwo`` package

- go to the mobile theming control panel and choose which url that should have the mobile theme.

- It is of course possible to enable the theme in diazo theme control panel and use it as a regular theme


When you want to edit the theme, you should do this on the file system.
If you duplicate it TTW, the overridden templates will not be used.

plone.app.themingplugins integration
------------------------------------

The theme uses ``plone.app.themingplugins`` package to override templates just for this theme.
These templates will not work if you duplicate the theme TTW (``plone.app.themingplugins`` package do not work for that).


Contribute
==========

- Issue Tracker: https://github.com/espenmn/medialog.mobilethemeTwo/issues
- Source Code: https://github.com/espenmn/medialog.mobilethemeTwo


License
=======

The project is licensed under the GPLv2.

Nice Icons from IcoMoon is included (GPL or CC BY 3.0) license.

Credits
-------

Author
^^^^^^

- Espen Moe-Nilssen (espen at medialog dot no), Grieg Medialog AS.

.. _`Grieg Medialog AS`: http://www.medialog.no/
.. _`plone.app.themingplugins`: https://pypi.org/project/plone.app.themingplugins/
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`zettwerk.mobiletheming`: https://github.com/collective/zettwerk.mobiletheming
