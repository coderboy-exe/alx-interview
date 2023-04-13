#!/usr/bin/python3
""" Reads stdin line-by-line and computes metrics """
import sys


status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
counter = 0


def get_stats():
    """ Function to print pre-computed metrics """
    print(f"File size: {total_size}")
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print(f"{key}: {value}")


if  __name__ == "__main__":

    try:
        for line in sys.stdin:
            line_args = line.split()
            if len(line_args) == 9:
                code = int(line_args[-2])
                file_size = int(line_args[-1])

                keys = status_codes.keys()
                if code in keys:
                    status_codes[code] += 1
                total_size += file_size
                counter += 1

            if counter == 10:
                get_stats()
                counter = 0

    except KeyboardInterrupt:
        get_stats()
