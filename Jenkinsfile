pipeline {
    agent any
    stages {
        stage('Config') {
		    steps {
		        // we need this stage to setup the venv
		        // and install needed packages (e.g., pybuilder itself)
			    sh ''' python3 -m venv $WORKSPACE/jenkins_venv
			    . $WORKSPACE/jenkins_venv/bin/activate
			    pip install pybuilder'''
            }
	    }
	    stage('Build/Unit Test') {
		    steps {
			    sh '''. $WORKSPACE/jenkins_venv/bin/activate
			    pyb -v'''
		    }
	    }
	}
}
