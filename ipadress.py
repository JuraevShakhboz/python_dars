import ipaddress

def ip_address_validator(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        print(f"{ip} is a valid IP address")
    except ValueError:
        print(f"ERROR: {ip} is not a valid IP address!")
        
ip_address_validator("192.168.5.1")