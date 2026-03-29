import pytest

from brickflowui.databricks.uc import _quote_identifier, _validated_limit


def test_quote_identifier_escapes_backticks():
    assert _quote_identifier("catalog`name") == "`catalog``name`"


def test_quote_identifier_rejects_empty_values():
    with pytest.raises(ValueError):
        _quote_identifier("")


def test_validated_limit_rejects_non_positive_values():
    with pytest.raises(ValueError):
        _validated_limit(0)
