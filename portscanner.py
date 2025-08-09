import socket
import time


# Zielhost festlegen
target = input("Host eingeben: ")
try:
    ip = socket.gethostbyname(target) # Wandelt Hostname in IP um
    print(f"Scanne {target} ({ip} ...)")
except socket.gaierror as e:
    print(f"[!] DNS-Auflösung fehlgeschlagen: {e}")
    exit()
# Abfrage Ports / festlegen
try:
    start_port = int(input("Startport eingeben: "))
    end_port = int(input("Endport: "))
except ValueError:
    print("Bitte nur Zahlen für Ports eingeben!")
    exit()
    
if start_port > end_port:
    start_port, end_port = end_port, start_port # Vertausche beide 
    
if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
    print("Ports müssen zwischen 1 und 65535 liegen!")
    exit()
        
try:
    # Startzeit messen
    start_time = time.time()

    open_ports = [] # Leere Liste mit offenen Ports

    for port in range(start_port, end_port + 1):
    # Socket erstellen
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)     # Timeout von 1 Sekunde
    # Verbindung versuchen
        try:     
            result = s.connect_ex((target, port))    
            if result == 0:     
                open_ports.append(port) # Fügt hier alle Offen- gescannten Ports der obigen Liste hinzu
                print(f"[+] Port {port} ist offen!")
            else: 
                print(f"[-] Port {port} ist geschlossen!")
        except Exception as e:     
            print(f"Fehler {e} ist aufgetreten!")      
        finally:    
            s.close     
except KeyboardInterrupt:
    print("\n [!] Scan manuell abgebrochen.")
         
# Endzeit messen
end_time = time.time()
# Dauer berechnen und ausgeben
scan_time = end_time - start_time
         
print(f"Offene Ports: {open_ports if open_ports else 'keine'}") # WENN in open_ports etwas enhalten, print(inhalt). Else print("keine").
print(f"Scan abgeschlossen in {scan_time:.2f} Sekunden.")




