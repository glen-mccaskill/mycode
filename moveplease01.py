#!/usr/bin/env python3

import shutil
import os

os.chdir("/home/glen/mycode/")
shutil.move("raynor.obj", "ceph_storage/")  # This moves raynor.obj into the ceph_storage directory.

xname = input("What is the new name for kerrigan.obj? ")
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)
