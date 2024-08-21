pipeline {

    agent {
        kubernetes {
            label 'shlee-jenkins-ubuntu'
            defaultContainer 'ubuntu' // 사용할 컨테이너의 이름
            yaml '''
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                app: jenkins
            spec:
              containers:
                - name: ubuntu
                  image: ubuntu:latest
                  command:
                    - cat
                  tty: true
                  resources:
                    requests:
                      memory: "512Mi"
                      cpu: "500m"
            '''
        }
    }
    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[credentialsId: 'test-pipeline-key', url: 'https://github.com/shlee3048/test-pipeline.git']]
                    )
                }
            }
        }
        stage('Build') {
            steps {
                // test.py 프로젝트 테스트
                sh 'sudo apt install -y python3'
                sh 'python3 test.py'
                
            }
        }
    }
}
