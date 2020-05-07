from sqlalchemy.dialects import registry
import pytest

registry.register(
    "sybase.pyodbc", "sqlalchemy_sybase.pyodbc", "SybaseDialect_pyodbc"
)

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")

from sqlalchemy.testing.plugin.pytestplugin import *
