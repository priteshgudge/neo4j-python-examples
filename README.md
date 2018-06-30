# neo4j-python-examples
Neo4j Python Examples with docker installation of neo4j

## Run NEO4j instance
docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/temp/neo4j/data:/data \
    --volume=$HOME/temp/neo4j/logs:/logs \
    neo4j:3.0

Go to http://localhost:7474 and set username(neo4j) and password

## Install Packages
pip install neomodel

## Run script
Modify and run sample script in python


