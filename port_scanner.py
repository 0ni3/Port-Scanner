import socket


OPEN_PORTS = []


def get_host_ip(target):
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror() as e:
        # get address info error
        print(f"C'è stato un errore... {e}")
    else:
        return ip_addr


def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    status = sock.connect_ex((ip, port))
    # aggiungiamo la porta se lo stato è uguale a 0
    if status == 0:
        OPEN_PORTS.append(port)
    sock.close()


if __name__ == "__main__":
    print("Port Scanner")
    target = input("Inserisci un target: ")
    ip_addr = get_host_ip(target)
    while True:
        try:
            port = int(input("Inserisci la porta: "))
            scan_port(ip_addr, port)
            print(OPEN_PORTS)
        except KeyboardInterrupt:
            print("\nProgramma terminato...")
            break


