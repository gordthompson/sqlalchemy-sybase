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
from sqlalchemy.testing.suite import (
    DeprecatedCompoundSelectTest as _DeprecatedCompoundSelectTest,
)
from sqlalchemy.testing.suite import (
    DifficultParametersTest as _DifficultParametersTest,
)
from sqlalchemy.testing.suite import (
    ExpandingBoundInTest as _ExpandingBoundInTest,
)
from sqlalchemy.testing.suite import HasIndexTest as _HasIndexTest
from sqlalchemy.testing.suite import HasTableTest as _HasTableTest
from sqlalchemy.testing.suite import InsertBehaviorTest as _InsertBehaviorTest
from sqlalchemy.testing.suite import IntegerTest as _IntegerTest
from sqlalchemy.testing.suite import TimeTest as _TimeTest
from sqlalchemy.testing.suite import UnicodeVarcharTest as _UnicodeVarcharTest


class ComponentReflectionTest(_ComponentReflectionTest):
    @testing.skip("sybase")
    def test_get_indexes(self):
        # we don't handle exclusions
        return

    @testing.skip("sybase")
    def test_get_unique_constraints(self):
        # "Incorrect syntax near ','."
        # (... but the same query works okay from a DBeaver SQL Editor pane)
        return

    @testing.skip("sybase")
    def test_get_multi_columns(self):
        # (not yet supported)
        return

    @testing.skip("sybase")
    def test_get_multi_indexes(self):
        # (not yet supported)
        return

    @testing.skip("sybase")
    def test_get_multi_pk_constraint(self):
        # (not yet supported)
        return

    @testing.skip("sybase")
    def test_get_multi_unique_constraints(self):
        # (not yet supported)
        return

    @testing.skip("sybase")
    def test_metadata(self):
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

    @testing.skip("sybase")
    def test_select_direct(self):
        return


class DateTimeCoercedToDateTimeTest(_DateTimeCoercedToDateTimeTest):
    @testing.skip("sybase")
    def test_null_bound_comparison(self):
        # "The datatype of a parameter marker used in the dynamic
        #  prepare statement could not be resolved."
        return

    @testing.skip("sybase")
    def test_select_direct(self):
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

    @testing.skip("sybase")
    def test_select_direct(self):
        return


class DeprecatedCompoundSelectTest(_DeprecatedCompoundSelectTest):
    @testing.skip("sybase")
    def test_distinct_selectable_in_unions(self):
        # LIMIT clause is not allowed in UNION.
        return

    @testing.skip("sybase")
    def test_limit_offset_aliased_selectable_in_unions(self):
        # LIMIT clause is not allowed in UNION.
        return

    @testing.skip("sybase")
    def test_limit_offset_selectable_in_unions(self):
        # Incorrect syntax near the keyword 'ORDER'.
        return

    @testing.skip("sybase")
    def test_order_by_selectable_in_unions(self):
        # LIMIT clause is not allowed in UNION.
        return


class DifficultParametersTest(_DifficultParametersTest):
    @testing.skip("sybase")
    def test_round_trip_same_named_column(self):
        return


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


class HasIndexTest(_HasIndexTest):
    @testing.skip("sybase")
    def test_has_index(self):
        return


class HasTableTest(_HasTableTest):
    @testing.skip("sybase")
    def test_has_table_cache(self):
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


class IntegerTest(_IntegerTest):
    @testing.skip("sybase")
    def test_huge_int_auto_accommodation(self):
        return


class TimeTest(_TimeTest):
    @testing.skip("sybase")
    def test_select_direct(self):
        return


class QuotedNameArgumentTest:
    """Some of these tests can hang the test run."""
    pass


class UnicodeVarcharTest(_UnicodeVarcharTest):
    @testing.skip("sybase")
    def test_literal_non_ascii(self):
        # (test hangs)
        return

    @testing.skip("sybase")
    def test_literal_nonnative_text(self):
        # (test hangs)
        return


class UuidTest:
    """Some of these tests can hang the test run."""
    pass
