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
    securityContext:    #
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
        // docker push를 위한 docker hub 로그인용 Credentials
        // 사용 전 Jenkins에서 설정 필요
        DOCKERHUB_CREDENTIALS = credentials('dockerCredentials') 
    }
    stages {
        stage('Git Clone') {    // GitHub에서 정보를 가져온다.
            steps {
                container('docker') {   // 위에서 생성한 Pod의 docker 컨테이너에서 실행
                    echo 'Git Clone'    // WebHook을 위해 gitToken 사용했으며 Credential 설정 필요
                    git url: 'https://github.com/portalchu/djangoweb.git', branch: 'main',
                    credentialsId: 'gitToken'                
                }
            }
        }
        stage('Docker Image Build') {
            steps {
                container('docker') {
                    dir("${env.WORKSPACE}") {
                        echo 'Docker Image Build'   // GitHub에 있는 Dockerfile을 빌드
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
                    echo 'Docker Login'     // Docker Hub에 올리기 위해 로그인 필요
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
            }
        }
        stage('Docker Image Push') {
            steps {
                container('docker') {
                    echo 'Docker Image Push'    // Docker Hub에 이미지 Push
                    sh "docker push giry0612/djangotour:$BUILD_NUMBER"
                    sh "docker push giry0612/djangotour:latest"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                container('kubectl') {  // 위에서 생성한 Pod의 kubectl 컨테이너에서 실행
                    echo 'Deploy to Kubernetes' // 기존의 django deployment의 이미지를 새로 빌드한 이미지로 수정
                    sh "kubectl set image deployment/django django-app=giry0612/djangotour:$BUILD_NUMBER -n default --record"
                }
            }
        }
    }
}

