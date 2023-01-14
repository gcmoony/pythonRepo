from paramiko import SSHClient, AutoAddPolicy, HostKeys
import getpass
import time

# Create the SSH client
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())

hosts = []
commands = []

# Get the hostnames in the text file
with open("./devices.txt") as f:
    for line in f:
        hosts.append(line.strip())


# Get the commands to run in the text file
with open("./commands_raw.txt") as f:
    for line in f:
        # To ignore the Cisco comments and empty new lines
        if not (line.startswith("!") or line.startswith("\n")):
            commands.append(line.strip() + "\n")



username = getpass.getuser()
password = getpass.getpass("Please enter your password: ")
print("Connecting, please wait...")


for host in hosts:
    # Connect to a device
    client.connect(
        hostname = host,
        username = username, 
        password = password, 
        allow_agent = False,
        look_for_keys = False)

    # Start the shell to send commands
    device_access = client.invoke_shell()
    for command in commands:
        device_access.send(command)
        time.sleep(3)
    
    # Start device info display
    print("#"*5, host, "#"*5)
    output = device_access.recv(65000)
    print(output.decode("utf8"), "\n\n")

    # Close current ssh session
    client.close()


print("#"*5, " Program Completed! ", "#"*5, "\n")