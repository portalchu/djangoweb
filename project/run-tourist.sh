#!/bin/bash
kubectl create -f mysql.yml
sleep 5s
kubectl create -f django.yml
sleep 5s
kubectl create -f metallb_native.yml
sleep 60s
kubectl create -f ip-pool.yml
sleep 5s
kubectl create -f network-l2-lb.yml
sleep 5s
kubectl create -f django-svc.yml

