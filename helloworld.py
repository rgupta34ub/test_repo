# helloworld.py
import os
import sys

EXAMPLE_KEY = os.environ.get("EXAMPLE_KEY")
if not EXAMPLE_KEY:
    print("ERROR: EXAMPLE_KEY environment variable is not set.", file=sys.stderr)
    sys.exit(1)

print("Hello World! Secret length:", len(EXAMPLE_KEY))
# ...use EXAMPLE_KEY safely in your code...
