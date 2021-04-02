# sybase/__init__.py
# Copyright (C) 2005-2020 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from sqlalchemy.dialects import registry as _registry
from . import base  # noqa
from . import pyodbc  # noqa
from .base import BIGINT
from .base import BINARY
from .base import BIT
from .base import CHAR
from .base import DATE
from .base import DATETIME
from .base import FLOAT
from .base import IMAGE
from .base import INT
from .base import INTEGER
from .base import MONEY
from .base import NCHAR
from .base import NUMERIC
from .base import NVARCHAR
from .base import SMALLINT
from .base import SMALLMONEY
from .base import TEXT
from .base import TIME
from .base import TINYINT
from .base import UNICHAR
from .base import UNITEXT
from .base import UNIVARCHAR
from .base import VARBINARY
from .base import VARCHAR
from .pyodbc import get_odbc_info

__version__ = "1.0.6"

# default (and only) dialect
base.dialect = dialect = pyodbc.dialect

_registry.register(
    "sybase.pyodbc", "sqlalchemy_sybase.pyodbc", "SybaseDialect_pyodbc"
)

__all__ = (
    "CHAR",
    "VARCHAR",
    "TIME",
    "NCHAR",
    "NVARCHAR",
    "TEXT",
    "DATE",
    "DATETIME",
    "FLOAT",
    "NUMERIC",
    "BIGINT",
    "INT",
    "INTEGER",
    "SMALLINT",
    "BINARY",
    "VARBINARY",
    "UNITEXT",
    "UNICHAR",
    "UNIVARCHAR",
    "IMAGE",
    "BIT",
    "MONEY",
    "SMALLMONEY",
    "TINYINT",
    "dialect",
)
