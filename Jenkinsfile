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
                    // Build your Docker image using Dockerfile
                    try {
                        echo "Building Docker image..."
                        def image = docker.build("tictactoe-app", "-f Dockerfile .")
                        echo "Docker image built successfully: ${image.id}"
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
                    // Run Docker container interactively with TTY support
                    try {
                        echo "Running Docker container..."
                        sh 'docker run --rm tictactoe-app'
                    } catch (Exception e) {
                        println("Error running Docker container: ${e.message}")
                        throw e
                    }
                }
            }
        }
    }
    
    options {
        // Enable parallel execution of stages if applicable
        parallelsAlwaysFailFast()
    }
}
