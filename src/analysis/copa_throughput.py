# plot_throughput.py
import re
import matplotlib.pyplot as plt

def extract_data_from_log(log_file_path):
    throughput_data = []
    packet_size = 1504  # Bytes per packet
    time_interval = 1  # Time in seconds (assuming 1-second intervals for simplicity)

    # Open the log file and read lines
    with open(log_file_path, 'r') as file:
        for line in file:
            # Check if the line contains the packet size (1504)
            if "1504" in line:  
                # Calculate throughput (in bits per second)
                throughput = packet_size * 8  # Convert bytes to bits
                throughput_data.append(throughput)  # Store throughput
                
    # Debugging: Print extracted data
    print("Extracted Throughput Data:", throughput_data)
    return throughput_data

def plot_data(throughput_data):
    time = [i for i in range(1, len(throughput_data) + 1)]  # Time intervals (1 per packet)

    plt.figure(figsize=(10, 6))

    # Plot throughput over time
    plt.plot(time, throughput_data, color='blue', label='Throughput')

    # Set labels and title
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Throughput (bps)', fontsize=12)
    plt.title('Throughput Over Time for copa', fontsize=14)
    plt.grid(True)
    plt.legend()

    # Save the plot as a PNG file instead of showing it
    plt.savefig('copa_throughput_plot.png', dpi=300, bbox_inches='tight')  # Save as PNG file

    # Optionally, you can also save as PDF
    # plt.savefig('throughput_plot.pdf', dpi=300, bbox_inches='tight')

    # Close the plot to avoid memory issues
    plt.close()

    print("Plot saved as 'throughput_plot.png'")

if __name__ == "__main__":
    log_file_path = '/home/navreet/Desktop/pantheon/output_1mbps/copa_mm_acklink_run1.log'
    print(f"Reading from log file: {log_file_path}")

    # Extract data from log
    throughput_data = extract_data_from_log(log_file_path)

    # Plot the data
    plot_data(throughput_data)