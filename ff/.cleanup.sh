#!/bin/bash
find . -name "*.pyc" -exec rm -rf {} \;
rm .ff-ff.db
rm .ffconfig
