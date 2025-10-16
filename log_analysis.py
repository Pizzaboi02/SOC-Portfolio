import re
from collections import Counter

# Path to you r log file
log_file = "sample_auth.log"

# Read the log file
with open(log_file, "r") as f:
    logs = f.readlines()

# Regex pattern to match failed attempts
ip_pattern = r"(?:(?:\d{1,3}\.){3}\d{1,3})"

# Create a list to store extracted IPs
Ips = []

for line in logs:
    match = re.search(ip_pattern, line)
    if match:
        Ips.append(match.group())

# If no IPs found
if not Ips:
    print("No IPs found. Check your regex or log file path.")
    exit()

# Count occurrences of each IP
ip_counts = Counter(Ips)

# Sort IPs by frequency (most to least)
sorted_ips = ip_counts.most_common()

print("IP Frequency Report\n")

for ip, count in sorted_ips:
    # Highlight IPs with more than 3 hits
    if count >= 3:
        print(f"{ip} - {count} hits (SUSPICIOUS)")
    else:
        print(f"{ip} - {count} hits")

print(f"\nTotal unique IPs: {len(sorted_ips)}")
        
import csv

with open("ip_report.csv", "w", newline="") as csvfile:
    writer = csv. writer(csvfile)
    writer.writerow(["IP Address", "Hit Count", "Status"])
    for ip, count in sorted_ips:
        status = "SUSPICIOUS" if count >= 3 else "Ok"
        writer.writerow([ip, count, status])

print("\n Report saved as ip_report.csv")