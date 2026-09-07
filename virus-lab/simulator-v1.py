from pathlib import Path
import time

LAB = Path.home() / "virus-lab" / "test-files"
LOG = Path.home() / "virus-lab" / "activity.log"


def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with LOG.open("a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[SIMULATOR] {message}")


def simulate_file_activity():
    log("Starting simulated malware activity.")

    files = list(LAB.glob("*"))

    for file in files:
        if file.is_file():
            log(f"Detected file: {file.name}")
            time.sleep(0.3)

    log(f"Simulation complete. Examined {len(files)} files.")


if __name__ == "__main__":
    if not LAB.exists():
        print("Lab directory does not exist.")
        exit(1)

    simulate_file_activity()
