from scapy.all import sniff
import csv
import time

# Function to capture packets and save to CSV
def capture_packets(output_file="packets.csv"):
    # Define packet processing function
    def process_packet(packet):
        if packet.haslayer('IP'):
            packet_data = {
                "timestamp": time.time(),
                "src_ip": packet['IP'].src,
                "dst_ip": packet['IP'].dst,
                "protocol": packet['IP'].proto,
                "packet_length": len(packet)
            }
            # Append packet data to CSV
            with open(output_file, mode='a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=packet_data.keys())
                writer.writerow(packet_data)
            print(f"Captured packet: {packet_data}")

    # Sniff packets in real-time
    sniff(prn=process_packet, store=0)

# Run the packet capture function
capture_packets()
