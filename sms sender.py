import requests
import time
import os
import json

# Terminal colors for Termux
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Clear screen
def clear():
    os.system('clear')

# Display banner
def banner():
    print(CYAN + "="*50)
    print("        📲 Infobip SMS Sender (Termux Edition)")
    print("        👨‍💻 Author: Md. Jahid Hasan")
    print("="*50 + RESET)

# Send SMS via Infobip
def send_sms(number, message):
    url = "https://api.infobip.com/sms/2/text/advanced"
    payload = json.dumps({
        "messages": [
            {
                "from": "InfoSMS",  # Set a valid registered sender ID
                "destinations": [{"to": f"88{number}"}],  # Infobip expects full international number
                "text": message
            }
        ]
    })

    headers = {
        'Authorization': 'App e81d1ecd545bd323f4c2cce7d375778e-5f5d9467-1496-4001-85a3-9699e908046e',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            print(GREEN + f"✅ SMS sent to {number} | Message: {message}" + RESET)
        else:
            print(RED + f"❌ Failed to send SMS. Code: {response.status_code} | {response.text}" + RESET)
    except Exception as e:
        print(RED + f"❌ Error: {e}" + RESET)

# Validate BD number
def is_valid_number(number):
    return number.isdigit() and len(number) == 11 and number.startswith("01")

# Main function
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
