from random import randint
import pdb

def clock():
    x = 0
    while True:
        yield x
        x += 1

def processor():
    last_packet = 0
    while True:
        x = yield
        yield last_packet * 0.5
        last_packet = x

def algorithm():
    p = processor()
    last_packet = 0
    for i in clock():
        packet = randint(0, 10)
        if packet == 0:
            exit("Exiting")
        next(p)
        response = p.send(packet)
        try:
            assert response * 2 == last_packet
        except Exception as e:
            print("AssetionError")
        print("Tick: %s, Random number: %s, Packet: %s, Response: %s, Loop count: %s" % (
            i, packet, last_packet, response, i
        ))
        last_packet = packet

if __name__ == '__main__':
    algorithm()

