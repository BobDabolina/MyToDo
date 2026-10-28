# Oh boy my first shell scripts wowee!
# (We never learned these during my bachelors...)

docker build -t mytodo-tasks .\src\task-service
docker build -t mytodo-stats .\src\stat-service

# Task Service
docker run -d --name mytodo-task-container --network mytodo-net -p 8000:8000 -e MONGO_URI=mongodb://tasks-db:27017 mytodo-tasks

# Stats Service
docker run -d --name mytodo-stats-container --network mytodo-net -p 8001:8000 -e MONGO_URI=mongodb://tasks-db:27017 mytodo-stats