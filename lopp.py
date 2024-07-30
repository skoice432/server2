import time

print("Codespace keeper is running. Press Ctrl+C to exit.")

try:
    while True:
        # Run a simple command to keep the codespace active
        print(".", end="", flush=True)
        time.sleep(60)  # wait for 1 minute
except KeyboardInterrupt:
    print("\nExiting codespace keeper.")