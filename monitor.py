#!/usr/bin/env python3
# =========================================
# System Monitor Tool
# Author: Mehriban Shukrieva
# Description: Displays CPU, memory, and disk usage in real time
# =========================================

import psutil
import time
import os

def clear_screen():
    """Clear the terminal for better visibility."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_system_stats():
    """Display system usage stats."""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"🖥️  CPU Usage: {cpu}%")
    print(f"💾 Memory Usage: {memory}%")
    print(f"📀 Disk Usage: {disk}%")
    print("-" * 30)

def main():
    print("🔹 Starting System Monitor (press Ctrl+C to exit)")
    try:
        while True:
            clear_screen()
            display_system_stats()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n✅ Monitoring stopped by user.")

if __name__ == "__main__":
    main()
