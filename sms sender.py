import requests
import time
import os

# Colors for better display in Termux
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def clear():
    os.system('clear')

def banner():
    print(CYAN + "="*50)
    print("        📲 Custom Advanced SMS Sender")
    print("        👨‍💻 Author: Jundul Kafa")
    print("="*50 + RESET)

def send_sms(number, message):
    url = f"https://riad.nagad.my.id/api/api.php?key=EID-GIFT&number={number}&msg={message}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(GREEN + f"✅ SMS sent to {number} | Message: {message}" + RESET)
        else:
            print(RED + f"❌ Failed to send SMS. Status Code: {response.status_code}" + RESET)
    except Exception as e:
        print(RED + f"❌ Error: {e}" + RESET)

def is_valid_number(number):
    return number.isdigit() and len(number) == 11 and number.startswith("01")

def main():
    while True:
        clear()
        banner()
        number = input("📱 Enter target number (BD only, 11 digits): ")
        if not is_valid_number(number):
            print(RED + "❌ Invalid number. Must be 11 digits and start with 01." + RESET)
            time.sleep(2)
            continue

        message = input("💬 Enter your custom message: ")
        try:
            count = int(input("🔁 How many times to send?: "))
        except ValueError:
            print(RED + "❌ Invalid number of times." + RESET)
            time.sleep(2)
            continue

        print(YELLOW + "\n🚀 Sending SMS...\n" + RESET)
        for i in range(count):
            send_sms(number, message)
            time.sleep(1)

        again = input("\n🔄 Send another SMS? (y/n): ").lower()
        if again != 'y':
            print(CYAN + "👋 Exiting... Thanks for using the script!" + RESET)
            break

if __name__ == "__main__":
    main()
