pipeline {
    agent {
        docker {
            image 'python:3.9' // Use an official Python Docker image
        }
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/hagop-h/TicTacToe.git'
            }
        }
        stage('Run Script') {
            steps {
                sh 'python TicTacToe.py'
            }
        }
    }
}
