pipeline {

    tools {
        PythonInstallation 'python3'
    }
    agent any
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
                sh 'python3 test.py'
                
            }
        }
    }
}
