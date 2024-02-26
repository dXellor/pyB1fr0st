class ICMPPacket():

    def __init__(self, source_address: str, destination_address: str):
        self.source_address = source_address
        self.destination_address = destination_address
        self.type = 8
        self.code = 0
        self.checksum = 0
        self.payload = 'Ide gas'

    def __str__(self):
        pass

    def calculate_checksum(self):
        pass