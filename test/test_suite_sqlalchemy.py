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
    ExpandingBoundInTest as _ExpandingBoundInTest,
)
from sqlalchemy.testing.suite import InsertBehaviorTest as _InsertBehaviorTest


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
