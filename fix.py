# fix_requirements.py
with open("requirements.txt") as f:
    lines = f.readlines()

with open("requirements.txt", "w") as f:
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            # split by '=' and take first 2 parts (package and version)
            parts = line.split("=")
            pkg = parts[0]
            ver = parts[1] if len(parts) > 1 else ""
            f.write(f"{pkg}=={ver}\n")
