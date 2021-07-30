# Defanging IP Address: Problem Statement
# Defanging ip address means replacing "." with "[.]"


def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    print(split_address)
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address


ip_address_new = ip_address("1.1.2.3")
print(ip_address_new)
