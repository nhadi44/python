import socket
def getMachineInfo():
    remote_host = 'www.kreditpintar.com'
    try:
        print("IP address of %s: %s" %(remote_host,socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print("%s: %s" %s(remote_host, err_msg))

if __name__ == "__main__":
    getMachineInfo()    