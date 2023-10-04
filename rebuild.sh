#!/bin/bash

source .python3/bin/activate
python3 generate-readme.py && git add schema/ && git commit -m "Update" && git push

