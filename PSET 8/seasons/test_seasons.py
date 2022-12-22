import datetime
from seasons import get_dob
import pytest
import sys


def test_get_dob():
    assert get_dob("2005-12-31") == datetime.date(2005, 12, 31)
    with pytest.raises(SystemExit):
        assert get_dob("January 1, 1999")


if __name__ == "__main__":
    main()
