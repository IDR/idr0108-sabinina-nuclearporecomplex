
import re

"""
Generate the filePaths.tsv and a list of 'ln -s' commands. That's because
the original upload contains broken files which need to be "replaced" 
by the "resent" files. Note: The lns commands have to be run from 
within the "20210304" directory (it will create the links and 
dataset directories underneath)
"""

basedir = "/uod/idr/filesets/idr0108-sabinina-nuclearporecomplex"
lnsdir = "20210304"  # has to exist

infilepath = "idr0108_files.txt"
cmdsfilepath = "lns_cmds.sh"
filepaths = "../experimentA/idr0108-experimentA-filePaths.tsv"

#20210221-ftp/SNAP-NUP107/01_638i100_UVi50_Boosti150mW_x20_2C-A647-CF680_1_MMStack_Pos0.ome.tif  <- only these files have to imported
#20210221-ftp/SNAP-NUP107/01_638i100_UVi50_Boosti150mW_x20_2C-A647-CF680_1_MMStack_Pos0_1.ome.tif  <- not these, part of multifile image
#...
#20210226-ftp/resent/SNAP-RANBP2/01_638i100_640i150_405i50_x20_1_locprec_10_z35_LL1-6_1_MMStack_11.ome.tif  <- re-uploaded files
FORMAT = ".+/(SNAP-.+)/(.+\.ome\.tif)"


cmds_out = open(cmdsfilepath, "w")
fpaths_out = open(filepaths, "w")
entries = open(infilepath, 'r').readlines()

# Misusing this as ordered set (>= Python 3.7)
lns_cmds = {}

for entry in entries:
    entry = entry.strip()
    if match := re.search(FORMAT, entry, re.IGNORECASE):
        dataset = match.group(1)
        filename = match.group(2)
    else:
        continue

    if not re.search("_\d+\.ome\.tif$", filename, re.IGNORECASE):
        fpaths_out.write(f"Dataset:name:{dataset}\t{basedir}/{lnsdir}/{dataset}/{filename}\n")

    lns_cmds[f"mkdir {dataset}"] = ""
    # newer uploaded files will just overwrite existing links
    lns_cmds[f"ln -sf {basedir}/{entry} {dataset}/{filename}"] = ""

for k in lns_cmds.keys():
    cmds_out.write(f"{k}\n")

cmds_out.close()
fpaths_out.close()
