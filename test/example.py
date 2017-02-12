#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, './../python-cobol')

import cobol

with open("example.cbl",'r') as f:
    for row in cobol.process_cobol(f.readlines()):
        print(row['name'])
