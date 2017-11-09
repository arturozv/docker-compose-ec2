#!/bin/bash
#https://gist.github.com/ReedD/a46c10ccce5af12c8d5f
#https://github.com/iliyahoo/terraform-up-and-running-code/tree/9c0d1924bb7d668e1dfae45a8907685d7e55271b/my_code/modules/services/webserver-cluster

cat <<'EOF' >>/home/ubuntu/docker/docker-compose.yml

version: '2'
services:
  seoweb:
    image: ${DOCKER_IMAGE}
    volumes:
      - /home/ubuntu/logs:/app/log
    environment:
      - SPRING_PROFILES_ACTIVE=${SPRING_PROFILES_ACTIVE}
      - JVM_MIN_MEMROY=${JVM_MIN_MEMORY}
      - JVM_MAX_MEMROY=${JVM_MAX_MEMORY}
    ports:
      - "80:${SERVER_PORT}"
    restart: always
EOF

chown ubuntu:ubuntu /home/ubuntu/docker/docker-compose.yml
docker login -e ${DOCKER_MAIL} -u ${DOCKER_USER} -p ${DOCKER_PASSWORD} 
/home/ubuntu/set_env_and_start.sh