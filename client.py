import logging
import time

from network import icmp_driver


def main() -> None:
    logging.info("Starting pyB1fr0st client")
    socket = icmp_driver.open_icmp_socket()
    logging.info("ICMP socket initialized")

    while True:
        icmp_driver.send_icmp_packet(socket, None)
        time.sleep(2)

if __name__ == '__main__':
    main()
