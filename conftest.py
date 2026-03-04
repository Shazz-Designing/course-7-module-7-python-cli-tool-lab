import os
import subprocess
import sys

os.environ["PYTHONUTF8"] = "1"

_original_run = subprocess.run

def _patched_run(args, **kwargs):
    env = kwargs.pop("env", None)
    if env is None:
        env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    if kwargs.get("text") or kwargs.get("universal_newlines"):
        kwargs["encoding"] = "utf-8"
    return _original_run(args, env=env, **kwargs)

subprocess.run = _patched_run