import serial
import argparse

MACRO_CMD = " W 0x12C04 "
CR = 0x0D

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--macro", "-m", help="macro number to call")
parser.add_argument("--port", "-p", help="serial port")
parser.add_argument("--node", "-n", help="target node to connect with")

# read arguments from the command line
args = parser.parse_args()

macro = 20
node = 32
port = 'COM4'

if args.macro:
    macro = int(args.macro)
if args.node:
    node = int(args.node)
if args.port:
    port = args.port


def create_ascii_cmd(macro_number=10, node_number=32):
    data = str(node_number) + MACRO_CMD + str(macro_number)
    asciified = [ord(x) for x in data]
    asciified.append(CR)
    return bytearray(asciified)

# print(bin(b)[2:].zfill(8))
# for b in asciified:

ser = serial.Serial()
ser.baudrate = 115200
ser.port = port
ser.open()

buffer = create_ascii_cmd(macro, node)
print(buffer)

ser.write(buffer)

ser.close()