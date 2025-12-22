import subprocess
import sys

browsers = ["chromium", "firefox", "webkit"]

file_path = ""
if len(sys.argv) > 1:
    file_path = sys.argv[1] if sys.argv[1] else ""
for browser in browsers:
    print(f"\n=== Running on {browser} ===")
    result = subprocess.run(["behave", "-D", f"browser={browser}", f"behave/features/{file_path}"])
    if result.returncode != 0:
        print(f"Failed on {browser}")
        sys.exit(result.returncode)

print("All browsers passed!")
