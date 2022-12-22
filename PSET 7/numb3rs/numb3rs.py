import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit(1)


def validate(ip):
    valid_ip_address_regex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    result = re.match(valid_ip_address_regex, ip)
    if result != None:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
