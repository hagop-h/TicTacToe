pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/hagop-h/TicTacToe.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip
                '''
            }
        }
        stage('Run Script') {
            steps {
                sh 'python3 TicTacToe.py'
            }
        }
    }
}
