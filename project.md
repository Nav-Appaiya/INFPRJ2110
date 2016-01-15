INFPRJ2110-collector-component based on Django REST Skeleton
====================

API endpoints for GET+POST:
    /positions
    /connections
    /events
    /monitoring

Features:
    - Presents a API for each datastream
    - Generates random dummy data

Dependencies:
    - Check /reqs/ folder for the requirements
    - To install requirements run:
        `pip install -r reqs/required.txt`

Project options:
    Setting up postgres:
        Run following command with your postgres info:
        echo "postgres://postgres@localhost:5432/project" > envdir/DATABASE_URL

    Setting project in Debug mode:
        To get usefull error messages, run following:
            echo "true" > envdir/DEBUG