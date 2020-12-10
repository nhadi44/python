import socket

def print_machine_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Host name : %s" %hostname)
    print("Ip Address : %s" %ip_address)

if __name__ == '__main__':
    print_machine_info()