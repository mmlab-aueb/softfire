#!/bin/bash
echo "Deleting old csar files..."
rm deploy/aueb.csar
rm deploy/Files/ns-aueb.csar
cd ns-aueb
zip -r ../deploy/Files/ns-aueb.csar . -x ".*" -x "*/.*"
cd ..
cd deploy
zip -r aueb.csar . -x ".*" -x "*/.*"
cd ..

