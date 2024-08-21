pipeline {
    agent any
    
    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[url: 'https://github.com/shlee3048/test-pipeline.git']]
                    )
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    // test.py 프로젝트 테스트
                    sh 'python3 test.py'
                }
            }
        }
    }
}
