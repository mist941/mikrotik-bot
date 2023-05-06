import paramiko
from messages import prepared_messages

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def connection(ssh_user, ssh_ip, ssh_password):
    client.connect(ssh_ip, username=ssh_user, password=ssh_password, look_for_keys=False)
    transport = client.get_transport()
    if transport is not None and transport.is_active():
        return prepared_messages["successful_connection"]
    else:
        return prepared_messages["failed_connection"]

