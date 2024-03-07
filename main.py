import socket
import argparse
import threading
import matplotlib.pyplot as plt

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

def scan_port(host, port, open_ports, timeout=1):
    # Scan a port on the specified host to check if it's open.
    #
    # Args:
    #     host (str): The target host IP address.
    #     port (int): The port number to scan.
    #     open_ports (list): A list to store open ports found during scanning.
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
            open_ports.append((port, service))
            # print(f"Port {port} ({service}) is open")
        # Close the socket
        s.close()
    except socket.error:
        pass

def single_threaded_scan(host, ports, timeout=1):
    # Perform single-threaded port scanning.
    #
    # Args:
    #     host (str): The target host IP address.
    #     ports (list): List of ports to scan.
    #     timeout (int): Connection timeout in seconds (default is 1).
    #
    # Returns:
    #     list: A list of tuples containing open ports and their associated services.
    
    open_ports = []
    print(f"Scanning host {host}...")
    for port in ports:
        scan_port(host, port, open_ports, timeout)
    return open_ports
    

def multi_threaded_scan(host, ports, threads=5, timeout=1):
    # Perform multi-threaded port scanning.
    #
    # Args:
    #     host (str): The target host IP address.
    #     ports (list): List of ports to scan.
    #     threads (int): Number of threads to use for scanning (default is 5).
    #     timeout (int): Connection timeout in seconds (default is 1).
    #
    # Returns:
    #     list: A list of tuples containing open ports and their associated services.
    
    open_ports = []
    print(f"Scanning host {host} with {threads} threads...")
    for i in range(0, len(ports), threads):
        thread_list = []
        for port in ports[i:i+threads]:
            thread = threading.Thread(target=scan_port, args=(host, port, open_ports, timeout))
            thread_list.append(thread)
            thread.start()
        for thread in thread_list:
            thread.join()
    return open_ports

def visualize_open_ports(open_ports):
    # Visualize the distribution of open ports by service type.
    #
    # Args:
    #     open_ports (list): A list of tuples containing open ports and their associated services.
    
    service_counts = {}
    for _, service in open_ports:
        service_counts[service] = service_counts.get(service, 0) + 1

    plt.bar(service_counts.keys(), service_counts.values())
    plt.xlabel("Service")
    plt.ylabel("Number of Open Ports")
    plt.title("Distribution of Open Ports by Service Type")
    # Set y-axis ticks to integer values
    plt.yticks(range(max(service_counts.values()) + 1))
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="Target host IP address")
    parser.add_argument("-p", "--ports", help="Ports to scan (comma-separated)")
    parser.add_argument("-t", "--timeout", type=float, help="Connection timeout in seconds", default=1)
    parser.add_argument("-T", "--threads", type=int, help="Number of threads to use", default=5)
    args = parser.parse_args()

    # #parsing port range
    # #to run = python host -p (1-..)
    # start_port, end_port = map(int, args.ports.split("-") if "-" in args.ports else (args.ports, args.ports))
    # ports_to_scan = range(start_port, end_port + 1)

    # Parsing ports individually
    # To run: python host -p 1,2..
    ports_to_scan = []
    if args.ports:
        ports_to_scan = [int(port) for port in args.ports.split(",")]

    if args.threads == 1:
        open_ports = single_threaded_scan(args.host, ports_to_scan, args.timeout)
    else:
        open_ports = multi_threaded_scan(args.host, ports_to_scan, args.threads, args.timeout)
        
    
    visualize_open_ports(open_ports)
