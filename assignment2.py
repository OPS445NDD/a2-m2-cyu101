#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Summer 2026
Program: assignment2.py 
Author: "Jared Yu"
The python code in this file is original work written by
"Jared Yu". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <OPS445 AS2 M2>

Date: 16th July

'''

import argparse
import os, sys

def parse_command_args() -> object:
    """Set up argparse here. Call this function inside main."""
    parser = argparse.ArgumentParser(
        description="Memory Visualiser -- See Memory Usage Report with bar charts",
        epilog="Copyright 2023"
    )

    parser.add_argument(
        "-H",
        "--human-readable",
        action="store_true",
        help="Prints sizes in human readable format"
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=20,
        help="Specify the length of the graph. Default is 20."
    )

    parser.add_argument(
        "program",
        type=str,
        nargs="?",
        help="if a program is specified, show memory use of all associated "
             "processes. Show only total use if not."
    )

    return parser.parse_args()

def percent_to_graph(percent: float, length: int=20) -> str:
    """Turn a decimal percentage from 0.0 to 1.0 into a bar graph."""
    hashes = int(percent * length)
    spaces = length - hashes
    return "#" * hashes + " " * spaces


def get_sys_mem() -> int:
    """Return total system memory in KiB."""
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])
    return 0


def get_avail_mem() -> int:
    """Return currently available system memory in KiB."""
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])
    return 0
def pids_of_prog(app_name: str) -> list:
    """Return all process IDs associated with an application."""
    pid_output = os.popen(f"pidof {app_name}").read().strip()

    if not pid_output:
        return []

    return pid_output.split()

def rss_mem_of_pid(proc_id: str) -> int:
    """Return total resident memory used by a process in KiB."""
    rss_total = 0

    with open(f"/proc/{proc_id}/smaps", "r") as smaps_file:
        for line in smaps_file:
            if line.startswith("Rss:"):
                rss_total += int(line.split()[1])

    return rss_total

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:  # not program name is specified.
        pass
    else:
        pass
