pipeline {
    agent {
        docker {
            image 'docker:19.03-dind'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
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
                sh 'docker pull python:3.9'
                sh 'docker run python:3.9 python TicTacToe.py'
            }
        }
    }
}
