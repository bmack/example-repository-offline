#!/usr/bin/env python3

# Load a target file into an existing Repository

# import our own "utils" module
from utils import *
import sys
from os import *

# base variables,
# @todo should be configurable via argv
basefolder = 'tuf-testrepo'
keystore = 'tufkeystore'
reponame = 'tufrepo'

absolute_source = sys.argv[1]
absolute_source = os.path.abspath(absolute_source)
target_location = sys.argv[2]
absolute_target = os.path.abspath(os.path.join(basefolder, reponame, 'targets', target_location));

print('Load existing TUF repository')
repository = tuf.load_repo(basefolder, reponame)

print('Load signing keys into repo')
tuf.load_signing_keys_into_repo(repository, keystore)

print('Adding target ', target_location, ' to repo')
tuf.add_target(repository, target_location, absolute_source, absolute_target)