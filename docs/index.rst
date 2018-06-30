Dunderfile: :code:`inspect` for humans
======================================

.. automodule:: dunderfile
   :no-members:

Example usage
-------------

.. code-block:: python

    from dunderfile import __LINE__, helper

    def function():
        print("This print statement is on line {}".format(__LINE__()))
        print("And this one is on line {}".format(helper.__LINE__))

-------------
API reference
-------------

.. autofunction:: dunderfile.dunderfile
.. autofunction:: dunderfile.dunderline
.. autofunction:: dunderfile.dunderfunc

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Helper properties for preprocessor-like usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:attribute:: dunderfile.helper.__FILE__

   Get the filename of the location where this property is used.

   .. code-block:: python

      from dunderfile import helper as h
      print(h.__FILE__)

.. py:attribute:: dunderfile.helper.__LINE__

   Get the line number of the location where this property is used.

   .. code-block:: python

      from dunderfile import helper as h
      print(h.__LINE__)

.. py:attribute:: dunderfile.helper.__func__

   Get the function name of the location where this property is used.

   .. code-block:: python

      from dunderfile import helper as h
      print(h.__func__)
