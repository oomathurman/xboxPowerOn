import sys, getopt, socket, select, time, codecs, binascii

xbox_port = 5050
xbox_ping = "dd00000a000000000000000400000002"
xbox_power = "dd02001300000010"

py3 = sys.version_info[0] > 2

def main(argv):
    ip_addr = ""
    live_id = ""
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setblocking(0)
    s.bind(("", 0))
    s.connect((ip_addr, xbox_port))

    if isinstance(live_id, str):
        live_id = live_id.encode()

    if py3:
        WoL = bytes.fromhex(xbox_power)
        WoL = WoL + live_id + b'\x00'
    else:
        WoL = xbox_power + live_id.encode("hex") + "00"
        WoL = WoL.decode("hex")

    print "Sending power on packets to " + ip_addr
    for i in range(1, 16):
        s.send(WoL)
        time.sleep(.5)
        print "Sending Packet:",i
    print("+-------------------------------------+")
    print("|    Xbox One Should Now Be Online!   |")
    print("+-------------------------------------+")

    s.close()

if __name__ == "__main__":
    main(sys.argv[1:])