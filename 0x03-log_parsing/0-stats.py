#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_code_counts = {}
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0

# Regex pattern for parsing log lines
log_pattern = re.compile(r'^\d{1,3}(\.\d{1,3}){3} - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_stats():
    """Prints the statistics collected so far."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def handle_interrupt(signum, frame):
    """Handles keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, handle_interrupt)

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    match = log_pattern.match(line)
    if match:
        status_code = int(match.group(2))
        file_size = int(match.group(3))
        
        # Accumulate total file size
        total_file_size += file_size
        
        # Count the status code
        if status_code not in status_code_counts:
            status_code_counts[status_code] = 0
        status_code_counts[status_code] += 1
        
        # Increase line count
        line_count += 1
        
        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

# Print final stats if end of input is reached
print_stats()

