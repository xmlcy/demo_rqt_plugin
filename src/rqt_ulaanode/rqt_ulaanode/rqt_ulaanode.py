import os
from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from PyQt5.QtWidgets import *
import rclpy
import rospkg
from rclpy.node import Node
from std_msgs.msg import String
from rqt_ulaanode.ssh_connect import SSHConnect

class MyPlugin(Node, Plugin):
    def __init__(self, context):
        super(MyPlugin, self).__init__("rqt_ulaanode")
        super(Plugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('MyPlugin')
        self.ssh = SSHConnect("192.168.50.240", "robot")

        # Process standalone plugin command-line arguments
        from argparse import ArgumentParser
        parser = ArgumentParser()
        # Add argument(s) to the parser.
        parser.add_argument("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print('arguments: ', args)
            print('unknowns: ', unknowns)

        # Create QWidget
        self._widget_connect = QWidget()
        ui_file = os.path.join(os.path.dirname(__file__), '../../../', 'rqt_ulaanode/connect.ui')
        loadUi(ui_file, self._widget_connect)
        # Create QWidget
        self._widget_ulaanode = QWidget()
        ui_file = os.path.join(os.path.dirname(__file__), '../../../', 'rqt_ulaanode/ulaanode.ui')
        loadUi(ui_file, self._widget_ulaanode)
        # Create QStackedWidget
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setWindowTitle('Ulaa Node')
        self.stackedWidget.addWidget(self._widget_connect)
        self.stackedWidget.addWidget(self._widget_ulaanode)
        self.stackedWidget.setCurrentWidget(self._widget_connect)
        # Add widget to the user interface
        context.add_widget(self.stackedWidget)

        self._widget_connect.pushButton_connect.clicked.connect(self.Connect)
    
        self._widget_ulaanode.pushButton_disconnect.clicked.connect(self.Disconnect)
        self._widget_ulaanode.pushButton_stop_all.clicked.connect(self.StopAll)
        self._widget_ulaanode.pushButton_start_all.clicked.connect(self.StartAll)

        self.pub = self.create_publisher(String, "robot_state", 10) # ?????????????????? ????????????

    def shutdown_plugin(self):
        # TODO unregister all publishers here
        self.Disconnect()
        self.destroy_node()
        pass

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    #def trigger_configuration(self):
        # Comment in to signal that the plugin has a way to configure
        # This will enable a setting button (gear icon) in each dock widget title bar
        # Usually used to open a modal configuration dialog

    def Connect(self):
        hostname = self._widget_connect.lineEdit_ip.text()
        username = self._widget_connect.lineEdit_username.text()
        passwd = self._widget_connect.lineEdit_passwd.text()
        self.ssh.set_host(hostname, username)
        if self.ssh.connect(passwd):
            self.stackedWidget.setCurrentWidget(self._widget_ulaanode)
            print('Connect')
        else:
            print('Connect faild')
    def Disconnect(self):
        self.StopAll()
        self.ssh.close()
        self.stackedWidget.setCurrentWidget(self._widget_connect)
        print('Disconnect')
    def StopAll(self):
        print("Stop All")
        self.ssh.exec_cmd("./gui/stopall.sh")
        self._widget_ulaanode.pushButton_ulaahead.setChecked(False)
        self._widget_ulaanode.pushButton_ulaabody.setChecked(False)
        self._widget_ulaanode.pushButton_ulaachassis.setChecked(False)
    def StartAll(self):
        print("Start All")
        self.ssh.exec_cmd("./gui/startall.sh")
        self._widget_ulaanode.pushButton_ulaahead.setChecked(True)
        self._widget_ulaanode.pushButton_ulaabody.setChecked(True)
        self._widget_ulaanode.pushButton_ulaachassis.setChecked(True)
    
