import pandas as pd
from datetime import datetime, timedelta
import random

# Define the number of records you want to generate
num_records = 10

# Define possible values for source and destination IPs, protocols, and ports
src_ips = ['192.168.1.1', '192.168.1.2', '10.0.0.1', '172.16.0.1', '192.168.1.3']
dst_ips = ['192.168.1.2', '192.168.1.3', '10.0.0.2', '172.16.0.2', '192.168.1.4']
protocols = ['TCP', 'UDP']
ports = [22, 80, 443, 8080, 3306]

# Initialize an empty list to hold the data
data = []

# Generate the data
start_time = datetime(2025, 1, 25, 10, 0)  # Start at 10:00 AM

for i in range(num_records):
    timestamp = start_time + timedelta(minutes=i)
    src_ip = random.choice(src_ips)
    dst_ip = random.choice(dst_ips)
    src_port = random.choice(ports)
    dst_port = random.choice(ports)
    protocol = random.choice(protocols)
    bytes_sent = random.randint(256, 4096)
    packet_length = random.randint(128, 2048)
    
    # Append a row of data to the list
    data.append([timestamp.strftime('%Y-%m-%d %H:%M:%S'), src_ip, dst_ip, src_port, dst_port, protocol, bytes_sent, packet_length])

# Create a DataFrame
df = pd.DataFrame(data, columns=['timestamp', 'src_ip', 'dst_ip', 'src_port', 'dst_port', 'protocol', 'bytes', 'packet_length'])

# Save the DataFrame to a CSV file
df.to_csv('packets.csv', index=False)

print("CSV file 'packets.csv' has been created.")



