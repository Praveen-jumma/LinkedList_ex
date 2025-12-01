pipeline {
    agent any

    environment {
        PYTHON = "/usr/bin/python3"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Praveen-jumma/LinkedList_ex.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '''
                    python3 --version
                    pip3 --version || true
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    if [ -f requirements.txt ]; then
                        pip3 install -r requirements.txt
                    else
                        echo "No requirements.txt found. Skipping"
                    fi
                '''
            }
        }

        stage('Run Code Quality Checks') {
            steps {
                sh '''
                    echo "Running syntax check..."
                    python3 -m py_compile DEVOPS_EX/LinkedList.py
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                    echo "Executing LinkedList.py"
                    python3 DEVOPS_EX/LinkedList.py || true
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                sh '''
                    mkdir -p artifacts
                    cp DEVOPS_EX/LinkedList.py artifacts/
                '''
                archiveArtifacts artifacts: 'artifacts/*', fingerprint: true
            }
        }

        stage('Deploy (Optional)') {
            when {
                expression { return false }   
            }
            steps {
                sh "echo Deploy step placeholder"
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully."
        }
        failure {
            echo "Pipeline failed. Fix your code."
        }
    }
}

