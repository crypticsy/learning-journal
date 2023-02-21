#!/bin/bash

# Get today's date in YYYY-MM-DD format
TODAY=$(date +"%Y-%m-%d")

# add all changes
git add *
# commit changes
git commit -m "66 Days of Data Science : Updated learnig log till $TODAY"
git push origin master