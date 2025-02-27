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
PySide2.Qt3DCore, except for defaults which are replaced by "...".
"""

# Module PySide2.Qt3DCore
import PySide2
import typing

import shiboken2 as Shiboken

import PySide2.QtCore
import PySide2.QtGui
import PySide2.Qt3DCore

class Qt3DCore(Shiboken.Object):
    AllChanges: Qt3DCore.ChangeFlag = ...  # -0x1
    NodeCreated: Qt3DCore.ChangeFlag = ...  # 0x1
    NodeDeleted: Qt3DCore.ChangeFlag = ...  # 0x2
    PropertyUpdated: Qt3DCore.ChangeFlag = ...  # 0x4
    PropertyValueAdded: Qt3DCore.ChangeFlag = ...  # 0x8
    PropertyValueRemoved: Qt3DCore.ChangeFlag = ...  # 0x10
    ComponentAdded: Qt3DCore.ChangeFlag = ...  # 0x20
    ComponentRemoved: Qt3DCore.ChangeFlag = ...  # 0x40
    CommandRequested: Qt3DCore.ChangeFlag = ...  # 0x80
    CallbackTriggered: Qt3DCore.ChangeFlag = ...  # 0x100

    class ChangeFlag(object):
        AllChanges: Qt3DCore.ChangeFlag = ...  # -0x1
        NodeCreated: Qt3DCore.ChangeFlag = ...  # 0x1
        NodeDeleted: Qt3DCore.ChangeFlag = ...  # 0x2
        PropertyUpdated: Qt3DCore.ChangeFlag = ...  # 0x4
        PropertyValueAdded: Qt3DCore.ChangeFlag = ...  # 0x8
        PropertyValueRemoved: Qt3DCore.ChangeFlag = ...  # 0x10
        ComponentAdded: Qt3DCore.ChangeFlag = ...  # 0x20
        ComponentRemoved: Qt3DCore.ChangeFlag = ...  # 0x40
        CommandRequested: Qt3DCore.ChangeFlag = ...  # 0x80
        CallbackTriggered: Qt3DCore.ChangeFlag = ...  # 0x100

        def __index__(self) -> int: ...
        def __init__(self, value: typing.Union[int, ChangeFlag] = ...) -> None: ...
        def __or__(self, other: typing.Union[int, ChangeFlag]) -> ChangeFlags: ...
        def __and__(self, other: typing.Union[int, ChangeFlag]) -> ChangeFlags: ...
        def __xor__(self, other: typing.Union[int, ChangeFlag]) -> ChangeFlags: ...
        def __ror__(self, other: typing.Union[int, ChangeFlag]) -> ChangeFlags: ...
        def __rand__(self, other: typing.Union[int, ChangeFlag]) -> ChangeFlags: ...
        def __rxor__(self, other: typing.Union[int, ChangeFlag]) -> ChangeFlags: ...
        def __ior__(self, other: typing.Union[int, ChangeFlag]) -> ChangeFlags: ...
        def __iand__(self, other: typing.Union[int, ChangeFlag]) -> ChangeFlags: ...
        def __ixor__(self, other: typing.Union[int, ChangeFlag]) -> ChangeFlags: ...
        def __invert__(self) -> ChangeFlags: ...

    class ChangeFlags(object):
        def __index__(self) -> int: ...
        def __init__(
            self, value: typing.Union[int, ChangeFlag, ChangeFlags] = ...
        ) -> None: ...
        def __or__(
            self, other: typing.Union[int, ChangeFlag, ChangeFlags]
        ) -> ChangeFlags: ...
        def __and__(
            self, other: typing.Union[int, ChangeFlag, ChangeFlags]
        ) -> ChangeFlags: ...
        def __xor__(
            self, other: typing.Union[int, ChangeFlag, ChangeFlags]
        ) -> ChangeFlags: ...
        def __ror__(
            self, other: typing.Union[int, ChangeFlag, ChangeFlags]
        ) -> ChangeFlags: ...
        def __rand__(
            self, other: typing.Union[int, ChangeFlag, ChangeFlags]
        ) -> ChangeFlags: ...
        def __rxor__(
            self, other: typing.Union[int, ChangeFlag, ChangeFlags]
        ) -> ChangeFlags: ...
        def __ior__(
            self, other: typing.Union[int, ChangeFlag, ChangeFlags]
        ) -> ChangeFlags: ...
        def __iand__(
            self, other: typing.Union[int, ChangeFlag, ChangeFlags]
        ) -> ChangeFlags: ...
        def __ixor__(
            self, other: typing.Union[int, ChangeFlag, ChangeFlags]
        ) -> ChangeFlags: ...
        def __invert__(self) -> ChangeFlags: ...

    class QAbstractAspect(PySide2.QtCore.QObject):
        def __init__(
            self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
        ) -> None: ...
        def rootEntityId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def unregisterBackendType(self, arg__1: PySide2.QtCore.QMetaObject) -> None: ...

    class QAbstractSkeleton(PySide2.Qt3DCore.QNode):
        jointCountChanged: PySide2.QtCore.Signal

        def jointCount(self) -> int: ...

    class QArmature(PySide2.Qt3DCore.QComponent):
        skeletonChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def setSkeleton(
            self, skeleton: PySide2.Qt3DCore.Qt3DCore.QAbstractSkeleton
        ) -> None: ...
        def skeleton(self) -> PySide2.Qt3DCore.Qt3DCore.QAbstractSkeleton: ...

    class QAspectEngine(PySide2.QtCore.QObject):
        Manual: Qt3DCore.QAspectEngine.RunMode = ...  # 0x0
        Automatic: Qt3DCore.QAspectEngine.RunMode = ...  # 0x1

        class RunMode(object):
            Manual: Qt3DCore.QAspectEngine.RunMode = ...  # 0x0
            Automatic: Qt3DCore.QAspectEngine.RunMode = ...  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
        ) -> None: ...
        def aspects(self) -> typing.List: ...
        def executeCommand(self, command: str) -> typing.Any: ...
        def processFrame(self) -> None: ...
        @typing.overload
        def registerAspect(
            self, aspect: PySide2.Qt3DCore.Qt3DCore.QAbstractAspect
        ) -> None: ...
        @typing.overload
        def registerAspect(self, name: str) -> None: ...
        def runMode(self) -> PySide2.Qt3DCore.Qt3DCore.QAspectEngine.RunMode: ...
        def setRunMode(
            self, mode: PySide2.Qt3DCore.Qt3DCore.QAspectEngine.RunMode
        ) -> None: ...
        @typing.overload
        def unregisterAspect(
            self, aspect: PySide2.Qt3DCore.Qt3DCore.QAbstractAspect
        ) -> None: ...
        @typing.overload
        def unregisterAspect(self, name: str) -> None: ...

    class QAspectJob(Shiboken.Object):
        def __init__(self) -> None: ...
        def run(self) -> None: ...

    class QBackendNode(Shiboken.Object):
        ReadOnly: Qt3DCore.QBackendNode.Mode = ...  # 0x0
        ReadWrite: Qt3DCore.QBackendNode.Mode = ...  # 0x1

        class Mode(object):
            ReadOnly: Qt3DCore.QBackendNode.Mode = ...  # 0x0
            ReadWrite: Qt3DCore.QBackendNode.Mode = ...  # 0x1
        def __init__(
            self, mode: PySide2.Qt3DCore.Qt3DCore.QBackendNode.Mode = ...
        ) -> None: ...
        def isEnabled(self) -> bool: ...
        def mode(self) -> PySide2.Qt3DCore.Qt3DCore.QBackendNode.Mode: ...
        def peerId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def setEnabled(self, enabled: bool) -> None: ...

    class QComponent(PySide2.Qt3DCore.QNode):
        addedToEntity: PySide2.QtCore.Signal
        removedFromEntity: PySide2.QtCore.Signal
        shareableChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def entities(self) -> typing.List: ...
        def isShareable(self) -> bool: ...
        def setShareable(self, isShareable: bool) -> None: ...

    class QComponentAddedChange(PySide2.Qt3DCore.QSceneChange):
        @typing.overload
        def __init__(
            self,
            component: PySide2.Qt3DCore.Qt3DCore.QComponent,
            entity: PySide2.Qt3DCore.Qt3DCore.QEntity,
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            entity: PySide2.Qt3DCore.Qt3DCore.QEntity,
            component: PySide2.Qt3DCore.Qt3DCore.QComponent,
        ) -> None: ...
        def componentId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def componentMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
        def entityId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QComponentRemovedChange(PySide2.Qt3DCore.QSceneChange):
        @typing.overload
        def __init__(
            self,
            component: PySide2.Qt3DCore.Qt3DCore.QComponent,
            entity: PySide2.Qt3DCore.Qt3DCore.QEntity,
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            entity: PySide2.Qt3DCore.Qt3DCore.QEntity,
            component: PySide2.Qt3DCore.Qt3DCore.QComponent,
        ) -> None: ...
        def componentId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def componentMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
        def entityId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QDynamicPropertyUpdatedChange(PySide2.Qt3DCore.QPropertyUpdatedChangeBase):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def propertyName(self) -> PySide2.QtCore.QByteArray: ...
        def setPropertyName(self, name: PySide2.QtCore.QByteArray) -> None: ...
        def setValue(self, value: typing.Any) -> None: ...
        def value(self) -> typing.Any: ...

    class QEntity(PySide2.Qt3DCore.QNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addComponent(self, comp: PySide2.Qt3DCore.Qt3DCore.QComponent) -> None: ...
        def components(self) -> typing.List: ...
        def parentEntity(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def removeComponent(
            self, comp: PySide2.Qt3DCore.Qt3DCore.QComponent
        ) -> None: ...

    class QJoint(PySide2.Qt3DCore.QNode):
        inverseBindMatrixChanged: PySide2.QtCore.Signal
        nameChanged: PySide2.QtCore.Signal
        rotationChanged: PySide2.QtCore.Signal
        rotationXChanged: PySide2.QtCore.Signal
        rotationYChanged: PySide2.QtCore.Signal
        rotationZChanged: PySide2.QtCore.Signal
        scaleChanged: PySide2.QtCore.Signal
        translationChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addChildJoint(self, joint: PySide2.Qt3DCore.Qt3DCore.QJoint) -> None: ...
        def childJoints(self) -> typing.List: ...
        def inverseBindMatrix(self) -> PySide2.QtGui.QMatrix4x4: ...
        def name(self) -> str: ...
        def removeChildJoint(self, joint: PySide2.Qt3DCore.Qt3DCore.QJoint) -> None: ...
        def rotation(self) -> PySide2.QtGui.QQuaternion: ...
        def rotationX(self) -> float: ...
        def rotationY(self) -> float: ...
        def rotationZ(self) -> float: ...
        def scale(self) -> PySide2.QtGui.QVector3D: ...
        def setInverseBindMatrix(
            self, inverseBindMatrix: PySide2.QtGui.QMatrix4x4
        ) -> None: ...
        def setName(self, name: str) -> None: ...
        def setRotation(self, rotation: PySide2.QtGui.QQuaternion) -> None: ...
        def setRotationX(self, rotationX: float) -> None: ...
        def setRotationY(self, rotationY: float) -> None: ...
        def setRotationZ(self, rotationZ: float) -> None: ...
        def setScale(self, scale: PySide2.QtGui.QVector3D) -> None: ...
        def setToIdentity(self) -> None: ...
        def setTranslation(self, translation: PySide2.QtGui.QVector3D) -> None: ...
        def translation(self) -> PySide2.QtGui.QVector3D: ...

    class QNode(PySide2.QtCore.QObject):
        defaultPropertyTrackingModeChanged: PySide2.QtCore.Signal
        enabledChanged: PySide2.QtCore.Signal
        nodeDestroyed: PySide2.QtCore.Signal
        parentChanged: PySide2.QtCore.Signal

        TrackFinalValues: Qt3DCore.QNode.PropertyTrackingMode = ...  # 0x0
        DontTrackValues: Qt3DCore.QNode.PropertyTrackingMode = ...  # 0x1
        TrackAllValues: Qt3DCore.QNode.PropertyTrackingMode = ...  # 0x2

        class PropertyTrackingMode(object):
            TrackFinalValues: Qt3DCore.QNode.PropertyTrackingMode = ...  # 0x0
            DontTrackValues: Qt3DCore.QNode.PropertyTrackingMode = ...  # 0x1
            TrackAllValues: Qt3DCore.QNode.PropertyTrackingMode = ...  # 0x2
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def blockNotifications(self, block: bool) -> bool: ...
        def childNodes(self) -> typing.List: ...
        def clearPropertyTracking(self, propertyName: str) -> None: ...
        def clearPropertyTrackings(self) -> None: ...
        def defaultPropertyTrackingMode(
            self,
        ) -> PySide2.Qt3DCore.Qt3DCore.QNode.PropertyTrackingMode: ...
        def id(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def isEnabled(self) -> bool: ...
        def notificationsBlocked(self) -> bool: ...
        def parentNode(self) -> PySide2.Qt3DCore.Qt3DCore.QNode: ...
        def propertyTracking(
            self, propertyName: str
        ) -> PySide2.Qt3DCore.Qt3DCore.QNode.PropertyTrackingMode: ...
        def setDefaultPropertyTrackingMode(
            self, mode: PySide2.Qt3DCore.Qt3DCore.QNode.PropertyTrackingMode
        ) -> None: ...
        def setEnabled(self, isEnabled: bool) -> None: ...
        @typing.overload
        def setParent(self, parent: PySide2.Qt3DCore.Qt3DCore.QNode) -> None: ...
        @typing.overload
        def setParent(self, parent: PySide2.QtCore.QObject) -> None: ...
        def setPropertyTracking(
            self,
            propertyName: str,
            trackMode: PySide2.Qt3DCore.Qt3DCore.QNode.PropertyTrackingMode,
        ) -> None: ...

    class QNodeCommand(PySide2.Qt3DCore.QSceneChange):
        def __init__(self, id: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def commandId(self) -> int: ...
        def data(self) -> typing.Any: ...
        def inReplyTo(self) -> int: ...
        def name(self) -> str: ...
        def setData(self, data: typing.Any) -> None: ...
        def setName(self, name: str) -> None: ...
        def setReplyToCommandId(self, id: int) -> None: ...

    class QNodeCreatedChangeBase(PySide2.Qt3DCore.QSceneChange):
        def __init__(self, node: PySide2.Qt3DCore.Qt3DCore.QNode) -> None: ...
        def isNodeEnabled(self) -> bool: ...
        def parentId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QNodeDestroyedChange(PySide2.Qt3DCore.QSceneChange):
        def __init__(
            self, node: PySide2.Qt3DCore.Qt3DCore.QNode, subtreeIdsAndTypes: typing.List
        ) -> None: ...
        def subtreeIdsAndTypes(self) -> typing.List: ...

    class QNodeId(Shiboken.Object):
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, QNodeId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        @staticmethod
        def __copy__() -> None: ...
        @staticmethod
        def createId() -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def id(self) -> int: ...
        def isNull(self) -> bool: ...

    class QNodeIdTypePair(Shiboken.Object):
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(
            self, QNodeIdTypePair: PySide2.Qt3DCore.Qt3DCore.QNodeIdTypePair
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            _id: PySide2.Qt3DCore.Qt3DCore.QNodeId,
            _type: PySide2.QtCore.QMetaObject,
        ) -> None: ...
        @staticmethod
        def __copy__() -> None: ...

    class QPropertyNodeAddedChange(
        PySide2.Qt3DCore.QStaticPropertyValueAddedChangeBase
    ):
        def __init__(
            self,
            subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId,
            node: PySide2.Qt3DCore.Qt3DCore.QNode,
        ) -> None: ...
        def addedNodeId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QPropertyNodeRemovedChange(
        PySide2.Qt3DCore.QStaticPropertyValueRemovedChangeBase
    ):
        def __init__(
            self,
            subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId,
            node: PySide2.Qt3DCore.Qt3DCore.QNode,
        ) -> None: ...
        def removedNodeId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QPropertyUpdatedChange(PySide2.Qt3DCore.QStaticPropertyUpdatedChangeBase):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def setValue(self, value: typing.Any) -> None: ...
        def value(self) -> typing.Any: ...

    class QPropertyUpdatedChangeBase(PySide2.Qt3DCore.QSceneChange):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...

    class QPropertyValueAddedChange(
        PySide2.Qt3DCore.QStaticPropertyValueAddedChangeBase
    ):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def addedValue(self) -> typing.Any: ...
        def setAddedValue(self, value: typing.Any) -> None: ...

    class QPropertyValueAddedChangeBase(PySide2.Qt3DCore.QSceneChange):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...

    class QPropertyValueRemovedChange(
        PySide2.Qt3DCore.QStaticPropertyValueRemovedChangeBase
    ):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def removedValue(self) -> typing.Any: ...
        def setRemovedValue(self, value: typing.Any) -> None: ...

    class QPropertyValueRemovedChangeBase(PySide2.Qt3DCore.QSceneChange):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...

    class QSceneChange(Shiboken.Object):
        BackendNodes: Qt3DCore.QSceneChange.DeliveryFlag = ...  # 0x1
        Nodes: Qt3DCore.QSceneChange.DeliveryFlag = ...  # 0x10
        DeliverToAll: Qt3DCore.QSceneChange.DeliveryFlag = ...  # 0x11

        class DeliveryFlag(object):
            BackendNodes: Qt3DCore.QSceneChange.DeliveryFlag = ...  # 0x1
            Nodes: Qt3DCore.QSceneChange.DeliveryFlag = ...  # 0x10
            DeliverToAll: Qt3DCore.QSceneChange.DeliveryFlag = ...  # 0x11

            def __index__(self) -> int: ...
            def __init__(
                self, value: typing.Union[int, DeliveryFlag] = ...
            ) -> None: ...
            def __or__(
                self, other: typing.Union[int, DeliveryFlag]
            ) -> DeliveryFlags: ...
            def __and__(
                self, other: typing.Union[int, DeliveryFlag]
            ) -> DeliveryFlags: ...
            def __xor__(
                self, other: typing.Union[int, DeliveryFlag]
            ) -> DeliveryFlags: ...
            def __ror__(
                self, other: typing.Union[int, DeliveryFlag]
            ) -> DeliveryFlags: ...
            def __rand__(
                self, other: typing.Union[int, DeliveryFlag]
            ) -> DeliveryFlags: ...
            def __rxor__(
                self, other: typing.Union[int, DeliveryFlag]
            ) -> DeliveryFlags: ...
            def __ior__(
                self, other: typing.Union[int, DeliveryFlag]
            ) -> DeliveryFlags: ...
            def __iand__(
                self, other: typing.Union[int, DeliveryFlag]
            ) -> DeliveryFlags: ...
            def __ixor__(
                self, other: typing.Union[int, DeliveryFlag]
            ) -> DeliveryFlags: ...
            def __invert__(self) -> DeliveryFlags: ...

        class DeliveryFlags(object):
            def __index__(self) -> int: ...
            def __init__(
                self, value: typing.Union[int, DeliveryFlag, DeliveryFlags] = ...
            ) -> None: ...
            def __or__(
                self, other: typing.Union[int, DeliveryFlag, DeliveryFlags]
            ) -> DeliveryFlags: ...
            def __and__(
                self, other: typing.Union[int, DeliveryFlag, DeliveryFlags]
            ) -> DeliveryFlags: ...
            def __xor__(
                self, other: typing.Union[int, DeliveryFlag, DeliveryFlags]
            ) -> DeliveryFlags: ...
            def __ror__(
                self, other: typing.Union[int, DeliveryFlag, DeliveryFlags]
            ) -> DeliveryFlags: ...
            def __rand__(
                self, other: typing.Union[int, DeliveryFlag, DeliveryFlags]
            ) -> DeliveryFlags: ...
            def __rxor__(
                self, other: typing.Union[int, DeliveryFlag, DeliveryFlags]
            ) -> DeliveryFlags: ...
            def __ior__(
                self, other: typing.Union[int, DeliveryFlag, DeliveryFlags]
            ) -> DeliveryFlags: ...
            def __iand__(
                self, other: typing.Union[int, DeliveryFlag, DeliveryFlags]
            ) -> DeliveryFlags: ...
            def __ixor__(
                self, other: typing.Union[int, DeliveryFlag, DeliveryFlags]
            ) -> DeliveryFlags: ...
            def __invert__(self) -> DeliveryFlags: ...

        def __init__(
            self,
            type: PySide2.Qt3DCore.Qt3DCore.ChangeFlag,
            subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId,
        ) -> None: ...
        def deliveryFlags(
            self,
        ) -> PySide2.Qt3DCore.Qt3DCore.QSceneChange.DeliveryFlags: ...
        def setDeliveryFlags(
            self, flags: PySide2.Qt3DCore.Qt3DCore.QSceneChange.DeliveryFlags
        ) -> None: ...
        def subjectId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def type(self) -> PySide2.Qt3DCore.Qt3DCore.ChangeFlag: ...

    class QSkeleton(PySide2.Qt3DCore.QAbstractSkeleton):
        rootJointChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def rootJoint(self) -> PySide2.Qt3DCore.Qt3DCore.QJoint: ...
        def setRootJoint(self, rootJoint: PySide2.Qt3DCore.Qt3DCore.QJoint) -> None: ...

    class QSkeletonLoader(PySide2.Qt3DCore.QAbstractSkeleton):
        createJointsEnabledChanged: PySide2.QtCore.Signal
        rootJointChanged: PySide2.QtCore.Signal
        sourceChanged: PySide2.QtCore.Signal
        statusChanged: PySide2.QtCore.Signal

        NotReady: Qt3DCore.QSkeletonLoader.Status = ...  # 0x0
        Ready: Qt3DCore.QSkeletonLoader.Status = ...  # 0x1
        Error: Qt3DCore.QSkeletonLoader.Status = ...  # 0x2

        class Status(object):
            NotReady: Qt3DCore.QSkeletonLoader.Status = ...  # 0x0
            Ready: Qt3DCore.QSkeletonLoader.Status = ...  # 0x1
            Error: Qt3DCore.QSkeletonLoader.Status = ...  # 0x2
        @typing.overload
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            source: PySide2.QtCore.QUrl,
            parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...,
        ) -> None: ...
        def isCreateJointsEnabled(self) -> bool: ...
        def rootJoint(self) -> PySide2.Qt3DCore.Qt3DCore.QJoint: ...
        def setCreateJointsEnabled(self, enabled: bool) -> None: ...
        def setSource(self, source: PySide2.QtCore.QUrl) -> None: ...
        def source(self) -> PySide2.QtCore.QUrl: ...
        def status(self) -> PySide2.Qt3DCore.Qt3DCore.QSkeletonLoader.Status: ...

    class QStaticPropertyUpdatedChangeBase(PySide2.Qt3DCore.QPropertyUpdatedChangeBase):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def propertyName(self) -> bytes: ...
        def setPropertyName(self, name: bytes) -> None: ...

    class QStaticPropertyValueAddedChangeBase(
        PySide2.Qt3DCore.QPropertyValueAddedChangeBase
    ):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def propertyName(self) -> bytes: ...
        def setPropertyName(self, name: bytes) -> None: ...

    class QStaticPropertyValueRemovedChangeBase(
        PySide2.Qt3DCore.QPropertyValueRemovedChangeBase
    ):
        def __init__(self, subjectId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def propertyName(self) -> bytes: ...
        def setPropertyName(self, name: bytes) -> None: ...

    class QTransform(PySide2.Qt3DCore.QComponent):
        matrixChanged: PySide2.QtCore.Signal
        rotationChanged: PySide2.QtCore.Signal
        rotationXChanged: PySide2.QtCore.Signal
        rotationYChanged: PySide2.QtCore.Signal
        rotationZChanged: PySide2.QtCore.Signal
        scale3DChanged: PySide2.QtCore.Signal
        scaleChanged: PySide2.QtCore.Signal
        translationChanged: PySide2.QtCore.Signal
        worldMatrixChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        @staticmethod
        def fromAxes(
            xAxis: PySide2.QtGui.QVector3D,
            yAxis: PySide2.QtGui.QVector3D,
            zAxis: PySide2.QtGui.QVector3D,
        ) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxesAndAngles(
            axis1: PySide2.QtGui.QVector3D,
            angle1: float,
            axis2: PySide2.QtGui.QVector3D,
            angle2: float,
        ) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxesAndAngles(
            axis1: PySide2.QtGui.QVector3D,
            angle1: float,
            axis2: PySide2.QtGui.QVector3D,
            angle2: float,
            axis3: PySide2.QtGui.QVector3D,
            angle3: float,
        ) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxisAndAngle(
            axis: PySide2.QtGui.QVector3D, angle: float
        ) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromAxisAndAngle(
            x: float, y: float, z: float, angle: float
        ) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromEulerAngles(
            eulerAngles: PySide2.QtGui.QVector3D,
        ) -> PySide2.QtGui.QQuaternion: ...
        @typing.overload
        @staticmethod
        def fromEulerAngles(
            pitch: float, yaw: float, roll: float
        ) -> PySide2.QtGui.QQuaternion: ...
        def matrix(self) -> PySide2.QtGui.QMatrix4x4: ...
        @staticmethod
        def rotateAround(
            point: PySide2.QtGui.QVector3D, angle: float, axis: PySide2.QtGui.QVector3D
        ) -> PySide2.QtGui.QMatrix4x4: ...
        @staticmethod
        def rotateFromAxes(
            xAxis: PySide2.QtGui.QVector3D,
            yAxis: PySide2.QtGui.QVector3D,
            zAxis: PySide2.QtGui.QVector3D,
        ) -> PySide2.QtGui.QMatrix4x4: ...
        def rotation(self) -> PySide2.QtGui.QQuaternion: ...
        def rotationX(self) -> float: ...
        def rotationY(self) -> float: ...
        def rotationZ(self) -> float: ...
        def scale(self) -> float: ...
        def scale3D(self) -> PySide2.QtGui.QVector3D: ...
        def setMatrix(self, matrix: PySide2.QtGui.QMatrix4x4) -> None: ...
        def setRotation(self, rotation: PySide2.QtGui.QQuaternion) -> None: ...
        def setRotationX(self, rotationX: float) -> None: ...
        def setRotationY(self, rotationY: float) -> None: ...
        def setRotationZ(self, rotationZ: float) -> None: ...
        def setScale(self, scale: float) -> None: ...
        def setScale3D(self, scale: PySide2.QtGui.QVector3D) -> None: ...
        def setTranslation(self, translation: PySide2.QtGui.QVector3D) -> None: ...
        def translation(self) -> PySide2.QtGui.QVector3D: ...
        def worldMatrix(self) -> PySide2.QtGui.QMatrix4x4: ...

    @staticmethod
    def qHash(id: PySide2.Qt3DCore.Qt3DCore.QNodeId, seed: int = ...) -> int: ...
    @staticmethod
    def qIdForNode(
        node: PySide2.Qt3DCore.Qt3DCore.QNode,
    ) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

# eof
