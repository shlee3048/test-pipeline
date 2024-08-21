pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/shlee3048/test-pipeline.git'
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
