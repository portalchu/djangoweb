pipeline {
    agent {
        Kubernetes {
            label 'build'
            yaml"""
apiVersion: v1
kind: Pod
metadata:
  label: build
spec:
  containers:
  - name: docker
    image: docker:latest
    command:
    - cat
    tty: true
    securityContext:
      privileged: true
  - name: kubectl
    image: lachlanevenson/k8s-kubectl
    command:
    - cat
    tty: true
    securityContext:
      privileged: true
"""
        }
    }
    environment { 
        DOCKERHUB_CREDENTIALS = credentials('dockerCredentials') 
    }
    stages {
        stage('Git Clone') {
                container('docker') {
                    echo 'Git Clone'
                    git url: 'https://github.com/portalchu/djangoweb.git', branch: 'main'
                    //credentialsId: 'gitToken'                
                }
        }
        stage('Docker Image Build') {
            container('docker') {
                dir("${env.WORKSPACE}") {
                    echo 'Docker Image Build'
                    sh """
                    docker build -t giry0612/djangotour:$BUILD_NUMBER .
                    docker tag giry0612/djangotour:$BUILD_NUMBER giry0612/djangotour:latest
                    """
                }
            }
        }
        stage('Docker Login') {
            container('docker') { 
                echo 'Docker Login'
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
            }
        }
        stage('Docker Image Push') {
            container('docker') {
                echo 'Docker Image Push'
                sh "docker push giry0612/djangotour:$BUILD_NUMBER"
            }
        }
        stage('Deploy to Kubernetes') {
            container('kubectl') {
                echo 'Deploy to Kubernetes'
                sh "kubectl set image deployment/django django-app=giry0612/djangotour:10 -n jenkins --record"
            }
        }
    }
}

