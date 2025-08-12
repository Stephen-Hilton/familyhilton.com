#!/bin/bash
. ./build.sh

# push to github
git add ${PUBPATH}
git add root
git commit -m "update site with new content"
git push -u origin main