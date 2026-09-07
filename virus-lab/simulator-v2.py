from pathlib import Path
import time

LAB = Path.home() / "virus-lab" / "test-files"
LOG = Path.home() / "virus-lab" / "v2-activity.log"


def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with LOG.open("a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[SIMULATOR] {message}")


def simulate_ransomware():
    log("=== V2 SIMULATION STARTED ===")
    log("WARNING: This is a harmless simulation.")

    files = list(LAB.glob("*.txt"))

    for file in files:
        locked = file.with_suffix(".locked")

        log(f"SIMULATING LOCK: {file.name} -> {locked.name}")

        # We only rename the harmless test file.
        file.rename(locked)

        time.sleep(0.5)

    log(f"Simulation complete. Simulated locking of {len(files)} files.")


def restore_files():
    log("=== RESTORE STARTED ===")

    files = list(LAB.glob("*.locked"))

    for file in files:
        restored = file.with_suffix(".txt")

        log(f"RESTORING: {file.name} -> {restored.name}")

        file.rename(restored)

        time.sleep(0.3)

    log(f"Restore complete. Restored {len(files)} files.")


def main():
    if not LAB.exists():
        print("Lab directory does not exist.")
        return

    print("\n1. Simulate ransomware")
    print("2. Restore test files")
    print("3. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        simulate_ransomware()
    elif choice == "2":
        restore_files()
    else:
        print("Exiting.")


if __name__ == "__main__":
    main()
