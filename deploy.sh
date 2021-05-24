#! bin/bash

# build server
docker build -t animal_noises_server server
# build api
docker build -t animal_noises_api animal_api
# create network
docker network create animal_noises_network
# run containers
docker run -d -p 5000:5000 --network animal_noises_network --name server animal_noises_server
docker run -d --network animal_noises_network --name animal-api animal_noises_api
