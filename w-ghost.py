#!/usr/bin/env python3
"""
W-GHOST - Professional Vulnerability Scanning Tool
Developed by Emad Zawawid
For Educational and Research Purposes Only
"""

import nmap
import argparse
import json
import sys
import time
import threading
import os
from datetime import datetime
from colorama import init, Fore, Style, Back
from tabulate import tabulate
import socket

# Initialize colorama
init(autoreset=True)

class WGhostScanner:
    def __init__(self):
        self.target = None
        self.scan_results = []
        self.vuln_results = []
        self.os_info = None
        self.progress = 0
        self.scanning = False
        
    def display_logo(self):
        """Display the W-GHOST ASCII logo"""
        logo = f"""
{Fore.GREEN}{Style.BRIGHT}
██╗    ██╗       ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
██║    ██║      ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
██║ █╗ ██║█████╗██║  ███╗███████║██║   ██║███████╗   ██║   
██║███╗██║╚════╝██║   ██║██╔══██║██║   ██║╚════██║   ██║   
╚███╔███╔╝      ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
 ╚══╝╚══╝        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   
{Fore.RED}{Style.BRIGHT}
              ╔══════════════════════════════════════════╗
              ║       PROFESSIONAL VULNERABILITY          ║
              ║            SCANNING TOOL                  ║
              ╚══════════════════════════════════════════╝
{Fore.YELLOW}{Style.BRIGHT}
                   Developed by Emad Zawawid
{Fore.CYAN}
        [ TERMUX EDITION | CYBERSECURITY RESEARCH ]
{Style.RESET_ALL}
"""
        print(logo)
        print(f"{Fore.RED}=" * 60)
        print(f"{Fore.GREEN}[*] Starting W-GHOST Security Scanner...")
        print(f"{Fore.GREEN}[*] Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Fore.RED}=" * 60 + "\n")

    def validate_target(self, target):
        """Validate the target IP address or hostname"""
        try:
            # Check if it's a valid IP address
            socket.inet_aton(target)
            return True
        except socket.error:
            try:
                # Check if it's a valid hostname
                socket.gethostbyname(target)
                return True
            except socket.gaierror:
                return False

    def progress_indicator(self):
        """Show scanning progress"""
        animation = "|/-\\"
        idx = 0
        while self.scanning:
            progress_bar = "█" * (self.progress // 5) + "░" * (20 - self.progress // 5)
            sys.stdout.write(f"\r{Fore.CYAN}[{progress_bar}] {self.progress}% {animation[idx % len(animation)]}")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.1)
        sys.stdout.write("\r" + " " * 50 + "\r")
        sys.stdout.flush()

    def scan_ports(self, target):
        """Perform port scanning"""
        try:
            self.progress = 20
            nm = nmap.PortScanner()
            
            print(f"{Fore.YELLOW}[+] Scanning ports on {target}...")
            nm.scan(target, arguments='-sS -sV -T4 --top-ports 1000')
            
            self.progress = 40
            
            for host in nm.all_hosts():
                host_info = {
                    'host': host,
                    'hostname': nm[host].hostname(),
                    'state': nm[host].state(),
                    'protocols': []
                }
                
                for proto in nm[host].all_protocols():
                    ports = nm[host][proto].keys()
                    for port in ports:
                        port_info = nm[host][proto][port]
                        host_info['protocols'].append({
                            'port': port,
                            'protocol': proto,
                            'state': port_info['state'],
                            'service': port_info['name'],
                            'version': port_info['version']
                        })
                
                self.scan_results.append(host_info)
            
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Port scanning error: {e}")
            return False

    def os_fingerprint(self, target):
        """Perform OS fingerprinting"""
        try:
            self.progress = 60
            nm = nmap.PortScanner()
            
            print(f"{Fore.YELLOW}[+] Performing OS fingerprinting...")
            nm.scan(target, arguments='-O --osscan-guess')
            
            self.progress = 70
            
            if 'osmatch' in nm[target]:
                self.os_info = nm[target]['osmatch']
            
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] OS fingerprinting error: {e}")
            return False

    def vulnerability_scan(self, target):
        """Scan for vulnerabilities using NSE scripts"""
        try:
            self.progress = 80
            nm = nmap.PortScanner()
            
            print(f"{Fore.YELLOW}[+] Running vulnerability assessment...")
            nm.scan(target, arguments='--script vuln,vulners -sV')
            
            self.progress = 90
            
            for host in nm.all_hosts():
                if 'script' in nm[host]:
                    for script_name, script_output in nm[host]['script'].items():
                        self.vuln_results.append({
                            'script': script_name,
                            'output': script_output
                        })
            
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Vulnerability scanning error: {e}")
            return False

    def display_results(self):
        """Display scan results in structured format"""
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"{Fore.CYAN}{Style.BRIGHT}[ SCAN RESULTS ]")
        print(f"{Fore.GREEN}{'='*60}\n")
        
        # Display host information
        for host in self.scan_results:
            print(f"{Fore.YELLOW}[+] Target: {host['host']}")
            print(f"{Fore.YELLOW}[+] Hostname: {host['hostname']}")
            print(f"{Fore.YELLOW}[+] State: {host['state']}")
            
            # Display open ports
            if host['protocols']:
                print(f"\n{Fore.CYAN}[ Open Ports and Services ]")
                table_data = []
                for service in host['protocols']:
                    table_data.append([
                        service['port'],
                        service['protocol'].upper(),
                        service['state'],
                        service['service'],
                        service['version'] if service['version'] else 'Unknown'
                    ])
                
                headers = ['Port', 'Protocol', 'State', 'Service', 'Version']
                print(tabulate(table_data, headers=headers, tablefmt='grid'))
        
        # Display OS information
        if self.os_info:
            print(f"\n{Fore.CYAN}[ Operating System Detection ]")
            os_table = []
            for os in self.os_info[:3]:  # Show top 3 matches
                os_table.append([os['name'], f"{os['accuracy']}%"])
            
            print(tabulate(os_table, headers=['OS Match', 'Accuracy'], tablefmt='grid'))
        
        # Display vulnerabilities
        if self.vuln_results:
            print(f"\n{Fore.RED}{Style.BRIGHT}[ Vulnerability Assessment ]")
            for vuln in self.vuln_results:
                print(f"\n{Fore.YELLOW}Script: {vuln['script']}")
                print(f"{Fore.WHITE}{vuln['output'][:500]}")  # Limit output length
                if len(vuln['output']) > 500:
                    print(f"{Fore.RED}[... Output truncated ...]")
        else:
            print(f"\n{Fore.GREEN}[+] No critical vulnerabilities detected")

    def save_report(self, filename, format_type='txt'):
        """Save scan report to file"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'target': self.target,
            'scan_results': self.scan_results,
            'os_info': self.os_info,
            'vulnerabilities': self.vuln_results
        }
        
        if format_type == 'json':
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
        else:
            with open(filename, 'w') as f:
                f.write(f"W-GHOST Security Scan Report\n")
                f.write(f"Generated: {report['timestamp']}\n")
                f.write(f"Target: {report['target']}\n")
                f.write("="*60 + "\n\n")
                
                for host in report['scan_results']:
                    f.write(f"Host: {host['host']} ({host['hostname']})\n")
                    f.write(f"State: {host['state']}\n\n")
                    
                    for service in host['protocols']:
                        f.write(f"Port {service['port']}/{service['protocol']}: {service['service']} {service['version']}\n")
                    
                if report['os_info']:
                    f.write("\nOS Detection:\n")
                    for os in report['os_info'][:3]:
                        f.write(f"- {os['name']} (Accuracy: {os['accuracy']}%)\n")
                
                if report['vulnerabilities']:
                    f.write("\nVulnerabilities Found:\n")
                    for vuln in report['vulnerabilities']:
                        f.write(f"\n{vuln['script']}:\n{vuln['output']}\n")

    def scan(self, target, save_report=False, report_format='txt'):
        """Main scan function"""
        self.target = target
        
        # Validate target
        if not self.validate_target(target):
            print(f"{Fore.RED}[!] Invalid target: {target}")
            return
        
        # Start progress indicator
        self.scanning = True
        progress_thread = threading.Thread(target=self.progress_indicator)
        progress_thread.daemon = True
        progress_thread.start()
        
        try:
            # Perform scans
            if not self.scan_ports(target):
                return
            
            self.os_fingerprint(target)
            self.vulnerability_scan(target)
            
            self.progress = 100
            time.sleep(0.5)
            
        finally:
            self.scanning = False
            progress_thread.join(timeout=1)
        
        # Display results
        self.display_results()
        
        # Save report if requested
        if save_report:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"wghost_report_{timestamp}.{report_format}"
            self.save_report(filename, report_format)
            print(f"\n{Fore.GREEN}[+] Report saved to: {filename}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='W-GHOST - Professional Vulnerability Scanning Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python w-ghost.py -t 192.168.1.1
  python w-ghost.py -t example.com -o report
  python w-ghost.py -t 10.0.0.1 -o scan_results -f json
        '''
    )
    
    parser.add_argument('-t', '--target', 
                        required=True,
                        help='Target IP address or hostname')
    
    parser.add_argument('-o', '--output',
                        help='Save report to file (without extension)')
    
    parser.add_argument('-f', '--format',
                        choices=['txt', 'json'],
                        default='txt',
                        help='Report format (default: txt)')
    
    args = parser.parse_args()
    
    # Create scanner instance
    scanner = WGhostScanner()
    
    # Display logo
    scanner.display_logo()
    
    # Check if running with root (helpful for some scan types)
    if os.geteuid() != 0:
        print(f"{Fore.YELLOW}[!] Warning: Running without root privileges.")
        print(f"{Fore.YELLOW}[!] Some advanced features may be limited.")
        print(f"{Fore.YELLOW}[!] Consider using 'tsu' or 'sudo' for full functionality.\n")
    
    # Start scan
    scanner.scan(
        target=args.target,
        save_report=args.output is not None,
        report_format=args.format
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}[!] Unexpected error: {e}")
        sys.exit(1)

