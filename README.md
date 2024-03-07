Sneak Peak: Python Port Scanner

Description:

Sneak Peak is a customizable Python-based port scanning tool designed to assess network security by identifying open ports on remote hosts. The tool utilizes socket programming and multi-threading to enhance scanning speed and efficiency. It supports user-defined scan parameters, including port range specification and timeout settings, providing flexibility in diverse network environments.


Key Features:

1. Single-threaded and multi-threaded scanning modes for sequential and concurrent port exploration.

2. Customizable scan options, including port range specification and timeout period configuration.

3. Service identification functionality to determine the type of service running on open ports, enhancing network visibility.

4. Network visualization capabilities for graphical representation of scanned hosts, open ports, and detected services.

5. Cross-platform compatibility across Windows, Linux, and macOS environments.
Usage:


To use the port scanner, execute the main.py script with the following command-line arguments:

python main.py <host> -p <ports>

Replace <host> with the target host IP address and <ports> with the comma-separated list of ports to scan. For example (Output for Windows.png):

python main.py google.com -p 80,443

Note: Be cautious when scanning external hosts, as scanning all ports without permission may be illegal. In our testing, we only scanned a limited number of ports for demonstration purposes.

Testing on Kali Linux (Output for Kali Linux VM.png):

We tested the port scanner on Kali Linux using Oracle VM VirtualBox with shared folders. However, we encountered an issue with scanning port 443 for Google, despite confirming its accessibility through other methods (e.g., HTTPS, DNS, curl). Further troubleshooting is required to resolve this issue.

Testing on macOS:

We were unable to test the port scanner on macOS due to not having access to a Mac product and the inability to download a macOS VM. However, the tool is designed to be cross-platform compatible, and we are confident that it would work on macOS systems with the appropriate setup.