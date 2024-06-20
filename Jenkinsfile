pipeline {
    agent any
    
    environment {
        DOCKER_HOME = tool name: 'Docker', type: 'Tool'
    }
    
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
                        def dockerCmd = "${DOCKER_HOME}/docker"
                        docker.withRegistry('https://docker.mycorp.com/') {
                            def customImage = docker.build("mycorp/tictactoe-app", "-f Dockerfile .")
                            echo "Docker image built successfully: ${customImage.id}"
                        }
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
                        def dockerCmd = "${DOCKER_HOME}/docker"
                        def customImage = docker.image('mycorp/tictactoe-app')
                        customImage.inside {
                            sh 'python ./TicTacToe.py'
                        }
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
