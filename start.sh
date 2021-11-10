#!/bin/bash

case $1 in
	"services")
		echo "services"
		cd ./services; docker-compose up --build -d; echo 'proxy | rabbitMQ | MongoDB started'
		;;
	"queue")
		echo "queue"
		cd ./queue; docker-compose up --build -d; echo 'publisher | consumer started'
		;;
	"dashboard")
		echo "dashboard"
		cd ./dashboard; docker-compose up --build; echo 'dashboard started'
		;;
	"all")
		echo "all"
		cd ./services; docker-compose up --build -d; echo 'proxy | rabbitMQ | MongoDB started'; cd ..
		cd ./queue; docker-compose up --build -d; echo 'publisher | consumer started'; cd ..
		cd ./dashboard; docker-compose up --build; echo 'dashboard started'
		;;
	*)
		echo $"Usage: $0 {all|services|dashboard|queue}"
		exit 1
esac