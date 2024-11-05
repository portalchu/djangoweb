#!groovy
podTemplate(
    label: 'deploy', 
    containers: [
        //container image는 docker search 명령 이용
        containerTemplate(name: "docker", image: "docker:latest", ttyEnabled: true, command: "cat"),
        containerTemplate(name: "kubectl", image: "lachlanevenson/k8s-kubectl", command: "cat", ttyEnabled: true)
    ]
) 
{
    environment { 
        DOCKERHUB_CREDENTIALS = credentials('dockerCredentials') 
        DOCKER_IMAGE = 'ahn1492/python-django:1.0'
    }
    node('deploy') {
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
                        //sh """
                        //docker build -t giry0612/djangotour:$BUILD_NUMBER .
                        //docker tag giry0612/djangotour:$BUILD_NUMBER giry0612/djangotour:latest
                        //"""
                    }
                }
        }
        stage('Docker Login') {
                container('docker') { 
                    echo 'Docker Login'
                    // docker hub 로그인
                    //sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                }
        }
        stage('Docker Image Push') {
                container('docker') {
                echo 'Docker Image Push'
                //sh "docker push giry0612/djangotour:$BUILD_NUMBER"
                }
        }
        stage('Deploy to Kubernetes') {
                //withKubeConfig([credentialsId: '94b3c173-9c2c-4b0f-babe-5945cb502227', namespace: 'default']) {
                container('kubectl') {
                echo 'Deploy to Kubernetes'
                sh "kubectl apply --help"
                sh "kubectl replace --help"
                sh "kubectl patch --help"
                sh "kubectl diff --help"
                sh "kubectl get all -n default"
                sh "kubectl set image deployment/django django-app=giry0612/djangotour:14 -n default --record"
                }
        }

    }
}

