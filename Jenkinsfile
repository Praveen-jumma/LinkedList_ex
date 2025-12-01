pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Praveen-jumma/LinkedList_ex.git'
            }
        }

        stage('Check Python Version') {
            steps {
                bat """
                    python --version
                    pip --version
                """
            }
        }

        stage('Syntax Check') {
            steps {
                bat """
                    python -m py_compile DEVOPS_EX\\LinkedList.py
                """
            }
        }

        stage('Run Application') {
            steps {
                bat """
                    python DEVOPS_EX\\LinkedList.py
                """
            }
        }

        stage('Archive Artifacts') {
            steps {
                bat "mkdir artifacts"
                bat "copy DEVOPS_EX\\LinkedList.py artifacts\\"
                archiveArtifacts artifacts: 'artifacts/*', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Build Success"
        }
        failure {
            echo "Build Failed"
        }
    }
}
