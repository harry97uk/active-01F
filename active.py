import argparse
import subprocess
import re

def nmap_scan(host, port_range, scan_type):
    command = ['nmap']

    if scan_type == 'tcp':
        command.extend(['-p', port_range])
    elif scan_type == 'udp':
        command.extend(['-sU', '-p', port_range])

    command.append(host)
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def parse_nmap_output(nmap_output):
    lines = nmap_output.split('\n')
    result = ""

    for line in lines:
        if re.match(r'\d+\/tcp.*\s+(open|filtered|closed)\s+\w+', line):
            parts = line.split()
            port_number = parts[0].split('/')[0]
            port_state = parts[1]
            result += (f"Port {port_number} is {port_state}\n")

    return result.removesuffix("\n")


def main():
    parser = argparse.ArgumentParser(description='Simple port scanner using Nmap')
    parser.add_argument('host', type=str, help='Target host')
    parser.add_argument('-p', '--port', type=str, required=True, help='Port or range of ports to scan (e.g., 80 or 80-100)')
    parser.add_argument('-u', '--udp', action='store_true', help='Perform UDP scan')
    parser.add_argument('-t', '--tcp', action='store_true', help='Perform TCP scan')
    
    args = parser.parse_args()

    if not args.tcp and not args.udp:
        print("Please specify either TCP or UDP scan with -t or -u.")
        return

    scan_type = 'tcp' if args.tcp else 'udp'

    result = nmap_scan(args.host, args.port, scan_type)

    print(result)
    print(parse_nmap_output(result))

if __name__ == "__main__":
    main()
