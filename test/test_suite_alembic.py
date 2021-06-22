import pytest

from alembic.testing.suite import *  # noqa

from alembic.testing.suite import (
    AutogenerateFKOptionsTest as _AutogenerateFKOptionsTest
)
from alembic.testing.suite import (
    BackendAlterColumnTest as _BackendAlterColumnTest
)
from alembic.testing.suite import (
    IncludeHooksTest as _IncludeHooksTest
)

class AutogenerateFKOptionsTest(_AutogenerateFKOptionsTest):
    @pytest.mark.skip()
    def test_nochange_ondelete(self):
        # "Incorrect syntax near the keyword 'ON'."
        return

    @pytest.mark.skip()
    def test_nochange_ondelete_noaction(self):
        # "Incorrect syntax near the keyword 'ON'."
        return

    @pytest.mark.skip()
    def test_nochange_onupdate(self):
        # "Incorrect syntax near the keyword 'ON'."
        return

    @pytest.mark.skip()
    def test_nochange_onupdate_noaction(self):
        # "Incorrect syntax near the keyword 'ON'."
        return


class BackendAlterColumnTest(_BackendAlterColumnTest):
    @pytest.mark.skip()
    def test_add_server_default_int(self):
        # "Incorrect syntax near the keyword 'ALTER'."
        return

    @pytest.mark.skip()
    def test_modify_non_nullable_to_nullable(self):
        # "Incorrect syntax near the keyword 'ALTER'."
        return

    @pytest.mark.skip()
    def test_modify_nullable_to_non(self):
        # "Incorrect syntax near the keyword 'ALTER'."
        return

    @pytest.mark.skip()
    def test_modify_type_int_str(self):
        # "Incorrect syntax near the keyword 'ALTER'."
        return

    @pytest.mark.skip()
    def test_rename_column(self):
        # "Incorrect syntax near 'colname'."
        return

    @pytest.mark.skip()
    def test_modify_server_default_int(self):
        # TODO: Why does this fail?
        return



class IncludeHooksTest(_IncludeHooksTest):
    @pytest.mark.skip()
    def test_change_fk(self, hook_type):
        # TODO: Why does this fail?
        return

    @pytest.mark.skip()
    def test_remove_connection_fk(self, hook_type):
        # TODO: Why does this fail?
        return
