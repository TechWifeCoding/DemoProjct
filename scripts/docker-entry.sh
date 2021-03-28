#!/bin/bash
/app/scripts/wait-for-it.sh db:3306
#./wait-for-it.sh db:3306
flask run -h "0.0.0.0"
