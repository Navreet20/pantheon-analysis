import csv
import matplotlib.pyplot as plt

def read_metrics_from_csv(csv_file_path):
    # Initialize empty lists for time, throughput, RTT, and loss
    time = []
    throughput = []
    rtt = []
    loss = []

    # Open the CSV file and read the data
    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)

        for row in csvreader:
            # Handle missing values by checking if RTT or Loss is empty
            if row['RTT'] == '' or row['Loss'] == '':
                # You can handle missing data by skipping the row, or using a default value like 0 or NaN
                continue  # Skip rows with missing RTT or Loss values
            else:
                # Append the valid data
                time.append(int(row['Time']))
                throughput.append(int(row['Throughput']))
                rtt.append(float(row['RTT']))
                loss.append(float(row['Loss']))

    return time, throughput, rtt, loss

def plot_throughput_over_time(time, throughput):
    plt.figure(figsize=(10, 6))
    plt.plot(time, throughput, color='blue', label='Throughput')
    plt.xlabel('Time (s)')
    plt.ylabel('Throughput (bps)')
    plt.title('Throughput Over Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('throughput_over_time.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Throughput over time plot saved as 'throughput_over_time.png'")

def plot_loss_rate_over_time(time, loss):
    plt.figure(figsize=(10, 6))
    plt.plot(time, loss, color='red', label='Loss Rate')
    plt.xlabel('Time (s)')
    plt.ylabel('Loss Rate')
    plt.title('Loss Rate Over Time')
    plt.grid(True)
    plt.legend()
    plt.savefig('loss_rate_over_time.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Loss rate over time plot saved as 'loss_rate_over_time.png'")

def calculate_rtt_statistics(rtt_data):
    avg_rtt = sum(rtt_data) / len(rtt_data) if rtt_data else 0
    p95_rtt = np.percentile(rtt_data, 95) if rtt_data else 0
    return avg_rtt, p95_rtt

def plot_rtt_vs_throughput(rtt, throughput):
    plt.figure(figsize=(10, 6))
    plt.scatter(rtt, throughput, color='green', label='RTT vs Throughput')
    plt.xlabel('RTT (ms)')
    plt.ylabel('Throughput (bps)')
    plt.title('RTT vs Throughput for Various Protocols')
    plt.grid(True)
    plt.legend()
    plt.savefig('rtt_vs_throughput.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("RTT vs Throughput plot saved as 'rtt_vs_throughput.png'")

def main():
    # Path to your CSV log file (replace with the actual file path)
    log_file_path = '/home/navreet/Desktop/pantheon/src/analysis/metrics.csv'
    
    # Step 1: Read the CSV data
    time, throughput, rtt, loss = read_metrics_from_csv(log_file_path)
    
    # Step 2: Plot the throughput over time
    plot_throughput_over_time(time, throughput)
    
    # Step 3: Plot the loss rate over time
    plot_loss_rate_over_time(time, loss)
    
    # Step 4: Calculate RTT statistics (average and 95th percentile)
    avg_rtt, p95_rtt = calculate_rtt_statistics(rtt)
    print(f"Average RTT: {avg_rtt} ms")
    print(f"95th Percentile RTT: {p95_rtt} ms")
    
    # Step 5: Plot RTT vs Throughput for comparison
    plot_rtt_vs_throughput(rtt, throughput)

if __name__ == '__main__':
    main()
