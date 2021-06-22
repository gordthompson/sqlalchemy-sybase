from sqlalchemy import extract
from sqlalchemy.testing import AssertsCompiledSQL
from sqlalchemy.testing.suite import *
from sqlalchemy.testing.suite import (
    ComponentReflectionTest as _ComponentReflectionTest,
)
from sqlalchemy.testing.suite import CompoundSelectTest as _CompoundSelectTest
from sqlalchemy.testing.suite import DateTest as _DateTest
from sqlalchemy.testing.suite import (
    DateTimeCoercedToDateTimeTest as _DateTimeCoercedToDateTimeTest,
)
from sqlalchemy.testing.suite import (
    DateTimeMicrosecondsTest as _DateTimeMicrosecondsTest,
)
from sqlalchemy.testing.suite import DateTimeTest as _DateTimeTest

try:
    from sqlalchemy.testing.suite import (
        DeprecatedCompoundSelectTest as _DeprecatedCompoundSelectTest,
    )
except ImportError:
    pass

try:
    from sqlalchemy.testing.suite import DistinctOnTest as _DistinctOnTest
except ImportError:
    pass

from sqlalchemy.testing.suite import (
    ExpandingBoundInTest as _ExpandingBoundInTest,
)
from sqlalchemy.testing.suite import InsertBehaviorTest as _InsertBehaviorTest

import sqlalchemy_sybase as sybase


class ComponentReflectionTest(_ComponentReflectionTest):
    @testing.skip("sybase")
    def test_get_unique_constraints(self):
        # "Incorrect syntax near ','."
        # (... but the same query works okay from a DBeaver SQL Editor pane)
        return


class CompoundSelectTest(_CompoundSelectTest):
    @testing.skip("sybase")
    def test_distinct_selectable_in_unions(self):
        # "LIMIT clause is not allowed in UNION."
        return

    @testing.skip("sybase")
    def test_limit_offset_aliased_selectable_in_unions(self):
        # "An ORDER BY clause is not allowed in a derived table."
        return

    @testing.skip("sybase")
    def test_limit_offset_in_unions_from_alias(self):
        # "An ORDER BY clause is not allowed in a derived table."
        return

    @testing.skip("sybase")
    def test_limit_offset_selectable_in_unions(self):
        # "Incorrect syntax near the keyword 'ORDER'."
        return

    @testing.skip("sybase")
    def test_order_by_selectable_in_unions(self):
        # "LIMIT clause is not allowed in UNION."
        return


class DateTest(_DateTest):
    @testing.skip("sybase")
    def test_null_bound_comparison(self):
        # "The datatype of a parameter marker used in the dynamic
        #  prepare statement could not be resolved."
        return


class DateTimeCoercedToDateTimeTest(_DateTimeCoercedToDateTimeTest):
    @testing.skip("sybase")
    def test_null_bound_comparison(self):
        # "The datatype of a parameter marker used in the dynamic
        #  prepare statement could not be resolved."
        return


class DateTimeMicrosecondsTest(_DateTimeMicrosecondsTest):
    @testing.skip("sybase")
    def test_null_bound_comparison(self):
        # "The datatype of a parameter marker used in the dynamic
        #  prepare statement could not be resolved."
        return


class DateTimeTest(_DateTimeTest):
    @testing.skip("sybase")
    def test_null_bound_comparison(self):
        # "The datatype of a parameter marker used in the dynamic
        #  prepare statement could not be resolved."
        return


try:

    class DeprecatedCompoundSelectTest(_DeprecatedCompoundSelectTest):
        @testing.skip("sybase")
        def test_distinct_selectable_in_unions(self):
            # "LIMIT clause is not allowed in UNION."
            return

        @testing.skip("sybase")
        def test_limit_offset_aliased_selectable_in_unions(self):
            # "An ORDER BY clause is not allowed in a derived table."
            return

        @testing.skip("sybase")
        def test_limit_offset_selectable_in_unions(self):
            # "Incorrect syntax near the keyword 'ORDER'."
            return

        @testing.skip("sybase")
        def test_order_by_selectable_in_unions(self):
            # "LIMIT clause is not allowed in UNION."
            return


except NameError:
    pass

