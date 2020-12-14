import socket


def connect(hostname, port_):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((hostname, port_))
    sock.close()
    return result == 0


def brut_oct(ip, port_):
    ip_list_open_port.clear()
    for oct_4 in range(0, 256):
        print(ip + '.' + str(oct_4))
        res = connect(ip + '.' + str(oct_4), port_)
        if res:
            ip_list_open_port.append(ip + '.' + str(oct_4))
    return ip_list_open_port


def scan_network(file_name_, network_, port_):
    network_ = network_.split('.')
    mask = 0

    ip = ''
    for oct_ in network_:
        if oct_ == '0':
            mask += 1
        else:
            ip += '.' + oct_
    ip = ip[1:]

    if mask == 1:
        ip_list_open_port = brut_oct(ip, port_)
    elif mask == 2:
        for oct_3 in range(0, 256):
            ip_list_open_port = brut_oct(ip + '.' + str(oct_3), port_)

    pc_name_list = []

    file_name_ += '\\' + str((4 - mask) * 8) + ':' + str(port_)
    print(file_name_)
    pc_name_list.append(file_name_)

    for ip in ip_list_open_port:
        pc_name_list.append(str(socket.getfqdn(ip)).split('.')[0])

    with open('PC_name_open_port.txt', "a") as file:
        for name in pc_name_list:
            file.write(name + '\n')


with open(r'E:\GordeyGV$\WS\Python\files\networks.txt', 'r') as f:
    networks = f.read().splitlines()

with open(r'E:\GordeyGV$\WS\Python\files\ports.txt', 'r') as f:
    ports = f.read().splitlines()

ip_list_open_port = []

for port in ports:
    for network in networks:
        file_name = 'domen_names_' + network
        scan_network(file_name, network, int(port))
