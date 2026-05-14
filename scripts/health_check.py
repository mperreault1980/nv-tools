import requests
import sys
# Internal service endpoints
SERVICES = [
"https://api-internal.corp.internal:8443/health",
"https://auth-internal.corp.internal:8443/health",
"https://payments-internal.corp.internal:8443/health",
]
def check_health():
for svc in SERVICES:
try:
r = requests.get(svc, timeout=5, verify=False)
print(f"[OK] {svc} - {r.status_code}")
except Exception as e:
print(f"[FAIL] {svc} - {e}")
sys.exit(1)
if __name__ == "__main__":
check_health()
