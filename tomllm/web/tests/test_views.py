"""Minimal unit tests for the web tests package.

These tests are intentionally simple and don't require Django. They
are used to validate the test runner and avoid heavy Django setup for
quick CI feedback.
"""


def test_basic_math():
    """A trivial test to confirm the test runner is working."""
    assert 1 + 1 == 2


def test_string_operations():
    """Simple string test."""
    s = "hello"
    assert s.upper() == "HELLO"
