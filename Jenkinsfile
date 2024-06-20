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
                    try {
                        echo "Building Docker image..."
                        sh 'docker build -t tictactoe-app .'
                        echo "Docker image built successfully"
                    } catch (Exception e) {
                        println("Error building Docker image: ${e.message}")
                        throw e
                    }
                }
            }
        }
        
        stage('Run TicTacToe') {
            steps {
                script {
                    try {
                        echo "Running Docker container..."
                        sh 'docker run --rm tictactoe-app'
                        echo "Docker container executed successfully"
                    } catch (Exception e) {
                        println("Error running Docker container: ${e.message}")
                        throw e
                    }
                }
            }
        }
    }
    
    options {
        parallelsAlwaysFailFast()
    }
}
