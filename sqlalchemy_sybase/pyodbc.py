# sybase/pyodbc.py
# Copyright (C) 2005-2020 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""
.. dialect:: sybase+pyodbc
    :name: PyODBC
    :dbapi: pyodbc
    :connectstring: sybase+pyodbc://<username>:<password>@<dsnname>[/<database>]
    :url: http://pypi.python.org/pypi/pyodbc/

Unicode Support
---------------

The pyodbc driver currently supports usage of these Sybase types with
Unicode or multibyte strings::

    CHAR
    NCHAR
    NVARCHAR
    TEXT
    VARCHAR

Currently *not* supported are::

    UNICHAR
    UNITEXT
    UNIVARCHAR

"""  # noqa

import decimal

import odbcinst
import pyodbc

from sqlalchemy import processors
from sqlalchemy import types as sqltypes
from sqlalchemy.connectors.pyodbc import PyODBCConnector
from sqlalchemy.exc import DBAPIError
from .base import SybaseDialect
from .base import SybaseExecutionContext


def get_odbc_info(engine):
    """retrieve ODBC configuration information for troubleshooting purposes
    """
    info = odbcinst.j()
    try:
        cnxn = engine.raw_connection()
        info["SQL_DRIVER_NAME"] = cnxn.getinfo(pyodbc.SQL_DRIVER_NAME)
        info["SQL_DRIVER_VER"] = cnxn.getinfo(pyodbc.SQL_DRIVER_VER)
        info["SQL_DBMS_VER"] = cnxn.getinfo(pyodbc.SQL_DBMS_VER)
    except DBAPIError:
        pass
    return info


class _SybNumeric_pyodbc(sqltypes.Numeric):
    """Turns Decimals with adjusted() < -6 into floats.

    It's not yet known how to get decimals with many
    significant digits or very large adjusted() into Sybase
    via pyodbc.

    """

    def bind_processor(self, dialect):
        super_process = super(_SybNumeric_pyodbc, self).bind_processor(dialect)

        def process(value):
            if self.asdecimal and isinstance(value, decimal.Decimal):

                if value.adjusted() < -6:
                    return processors.to_float(value)

            if super_process:
                return super_process(value)
            else:
                return value

        return process


class SybaseExecutionContext_pyodbc(SybaseExecutionContext):
    def set_ddl_autocommit(self, connection, value):
        if value:
            connection.autocommit = True
        else:
            connection.autocommit = False


class SybaseDialect_pyodbc(PyODBCConnector, SybaseDialect):
    execution_ctx_cls = SybaseExecutionContext_pyodbc

    supports_statement_cache = True  # for SQLA 1.4.5+

    colspecs = {sqltypes.Numeric: _SybNumeric_pyodbc}

    def __init__(self, fast_executemany=False, **params):
        super(SybaseDialect_pyodbc, self).__init__(**params)
        self.fast_executemany = fast_executemany

    @classmethod
    def dbapi(cls):
        return PyODBCConnector.dbapi()

    def on_connect(self):
        super_ = super(SybaseDialect_pyodbc, self).on_connect()

        def on_connect(conn):
            if super_ is not None:
                super_(conn)

        return on_connect

    def do_executemany(self, cursor, statement, parameters, context=None):
        if self.fast_executemany:
            cursor.fast_executemany = True
        super(SybaseDialect_pyodbc, self).do_executemany(
            cursor, statement, parameters, context=context
        )


dialect = SybaseDialect_pyodbc
