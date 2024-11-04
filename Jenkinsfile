pipeline {
    agent any
    environment { 
        DOCKERHUB_CREDENTIALS = credentials('dockerCredentials') 
        DOCKER_IMAGE = 'ahn1492/djangotour'
    }

    stages {
        stage('Git Clone') {
            steps {
                echo 'Git Clone'
                git url 'https://github.com/portalchu/djangoweb.git'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    dockerimage = docker.build("giry0612/djangotour")
                }
            }
        }
        stage('Docker Image Build') {
            steps {
                echo 'Docker Image Build'
                dir("${env.WORKSPACE}") {
                    sh """
                    docker build -t giry0612/djangotour:$BUILD_NUMBER .
                    docker tag giry0612/djangotour:$BUILD_NUMBER giry0612/djangotour:latest
                    """
                }
            }
        }
        stage('Docker Login') {
            steps {
                // docker hub 로그인
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
            }
        }
        stage('Docker Image Push') {
            steps {
                echo 'Docker Image Push'
                sh 'docker push giry0612/djangotour:latest'
            }
        }
        stage('Cleaning up') { 
            steps { 
                // docker image 제거
                echo 'Cleaning up unused Docker images on Jenkins server'
                sh """
                docker rmi giry0612/djangotour:$BUILD_NUMBER
                docker rmi giry0612/djangotour:latest
                """
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                dir("${env.WORKSPACE}") {
                    sh """
                    kubectl apply -f django.yml
                    """
                }
            }
        }
    }
}

