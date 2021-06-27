import paramiko

def ssh_command(ip, port, user, passwd, cmd):
	# See http://docs.paramiko.org/en/stable/api/client.html#paramiko.client.SSHClient.
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, port=port, username=user, password=passwd)

	_, stdout, stderr = client.exec_command(cmd)
	output = stdout.readlines() + stderr.readlines()
	if output:
		print('--- Output ---')
		for line in output:
			print(line.strip())

	client.close()

if __name__ == '__main__':
	import getpass
	user = input('Username: ')
	# See https://docs.python.org/3/library/getpass.html.
	password = getpass.getpass()

	ip = input('Enter server IP: ')
	port = input('Enter port or <CR>: ') or 22
	cmd = input('Enter command or <CR>: ') or 'id'
	ssh_command(ip, port, user, password, cmd)
