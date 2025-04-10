import urllib.parse

with open('#', 'r') as infile, open('#', 'w') as outfile:
    for line in infile:
        parts = line.strip().split(',', 1)
        if len(parts) == 2:
            bucket, key = parts
            encoded_key = urllib.parse.quote(key)
            outfile.write(f"{bucket},{encoded_key}\n")
