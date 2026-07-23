import os
import glob
import time
import random

# ============================================================
# Your target directory
# ============================================================
TARGET_DIR = "/home/d4v3-0-l0p3r/Desktop/scripts/ware/ransom/ransom_sim_test"

EXTENSION = ".locked"
RANSOM_NOTE = "README_RANSOM.txt"

# Icon mapping
ICON_WARNING = "\u26A0"      # ⚠️
ICON_ERROR = "\u274C"        # ❌
ICON_LOCK = "\U0001F512"     # 🔐
ICON_UNLOCK = "\U0001F513"   # 🔓
ICON_FILE = "\U0001F4C4"     # 📄
ICON_CHECK = "\u2714"        # ✔️
ICON_TRASH = "\U0001F5D1"    # 🗑️
ICON_FOLDER = "\U0001F4C1"   # 📁
ICON_MONEY = "\U0001F4B0"    # 💰
ICON_SKULL = "\U0001F480"    # 💀

# Funny fake crypto addresses
FAKE_BTC_ADDRESSES = [
    "1FakeBtcAddressForFun123456789",
    "3FunnyBtcWalletDontSendMoney",
    "bc1fakebitcoinaddressforlulz",
    "1MemesAndDreamsBtcAddress",
    "3NoReallyDontSendBitcoinToThis"
]

FAKE_ETH_ADDRESSES = [
    "0xFakeEthAddressForLaughs123456789",
    "0xFunnyEthWalletDontPayMe",
    "0xNoMoneyHereJustKidding"
]

def generate_funny_note():
    """Generate a humorous ransom note."""
    
    btc = random.choice(FAKE_BTC_ADDRESSES)
    eth = random.choice(FAKE_ETH_ADDRESSES)
    amount = random.randint(5, 50)
    
    jokes = [
        "Your files have been 'encrypted' with the power of friendship!",
        "Oops! Looks like your files took a vacation!",
        "Don't worry, this is just a simulation. Your files are fine!",
        "Your files are now... RENAMED! Scary, right?",
        "This is where we'd demand money if this was real ransomware!"
    ]
    
    return f"""
{'='*60}
   RANSOMWARE SIMULATION - EDUCATIONAL PURPOSES ONLY
{'='*60}

{random.choice(jokes)}

Your files have been SIMULATED as encrypted.
NO DATA WAS ACTUALLY MODIFIED OR ENCRYPTED.

--- FAKE RANSOM DEMAND (FOR FUN) ---

To 'decrypt' your files, you must send:
   {amount} BTC to: {btc}
   OR
   {amount*10} ETH to: {eth}

Just kidding! This is a simulation. 
To decrypt your files, simply run this script again and type 'decrypt'.

--- TECHNICAL DETAILS ---

Original folder: {TARGET_DIR}
Files affected: All files in the above folder
Encryption method: Renaming files (very secure... not really)

This is an educational tool to demonstrate how ransomware works
and why you should always backup your files!

Generated at: {time.strftime('%Y-%m-%d %H:%M:%S')}
{'='*60}
"""

def simulate_encrypt():
    """Renames all files in the target folder to simulate encryption."""
    
    if not os.path.exists(TARGET_DIR):
        print(f"{ICON_ERROR} Error: The folder '{TARGET_DIR}' does not exist.")
        print("Please create it and add some dummy .txt files.")
        return

    files = glob.glob(os.path.join(TARGET_DIR, "*"))
    # Exclude the ransom note itself and already locked files
    files = [f for f in files if not f.endswith(EXTENSION) and RANSOM_NOTE not in f]
    
    if not files:
        print(f"{ICON_WARNING} No files found to 'encrypt' in the target folder.")
        return

    print(f"{ICON_LOCK} Simulating ransomware encryption on {len(files)} files...")
    print(f"{ICON_SKULL} Your files are being renamed... MUAHAHAHA!")
    
    for file_path in files:
        # Simulate "encrypting" by just renaming the file
        new_path = file_path + EXTENSION
        os.rename(file_path, new_path)
        print(f"   {ICON_FILE} Encrypted: {os.path.basename(file_path)} -> {os.path.basename(new_path)}")
        time.sleep(0.1)  # Small delay to look realistic

    # Drop the ransom note
    note_path = os.path.join(TARGET_DIR, RANSOM_NOTE)
    with open(note_path, "w") as note:
        note.write(generate_funny_note())
    
    print(f"{ICON_FILE} Ransom note dropped: {note_path}")
    print(f"{ICON_MONEY} Fake ransom demand created (don't actually pay!)")
    print(f"{ICON_CHECK} Simulation complete. Your files are 'locked'.")
    print(f"\n{ICON_WARNING} To decrypt, run this script again and type 'decrypt'")


def simulate_decrypt():
    """Renames all '.locked' files back to their original names."""
    
    locked_files = glob.glob(os.path.join(TARGET_DIR, f"*{EXTENSION}"))
    
    if not locked_files:
        print(f"{ICON_WARNING} No '.locked' files found to decrypt.")
        return

    print(f"{ICON_UNLOCK} Simulating decryption on {len(locked_files)} files...")
    print("Removing '.locked' extensions...")
    
    for file_path in locked_files:
        # Remove the .locked extension to restore original name
        original_path = file_path.replace(EXTENSION, "")
        os.rename(file_path, original_path)
        print(f"   {ICON_FILE} Decrypted: {os.path.basename(file_path)} -> {os.path.basename(original_path)}")
        time.sleep(0.1)

    # Remove the ransom note
    note_path = os.path.join(TARGET_DIR, RANSOM_NOTE)
    if os.path.exists(note_path):
        os.remove(note_path)
        print(f"{ICON_TRASH} Ransom note removed.")

    print(f"{ICON_CHECK} All files have been 'decrypted' (restored to original names).")
    print("Your files are safe! Remember to backup your important data!")


# --- Main Menu ---
if __name__ == "__main__":
    print("\n" + "="*50)
    print("   RANSOMWARE SIMULATOR (Educational)")
    print("="*50)
    print(f"{ICON_FOLDER} Target Folder: {TARGET_DIR}")
    print(f"\n{ICON_WARNING} WARNING: Only run this on a test folder with dummy files!")
    print("="*50 + "\n")

    choice = input("Type 'encrypt' to lock files, or 'decrypt' to unlock them: ").strip().lower()

    if choice == "encrypt":
        simulate_encrypt()
    elif choice == "decrypt":
        simulate_decrypt()
    else:
        print(f"{ICON_ERROR} Invalid choice. Please type 'encrypt' or 'decrypt'.")
        
    