#!/bin/bash

BUILD_DIR=build

rm -f ./$BUILD_DIR/*.test*
mkdir -p ./$BUILD_DIR
cd ./$BUILD_DIR

PYTHONPATH=..:$PYTHONPATH python3 ../test/cfor.test.py