import socket

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((host, port))
        return result == 0
    except socket.gaierror:
        return None
    finally:
        sock.close()


host = input("Enter host or IP address: ").strip()

try:
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range.")
        raise SystemExit

    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        status = scan_port(host, port)

        if status is None:
            print("Host could not be resolved.")
            break

        if status:
            open_ports.append(port)
            print(f"Port {port}: OPEN")

    print("\nScan completed.")

    if open_ports:
        print("Open ports:", ", ".join(map(str, open_ports)))
    else:
        print("No open ports found in the selected range.")

except ValueError:
    print("Please enter valid numbers for the port range.")
