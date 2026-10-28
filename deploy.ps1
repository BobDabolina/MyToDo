kubectl apply -f .\kubernetes\mongodb.yaml
kubectl apply -f .\kubernetes\task-deployment.yaml
kubectl apply -f .\kubernetes\task-balancer.yaml
kubectl apply -f .\kubernetes\stat-deployment.yaml
kubectl apply -f .\kubernetes\stat-service.yaml

kubectl get pods
kubectl get services