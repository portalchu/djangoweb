pipeline {
    agent {
       kubernetes {
            yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    jenkins-build: app-build
    some-label: "build-app-${BUILD_NUMBER}"
spec:
  containers:
  - name: docker
    image: docker:dind
    securityContext:
      privileged: true
"""
        } 
    }
    environment { 
        DOCKERHUB_CREDENTIALS = credentials('dockerCredentials') 
        DOCKER_IMAGE = 'ahn1492/python-django:1.0'
    }

    stages {
        stage('Git Clone') {
            steps {
                container('docker') {
                    echo 'Git Clone'
                    git url: 'https://github.com/portalchu/djangoweb.git', branch: 'main'
                    //credentialsId: 'gitToken'                
                }
            }
        }
        stage('Docker Image Build') {
            steps {
                container('docker') {                
                    echo 'Docker Image Build'
                    dir("${env.WORKSPACE}") {
                        sh """
                        docker build -t giry0612/djangotour:$BUILD_NUMBER .
                        docker tag giry0612/djangotour:$BUILD_NUMBER giry0612/djangotour:latest
                        """
                    }
                }
            }
        }
        stage('Docker Login') {
            steps {
                container('docker') { 
                    echo 'Docker Login'
                    // docker hub 로그인
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
        }
        stage('Docker Image Push') {
            steps {
                container('docker') {
                echo 'Docker Image Push'
                sh "docker push giry0612/djangotour:$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                dir("${env.WORKSPACE}") {
                    sh """
                    kubectl set image deployment django django-app=giry0612/djangotour:$BUILD_NUMBER --record
                    """
                }
            }
        }
    }
}

