from enum import Enum
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
from img.PicGraphic import PicGraphic


class ButtStyle(Enum):
    ButtNorm = 0,
    ButtPress = 1,
    ButtRelease = 2,
    ButtEnter = 3,
    ButtLeave = 4,


class ImageButtonGraphics(PicGraphic):
    leftClick = pyqtSignal()
    rightClick = pyqtSignal()
    buttonPicture = None
    pressPicture = None
    releasePicture = None
    enterPicture = None
    leavePicture = None
    buttonPictureOrigin = None
    pressPictureOrigin = None
    releasePictureOrigin = None
    enterPictureOrigin = None
    leavePictureOrigin = None
    isAnimateEnable = False
    currentButtStyle = None

    def __init__(self, buttNormPic, x, y, animeGeomOn, animeOpacOn, parent):
        """
        初始化
        :param buttNormPic: QPixmap 按钮图片
        :param x: x位置
        :param y: y位置
        :param animeGeomOn: bool 几何动画开关
        :param animeOpacOn: bool 透明度动画开关
        :param parent:
        """
        super(ImageButtonGraphics, self).__init__(buttNormPic, x, y, animeGeomOn, animeOpacOn, parent)
        self.setAcceptHoverEvents(True)
        self.setAcceptDrops(True)
        self.buttonPicture = QPixmap(buttNormPic)
        self.pressPicture = QPixmap(buttNormPic)
        self.releasePicture = QPixmap(buttNormPic)
        self.enterPicture = QPixmap(buttNormPic)
        self.leavePicture = QPixmap(buttNormPic)
        self.currentButtStyle = ButtStyle.ButtNorm

    def setAllButtImage(self, buttNorm, buttEnter, buttPress):
        """
        设置三态按钮图片
        :param buttNorm: QPixmap
        :param buttEnter: QPixmap
        :param buttPress: QPixmap
        :return:
        """
        self.setButtonPicture(buttNorm)
        self.setEnterPicture(buttEnter)
        self.setLeavePicture(buttNorm)
        self.setPressPicture(buttPress)
        self.setReleasePicture(buttEnter)

    def setButtonPicture(self, pic):
        """
        设置普通态按钮图片
        :param pic: QPixmap
        :return:
        """
        self.buttonPicture = pic

    def setEnterPicture(self, pic):
        """
        设置进入态态按钮图片
        :param pic: QPixmap
        :return:
        """
        self.enterPicture = pic

    def setLeavePicture(self, pic):
        """
        设置离开态态按钮图片
        :param pic: QPixmap
        :return:
        """
        self.leavePicture = pic

    def setPressPicture(self, pic):
        """
        设置按下态按钮图片
        :param pic: QPixmap
        :return:
        """
        self.pressPicture = pic

    def setReleasePicture(self, pic):
        """
        设置释放态按钮图片
        :param pic: QPixmap
        :return:
        """
        self.releasePicture = pic

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setPixmap(self.pressPicture)
            self.currentButtStyle = ButtStyle.ButtPress

    def mouseReleaseEvent(self, event):
        if (event.button() & Qt.LeftButton) == 1:
            self.leftClick.emit()
            self.setPixmap(self.enterPicture)
            self.currentButtStyle = ButtStyle.ButtRelease
        elif (event.button() & Qt.RightButton) == 1:
            self.rightClick.emit()

    def hoverEnterEvent(self, event):
        QGraphicsPixmapItem.hoverEnterEvent(event)
        self.setPixmap(self.enterPicture)
        self.currentButtStyle = ButtStyle.ButtEnter

    def hoverLeaveEvent(self, event):
        QGraphicsPixmapItem.hoverLeaveEvent(event)
        self.setPixmap(self.leavePicture)
        self.currentButtStyle = ButtStyle.ButtLeave
