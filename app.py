print("Hello from Dockerized App!")
import os
print(f"Version: {os.environ.get('VERSION', 'unknown')}")
