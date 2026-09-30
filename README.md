# Network Port Scanner

A beginner-friendly Python cybersecurity project that checks TCP ports on a host and reports which ports are open.

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

## How It Works

```text
Enter Host/IP
      |
      v
Select Port Range
      |
      v
Create TCP Socket
      |
      v
Try Connection
      |
   +--+--+
   |     |
Success Failure
   |     |
 OPEN  CLOSED
   |
   v
Display Results
```

## Resume Description

**Network Port Scanner | Python**

Developed a Python-based network port scanner to identify open TCP ports on a specified host. Implemented socket programming and connection handling to test ports and determine their availability. Added configurable port ranges and exception handling to perform basic network reconnaissance in a controlled environment.

**Technologies:** Python, Socket Programming, TCP/IP, Exception Handling

## Interview Explanation

"I developed a Network Port Scanner using Python's socket library. The user provides a host and port range. The program attempts to establish a TCP connection with each port. If the connection succeeds, the port is reported as open. This project helped me understand TCP connections, socket programming, and basic network reconnaissance."

## Safety

Use this project only on systems you own or have explicit permission to test. For learning, `127.0.0.1` is a safe local target.
