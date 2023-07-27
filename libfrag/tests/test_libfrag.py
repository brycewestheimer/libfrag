"""
Unit and regression test for the libfrag package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import libfrag


def test_libfrag_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "libfrag" in sys.modules
