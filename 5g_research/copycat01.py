#!/usr/bin/env python3

import shutil
import os

os.chdir("/home/glen/mycode/")
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")  # copies the first file to 2nd
shutil.copytree("5g_research/", "5g_research_backup/")  # copies entire 1st directory to 2nd directory
