from working import convert
import pytest


def test_normal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_with_minutes():
    assert convert("6:30 PM to 2:30 AM") == "18:30 to 02:30"


def test_invalid_hours():
    with pytest.raises(ValueError):
        assert convert("18 AM to 26 PM")


def test_missing_to():
    with pytest.raises(ValueError):
        assert convert("9 AM 5 PM")


def test_invalid_range_format():
    with pytest.raises(ValueError):
        assert convert("9:00 AM, 17:00 PM")


def test_incorrect_time_format():
    with pytest.raises(ValueError):
        assert convert("9;00 AM to 5;00 PM")


if __name__ == "__main__":
    main()
