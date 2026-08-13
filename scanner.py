import socket
from datetime import datetime 
import ipaddress

services = {
    22: "SSH - Remote administration",
    25: "SMTP - Email",
    53: "DNS - Domain name service",
    80: "HTTP - Web traffic",
    443: "HTTPS - Secure web traffic",
    3306: "MySQL - Database"
}

target = input("Enter target IP: ")

try: 
    ipaddress.ip_address(target)
except ValueError:
    print("Invalid IP address.")
    exit()
try:
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
except ValueError:
    print("please enter valid port numbers.")
    exit()
if start_port > end_port :
    print("Start port cannot be greater than end port.")
    exit()

start_time = datetime.now()
formatted_start = start_time.strftime("%d-%m-%Y %H:%M:%S")
file = open("scan_results.txt", "w")

file.write("CYBERSECURITY PORT SCAN REPORT\n")
file.write("==============================\n")
file.write(f"Target: {target}\n")
file.write(f"Port Range: {start_port}-{end_port}\n\n")
file.write(f"Scanstarted:{formatted_start}\n\n")

print("\nScanning:", target)
print("Ports:", start_port, "to", end_port)
print("-" * 30)

open_ports = 0
for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))
    try:
      result = sock.connect_ex((target, port))
    except socket.error:
     print("Connection error occurred.")
     sock.close()
     exit()

    if result == 0:
        open_ports += 1

        try:
         service = socket.getservbyport(port)
        except OSError:
            service = "Unknown service"

        print(f"Port {port}: OPEN")
        print(f"Service: {service}")

        file.write(f"Port {port}: OPEN\n")
        file.write(f"Service: {service}\n\n")

    sock.close()
end_time = datetime.now()
duration = end_time - start_time
file.write(f"open ports found: {open_ports}\n")
file.write(f"Scan duration: {duration.total_seconds():.2f} seconds\n")

file.close()

print("\nScan completed.")
print("Report saved as scan_results.txt")