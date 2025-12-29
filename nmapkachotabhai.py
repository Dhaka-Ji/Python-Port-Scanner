import socket
import sys
from datetime import datetime

print("-" * 50)
print("Nmap Ka Chota Bhai...")
print("-" * 50)

target = input(" Enter Your Target : ")

try:
    target_ip = socket.gethostbyname(target)
    print(f"\n [+] Scannint Target : {target_ip} : thoda sabar kre jnab")
    print(f"[+] Scan start ho chuka hai : {str(datetime.now())}")
    print("-" * 50)

    for port in range(20,85):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} : OPEN !!! Darwaja khula hai jnab aaye")
        
        s.close()

except socket.gaierror:
    print("\n[!] Dhyan ki jrurt hai bhai tmhare ko ... port band hai susra")
except socket.error:
    print("\n[!!!] Bhai ke address diya hai sala connect hi na ho rha")
except KeyboardInterrupt:
    print("\n[!!!!] M bhai bnd hou apne aap tu jan tera kam jan .. hr kimi deta rhh")
    sys.exit()

print("-" * 50)
print("Sir m FOd Tera Scan, Khud ja kr, krle check agr gni dikkt hai to")