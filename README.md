# Rappi challenge

Author: Jorge Gómez Robles (j.gomezrb@gmail.com)

## Repository structure

This repository is structured as follows:

```bash
.
├── README.md
├── data
│   └── orders.csv
├── docker
│   ├── mlflow
│   ├── nginx
│   └── webapp
├── docker-compose.yml
├── notebooks
│   └── Modeling.ipynb
├── python
│   ├── utils
│   └── webapp
└── scripts
    ├── rappi-db.sql
    └── train.py
```

- `data`: where the original dataset for this challenge is stored.
- `docker`: where all the images used in this challenge are located.
- `docker-compose.yml`: compose file to start the containers.
- `notebooks`: where the notebook to solve and explore the __taken orders__
problem is stored.
- `python`: contains the two python packages for this solution (utilities and
the web endpoint).
- `scripts`:contains utility scripts.

## Environment

The solution was developed in an environment with the following specs:

- Virtual Python environment with python 3.9
- Docker Engine 20.10.8
- Compose 1.29.2

The solution requires the following environment variables (the values are just 
examples):

```bash
MYSQL_DATABASE=rappiml
MYSQL_USER=rappi
MYSQL_PASSWORD=abc123
MYSQL_ROOT_PASSWORD=abc123

SCRIPTS_DIR=/home/rappiml/scripts
MODELS_DIR=/home/rappiml/models
DATA_DIR=/home/rappiml/data
TAKEN_MODEL_DIR=/home/rappiml/models/taken-orders

APP_DIR=/home/rappiml
FLASK_APP=rappiml
```

Store these variables in a `.env` file at the same level of the 
`docker-compose.yml` file.

## Overview of the solution


## How to run the inference service

```bash
docker-compose up --build
```

## How to create the DB (only the first time)

When you start the services for the first time, the MySQL database does not have
any tables. In order to the create the table of inferences, wait until all
services are up and running and run the commands below. Once in the bash, copy
and paste the contents of `scripts/rappi-db.sql`.

```bash
# Start a local bash session from the mysql container
docker exec -it rappi-ml bash

# Create the bash
mysql -u rappi -p${MYSQL_ROOT_PASSWORD}
```

You can exit the bash session if you want.

## How to run inferences

The endpoint to obtain inferences from a list of observations is accesible at
`http://localhost:81/analytics/api/taken/` (accepts POST). The content-type of
the message must be JSON, with the format specified 
[here](http://localhost:81/analytics/api/taken/). An example is shown below.


```bash
curl http://localhost:81/analytics/api/taken/ -H 'Content-Type: application/json' -d '{
    "columns": ["order_id", "store_id", "to_user_distance", "to_user_elevation", "total_earning", "created_at"],
    "data": [[14364873, 30000009, 2.478101, -72.719360, 4200, "2017-09-07T20:02:17Z"], [14370123, 30000058, 0.451711, 37.754761, 4200, "2017-09-07T20:13:16Z"]]
}'
```