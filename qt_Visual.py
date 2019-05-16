# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_Visual.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#
import sys
import cv2
import time
import datetime
import threading
import imutils
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QImage, QPixmap, QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(880, 650)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.shot = QtWidgets.QPushButton(self.centralwidget)
        self.shot.setGeometry(QtCore.QRect(750, 140, 93, 35))
        self.shot.setFont(font)
        self.shot.setObjectName("shot")
        self.Recording = QtWidgets.QPushButton(self.centralwidget)
        self.Recording.setGeometry(QtCore.QRect(750, 220, 93, 35))
        self.Recording.setObjectName("Recording")
        self.Recording.setFont(font)
        self.Record_Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Record_Stop.setGeometry(QtCore.QRect(750, 300, 93, 35))
        self.Record_Stop.setObjectName("Record_Stop")
        self.Record_Stop.setFont(font)
        self.Visual_Tracking = QtWidgets.QPushButton(self.centralwidget)
        self.Visual_Tracking.setGeometry(QtCore.QRect(750, 380, 93, 35))
        self.Visual_Tracking.setObjectName("Visual_Tracking")
        self.Visual_Tracking.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 20, 191, 31))
        self.zoomax = QtWidgets.QPushButton(self.centralwidget)
        self.zoomax.setGeometry(QtCore.QRect(750, 460, 93, 35))
        self.zoomax.setObjectName("zoomax")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.DisplayLabel = QtWidgets.QLabel(self.centralwidget)
        self.DisplayLabel.setGeometry(QtCore.QRect(50, 70, 640, 480))
        self.DisplayLabel.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0);")
        self.DisplayLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DisplayLabel.setText("")
        self.DisplayLabel.setObjectName("DisplayLabel")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setGeometry(QtCore.QRect(340, 570, 93, 51))
        self.Open.setFont(font)
        self.Open.setObjectName("Open")
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(490, 570, 93, 51))
        self.Close.setFont(font)
        self.Close.setObjectName("Close")
        self.radioButtonCam = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonCam.setGeometry(QtCore.QRect(170, 570, 115, 19))
        self.radioButtonCam.setFont(font)
        self.radioButtonCam.setObjectName("radioButtonCam")
        self.radioButtonFile = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonFile.setGeometry(QtCore.QRect(170, 600, 115, 19))
        self.radioButtonFile.setFont(font)
        self.radioButtonFile.setObjectName("radioButtonFile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "可视化程序"))
        MainWindow.setWindowIcon(QIcon('自动识别.png'))
        self.shot.setText(_translate("MainWindow", "快照"))
        self.Recording.setText(_translate("MainWindow", "视频录制"))
        self.Record_Stop.setText(_translate("MainWindow", "录制停止"))
        self.Visual_Tracking.setText(_translate("MainWindow", "视觉追踪"))
        self.label.setText(_translate("MainWindow", "可  视  化  界  面"))
        self.Open.setText(_translate("MainWindow", "打开"))
        self.Close.setText(_translate("MainWindow", "关闭"))
        self.radioButtonCam.setText(_translate("MainWindow", "显微相机"))
        self.radioButtonFile.setText(_translate("MainWindow", "本地文件"))
        self.zoomax.setText(_translate("MainWindow", "窗口显示"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1300, 980)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.zoomLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomLabel.sizePolicy().hasHeightForWidth())
        self.zoomLabel.setSizePolicy(sizePolicy)
        self.zoomLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.zoomLabel.setText("")
        self.zoomLabel.setScaledContents(True)
        self.zoomLabel.setObjectName("label")
        self.gridLayout.addWidget(self.zoomLabel, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "可视化界面"))