try:

    class DistinctOnTest(_DistinctOnTest):
        @testing.skip("sybase")
        def test_distinct_on(self):
            # "AssertionError: Warnings were not seen: ..."
            return


except NameError:
    pass


class ExpandingBoundInTest(_ExpandingBoundInTest):
    @testing.skip("sybase")
    def test_empty_set_against_string(self):
        # "Implicit conversion from datatype 'VARCHAR' to 'INT' is not allowed."
        return

    @testing.skip("sybase")
    def test_empty_set_against_string_negation(self):
        # "Implicit conversion from datatype 'VARCHAR' to 'INT' is not allowed."
        return

    @testing.skip("sybase")
    def test_null_in_empty_set_is_false(self):
        # "Incorrect syntax near the keyword 'NULL'."
        return


class InsertBehaviorTest(_InsertBehaviorTest):
    @testing.skip("sybase")
    def test_empty_insert(self):
        # "Incorrect syntax near ')'."
        return

    @testing.skip("sybase")
    def test_empty_insert_multiple(self):
        # "Incorrect syntax near ')'."
        return

    @testing.skip("sybase")
    def test_limit_offset_selectable_in_unions(self):
        # "Incorrect syntax near the keyword 'ORDER'."
        return

    @testing.skip("sybase")
    def test_insert_from_select_with_defaults(self):
        # "Explicit value specified for identity field in table
        # 'includes_defaults' when 'SET IDENTITY_INSERT' is OFF."
        return


except NameError:
    pass

# =================================================
# ---------- End of Test Suite overrides ----------
# =================================================


class CompileTestImportedFromInternalDialect(
    fixtures.TestBase, AssertsCompiledSQL
):
    __dialect__ = sybase.dialect()

    def test_extract(self):
        t = sql.table("t", sql.column("col1"))

        mapping = {
            "day": "day",
            "doy": "dayofyear",
            "dow": "weekday",
            "milliseconds": "millisecond",
            "millisecond": "millisecond",
            "year": "year",
        }

        for field, subst in list(mapping.items()):
            self.assert_compile(
                select([extract(field, t.c.col1)]),
                'SELECT DATEPART("%s", t.col1) AS anon_1 FROM t' % subst,
            )

    def test_limit_offset(self):
        stmt = select([1]).limit(5).offset(6)
        assert stmt.compile().params == {"param_1": 5, "param_2": 6}
        self.assert_compile(
            stmt, "SELECT 1 ROWS LIMIT :param_1 OFFSET :param_2"
        )

    def test_offset(self):
        stmt = select([1]).offset(10)
        assert stmt.compile().params == {"param_1": 10}
        self.assert_compile(stmt, "SELECT 1 ROWS OFFSET :param_1")

    def test_limit(self):
        stmt = select([1]).limit(5)
        assert stmt.compile().params == {"param_1": 5}
        self.assert_compile(stmt, "SELECT 1 ROWS LIMIT :param_1")

    def test_delete_extra_froms(self):
        t1 = sql.table("t1", sql.column("c1"))
        t2 = sql.table("t2", sql.column("c1"))
        q = sql.delete(t1).where(t1.c.c1 == t2.c.c1)
        self.assert_compile(
            q, "DELETE FROM t1 FROM t1, t2 WHERE t1.c1 = t2.c1"
        )

    def test_delete_extra_froms_alias(self):
        a1 = sql.table("t1", sql.column("c1")).alias("a1")
        t2 = sql.table("t2", sql.column("c1"))
        q = sql.delete(a1).where(a1.c.c1 == t2.c.c1)
        self.assert_compile(
            q, "DELETE FROM a1 FROM t1 AS a1, t2 WHERE a1.c1 = t2.c1"
        )
        self.assert_compile(sql.delete(a1), "DELETE FROM t1 AS a1")


class TempTableDDLTest(fixtures.TablesTest):
    __backend__ = True

    @classmethod
    def define_tables(cls, metadata):
        pass

    @testing.provide_metadata
    def test_temp_table(self, connection):
        table_name = "#tmp"
        t = Table(
            table_name,
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("txt", String(50)),
        )
        t.create(connection)
        connection.execute(t.insert({"txt": "temp table test"}))
        result = connection.execute(t.select()).scalar()
        eq_(result, 1)
        connection.execute(text(f"DROP TABLE {table_name}"))
