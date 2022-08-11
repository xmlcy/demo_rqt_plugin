import paramiko

class SSHConnect(object):
    def __init__(self, hostname, username, port = 22, timeout = 30):
        self.hostname = hostname
        self.username = username
        self.port = port
        self.timeout = timeout
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh = ssh

    def connect(self, passwd):
        self.ssh.connect(hostname = self.hostname, port = self.port, username = self.username, password = passwd)
        if self.ssh:
            return True
        else:
            return False

    def exec_cmd(self, cmd):
        if cmd:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            return stderr.readlines()

    def close(self):
        if self.ssh:
            self.ssh.close()


if __name__ == '__main__':
    robot = SSHConnect("192.168.50.240", "robot")
    robot.connect("123456")
    print(robot.exec_cmd("pwd"))
    robot.close()