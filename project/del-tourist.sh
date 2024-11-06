#!/bin/bash
kubectl delete -f django-svc.yml
sleep 5s
kubectl delete -f network-l2-lb.yml
sleep 5s
kubectl delete -f ip-pool.yml
sleep 5s
kubectl delete -f metallb_native.yml
sleep 40s
kubectl delete -f django.yml
sleep 5s
kubectl delete -f mysql.yml













