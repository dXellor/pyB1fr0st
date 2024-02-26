import socket
import struct
import sys

from network import icmp_packet
from util.exit_codes import EXIT_CODES

def open_icmp_socket() -> socket.socket:
    try:
        icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        return icmp_socket
    except socket.error as e:
        print(f"Error while initializing ICMP socket: {e}")
        sys.exit(EXIT_CODES['CANT_OPEN_SOCKET'])

def send_icmp_packet(socket: socket.socket, payload: str) -> None:
    packet = icmp_packet.ICMPPacket('0.0.0.0', '192.168.0.1')
    socket.sendto(struct.pack('BBhhh7s', packet.type, packet.code, packet.checksum, 0, 0, b"test"), ('192.168.0.1', 7130))   