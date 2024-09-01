pipeline {
    agent {
        kubernetes {
            label 'python-docker-pod-template'
            defaultContainer 'python'
            yaml '''
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                app: python-docker
            spec:
              containers:
              - name: python
                image: python:3.10
                command:
                - cat
                tty: true
              - name: docker
                image: docker:stable
                command:
                - sleep
                args:
                - 9999999
                tty: true
                volumeMounts:
                - name: docker-sock
                  mountPath: /var/run/docker.sock
              volumes:
              - name: docker-sock
                hostPath:
                  path: /var/run/docker.sock
                
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
        stage('Install Dependencies') {
            steps {
                container('python') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test FastAPI Application') {
            steps {
                container('python') {
                    // FastAPI 애플리케이션 테스트
                    sh 'uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info &'
                    sh 'sleep 5' // 애플리케이션이 시작될 시간을 줌
                    sh 'curl -f -X GET http://localhost:8000/hello'
                    sh 'curl -f -X POST http://localhost:8000/echo -H "Content-Type: application/json" -d \'{"text":"Hello"}\''
                    sh 'pkill -f "uvicorn main:app"'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                container('docker') {
                    sh 'docker build -t shlee3048/fast-app:latest .'
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                container('docker') {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                        sh 'docker push shlee3048/fast-app:latest'
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                container('docker') {
                    sh 'kubectl set image deployment/myapp myapp=shlee3048/fast-app:latest --record'
                }
            }
        }
    }
}
