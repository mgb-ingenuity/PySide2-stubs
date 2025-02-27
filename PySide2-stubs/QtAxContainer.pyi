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
PySide2.QtAxContainer, except for defaults which are replaced by "...".
"""

# Module PySide2.QtAxContainer
import PySide2
import typing

import shiboken2 as Shiboken

import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtAxContainer

class QAxBase(Shiboken.Object):
    def __init__(self) -> None: ...
    def __lshift__(
        self, s: PySide2.QtCore.QDataStream
    ) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(
        self, s: PySide2.QtCore.QDataStream
    ) -> PySide2.QtCore.QDataStream: ...
    @staticmethod
    def argumentsToList(
        var1: typing.Any,
        var2: typing.Any,
        var3: typing.Any,
        var4: typing.Any,
        var5: typing.Any,
        var6: typing.Any,
        var7: typing.Any,
        var8: typing.Any,
    ) -> typing.List: ...
    def asVariant(self) -> typing.Any: ...
    def classContext(self) -> int: ...
    def className(self) -> bytes: ...
    def clear(self) -> None: ...
    def control(self) -> str: ...
    def disableClassInfo(self) -> None: ...
    def disableEventSink(self) -> None: ...
    def disableMetaObject(self) -> None: ...
    @typing.overload
    def dynamicCall(
        self,
        name: bytes,
        v1: typing.Any = ...,
        v2: typing.Any = ...,
        v3: typing.Any = ...,
        v4: typing.Any = ...,
        v5: typing.Any = ...,
        v6: typing.Any = ...,
        v7: typing.Any = ...,
        v8: typing.Any = ...,
    ) -> typing.Any: ...
    @typing.overload
    def dynamicCall(self, name: bytes, vars: typing.Sequence) -> typing.Any: ...
    def fallbackMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
    def generateDocumentation(self) -> str: ...
    def indexOfVerb(self, verb: str) -> int: ...
    def initializeFrom(self, that: PySide2.QtAxContainer.QAxBase) -> None: ...
    def internalRelease(self) -> None: ...
    def isNull(self) -> bool: ...
    def propertyBag(self) -> typing.Dict: ...
    def propertyWritable(self, arg__1: bytes) -> bool: ...
    def qObject(self) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def querySubObject(
        self,
        name: bytes,
        v1: typing.Any = ...,
        v2: typing.Any = ...,
        v3: typing.Any = ...,
        v4: typing.Any = ...,
        v5: typing.Any = ...,
        v6: typing.Any = ...,
        v7: typing.Any = ...,
        v8: typing.Any = ...,
    ) -> PySide2.QtAxContainer.QAxObject: ...
    @typing.overload
    def querySubObject(
        self, name: bytes, vars: typing.Sequence
    ) -> PySide2.QtAxContainer.QAxObject: ...
    def setClassContext(self, classContext: int) -> None: ...
    def setControl(self, arg__1: str) -> bool: ...
    def setPropertyBag(self, arg__1: typing.Dict) -> None: ...
    def setPropertyWritable(self, arg__1: bytes, arg__2: bool) -> None: ...
    def verbs(self) -> typing.List: ...

class QAxObject(PySide2.QtCore.QObject, PySide2.QtAxContainer.QAxBase):
    exception: PySide2.QtCore.Signal
    propertyChanged: PySide2.QtCore.Signal
    signal: PySide2.QtCore.Signal

    @typing.overload
    def __init__(
        self, c: str, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    def className(self) -> bytes: ...
    def doVerb(self, verb: str) -> bool: ...
    def fallbackMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
    def qObject(self) -> PySide2.QtCore.QObject: ...

class QAxScript(PySide2.QtCore.QObject):
    entered: PySide2.QtCore.Signal
    error: PySide2.QtCore.Signal
    finished: PySide2.QtCore.Signal
    stateChanged: PySide2.QtCore.Signal

    FunctionNames: QAxScript.FunctionFlags = ...  # 0x0
    FunctionSignatures: QAxScript.FunctionFlags = ...  # 0x1

    class FunctionFlags(object):
        FunctionNames: QAxScript.FunctionFlags = ...  # 0x0
        FunctionSignatures: QAxScript.FunctionFlags = ...  # 0x1
    def __init__(
        self, name: str, manager: PySide2.QtAxContainer.QAxScriptManager
    ) -> None: ...
    @typing.overload
    def call(self, function: str, arguments: typing.Sequence) -> typing.Any: ...
    @typing.overload
    def call(
        self,
        function: str,
        v1: typing.Any = ...,
        v2: typing.Any = ...,
        v3: typing.Any = ...,
        v4: typing.Any = ...,
        v5: typing.Any = ...,
        v6: typing.Any = ...,
        v7: typing.Any = ...,
        v8: typing.Any = ...,
    ) -> typing.Any: ...
    def functions(
        self, arg__1: PySide2.QtAxContainer.QAxScript.FunctionFlags = ...
    ) -> typing.List: ...
    def load(self, code: str, language: str = ...) -> bool: ...
    def scriptCode(self) -> str: ...
    def scriptEngine(self) -> PySide2.QtAxContainer.QAxScriptEngine: ...
    def scriptName(self) -> str: ...

class QAxScriptEngine(PySide2.QtAxContainer.QAxObject):
    Uninitialized: QAxScriptEngine.State = ...  # 0x0
    Started: QAxScriptEngine.State = ...  # 0x1
    Connected: QAxScriptEngine.State = ...  # 0x2
    Disconnected: QAxScriptEngine.State = ...  # 0x3
    Closed: QAxScriptEngine.State = ...  # 0x4
    Initialized: QAxScriptEngine.State = ...  # 0x5

    class State(object):
        Uninitialized: QAxScriptEngine.State = ...  # 0x0
        Started: QAxScriptEngine.State = ...  # 0x1
        Connected: QAxScriptEngine.State = ...  # 0x2
        Disconnected: QAxScriptEngine.State = ...  # 0x3
        Closed: QAxScriptEngine.State = ...  # 0x4
        Initialized: QAxScriptEngine.State = ...  # 0x5
    def __init__(
        self, language: str, script: PySide2.QtAxContainer.QAxScript
    ) -> None: ...
    def addItem(self, name: str) -> None: ...
    def hasIntrospection(self) -> bool: ...
    def isValid(self) -> bool: ...
    def scriptLanguage(self) -> str: ...
    def setState(self, st: PySide2.QtAxContainer.QAxScriptEngine.State) -> None: ...
    def state(self) -> PySide2.QtAxContainer.QAxScriptEngine.State: ...

class QAxScriptManager(PySide2.QtCore.QObject):
    error: PySide2.QtCore.Signal

    def __init__(
        self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    def addObject(self, object: PySide2.QtAxContainer.QAxBase) -> None: ...
    @typing.overload
    def call(self, function: str, arguments: typing.Sequence) -> typing.Any: ...
    @typing.overload
    def call(
        self,
        function: str,
        v1: typing.Any = ...,
        v2: typing.Any = ...,
        v3: typing.Any = ...,
        v4: typing.Any = ...,
        v5: typing.Any = ...,
        v6: typing.Any = ...,
        v7: typing.Any = ...,
        v8: typing.Any = ...,
    ) -> typing.Any: ...
    def functions(
        self, arg__1: PySide2.QtAxContainer.QAxScript.FunctionFlags = ...
    ) -> typing.List: ...
    @typing.overload
    def load(
        self, code: str, name: str, language: str
    ) -> PySide2.QtAxContainer.QAxScript: ...
    @typing.overload
    def load(self, file: str, name: str) -> PySide2.QtAxContainer.QAxScript: ...
    @staticmethod
    def registerEngine(name: str, extension: str, code: str = ...) -> bool: ...
    def script(self, name: str) -> PySide2.QtAxContainer.QAxScript: ...
    @staticmethod
    def scriptFileFilter() -> str: ...
    def scriptNames(self) -> typing.List: ...

class QAxSelect(PySide2.QtWidgets.QDialog):
    SandboxingNone: QAxSelect.SandboxingLevel = ...  # 0x0
    SandboxingProcess: QAxSelect.SandboxingLevel = ...  # 0x1
    SandboxingLowIntegrity: QAxSelect.SandboxingLevel = ...  # 0x2

    class SandboxingLevel(object):
        SandboxingNone: QAxSelect.SandboxingLevel = ...  # 0x0
        SandboxingProcess: QAxSelect.SandboxingLevel = ...  # 0x1
        SandboxingLowIntegrity: QAxSelect.SandboxingLevel = ...  # 0x2
    def __init__(
        self,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        flags: PySide2.QtCore.Qt.WindowFlags = ...,
    ) -> None: ...
    def clsid(self) -> str: ...
    def sandboxingLevel(self) -> PySide2.QtAxContainer.QAxSelect.SandboxingLevel: ...

class QAxWidget(PySide2.QtWidgets.QWidget, PySide2.QtAxContainer.QAxBase):
    exception: PySide2.QtCore.Signal
    propertyChanged: PySide2.QtCore.Signal
    signal: PySide2.QtCore.Signal

    @typing.overload
    def __init__(
        self,
        c: str,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        f: PySide2.QtCore.Qt.WindowFlags = ...,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        f: PySide2.QtCore.Qt.WindowFlags = ...,
    ) -> None: ...
    def changeEvent(self, e: PySide2.QtCore.QEvent) -> None: ...
    def className(self) -> bytes: ...
    def clear(self) -> None: ...
    @typing.overload
    def createHostWindow(self, arg__1: bool) -> bool: ...
    @typing.overload
    def createHostWindow(
        self, arg__1: bool, arg__2: PySide2.QtCore.QByteArray
    ) -> bool: ...
    def doVerb(self, verb: str) -> bool: ...
    def fallbackMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
    def minimumSizeHint(self) -> PySide2.QtCore.QSize: ...
    def qObject(self) -> PySide2.QtCore.QObject: ...
    def resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None: ...
    def sizeHint(self) -> PySide2.QtCore.QSize: ...
    def translateKeyEvent(self, message: int, keycode: int) -> bool: ...

# eof
