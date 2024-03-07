import socket
import argparse
import threading

# Dictionary mapping port numbers to service names
SERVICE_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
    # We can add more services if needed
}

def scan_port(host, port, timeout=1):

    # Function to check if a port on the host is open or closed.
    
    # Args:
    #     host (str): The target host IP address.
    #     port (int): The port number to scan.
    #     timeout (int): Connection timeout in seconds (default is 1).
    
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        s.settimeout(timeout)
        # Attempt to connect to the host and port
        result = s.connect_ex((host, port))
        # Check if the port is open
        if result == 0:
            service = SERVICE_PORTS.get(port, "Unknown")
            print(f"Port {port} ({service}) is open")
        # Close the socket
        s.close()
    except socket.error:
        pass

def single_threaded_scan(host, ports, timeout=1):

    # Function to perform single-threaded port scanning.
    
    # Args:
    #     host (str): The target host IP address.
    #     ports (list): List of ports to scan.
    #     timeout (int): Connection timeout in seconds (default is 1).

    print(f"Scanning host {host}...")
    for port in ports:
        scan_port(host, port, timeout)

def multi_threaded_scan(host, ports, threads=5, timeout=1):

    # Function to perform multi-threaded port scanning.
    
    # Args:
    #     host (str): The target host IP address.
    #     ports (list): List of ports to scan.
    #     threads (int): Number of threads to use for scanning (default is 5).
    #     timeout (int): Connection timeout in seconds (default is 1).

    print(f"Scanning host {host} with {threads} threads...")
    for i in range(0, len(ports), threads):
        thread_list = []
        for port in ports[i:i+threads]:
            thread = threading.Thread(target=scan_port, args=(host, port, timeout))
            thread_list.append(thread)
            thread.start()
        for thread in thread_list:
            thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="Target host IP address")
    parser.add_argument("-p", "--ports", help="Ports to scan (comma-separated)", default="1-1024")
    parser.add_argument("-t", "--timeout", type=float, help="Connection timeout in seconds", default=1)
    parser.add_argument("-T", "--threads", type=int, help="Number of threads to use", default=5)
    args = parser.parse_args()

    # #parsing port range
    # #to run = python host -p (1-..)
    # start_port, end_port = map(int, args.ports.split("-") if "-" in args.ports else (args.ports, args.ports))
    # ports_to_scan = range(start_port, end_port + 1)
    
    #parsing ports individually
    #to run = python host -p 1,2..
    ports_to_scan = []
    if args.ports:
        ports_to_scan = [int(port) for port in args.ports.split(",")]

    if args.threads == 1:
        single_threaded_scan(args.host, ports_to_scan, args.timeout)
    else:
        multi_threaded_scan(args.host, ports_to_scan, args.threads, args.timeout)
