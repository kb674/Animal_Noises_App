#!/bin/bash

docker-compose up -d
docker exec server python3 create.py
