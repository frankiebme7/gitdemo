from netmiko import ConnectHandler
from getpass import getpass


user = input('Please enter your username: ')
secret = getpass('Please enter your password: ')


ciscoDevice = {
    'device_type': 'cisco_ios',
    'host': '192.168.21.131',
    'username': user,
    'password': secret
}

connection = ConnectHandler(**ciscoDevice)
