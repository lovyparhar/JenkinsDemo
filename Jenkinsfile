pipeline { 
agent any
    stages {
        stage('Fetch the files') {
            steps {
                git 'https://github.com/lovyparhar/JenkinsDemo'
            }
        }

        stage('Run function in main') {
            steps {
		sh "chmod u+x main.py"
                sh "python3 main.py"
            }
        }
        
        stage('Run tests for the function') {
            steps {
		sh "chmod u+x tests.py"
                sh "python3 tests.py"
            }
        }
    } 
}
