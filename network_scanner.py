import nmap as nmap

def scan_network(target):
    nm = nmap.PortScanner()

    print("\nScanning network...")

    nm.scan(target, '1-1024', arguments='-sV')

    open_ports = []
    vulnerabilities = []

    for host in nm.all_hosts():

        for proto in nm[host].all_protocols():

            ports = nm[host][proto].keys()

            for port in ports:

                service = nm[host][proto][port]['name']

                version = nm[host][proto][port].get(
                    'version',
                    'Unknown'
                )

                open_ports.append(
                    {
                        "port": port,
                        "service": service,
                        "version": version
                    }
                )

                if port == 21:
                    vulnerabilities.append(
                        "FTP detected (unencrypted protocol)"
                    )

                if port == 23:
                    vulnerabilities.append(
                        "Telnet detected (insecure remote access)"
                    )

                if port == 445:
                    vulnerabilities.append(
                        "SMB exposed"
                    )

    return open_ports, vulnerabilities