import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def connection(ssh_user, ssh_ip, ssh_password):
    try:
        client.connect(ssh_ip, username=ssh_user, password=ssh_password, look_for_keys=False)
        return 'Successful connection'
    except:
        return 'Failed connection'

def update():
    try:

        return 'Successfully updated'
    except:
        return 'Failed update'