class Display:
    def __init__(self, ui, mainWnd):
        self.ui = ui
        self.mainWnd = mainWnd

        # 默认视频源为相机
        self.ui.radioButtonCam.setChecked(True)
        self.isCamera = True

        # 按钮初始化
        self.ui.shot.setEnabled(False)
        self.ui.Recording.setEnabled(False)
        self.ui.Record_Stop.setEnabled(False)
        self.ui.Visual_Tracking.setEnabled(False)

        # 信号槽设置
        ui.Open.clicked.connect(self.Open)
        ui.Close.clicked.connect(self.Close)
        ui.radioButtonCam.clicked.connect(self.radioButtonCam)
        ui.radioButtonFile.clicked.connect(self.radioButtonFile)
        ui.shot.clicked.connect(self.shot)
        ui.Recording.clicked.connect(self.Recording)
        ui.Record_Stop.clicked.connect(self.recordStop)
        ui.Visual_Tracking.clicked.connect(self.VisualTracking)

        # 创建一个关闭事件并设为未触发
        self.stopEvent = threading.Event()
        self.stopEvent.clear()

        # 创建一个拍照事件并设为未触发
        self.shotEvent = threading.Event()
        self.shotEvent.clear()

        # 创建一个视频录制事件并设为未触发
        self.recordingEvent = threading.Event()
        self.recordingEvent.clear()

        # 创建一个录制停止事件并设为未触发
        self.recordstopEvent = threading.Event()
        self.recordstopEvent.clear()

        # 创建一个视觉追踪算法事件并设为未触发
        self.VisualTrackingEvent = threading.Event()
        self.VisualTrackingEvent.clear()

        self.Open()

    def radioButtonCam(self):
        if self.cap.isOpened():
            self.ui.Close.setEnabled(False)
            self.ui.Open.setEnabled(True)
            self.VisualTrackingEvent.clear()
            self.cap.release()
            cv2.destroyAllWindows()
            self.ui.DisplayLabel.clear()
        self.isCamera = True

    def radioButtonFile(self):
        if self.cap.isOpened():
            self.ui.Close.setEnabled(False)
            self.ui.Open.setEnabled(True)
            self.VisualTrackingEvent.clear()
            self.cap.release()
            cv2.destroyAllWindows()
            self.ui.DisplayLabel.clear()
        self.isCamera = False

    def Open(self):
        if not self.isCamera:
            self.fileName, self.fileType = QFileDialog.getOpenFileName(
                self.mainWnd, 'Choose file', '', '*.mp4;;*.avi;;All Files(*)')
            if self.fileName:
                self.cap = cv2.VideoCapture(self.fileName)
                self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
                # 创建视频显示线程
                th = threading.Thread(target=self.Display)
                th.start()
                self.ui.shot.setEnabled(True)
                self.ui.Recording.setEnabled(True)
                self.ui.Record_Stop.setEnabled(False)
                self.ui.Visual_Tracking.setEnabled(True)
                self.ui.zoomax.setEnabled(True)
        else:
            self.cap = cv2.VideoCapture(0)
            # self.cap.set(3, 2048)
            # self.cap.set(4, 1536)
            # self.cap.set(cv2.CAP_PROP_FPS, 40)
            # 创建视频显示线程
            th = threading.Thread(target=self.Display)
            th.start()
            self.ui.shot.setEnabled(True)
            self.ui.Recording.setEnabled(True)
            self.ui.Record_Stop.setEnabled(False)
            self.ui.Visual_Tracking.setEnabled(True)
            self.ui.zoomax.setEnabled(True)

    def Close(self):
        # 关闭事件设为触发，关闭视频播放
        self.stopEvent.set()

    def Display(self):
        self.ui.Open.setEnabled(False)
        self.ui.Close.setEnabled(True)

        while self.cap.isOpened():
            success, frame = self.cap.read()
            # 如果不能抓取到一帧，说明到了视频的结尾
            if not success:
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.ui.DisplayLabel.clear()
                self.ui.Close.setEnabled(False)
                self.ui.Open.setEnabled(True)
                self.VisualTrackingEvent.clear()
                self.cap.release()
                cv2.destroyAllWindows()
                break

            # 快照
            if self.shotEvent.is_set():
                cv2.imwrite("./photos/{}.png".format(
                    time.strftime("%Y%m%d%H%M%S", time.localtime())),
                            imutils.resize(frame, width=2592, height=1944))
                self.shotEvent.clear()

            # 视频录制
            if self.recordingEvent.is_set():
                self.vidout.write(imutils.resize(frame, width=2048, height=1536))
                if self.recordstopEvent.is_set():
                    self.vidout.release()
                    self.recordingEvent.clear()
                    self.recordstopEvent.clear()

            # 运动检测
            if self.VisualTrackingEvent.is_set():
                text = "Normal"
                # 调整该帧的大小，转换为灰阶图像并且对其进行高斯模糊
                frame = imutils.resize(frame, width=640, height=480)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)
                # 如果第一帧是None，对其进行初始化
                if self.firstFrame is None:
                    self.firstFrame = gray
                    continue
                # 计算当前帧和第一帧的不同
                frameDelta = cv2.absdiff(self.firstFrame, gray)
                thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
                # 扩展阀值图像填充孔洞，然后找到阀值图像上的轮廓
                thresh = cv2.dilate(thresh, None, iterations=2)
                (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                contours = 0
                img_area = frame.shape
                # 遍历轮廓
                for c in cnts:
                    # if the contour is too small, ignore it
                    contours = contours + cv2.contourArea(c)
                    if cv2.contourArea(c) < 150:
                        continue
                    # 计算轮廓的边界框，在当前帧中画出该框
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    text = "Occupied"
                # draw the text and timestamp on the frame
                # 在当前帧上写文字以及时间戳
                cv2.putText(frame, "Status: {}, Area: {}%".format(text, str(
                    (contours / (img_area[0] * img_area[1])) * 100)), (15, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                            (15, frame.shape[0] - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                if child.isVisible():
                    child.child.zoomLabel.setPixmap(QPixmap.fromImage(img))
                self.ui.DisplayLabel.setPixmap(QPixmap.fromImage(img))
            else:
                frame = imutils.resize(frame, width=640, height=480)
                # RGB转BGR
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                            (15, frame.shape[0] - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
                img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                if child.isVisible():
                    child.child.zoomLabel.setPixmap(QPixmap.fromImage(img))
                self.ui.DisplayLabel.setPixmap(QPixmap.fromImage(img))

            if self.isCamera:
                cv2.waitKey(1)
            else:
                cv2.waitKey(int(1000 / self.frameRate))

            # 判断关闭事件是否已触发
            if self.stopEvent.is_set():
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.ui.DisplayLabel.clear()
                self.ui.Close.setEnabled(False)
                self.ui.Open.setEnabled(True)
                self.VisualTrackingEvent.clear()
                self.cap.release()
                cv2.destroyAllWindows()
                self.ui.shot.setEnabled(False)
                self.ui.Recording.setEnabled(False)
                self.ui.Record_Stop.setEnabled(False)
                self.ui.Visual_Tracking.setEnabled(False)
                self.ui.zoomax.setEnabled(False)
                break

    def shot(self):
        self.shotEvent.set()

    def Recording(self):
        self.ui.Recording.setEnabled(False)
        self.ui.Record_Stop.setEnabled(True)
        # 录制视频大小设置，获取帧宽度，获取帧高度
        # sz = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        sz = (2048, 1536)
        fps = 40
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.vidout = cv2.VideoWriter("./videos/Video{}.mp4".format(
            time.strftime("%Y%m%d%H%M%S", time.localtime())), fourcc, fps, sz, True)
        self.recordingEvent.set()

    def recordStop(self):
        self.ui.Recording.setEnabled(True)
        self.ui.Record_Stop.setEnabled(False)
        self.recordstopEvent.set()

    def VisualTracking(self):
        self.firstFrame = None
        if self.VisualTrackingEvent.is_set():
            self.VisualTrackingEvent.clear()
        else:
            self.VisualTrackingEvent.set()


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)


class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = parentWindow()
    child = childWindow()
    zoom = window.main_ui.zoomax
    zoom.clicked.connect(child.show)
    display = Display(window.main_ui, window)
    window.show()
    sys.exit(app.exec_())
