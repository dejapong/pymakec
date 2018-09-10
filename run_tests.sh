#!/bin/bash

BUILD_DIR=build

rm -f ./$BUILD_DIR/*.test*
mkdir -p ./$BUILD_DIR
cd ./$BUILD_DIR

for filename in ../test/*.test.py; do
    [ -e "$filename" ] || continue
    PYTHONPATH=..:$PYTHONPATH python3 $filename
done