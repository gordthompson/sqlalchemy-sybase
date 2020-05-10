#!/usr/bin/bash
python _cleanup_test_tables.py
# use the "default=" URI in test.cfg
pytest
