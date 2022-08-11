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

    def set_host(self, hostname, username):
        self.hostname = hostname
        self.username = username

    def connect(self, passwd):
        self.ssh.connect(hostname = self.hostname, port = self.port, username = self.username, password = passwd)
        if self.ssh:
            return True
        else:
            return False

    def exec_cmd(self, cmd):
        self.transport = self.ssh.get_transport()
        self.channel = self.transport.open_session()
        if cmd:
            '''
            阻塞
            '''
            # stdin, stdout, stderr = self.ssh.exec_command(cmd)
            # return stderr.readlines()
            '''
            非阻塞 无返回值
            '''
            self.channel.exec_command(cmd)

    def close(self):
        if self.ssh:
            self.ssh.close()


if __name__ == '__main__':
    robot = SSHConnect("192.168.50.240", "robot")
    robot.connect("123456")
    print(robot.exec_cmd("./gui/startall.sh"))
    robot.close()