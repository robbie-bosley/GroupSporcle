import paramiko
import sys, msvcrt, getpass

def put_file(machinename, dirname, filename, data):
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	username=input("Enter your username\n")
	if ("win" in sys.platform):
		#seems to be bug with hiding password in gitbash...
		password=input("Enter your password\n")
	else:
		password=getpass.getpass("Enter your password\n")
	#probably possible to make it remember username and password...
	ssh.connect(machinename, username=username, password=password)
	sftp = ssh.open_sftp()
	try:
		sftp.mkdir(dirname)
	except IOError:
		pass
	f =sftp.open(dirname+'/'+filename,'a')
	f.write(data+'\n')
	f.close()
	ssh.close()
		
	
