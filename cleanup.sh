 #! /bin/bash

docker rm -f animal-api server

docker rmi animal_noises_api animal_noises_server

docker network rm animal_noises_network
