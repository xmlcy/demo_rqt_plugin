import os
from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from PyQt5.QtWidgets import *
import rclpy
import rospkg
from rclpy.node import Node
from std_msgs.msg import String

class MyPlugin(Node, Plugin):
    def __init__(self, context):
        super(MyPlugin, self).__init__("rqt_ulaactrl")
        super(Plugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('MyPlugin')

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
        self._widget_ulaahead = QWidget()
        ui_file = os.path.join(os.path.dirname(__file__), '../../../', 'rqt_ulaactrl/ulaahead.ui')
        loadUi(ui_file, self._widget_ulaahead)
        self._widget_ulaahead.setObjectName('MyPluginUi')
        self._widget_ulaahead.setWindowTitle('Ulaa Ctrl')
        if context.serial_number() > 1:
            self._widget_ulaahead.setWindowTitle(self._widget_ulaahead.windowTitle() + (' (%d)' % context.serial_number()))
        # Create QWidget
        self._widget_menu = QWidget()
        ui_file = os.path.join(os.path.dirname(__file__), '../../../', 'rqt_ulaactrl/menu.ui')
        loadUi(ui_file, self._widget_menu)
        self._widget_menu.setObjectName('MyPluginMenu')
        self._widget_menu.setWindowTitle('Ulaa Menu')
        if context.serial_number() > 1:
            self._widget_menu.setWindowTitle(self._widget_menu.windowTitle() + (' (%d)' % context.serial_number()))
        # self._widget_menu.show()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setWindowTitle('Ulaa Ctrl')
        self.stackedWidget.addWidget(self._widget_ulaahead)
        self.stackedWidget.addWidget(self._widget_menu)
        self.stackedWidget.setCurrentWidget(self._widget_menu)
        # Add widget to the user interface
        context.add_widget(self.stackedWidget)

        # TODO: 换成组合
        self._widget_ulaahead.pushButton_0.clicked.connect(self.pushButton_0_Clicked)
        self._widget_ulaahead.pushButton_1.clicked.connect(self.pushButton_1_Clicked)
        self._widget_ulaahead.pushButton_2.clicked.connect(self.pushButton_2_Clicked)
        self._widget_ulaahead.pushButton_3.clicked.connect(self.pushButton_3_Clicked)
        self._widget_ulaahead.pushButton_4.clicked.connect(self.pushButton_4_Clicked)
        self._widget_ulaahead.pushButton_5.clicked.connect(self.pushButton_5_Clicked)
        self._widget_ulaahead.pushButton_6.clicked.connect(self.pushButton_6_Clicked)
        self._widget_ulaahead.pushButton_7.clicked.connect(self.pushButton_7_Clicked)
        self._widget_ulaahead.pushButton_8.clicked.connect(self.pushButton_8_Clicked)
        self._widget_ulaahead.pushButton_9.clicked.connect(self.pushButton_9_Clicked)
        self._widget_ulaahead.pushButton_10.clicked.connect(self.pushButton_10_Clicked)
        self._widget_ulaahead.pushButton_11.clicked.connect(self.pushButton_11_Clicked)
        self._widget_ulaahead.pushButton_12.clicked.connect(self.pushButton_12_Clicked)
        self._widget_ulaahead.pushButton_13.clicked.connect(self.pushButton_13_Clicked)
        self._widget_ulaahead.pushButton_14.clicked.connect(self.pushButton_14_Clicked)
        self._widget_ulaahead.pushButton_15.clicked.connect(self.pushButton_15_Clicked)
        self._widget_ulaahead.pushButton_16.clicked.connect(self.pushButton_16_Clicked)

        self._widget_ulaahead.pushButton_w1.clicked.connect(self.pushButton_w1_Clicked)
        self._widget_ulaahead.pushButton_w2.clicked.connect(self.pushButton_w2_Clicked)
        self._widget_ulaahead.pushButton_w3.clicked.connect(self.pushButton_w3_Clicked)
        self._widget_ulaahead.pushButton_w4.clicked.connect(self.pushButton_w4_Clicked)

        self._widget_ulaahead.pushButton_menu.clicked.connect(self.pushButton_menu_Clicked)
    
        self.pub = self.create_publisher(String, "action", 10) # 解析动作指令 发布消息
        self.msg_pub = String()
        self.msg_pub.data = "你好ulaa"
        self.pub.publish(self.msg_pub)

        self._widget_menu.pushButton_ulaahead.clicked.connect(self.pushButton_ulaahead_Clicked)

    def shutdown_plugin(self):
        # TODO unregister all publishers here
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

    def PubMsg(self, data):
        self.msg_pub.data = data
        self.pub.publish(self.msg_pub)

    def pushButton_0_Clicked(self):
        print("pushButton_0_Clicked")
        self.PubMsg("初始化")
    def pushButton_1_Clicked(self):
        print("pushButton_1_Clicked")
        self.PubMsg("单次眨眼")
    def pushButton_2_Clicked(self):
        print("pushButton_2_Clicked")
        self.PubMsg("单纯摇头（否定）")
    def pushButton_3_Clicked(self):
        print("pushButton_3_Clicked")
        self.PubMsg("单次点头（肯定）")
    def pushButton_4_Clicked(self):
        print("pushButton_4_Clicked")
        self.PubMsg("皱眉摇头（强烈否定）")
    def pushButton_5_Clicked(self):
        print("pushButton_5_Clicked")
        self.PubMsg("皱眉瞪眼（生气）")
    def pushButton_6_Clicked(self):
        print("pushButton_6_Clicked")
        self.PubMsg("挑眉大眼（惊奇）")
    def pushButton_7_Clicked(self):
        print("pushButton_7_Clicked")
        self.PubMsg("挑眉大眼张嘴（惊吓）")
    def pushButton_8_Clicked(self):
        print("pushButton_8_Clicked")
        self.PubMsg("摇头皱眉（困惑）")
    def pushButton_9_Clicked(self):
        print("pushButton_9_Clicked")
        self.PubMsg("东张希望")
    def pushButton_10_Clicked(self):
        print("pushButton_10_Clicked")
        self.PubMsg("思考反应（短时）")
    def pushButton_11_Clicked(self):
        print("pushButton_11_Clicked")
        self.PubMsg("挤眉弄眼（调戏）")
    def pushButton_12_Clicked(self):
        print("pushButton_12_Clicked")
        self.PubMsg("莞尔一笑")
    def pushButton_13_Clicked(self):
        print("pushButton_13_Clicked")
        self.PubMsg("综合动作")
    def pushButton_14_Clicked(self):
        print("pushButton_14_Clicked")
        self.PubMsg("收到")
    def pushButton_15_Clicked(self):
        print("pushButton_15_Clicked")
        self.PubMsg("说话短")
    def pushButton_16_Clicked(self):
        print("pushButton_16_Clicked")
        self.PubMsg("说话长")

    def pushButton_w1_Clicked(self):
        print("pushButton_w1_Clicked")
        self.PubMsg("微表情一")
    def pushButton_w2_Clicked(self):
        print("pushButton_w2_Clicked")
        self.PubMsg("微表情二")
    def pushButton_w3_Clicked(self):
        print("pushButton_w3_Clicked")
        self.PubMsg("微表情三")
    def pushButton_w4_Clicked(self):
        print("pushButton_w4_Clicked")
        self.PubMsg("微表情四")

    def pushButton_menu_Clicked(self):
        self.stackedWidget.setCurrentWidget(self._widget_menu)
    def pushButton_ulaahead_Clicked(self):
        self.stackedWidget.setCurrentWidget(self._widget_ulaahead)
