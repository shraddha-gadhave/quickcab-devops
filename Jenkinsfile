pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/shraddha-gadhave/quickcab-devops.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building QuickCab application...'
                sh 'docker build -t quickcab-devops .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'docker run --rm quickcab-devops pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'QuickCab deployment stage completed.'
            }
        }
    }
}
