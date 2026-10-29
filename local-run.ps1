# Oh boy my first shell scripts wowee!
# (We never learned these during my bachelors...)

# Starts the services locally

docker start tasks-db

docker build -t mytodo-tasks .\src\task-service
docker build -t mytodo-stats .\src\stat-service

docker rm -f mytodo-task-container 2>$null
docker rm -f mytodo-task-container 2>$null

# Task Service
docker run -d --name mytodo-task-container --network mytodo-net -p 8000:8000 -e MONGO_URI=mongodb://tasks-db:27017 mytodo-tasks

# Stats Service
docker run -d --name mytodo-stats-container --network mytodo-net -p 8001:8000 -e MONGO_URI=mongodb://tasks-db:27017 mytodo-stats