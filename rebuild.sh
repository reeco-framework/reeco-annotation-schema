#!/bin/bash

source .python3/bin/activate
git add generate-* reeco.py
python3 generate-schema.py && python3 generate-readme.py && git add schema/ && git commit -m "Update" && git push

