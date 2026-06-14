# import subprocess
# import datetime
# import time
# import os

# targets = [
#     "google.com",
#     "cisco.com",
#     "github.com",
#     "8.8.8.8",
#     "1.1.1.1"
# ]

# def ping(host):
#     result = subprocess.run(
#         ["ping", "-n", "1", host],
#         capture_output=True,
#         text=True
#     )
#     if "TTL=" in result.stdout:
#         return "ONLINE"
#     else:
#         return "OFFLINE"
    
# def save_log(timestamp, results):
#     with open("network_log.txt", "a") as f:
#         f.write(f"\n{'='*45}\n")
#         f.write(f"Scan Time: {timestamp}\n")
#         f.write(f"{'='*45}\n")
#         for r in results:
#             f.write(r + "\n")

# def monitor():
#     scan_number = 1
    
#     print("\n🚀 Network Monitor Started!")
#     print("   Press Ctrl+C to stop\n")
    
#     while True:
#         os.system('cls')  #Clear screen each scan
        
#         timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
#         print("="*45)
#         print("   🌐 NETWORK MONITOR TOOL")
#         print(f"   🕐 Time  : {timestamp}")
#         print(f"   🔁 Scan  : #{scan_number}")
#         print("="*45)
        
#         results = []
#         online_count = 0
#         offline_count = 0
    
#     for target in targets:
#         status = ping(target)
#         emoji = "🟢" if status == "ONLINE" else "🔴"
#         print(f"  {target:<20} {emoji} {status}")
#         results.append(f"{target:<20} {status}")
    
#         if status == "ONLINE":
#                 online_count += 1
#         else:
#                 offline_count += 1
        
#         print("="*45)
#         print(f"  ✅ Online : {online_count}  |  ❌ Offline: {offline_count}")
#         print("="*45)
#         print(f"\n  💾 Log saved! Next scan in 30 seconds...")
        
#         save_log(timestamp, results)
        
#         scan_number += 1
#         time.sleep(30)  # Wait 30 seconds

# try:
#     monitor()
# except KeyboardInterrupt:
#     print("\n\n⛔ Monitor stopped by user. Goodbye!")

import subprocess
import datetime
import time

targets = [
    "google.com",
    "cisco.com", 
    "github.com",
    "8.8.8.8",
    "1.1.1.1"
]

def ping(host):
    result = subprocess.run(
        ["ping", "-n", "1", host],
        capture_output=True,
        text=True
    )
    if "TTL=" in result.stdout:
        return "ONLINE"
    else:
        return "OFFLINE"

def monitor():
    scan_number = 1
    print("\n🚀 Network Monitor Started! Press Ctrl+C to stop\n")
    
    while True:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n{'='*45}")
        print(f"  🌐 SCAN #{scan_number} | {timestamp}")
        print(f"{'='*45}")
        
        online = 0
        offline = 0
        
        for target in targets:
            status = ping(target)
            emoji = "🟢" if status == "ONLINE" else "🔴"
            print(f"  {target:<20} {emoji} {status}")
            if status == "ONLINE":
                online += 1
            else:
                offline += 1
        
        print(f"{'='*45}")
        print(f"  ✅ Online: {online} | ❌ Offline: {offline}")
        print(f"  ⏳ Next scan in 30 sec...")
        
        scan_number += 1
        time.sleep(30)

try:
    monitor()
except KeyboardInterrupt:
    print("\n⛔ Stopped. Goodbye!")