#!/bin/bash
sleep 10s
kubectl delete -f django-svc.yml
sleep 10s
kubectl delete -f network-l2-lb.yml
sleep 10s
kubectl delete -f ip-pool.yml
sleep 10s
kubectl delete -f metallb_native.yml
sleep 30s
kubectl delete -f django.yml
sleep 10s
kubectl delete -f mysql.yml
sleep 10s













