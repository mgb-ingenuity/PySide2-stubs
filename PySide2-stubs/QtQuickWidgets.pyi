# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2020 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtQuickWidgets, except for defaults which are replaced by "...".
"""

# Module PySide2.QtQuickWidgets
import PySide2
import typing

import shiboken2 as Shiboken

import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtQml
import PySide2.QtQuick
import PySide2.QtQuickWidgets

class QQuickWidget(PySide2.QtWidgets.QWidget):
    sceneGraphError: PySide2.QtCore.Signal
    statusChanged: PySide2.QtCore.Signal

    Null: QQuickWidget.Status = ...  # 0x0
    SizeViewToRootObject: QQuickWidget.ResizeMode = ...  # 0x0
    Ready: QQuickWidget.Status = ...  # 0x1
    SizeRootObjectToView: QQuickWidget.ResizeMode = ...  # 0x1
    Loading: QQuickWidget.Status = ...  # 0x2
    Error: QQuickWidget.Status = ...  # 0x3

    class ResizeMode(object):
        SizeViewToRootObject: QQuickWidget.ResizeMode = ...  # 0x0
        SizeRootObjectToView: QQuickWidget.ResizeMode = ...  # 0x1

    class Status(object):
        Null: QQuickWidget.Status = ...  # 0x0
        Ready: QQuickWidget.Status = ...  # 0x1
        Loading: QQuickWidget.Status = ...  # 0x2
        Error: QQuickWidget.Status = ...  # 0x3
    @typing.overload
    def __init__(
        self, engine: PySide2.QtQml.QQmlEngine, parent: PySide2.QtWidgets.QWidget
    ) -> None: ...
    @typing.overload
    def __init__(
        self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        source: PySide2.QtCore.QUrl,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
    ) -> None: ...
    def dragEnterEvent(self, arg__1: PySide2.QtGui.QDragEnterEvent) -> None: ...
    def dragLeaveEvent(self, arg__1: PySide2.QtGui.QDragLeaveEvent) -> None: ...
    def dragMoveEvent(self, arg__1: PySide2.QtGui.QDragMoveEvent) -> None: ...
    def dropEvent(self, arg__1: PySide2.QtGui.QDropEvent) -> None: ...
    def engine(self) -> PySide2.QtQml.QQmlEngine: ...
    def errors(self) -> typing.List: ...
    def event(self, arg__1: PySide2.QtCore.QEvent) -> bool: ...
    def focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None: ...
    def focusNextPrevChild(self, next: bool) -> bool: ...
    def focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None: ...
    def format(self) -> PySide2.QtGui.QSurfaceFormat: ...
    def grabFramebuffer(self) -> PySide2.QtGui.QImage: ...
    def hideEvent(self, arg__1: PySide2.QtGui.QHideEvent) -> None: ...
    def initialSize(self) -> PySide2.QtCore.QSize: ...
    def keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None: ...
    def keyReleaseEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None: ...
    def mouseDoubleClickEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None: ...
    def paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None: ...
    def quickWindow(self) -> PySide2.QtQuick.QQuickWindow: ...
    def resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None: ...
    def resizeMode(self) -> PySide2.QtQuickWidgets.QQuickWidget.ResizeMode: ...
    def rootContext(self) -> PySide2.QtQml.QQmlContext: ...
    def rootObject(self) -> PySide2.QtQuick.QQuickItem: ...
    def setClearColor(
        self,
        color: Union[PySide2.QtGui.QColor, PySide2.QtCore.Qt.GlobalColor, str, int],
    ) -> None: ...
    def setContent(
        self,
        url: PySide2.QtCore.QUrl,
        component: PySide2.QtQml.QQmlComponent,
        item: PySide2.QtCore.QObject,
    ) -> None: ...
    def setFormat(self, format: PySide2.QtGui.QSurfaceFormat) -> None: ...
    def setResizeMode(
        self, arg__1: PySide2.QtQuickWidgets.QQuickWidget.ResizeMode
    ) -> None: ...
    def setSource(self, arg__1: PySide2.QtCore.QUrl) -> None: ...
    def showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None: ...
    def sizeHint(self) -> PySide2.QtCore.QSize: ...
    def source(self) -> PySide2.QtCore.QUrl: ...
    def status(self) -> PySide2.QtQuickWidgets.QQuickWidget.Status: ...
    def timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None: ...
    def wheelEvent(self, arg__1: PySide2.QtGui.QWheelEvent) -> None: ...

# eof
