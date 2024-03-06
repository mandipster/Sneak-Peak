import socket
import argparse

#function to check if port on host is open or closed 
def scan_port(host, port, timeout=2):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        s.settimeout(timeout)
        # Attempt to connect to the host and port
        result = s.connect_ex((host, port))
        # Check if the port is open
        if result == 0:
            print(f"Port {port} is open")
        # Close the socket
        s.close()
    except socket.error:
        pass

#function that uses scan_port() to scan multiple ports
def single_threaded_scan(host, ports, timeout=1):
    print(f"Scanning host {host}...")
    for port in ports:
        scan_port(host, port, timeout)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Simple port scanner")
#     parser.add_argument("host", help="Target host IP address")
#     parser.add_argument("-p", "--ports", help="Ports to scan (comma-separated)", default="1-1024")
#     parser.add_argument("-t", "--timeout", type=float, help="Connection timeout in seconds", default=1)
#     args = parser.parse_args()

#     # Parse port range
#     start_port, end_port = map(int, args.ports.split("-") if "-" in args.ports else (args.ports, args.ports))
#     ports_to_scan = range(start_port, end_port + 1)

#     single_threaded_scan(args.host, ports_to_scan, args.timeout)