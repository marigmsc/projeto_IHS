#!/usr/bin/python3

import os, sys
from fcntl import ioctl

# ioctl commands defined at the pci driver
RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

def main():
    if len(sys.argv) < 2:
        print("Error: expected more command line arguments")
        print("Syntax: %s </dev/device_file>"%sys.argv[0])
        exit(1)

    fd = os.open(sys.argv[1], os.O_RDWR)

    ioctl(fd, RD_PBUTTONS)
    red = os.read(fd, 4); # read 4 bytes and store in red var
    red_number = int.from_bytes(red, 'little')

    if red_number == 0x7:
        print("botao 1")
    elif red_number == 0xB:
        print("botao 2")
    elif red_number == 0xD:
        print("botao 3")
    elif red_number == 0xE:
        print("botao 4")

    os.close(fd)

if __name__ == '__main__':
    main()

