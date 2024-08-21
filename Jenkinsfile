pipeline {
    agent {
         kubernetes {
            label 'python'
            yaml '''
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                app: python
            spec:
              containers:
              - name: python
                image: python:3.8
                imagePullPolicy: IfNotPresent
                command:
                - cat
                tty: true

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
                sh 'python3 test.py'
                
            }
        }
    }
}
