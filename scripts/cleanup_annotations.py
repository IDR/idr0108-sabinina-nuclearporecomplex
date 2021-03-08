
import re

in_file = "../assays_concatenated.csv"
out_file = "../experimentA/idr0108-experimentA-annotation.csv"

out = open(out_file, "w")
entries = open(in_file, 'r').readlines()

for entry in entries:
    entry = entry.strip()
    image_name = entry.split(',')[1].strip()
    if not re.search("_\d+\.ome.tif", image_name, re.IGNORECASE):
        out.write(f"{entry}\n")

out.close()
