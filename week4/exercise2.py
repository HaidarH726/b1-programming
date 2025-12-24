# List of devices IP addresses and their ports
devices = [  ("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23,
80, 3389]) ]


risky_ports = [21, 23, 3389]

print("Scanning network devices...")

risk_count=0

for device in devices:
    ip_address = device[0]
    port = device[1]

    for port in port:
        if port in risky_ports:
            risk_count+=1
            print(f"WARNING {ip_address} has a risky port {port}")





print(f" complete {risk_count} risky devices.")

            



