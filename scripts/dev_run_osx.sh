#! /usr/bin/env bash
BASEDIR=$(dirname "$0")
cd "$BASEDIR"
docker-machine start
eval $(docker-machine env)
docker-compose start
