=================
Template Explorer
=================

Template Explorer is a Django app to aid getting a handle on your
project's templates.

----------
Quickstart
----------

Installing
==========

.. code-block:: bash

   $ pip install git+https://github.com/macro1/django-template-explorer.git

Project configuration
=====================

Add :code:`template_explorer` to your :code:`INSTALLED_APPS`:

.. code-block:: python

   INSTALLED_APPS = [
      # ...
      'template_explorer',
   ]

Run the commands
================

View templates available in your project:

.. code-block:: bash

   $ python manage.py template_tree
