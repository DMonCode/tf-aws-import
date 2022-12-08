#!/usr/bin/env python3

import os, sys, yaml

file = sys.argv[2]

importer = sys.argv[1]

with open(file) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    for member in data[importer]:
        str = "terraform import " + member["key"] + "  " + member["value"]
        #print(str)
        os.system(str)
