import paramiko

try:

    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('localhost',
                    username='developer',
                    password='4linux',
                    port='2222')

except Exception as e:

    print(f'Erro de conexão: {e}')
    exit()

stdin, stdout, stderr = client.exec_command('ls -la')

if stdout.channel.recv_exit_status() == 0:

    print(stdout.read().decode('utf-8'))

else:
    
    print(stderr.read().decode('utf-8'))