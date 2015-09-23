import nxppy
import time
import os.path,subprocess
from subprocess import STDOUT,PIPE


#def compile_java(java_file):
#    subprocess.check_call(['javac', java_file])

def execute_java(java_file, stdin):
    java_class,ext = os.path.splitext(java_file)
    cmd = ['java', java_class]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout,stderr = proc.communicate(stdin)
    print ("SERVER RESPONSE: " + stdout)	#OUTPUT OF JAVA PROGRAM


mifare = nxppy.Mifare()

# Print card UIDs as they are detected
while True:
    try:
	
	uid = mifare.select()		#REQUIRED
	
	# Read 16 bytes starting from block 
	# each block is 4 bytes, i.e. reads 4 blocks
	block_data = mifare.read_block(4)
 
	print "ID: ", block_data[0:12]

	#compile_java('HttpUtilityTester.java')
	
	execute_java('HttpUtilityTester', block_data[0:12])		
    
    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(1)


