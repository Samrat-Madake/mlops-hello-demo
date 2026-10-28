
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
        VENV = '.venv-jenkins'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '"%PYTHON%" -m venv "%VENV%"'
                bat '"%VENV%\\Scripts\\python.exe" -m pip install --upgrade pip'
                bat '"%VENV%\\Scripts\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat '"%VENV%\\Scripts\\python.exe" hello.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%VENV%\\Scripts\\python.exe" -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '"%VENV%\\Scripts\\python.exe" monitoring.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mlops-hello .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f mlops-hello-container 2>NUL || exit /b 0'
                bat 'docker run -d --name mlops-hello-container mlops-hello'
                bat 'docker ps --filter "name=mlops-hello-container"'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'drift_report.html',
                             allowEmptyArchive: true
        }
        success {
            echo 'MLOps pipeline completed successfully!'
        }
    }
}




