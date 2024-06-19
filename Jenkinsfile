pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: 'main']],
                          userRemoteConfigs: [[url: 'https://github.com/hagop-h/TicTacToe.git']]])
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build your Docker image
                    docker.build('Dockerfile')
                }
            }
        }
        
        stage('Run TicTacToe') {
            steps {
                script {
                    // Run Docker container interactively with TTY support
                    sh 'docker run --rm -it tictactoe-app'
                }
            }
        }
    }
    
    // Add more stages as needed for testing, deployment, etc.
}
