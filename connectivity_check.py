import socket
import requests
import sys

host = "generativelanguage.googleapis.com"

print(f"Testing connectivity to {host}...")

# 1. DNS Check
try:
    ip = socket.gethostbyname(host)
    print(f"[PASS] DNS Resolution: {host} -> {ip}")
except socket.gaierror as e:
    print(f"[FAIL] DNS Resolution: {e}")
    # If DNS fails, we can't proceed to HTTP Check usually, but let's try just in case instructions differ
    sys.exit(1)
except Exception as e:
    print(f"[FAIL] DNS Resolution (Unexpected): {e}")
    sys.exit(1)

# 2. HTTP Check
try:
    url = f"https://{host}"
    print(f"Attempting GET {url}...")
    response = requests.get(url, timeout=10)
    print(f"[PASS] HTTP Connection: Status Code {response.status_code}")
except Exception as e:
    print(f"[FAIL] HTTP Connection: {e}")
    sys.exit(1)
