pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your Git repository
                git 'https://github.com/yourusername/your-repo.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build your Docker image
                    docker.build('tictactoe-app')
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
