from numb3rs import validate

def main():
    test_string()
    test_valid_ip()
    test_invalid_ip()


def test_string():
    assert validate("cat") == False
    assert validate("123") == False


def test_valid_ip():
    assert validate("127.0.0.1") == True


def test_invalid_ip():
    assert validate("127.0.256.1") == False
    assert validate("256.999.789.321") == False


if __name__ == "__main__":
    main()
