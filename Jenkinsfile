pipeline {
    agent {
        kubernetes {
            yaml"""
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
    tty: true
    securityContext:
      privileged: true
  - name: kubectl
    image: lachlanevenson/k8s-kubectl
    tty: true
    command:
    - cat
"""
        }
    }
    environment { 
        DOCKERHUB_CREDENTIALS = credentials('dockerCredentials') 
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
                    dir("${env.WORKSPACE}") {
                        //echo 'Docker Image Build'
                        //sh """
                        //docker build -t giry0612/djangotour:$BUILD_NUMBER .
                        //docker tag giry0612/djangotour:$BUILD_NUMBER giry0612/djangotour:latest
                        //"""
                    }
                }
            }
        }
        stage('Docker Login') {
            steps {
                container('docker') { 
                    //echo 'Docker Login'
                    //sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
        }
        stage('Docker Image Push') {
            steps {
                container('docker') {
                    //echo 'Docker Image Push'
                    //sh "docker push giry0612/djangotour:$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                container('kubectl') {
                    echo 'Deploy to Kubernetes'
                    sh "kubectl get all -n jenkins"
                    sh "kubectl set image deployment/django django-app=giry0612/djangotour:10 -n jenkins --record"
                }
            }
        }
    }
}

