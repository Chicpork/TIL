
# 현재 실행중인 프로세스 모두 kill
docker rm -f $(docker ps -aq)