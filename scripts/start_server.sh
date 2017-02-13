#!/bin/bash
a2ensite pythonflaskexample.conf
service apache2 restart
echo "127.0.0.1 pythonflaskexample.com" >> /etc/hosts
pwd
cd .. && ./run_server.sh
