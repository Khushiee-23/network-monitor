from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess
import datetime
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

targets = [
    {"host": "google.com",  "type": "Web Service"},
    {"host": "cisco.com",   "type": "Cisco Server"},
    {"host": "github.com",  "type": "Code Repository"},
    {"host": "8.8.8.8",    "type": "Google DNS"},
    {"host": "1.1.1.1",    "type": "Cloudflare DNS"}
]

def ping(host):
    result = subprocess.run(
        ["ping", "-n", "1", host],
        capture_output=True,
        text=True
    )
    return "ONLINE" if "TTL=" in result.stdout else "OFFLINE"

def monitor_loop():
    scan_number = 1
    while True:
        results = []
        for target in targets:
            status = ping(target["host"])
            results.append({
                "host": target["host"],
                "type": target["type"],
                "status": status
            })
        
        data = {
            "scan": scan_number,
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "results": results,
            "online": sum(1 for r in results if r["status"] == "ONLINE"),
            "offline": sum(1 for r in results if r["status"] == "OFFLINE")
        }
        
        # Save log
        with open("network_log.txt", "a") as f:
            f.write(f"\nScan #{scan_number} | {data['timestamp']}\n")
            for r in results:
                f.write(f"  {r['host']:<20} {r['status']}\n")
        
        # Send to dashboard via WebSocket
        socketio.emit('network_update', data)
        print(f"✅ Scan #{scan_number} sent to dashboard!")
        
        scan_number += 1
        time.sleep(10)  # Scan every 10 seconds

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Start monitoring in background thread
    thread = threading.Thread(target=monitor_loop)
    thread.daemon = True
    thread.start()
    
    print("🚀 Server starting at http://localhost:5000")
    socketio.run(app, debug=False, port=5000)