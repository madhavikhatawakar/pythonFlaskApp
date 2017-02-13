#!/bin/bash
apt-get update
apt-get install -y apache2
pip install --upgrade pip
echo "upgraded pip"
pip install pybuilder
echo "installed pybuilder"
pyb install_dependencies
echo "installed dependencies"

