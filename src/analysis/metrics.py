import re
import csv

def extract_data_from_log(log_file_path):
    throughput_data = []
    rtt_data = []
    loss_data = []

    packet_size = 1504  # Bytes per packet
    time_interval = 1  # Time in seconds (assuming 1-second intervals for simplicity)

    with open(log_file_path, 'r') as file:
        for line in file:
            # Extract Throughput (assuming packet size is 1504)
            if "1504" in line:  
                throughput = packet_size * 8  # Convert bytes to bits (throughput)
                throughput_data.append(throughput)  # Store throughput

            # Extract RTT
            match_rtt = re.search(r"RTT: (\d+)", line)  # Modify based on your log format
            if match_rtt:
                rtt = int(match_rtt.group(1))  # RTT in milliseconds
                rtt_data.append(rtt)  # Store RTT

            # Extract Loss (Modify based on your log format)
            match_loss = re.search(r"loss: (\d+)", line)  # Modify this based on loss format
            if match_loss:
                loss = int(match_loss.group(1))  # Loss rate as percentage or count
                loss_data.append(loss)  # Store loss

    # Optionally, save the extracted data to CSV
    with open('metrics.csv', 'w', newline='') as csvfile:
        fieldnames = ['Time', 'Throughput', 'RTT', 'Loss']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Write each entry as a row in the CSV
        for i in range(len(throughput_data)):
            writer.writerow({'Time': i+1, 'Throughput': throughput_data[i], 'RTT': rtt_data[i] if i < len(rtt_data) else '', 'Loss': loss_data[i] if i < len(loss_data) else ''})

    print("Metrics extracted and saved to 'metrics.csv'")

if __name__ == "__main__":
    log_file_path = '/home/navreet/Desktop/pantheon/output_1mbps/cubic_mm_acklink_run1.log'  
    extract_data_from_log(log_file_path)
