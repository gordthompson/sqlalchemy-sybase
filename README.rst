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

Status
------

This dialect currently depends on SQLAlchemy features that have not been
officially released. For now you must **first** install SQLAlchemy from
source **before** installing this dialect.

For SQLAlchemy 1.3 ...::

    pip install git+https://github.com/sqlalchemy/sqlalchemy@rel_1_3

... or for (pre-release) SQLAlchemy 1.4 ...::

    pip install git+https://github.com/sqlalchemy/sqlalchemy.git

Pre-requisites
--------------

You will need an ODBC driver for Sybase installed on the machine from which
you want to connect to the Sybase server. This dialect is tested with
a *current version* of the FreeTDS ODBC driver.


Co-requisites
-------------

This dialect requires SQLAlchemy and pyodbc. They are both specified as requirements so ``pip`` will install
them if they are not already in place. To install, just::

    pip install sqlalchemy-sybase --pre

Getting Started
---------------

Create an `ODBC DSN (Data Source Name)`_ that points to your Sybase database.
Then, in your Python app, you can connect to the database via::

    from sqlalchemy import create_engine
    engine = create_engine("sybase+pyodbc://scott:tiger@your_dsn")

For other ways of connecting see the `Getting Connected`_ page in the Wiki.

.. _ODBC DSN (Data Source Name): https://support.microsoft.com/en-ca/help/966849/what-is-a-dsn-data-source-name
.. _Getting Connected: https://github.com/sqlalchemy/sqlalchemy-sybase/wiki/Getting-Connected

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
