#!/usr/bin/env python3

import sys

# Initialize variables to keep track of metrics
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Loop through lines from stdin
for i, line in enumerate(sys.stdin):
    try:
        # Parse the line to extract status code and file size
        fields = line.split()
        if len(fields) != 7:
            raise ValueError("Invalid input format")
        status_code = int(fields[4])
        file_size = int(fields[6])

        # Update metrics
        total_size += file_size
        status_code_counts[status_code] += 1

        # Print metrics after every 10 lines or on keyboard interrupt
        if i > 0 and i % 10 == 0:
            print(f"Total file size: {total_size}")
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")
            print("")

    except (ValueError, IndexError):
        # Skip invalid input lines
        pass
    except KeyboardInterrupt:
        # Print metrics on keyboard interrupt
        print(f"\nTotal file size: {total_size}")
        for code, count in sorted(status_code_counts.items()):
            if count > 0:
                print(f"{code}: {count}")
        break

