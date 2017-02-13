#!/bin/bash
apt-get update
apt-get install -y apache2
pip install pybuilder
pyb install_dependencies

