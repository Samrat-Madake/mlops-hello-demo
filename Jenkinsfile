
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python hello.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'python monitoring.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mlops-hello .'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'drift_report.html',
                             allowEmptyArchive: true
        }
    }
}
