#!/bin/bash
kubectl create -f volume.yml
sleep 10s
kubectl create -f mysql.yml
sleep 10s
kubectl create -f django.yml
sleep 10s
kubectl create -f metallb_native.yml
sleep 30s
kubectl create -f ip-pool.yml
sleep 10s
kubectl create -f network-l2-lb.yml
sleep 10s
kubectl create -f django-svc.yml
sleep 10s













