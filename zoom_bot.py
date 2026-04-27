import webbrowser
import time
import pyautogui
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    blue = Fore.BLUE

    print(blue + """
███████╗ ██████╗  ██████╗ ███╗   ███╗
╚══███╔╝██╔═══██╗██╔═══██╗████╗ ████║
  ███╔╝ ██║   ██║██║   ██║██╔████╔██║
 ███╔╝  ██║   ██║██║   ██║██║╚██╔╝██║
███████╗╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
""" + Style.RESET_ALL)

    print(blue + "        ZOOM BOT v1.0\n" + Style.RESET_ALL)

clear()
banner()

time.sleep(1)
print(Fore.BLUE + "[+] Initializing...")
time.sleep(1)
print(Fore.BLUE + "[+] Loading modules...")
time.sleep(1)
print(Fore.BLUE + "[+] Ready.\n")
time.sleep(0.5)

meeting_id = input("Meeting ID: ")
password = input("Password: ")
base_name = input("Name: ")
bots = int(input("Bots: "))

# Прев'ю
print("\n[CONFIG]")
print(f"Meeting ID : {meeting_id}")
print(f"Base name  : {base_name}")
print(f"Bots       : {bots}")

confirm = input("\nContinue? (Y/n): ").strip().lower()
if confirm != "y":
    print("[!] Aborted.")
    exit()

print("\n[+] Launching...\n")

success = 0
fail = 0

for i in range(bots):
    try:
        # Генеруємо ім'я для поточного бота
        if "_" in base_name or base_name.lower() == "bot":
            # Якщо в імені вже є нижнє підкреслення або це "bot" - додаємо номер
            bot_name = f"{base_name}_{i+1}"
        else:
            # Інакше просто додаємо номер
            bot_name = f"{base_name}{i+1}"
        
        # Альтернативний простий варіант (розкоментуйте і закоментуйте код вище якщо хочете):
        # bot_name = f"{base_name}_{i+1}" if base_name == "bot" else f"{base_name}{i+1}"
        
        print(f"[{i+1}] Joining as '{bot_name}'...", end=" ")
        
        url = f"https://zoom.us/wc/join/{meeting_id}?pwd={password}&uname={bot_name}"
        
        webbrowser.open(url)

        time.sleep(8)

        for _ in range(8):
            pyautogui.press("tab")
            time.sleep(0.15)

        pyautogui.press("enter")

        success += 1
        print("OK")

    except Exception as e:
        fail += 1
        print(f"FAIL ({str(e)[:30] if str(e) else 'error'})")

    time.sleep(3)

# Підсумок
print("\n[RESULT]")
print(f"Success: {success}")
print(f"Fail   : {fail}")
print(f"Total  : {bots}")

