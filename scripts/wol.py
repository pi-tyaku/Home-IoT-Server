import socket
import struct
from traceback import print_exc    
def wake_on_lan(mac):
    DEFAULT_PORT=7
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
        mac=mac.upper().replace("-","").replace(":","")     #":"や"-"を消去して大文字にする

        if len(mac) != 12:
            raise Exception("invalid MACaddres format")
        
        addr=b"f" * 12 + (mac * 20).encode()
        magicp= b''
        
        for i in range(0,len(addr),2):
            magicp += struct.pack('B',int(addr[i:i + 2] , 16))
        print(f"sending magic packet for:{format(mac)}")
        s.sendto(magicp,('<broadcast>',DEFAULT_PORT))

if __name__ == "__main__":
    try:
        mac_addr="D8:43:AE:1D:94:32"
        wake_on_lan(mac_addr)

    except BaseException:
        print_exc()