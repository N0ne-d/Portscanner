# Python Port Scanner

Ein einfacher Portscanner in Python, der überprüft, welche Ports bei einem Zielhost offen sind.

## Features
- Eingabe von Hostname oder IP
- Angabe von Start- und Endport
- Anzeige aller offenen Ports
- Messung der Scan-Dauer

## Nutzung
```bash
python3 portscanner.py
```
Dann einfach Host und Ports eingeben.

## Beispiel
```bash
Host eingeben: scanme.nmap.org
Startport eingeben: 1
Endport: 100
```
Ausgabe:
```
[+] Port 22 ist offen!
[+] Port 80 ist offen!
Offene Ports: [22, 80]
Scan abgeschlossen in 0.32 Sekunden.
```

## Anforderungen
- Python 3
- Keine zusätzlichen Bibliotheken erforderlich
