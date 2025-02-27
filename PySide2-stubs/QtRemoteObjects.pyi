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
PySide2.QtRemoteObjects, except for defaults which are replaced by "...".
"""

# Module PySide2.QtRemoteObjects
import PySide2
import typing

import shiboken2 as Shiboken

import PySide2.QtCore
import PySide2.QtRemoteObjects

class QAbstractItemModelReplica(PySide2.QtCore.QAbstractItemModel):
    initialized: PySide2.QtCore.Signal

    def availableRoles(self) -> typing.List: ...
    def columnCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def data(
        self, index: PySide2.QtCore.QModelIndex, role: int = ...
    ) -> typing.Any: ...
    def flags(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.Qt.ItemFlags: ...
    def hasChildren(self, parent: PySide2.QtCore.QModelIndex = ...) -> bool: ...
    def hasData(self, index: PySide2.QtCore.QModelIndex, role: int) -> bool: ...
    def headerData(
        self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int
    ) -> typing.Any: ...
    def index(
        self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = ...
    ) -> PySide2.QtCore.QModelIndex: ...
    def isInitialized(self) -> bool: ...
    @typing.overload
    def parent(self) -> PySide2.QtCore.QObject: ...
    @typing.overload
    def parent(
        self, index: PySide2.QtCore.QModelIndex
    ) -> PySide2.QtCore.QModelIndex: ...
    def roleNames(self) -> typing.Dict: ...
    def rowCount(self, parent: PySide2.QtCore.QModelIndex = ...) -> int: ...
    def selectionModel(self) -> PySide2.QtCore.QItemSelectionModel: ...
    def setData(
        self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = ...
    ) -> bool: ...

class QRemoteObjectAbstractPersistedStore(PySide2.QtCore.QObject):
    def __init__(
        self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    def restoreProperties(
        self, repName: str, repSig: PySide2.QtCore.QByteArray
    ) -> typing.List: ...
    def saveProperties(
        self, repName: str, repSig: PySide2.QtCore.QByteArray, values: typing.Sequence
    ) -> None: ...

class QRemoteObjectDynamicReplica(PySide2.QtRemoteObjects.QRemoteObjectReplica):
    initialized: PySide2.QtCore.Signal
    notified: PySide2.QtCore.Signal
    stateChanged: PySide2.QtCore.Signal

    ...

class QRemoteObjectHost(PySide2.QtRemoteObjects.QRemoteObjectHostBase):
    hostUrlChanged: PySide2.QtCore.Signal

    @typing.overload
    def __init__(
        self, address: PySide2.QtCore.QUrl, parent: PySide2.QtCore.QObject
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        address: PySide2.QtCore.QUrl,
        registryAddress: PySide2.QtCore.QUrl = ...,
        allowedSchemas: PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas = ...,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ) -> None: ...
    @typing.overload
    def __init__(
        self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    def hostUrl(self) -> PySide2.QtCore.QUrl: ...
    def setHostUrl(
        self,
        hostAddress: PySide2.QtCore.QUrl,
        allowedSchemas: PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas = ...,
    ) -> bool: ...

class QRemoteObjectHostBase(PySide2.QtRemoteObjects.QRemoteObjectNode):
    BuiltInSchemasOnly: QRemoteObjectHostBase.AllowedSchemas = ...  # 0x0
    AllowExternalRegistration: QRemoteObjectHostBase.AllowedSchemas = ...  # 0x1

    class AllowedSchemas(object):
        BuiltInSchemasOnly: QRemoteObjectHostBase.AllowedSchemas = ...  # 0x0
        AllowExternalRegistration: QRemoteObjectHostBase.AllowedSchemas = ...  # 0x1
    def addHostSideConnection(self, ioDevice: PySide2.QtCore.QIODevice) -> None: ...
    def disableRemoting(self, remoteObject: PySide2.QtCore.QObject) -> bool: ...
    @typing.overload
    def enableRemoting(
        self,
        model: PySide2.QtCore.QAbstractItemModel,
        name: str,
        roles: typing.List,
        selectionModel: typing.Optional[PySide2.QtCore.QItemSelectionModel] = ...,
    ) -> bool: ...
    @typing.overload
    def enableRemoting(
        self, object: PySide2.QtCore.QObject, name: str = ...
    ) -> bool: ...
    def hostUrl(self) -> PySide2.QtCore.QUrl: ...
    def proxy(
        self, registryUrl: PySide2.QtCore.QUrl, hostUrl: PySide2.QtCore.QUrl = ...
    ) -> bool: ...
    def reverseProxy(self) -> bool: ...
    def setHostUrl(
        self,
        hostAddress: PySide2.QtCore.QUrl,
        allowedSchemas: PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas = ...,
    ) -> bool: ...
    def setName(self, name: str) -> None: ...

class QRemoteObjectNode(PySide2.QtCore.QObject):
    error: PySide2.QtCore.Signal
    heartbeatIntervalChanged: PySide2.QtCore.Signal
    remoteObjectAdded: PySide2.QtCore.Signal
    remoteObjectRemoved: PySide2.QtCore.Signal

    NoError: QRemoteObjectNode.ErrorCode = ...  # 0x0
    RegistryNotAcquired: QRemoteObjectNode.ErrorCode = ...  # 0x1
    RegistryAlreadyHosted: QRemoteObjectNode.ErrorCode = ...  # 0x2
    NodeIsNoServer: QRemoteObjectNode.ErrorCode = ...  # 0x3
    ServerAlreadyCreated: QRemoteObjectNode.ErrorCode = ...  # 0x4
    UnintendedRegistryHosting: QRemoteObjectNode.ErrorCode = ...  # 0x5
    OperationNotValidOnClientNode: QRemoteObjectNode.ErrorCode = ...  # 0x6
    SourceNotRegistered: QRemoteObjectNode.ErrorCode = ...  # 0x7
    MissingObjectName: QRemoteObjectNode.ErrorCode = ...  # 0x8
    HostUrlInvalid: QRemoteObjectNode.ErrorCode = ...  # 0x9
    ProtocolMismatch: QRemoteObjectNode.ErrorCode = ...  # 0xa
    ListenFailed: QRemoteObjectNode.ErrorCode = ...  # 0xb

    class ErrorCode(object):
        NoError: QRemoteObjectNode.ErrorCode = ...  # 0x0
        RegistryNotAcquired: QRemoteObjectNode.ErrorCode = ...  # 0x1
        RegistryAlreadyHosted: QRemoteObjectNode.ErrorCode = ...  # 0x2
        NodeIsNoServer: QRemoteObjectNode.ErrorCode = ...  # 0x3
        ServerAlreadyCreated: QRemoteObjectNode.ErrorCode = ...  # 0x4
        UnintendedRegistryHosting: QRemoteObjectNode.ErrorCode = ...  # 0x5
        OperationNotValidOnClientNode: QRemoteObjectNode.ErrorCode = ...  # 0x6
        SourceNotRegistered: QRemoteObjectNode.ErrorCode = ...  # 0x7
        MissingObjectName: QRemoteObjectNode.ErrorCode = ...  # 0x8
        HostUrlInvalid: QRemoteObjectNode.ErrorCode = ...  # 0x9
        ProtocolMismatch: QRemoteObjectNode.ErrorCode = ...  # 0xa
        ListenFailed: QRemoteObjectNode.ErrorCode = ...  # 0xb
    @typing.overload
    def __init__(
        self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        registryAddress: PySide2.QtCore.QUrl,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ) -> None: ...
    def acquireDynamic(
        self, name: str
    ) -> PySide2.QtRemoteObjects.QRemoteObjectDynamicReplica: ...
    def acquireModel(
        self, name: str
    ) -> PySide2.QtRemoteObjects.QAbstractItemModelReplica: ...
    def addClientSideConnection(self, ioDevice: PySide2.QtCore.QIODevice) -> None: ...
    def connectToNode(self, address: PySide2.QtCore.QUrl) -> bool: ...
    def heartbeatInterval(self) -> int: ...
    def instances(self, typeName: str) -> typing.List: ...
    def lastError(self) -> PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode: ...
    def persistedStore(
        self,
    ) -> PySide2.QtRemoteObjects.QRemoteObjectAbstractPersistedStore: ...
    def registry(self) -> PySide2.QtRemoteObjects.QRemoteObjectRegistry: ...
    def registryUrl(self) -> PySide2.QtCore.QUrl: ...
    def setHeartbeatInterval(self, interval: int) -> None: ...
    def setName(self, name: str) -> None: ...
    def setPersistedStore(
        self,
        persistedStore: PySide2.QtRemoteObjects.QRemoteObjectAbstractPersistedStore,
    ) -> None: ...
    def setRegistryUrl(self, registryAddress: PySide2.QtCore.QUrl) -> bool: ...
    def timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None: ...
    def waitForRegistry(self, timeout: int = ...) -> bool: ...

class QRemoteObjectPendingCall(Shiboken.Object):
    NoError: QRemoteObjectPendingCall.Error = ...  # 0x0
    InvalidMessage: QRemoteObjectPendingCall.Error = ...  # 0x1

    class Error(object):
        NoError: QRemoteObjectPendingCall.Error = ...  # 0x0
        InvalidMessage: QRemoteObjectPendingCall.Error = ...  # 0x1
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(
        self, other: PySide2.QtRemoteObjects.QRemoteObjectPendingCall
    ) -> None: ...
    def error(self) -> PySide2.QtRemoteObjects.QRemoteObjectPendingCall.Error: ...
    @staticmethod
    def fromCompletedCall(
        returnValue: typing.Any,
    ) -> PySide2.QtRemoteObjects.QRemoteObjectPendingCall: ...
    def isFinished(self) -> bool: ...
    def returnValue(self) -> typing.Any: ...
    def waitForFinished(self, timeout: int = ...) -> bool: ...

class QRemoteObjectPendingCallWatcher(
    PySide2.QtCore.QObject, PySide2.QtRemoteObjects.QRemoteObjectPendingCall
):
    finished: PySide2.QtCore.Signal

    def __init__(
        self,
        call: PySide2.QtRemoteObjects.QRemoteObjectPendingCall,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ) -> None: ...
    def isFinished(self) -> bool: ...
    def waitForFinished(self) -> None: ...

class QRemoteObjectRegistry(PySide2.QtRemoteObjects.QRemoteObjectReplica):
    remoteObjectAdded: PySide2.QtCore.Signal
    remoteObjectRemoved: PySide2.QtCore.Signal

    def addSource(self, entry: typing.Tuple) -> None: ...
    def initialize(self) -> None: ...
    def pushToRegistryIfNeeded(self) -> None: ...
    @staticmethod
    def registerMetatypes() -> None: ...
    def removeSource(self, entry: typing.Tuple) -> None: ...
    def sourceLocations(self) -> typing.Dict: ...

class QRemoteObjectRegistryHost(PySide2.QtRemoteObjects.QRemoteObjectHostBase):
    def __init__(
        self,
        registryAddress: PySide2.QtCore.QUrl = ...,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ) -> None: ...
    def setRegistryUrl(self, registryUrl: PySide2.QtCore.QUrl) -> bool: ...

class QRemoteObjectReplica(PySide2.QtCore.QObject):
    initialized: PySide2.QtCore.Signal
    notified: PySide2.QtCore.Signal
    stateChanged: PySide2.QtCore.Signal

    Uninitialized: QRemoteObjectReplica.State = ...  # 0x0
    Default: QRemoteObjectReplica.State = ...  # 0x1
    Valid: QRemoteObjectReplica.State = ...  # 0x2
    Suspect: QRemoteObjectReplica.State = ...  # 0x3
    SignatureMismatch: QRemoteObjectReplica.State = ...  # 0x4

    class State(object):
        Uninitialized: QRemoteObjectReplica.State = ...  # 0x0
        Default: QRemoteObjectReplica.State = ...  # 0x1
        Valid: QRemoteObjectReplica.State = ...  # 0x2
        Suspect: QRemoteObjectReplica.State = ...  # 0x3
        SignatureMismatch: QRemoteObjectReplica.State = ...  # 0x4
    def __init__(self) -> None: ...
    def initialize(self) -> None: ...
    def initializeNode(
        self, node: PySide2.QtRemoteObjects.QRemoteObjectNode, name: str = ...
    ) -> None: ...
    def isInitialized(self) -> bool: ...
    def isReplicaValid(self) -> bool: ...
    def node(self) -> PySide2.QtRemoteObjects.QRemoteObjectNode: ...
    def persistProperties(
        self, repName: str, repSig: PySide2.QtCore.QByteArray, props: typing.Sequence
    ) -> None: ...
    def propAsVariant(self, i: int) -> typing.Any: ...
    def retrieveProperties(
        self, repName: str, repSig: PySide2.QtCore.QByteArray
    ) -> typing.List: ...
    def send(
        self, call: PySide2.QtCore.QMetaObject.Call, index: int, args: typing.Sequence
    ) -> None: ...
    def sendWithReply(
        self, call: PySide2.QtCore.QMetaObject.Call, index: int, args: typing.Sequence
    ) -> PySide2.QtRemoteObjects.QRemoteObjectPendingCall: ...
    def setChild(self, i: int, arg__2: typing.Any) -> None: ...
    def setNode(self, node: PySide2.QtRemoteObjects.QRemoteObjectNode) -> None: ...
    def setProperties(self, arg__1: typing.Sequence) -> None: ...
    def state(self) -> PySide2.QtRemoteObjects.QRemoteObjectReplica.State: ...
    def waitForSource(self, timeout: int = ...) -> bool: ...

class QRemoteObjectSettingsStore(
    PySide2.QtRemoteObjects.QRemoteObjectAbstractPersistedStore
):
    def __init__(
        self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    def restoreProperties(
        self, repName: str, repSig: PySide2.QtCore.QByteArray
    ) -> typing.List: ...
    def saveProperties(
        self, repName: str, repSig: PySide2.QtCore.QByteArray, values: typing.Sequence
    ) -> None: ...

class QRemoteObjectSourceLocationInfo(Shiboken.Object):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(
        self,
        QRemoteObjectSourceLocationInfo: PySide2.QtRemoteObjects.QRemoteObjectSourceLocationInfo,
    ) -> None: ...
    @typing.overload
    def __init__(self, typeName_: str, hostUrl_: PySide2.QtCore.QUrl) -> None: ...
    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(
        self, stream: PySide2.QtCore.QDataStream
    ) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(
        self, stream: PySide2.QtCore.QDataStream
    ) -> PySide2.QtCore.QDataStream: ...

# eof
