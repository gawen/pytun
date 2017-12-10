import pytun
import logging
import select

def pprint_buf(buf):
    """ Dirty & convenient function to display the hexademical
        repr. of a buffer.
    """

    DEFAULT_SIZE = 4

    def hex2(i, l = None):
        l = l if l is not None else DEFAULT_SIZE

        h = hex(i).upper()[2:]
        
        if len(h) != l:
            h = "0" * (l - len(h)) + h
        
        return h

    def displayable_char(c):
        if ord(c) < 0x20:
            c = "."

        return c

    print " " * DEFAULT_SIZE,
    for i in range(16): print hex2(i, 2),
    print

    raws = []
    for i, c in enumerate(buf):
        if i % 16 == 0:
            if i:
                print "\t" + "".join(raws)
                raws = []

            print hex2(i),
        raws.append(displayable_char(c))
        
        print hex2(ord(c), 2),

    print "   " * (15 - (i % 16)) + "\t" + "".join(raws)

def main():
    # Configure pytun's logger
    pytun.logger.setLevel(logging.DEBUG)
    logging.basicConfig()

    # Open the tunnel
    try:
        tun = pytun.open()

    except pytun.Tunnel.NotPermitted:
        print
        print "*" * 80
        print "You do have the rights to access the file %s." % (pytun.TUN_KO_PATH, )
        print "Give the access of this file to pytun, or if you trust me,"
        print "elevate this current script to root level."
        print "*" * 80
        print

        raise

    print "*" * 80
    print
    print "OK. The tunnel '%s' had been created." % (tun.name, )
    print
    print "If you want to play with it, first configure it."
    print
    print "1. Set up the network and set an IP"
    print "    $ ifconfig %s 192.168.42.1" % (tun.name, )
    print
    print "2. Add the network route"
    print "    $ route add -net 192.168.42.0/24 dev %s" % (tun.name, )
    print
    print "Then, try to ping some IP in this network ..."
    print "    $ ping 192.168.42.42"
    print
    print "Or do some UDP netcat magic."
    print "    $ nc 192.168.42.42 4242 -u"
    print
    print "Enjoy !"
    print
    print "*" * 80

    try:
        # Receive loop
        while True:
            buf = tun.recv()

            pytun.logger.info("Packet received !")
            pprint_buf(buf)
            print

    except KeyboardInterrupt:
        print "Keyboard interrupt. Closing."
    
    finally:
        # Close the tunnel
        tun.close()


if __name__ == "__main__":
    main()

