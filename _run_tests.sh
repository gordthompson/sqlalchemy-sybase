#!/usr/bin/bash
python _cleanup_test_tables.py
# use the "default=" URI in test.cfg
pytest

# possible subsets
#
#pytest test/test_suite_alembic.py
#pytest test/test_suite_sqlalchemy.py
