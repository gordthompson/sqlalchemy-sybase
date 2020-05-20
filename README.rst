sqlalchemy-sybase
=================

.. image:: https://img.shields.io/pypi/dm/sqlalchemy-sybase.svg
        :target: https://pypi.org/project/sqlalchemy-sybase/

SAP ASE (Sybase) support for SQLAlchemy.

Objectives
----------

This is a fork of SQLAlchemy's internal "sybase" dialect
which is soon to be deprecated and will be removed from a
future release.

Pre-requisites
--------------

You will need an ODBC driver for SAP ASE installed on the machine from which
you want to connect to the SAP ASE server. This dialect is tested with
a *current version* of the `FreeTDS`_ ODBC driver.

.. _FreeTDS: https://www.freetds.org/

Also, if you are running on Linux and using `unixODBC`_, check the version via
``odbcinst -j``. The official repositories of several Linux distributions
contain versions of unixODBC that are quite old and somewhat buggy.

.. _unixODBC: http://www.unixodbc.org/


Installing
----------

SQLAlchemy and pyodbc are specified as requirements so ``pip`` will install
them if they are not already in place. To install, just::

    pip install sqlalchemy-sybase

Getting Started
---------------

Create an `ODBC DSN (Data Source Name)`_ that points to your SAP ASE database.
Then, in your Python app, you can connect to the database via::

    from sqlalchemy import create_engine
    engine = create_engine("sybase+pyodbc://scott:tiger@your_dsn")

For other ways of connecting see the `Getting Connected`_ page in the Wiki.

.. _ODBC DSN (Data Source Name): https://support.microsoft.com/en-ca/help/966849/what-is-a-dsn-data-source-name
.. _Getting Connected: https://github.com/gordthompson/sqlalchemy-sybase/wiki/Getting-Connected

The SQLAlchemy Project
======================

sqlalchemy-sybase is affiliated with the `SQLAlchemy Project <https://www.sqlalchemy.org>`_ and
adheres to the same standards and conventions as the core project.

Development / Bug reporting / Pull requests
-------------------------------------------

Please refer to the
`SQLAlchemy Community Guide <https://www.sqlalchemy.org/develop.html>`_ for
guidelines on coding and participating in this project.

Code of Conduct
_______________

Above all, SQLAlchemy places great emphasis on polite, thoughtful, and
constructive communication between users and developers.
Please see the current Code of Conduct at
`Code of Conduct <https://www.sqlalchemy.org/codeofconduct.html>`_.

License
=======

sqlalchemy-sybase is distributed under the `MIT license
<https://opensource.org/licenses/MIT>`_.
