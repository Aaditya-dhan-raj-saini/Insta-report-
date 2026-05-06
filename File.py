import os
import time

def change_ip():
    print("[*] Changing Identity...")
    os.system("pkill -HUP tor") # Tor circuit ko refresh karta hai
    print("[✔] IP Changed successfully.")

# Loop mein use karne ke liye
# while True:
#     change_ip()
#     time.sleep(60)
