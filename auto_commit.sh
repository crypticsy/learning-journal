#!/bin/bash

# Get today's date in YYYY-MM-DD format
TODAY=$(date +"%a,%d %b, %Y %I:%M %p")

# add all changes
git add .
# commit changes
git commit -m "🤖 Updated learning log till $TODAY with leetcode"
git push origin master