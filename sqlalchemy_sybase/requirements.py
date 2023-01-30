from sqlalchemy.testing.requirements import SuiteRequirements as SuiteRequirementsSQLA
from alembic.testing.requirements import SuiteRequirements as SuiteRequirementsAlembic

from sqlalchemy.testing import exclusions


class Requirements(SuiteRequirementsSQLA, SuiteRequirementsAlembic):
    @property
    def array_type(self):
        return exclusions.closed()

    @property
    def bound_limit_offset(self):
        return exclusions.closed()

    @property
    def datetime_microseconds(self):
        return exclusions.closed()

    @property
    def empty_strings_varchar(self):
        return exclusions.closed()

    @property
    def floats_to_four_decimals(self):
        return exclusions.closed()

    @property
    def foreign_key_constraint_reflection(self):
        return exclusions.closed()

    @property
    def nullable_booleans(self):
        return exclusions.closed()

    @property
    def precision_generic_float_type(self):
        return exclusions.closed()

    @property
    def reflects_pk_names(self):
        return exclusions.open()

    @property
    def schemas(self):
        return exclusions.closed()

    @property
    def sql_expression_limit_offset(self):
        return exclusions.closed()

    @property
    def standalone_null_binds_whereclause(self):
        return exclusions.closed()

    @property
    def supports_is_distinct_from(self):
        return exclusions.closed()

    @property
    def temporary_tables(self):
        return exclusions.closed()

    @property
    def temp_table_reflection(self):
        return exclusions.closed()

    @property
    def temp_table_reflect_indexes(self):
        return exclusions.closed()

    @property
    def temporary_views(self):
        return exclusions.closed()

    @property
    def text_type(self):
        # "Implicit conversion from datatype 'TEXT' to 'VARCHAR'
        #  is not allowed.  Use the CONVERT function ..."
        return exclusions.closed()

    @property
    def time_microseconds(self):
        return exclusions.closed()

    # Alembic test suite requirements

    @property
    def fk_ondelete_restrict(self):
        return exclusions.closed()

    @property
    def fk_onupdate_restrict(self):
        return exclusions.closed()

    @property
    def uuid_data_type(self):
        return exclusions.closed()

    @property
    def view_column_reflection(self):
        return exclusions.open()
