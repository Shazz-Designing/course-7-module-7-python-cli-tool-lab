# Forces UTF-8 encoding for all Python processes in this project (fixes Windows emoji output)
import sys
import io
import os

os.environ["PYTHONUTF8"] = "1"

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)
if hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace', line_buffering=True)