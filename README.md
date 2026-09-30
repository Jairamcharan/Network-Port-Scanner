# Network Port Scanner
checks TCP ports on a host and reports which ports are open.

## Features

- Accepts a hostname or IP address
- Allows the user to choose a port range
- Uses TCP socket connections
- Detects open ports
- Handles invalid input and connection errors
- Displays a simple scan summary

## Technologies

Python 3, Socket Programming, TCP/IP, Exception Handling

## How to Run

```bash
python port_scanner.py
```

Example:

```text
Enter host or IP address: 127.0.0.1
Enter starting port: 1
Enter ending port: 100

Scanning 127.0.0.1 from port 1 to 100...

Port 22: OPEN
Port 80: OPEN

Scan completed.
Open ports: 22, 80
```





