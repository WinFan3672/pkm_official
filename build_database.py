#!/usr/bin/python
import os
import pickle
db = {}
print("build: Beginning build process.")
for item in os.listdir():
    if os.path.isdir(item):
        ## Check for contents
        if "package.szip3" in os.listdir(item) and "program.info" in os.listdir(item):
            url = "https://github.com/WinFan3672/pkm_official/raw/main/{}/package.szip3".format(item)
            with open(f"{item}/program.info") as f:
                g = f.read().split("|")
                if len(g) != 2:
                    print("ERROR: Invalid package info for {}.".format(item))
                    continue
            dic = {"name":g[0],
                "url":url,
                "desc":g[1],
                }
            db[item] = dic
        else:
            print("ERROR: Package '{}' has missing files.".format(item))
with open("pkm.db.cfg","wb") as f:
    pickle.dump(db,f)
print("Build finished.")