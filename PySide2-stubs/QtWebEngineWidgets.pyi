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
PySide2.QtWebEngineWidgets, except for defaults which are replaced by "...".
"""

# Module PySide2.QtWebEngineWidgets
import PySide2
import typing

import shiboken2 as Shiboken

import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtPrintSupport
import PySide2.QtWebChannel
import PySide2.QtWebEngineCore
import PySide2.QtWebEngineWidgets

class QWebEngineCertificateError(Shiboken.Object):
    CertificateKnownInterceptionBlocked: QWebEngineCertificateError.Error = ...  # -0xd9
    CertificateTransparencyRequired: QWebEngineCertificateError.Error = ...  # -0xd6
    CertificateValidityTooLong: QWebEngineCertificateError.Error = ...  # -0xd5
    CertificateNameConstraintViolation: QWebEngineCertificateError.Error = ...  # -0xd4
    CertificateWeakKey: QWebEngineCertificateError.Error = ...  # -0xd3
    CertificateNonUniqueName: QWebEngineCertificateError.Error = ...  # -0xd2
    CertificateWeakSignatureAlgorithm: QWebEngineCertificateError.Error = ...  # -0xd0
    CertificateInvalid: QWebEngineCertificateError.Error = ...  # -0xcf
    CertificateRevoked: QWebEngineCertificateError.Error = ...  # -0xce
    CertificateUnableToCheckRevocation: QWebEngineCertificateError.Error = ...  # -0xcd
    CertificateNoRevocationMechanism: QWebEngineCertificateError.Error = ...  # -0xcc
    CertificateContainsErrors: QWebEngineCertificateError.Error = ...  # -0xcb
    CertificateAuthorityInvalid: QWebEngineCertificateError.Error = ...  # -0xca
    CertificateDateInvalid: QWebEngineCertificateError.Error = ...  # -0xc9
    CertificateCommonNameInvalid: QWebEngineCertificateError.Error = ...  # -0xc8
    SslPinnedKeyNotInCertificateChain: QWebEngineCertificateError.Error = ...  # -0x96

    class Error(object):
        CertificateKnownInterceptionBlocked: QWebEngineCertificateError.Error = (
            ...
        )  # -0xd9
        CertificateTransparencyRequired: QWebEngineCertificateError.Error = ...  # -0xd6
        CertificateValidityTooLong: QWebEngineCertificateError.Error = ...  # -0xd5
        CertificateNameConstraintViolation: QWebEngineCertificateError.Error = (
            ...
        )  # -0xd4
        CertificateWeakKey: QWebEngineCertificateError.Error = ...  # -0xd3
        CertificateNonUniqueName: QWebEngineCertificateError.Error = ...  # -0xd2
        CertificateWeakSignatureAlgorithm: QWebEngineCertificateError.Error = (
            ...
        )  # -0xd0
        CertificateInvalid: QWebEngineCertificateError.Error = ...  # -0xcf
        CertificateRevoked: QWebEngineCertificateError.Error = ...  # -0xce
        CertificateUnableToCheckRevocation: QWebEngineCertificateError.Error = (
            ...
        )  # -0xcd
        CertificateNoRevocationMechanism: QWebEngineCertificateError.Error = (
            ...
        )  # -0xcc
        CertificateContainsErrors: QWebEngineCertificateError.Error = ...  # -0xcb
        CertificateAuthorityInvalid: QWebEngineCertificateError.Error = ...  # -0xca
        CertificateDateInvalid: QWebEngineCertificateError.Error = ...  # -0xc9
        CertificateCommonNameInvalid: QWebEngineCertificateError.Error = ...  # -0xc8
        SslPinnedKeyNotInCertificateChain: QWebEngineCertificateError.Error = (
            ...
        )  # -0x96
    @typing.overload
    def __init__(
        self,
        error: int,
        url: PySide2.QtCore.QUrl,
        overridable: bool,
        errorDescription: str,
    ) -> None: ...
    @typing.overload
    def __init__(
        self, other: PySide2.QtWebEngineWidgets.QWebEngineCertificateError
    ) -> None: ...
    def answered(self) -> bool: ...
    def certificateChain(self) -> typing.List: ...
    def defer(self) -> None: ...
    def deferred(self) -> bool: ...
    def error(self) -> PySide2.QtWebEngineWidgets.QWebEngineCertificateError.Error: ...
    def errorDescription(self) -> str: ...
    def ignoreCertificateError(self) -> None: ...
    def isOverridable(self) -> bool: ...
    def rejectCertificate(self) -> None: ...
    def url(self) -> PySide2.QtCore.QUrl: ...

class QWebEngineContextMenuData(Shiboken.Object):
    MediaTypeNone: QWebEngineContextMenuData.MediaType = ...  # 0x0
    CanUndo: QWebEngineContextMenuData.EditFlag = ...  # 0x1
    MediaInError: QWebEngineContextMenuData.MediaFlag = ...  # 0x1
    MediaTypeImage: QWebEngineContextMenuData.MediaType = ...  # 0x1
    CanRedo: QWebEngineContextMenuData.EditFlag = ...  # 0x2
    MediaPaused: QWebEngineContextMenuData.MediaFlag = ...  # 0x2
    MediaTypeVideo: QWebEngineContextMenuData.MediaType = ...  # 0x2
    MediaTypeAudio: QWebEngineContextMenuData.MediaType = ...  # 0x3
    CanCut: QWebEngineContextMenuData.EditFlag = ...  # 0x4
    MediaMuted: QWebEngineContextMenuData.MediaFlag = ...  # 0x4
    MediaTypeCanvas: QWebEngineContextMenuData.MediaType = ...  # 0x4
    MediaTypeFile: QWebEngineContextMenuData.MediaType = ...  # 0x5
    MediaTypePlugin: QWebEngineContextMenuData.MediaType = ...  # 0x6
    CanCopy: QWebEngineContextMenuData.EditFlag = ...  # 0x8
    MediaLoop: QWebEngineContextMenuData.MediaFlag = ...  # 0x8
    CanPaste: QWebEngineContextMenuData.EditFlag = ...  # 0x10
    MediaCanSave: QWebEngineContextMenuData.MediaFlag = ...  # 0x10
    CanDelete: QWebEngineContextMenuData.EditFlag = ...  # 0x20
    MediaHasAudio: QWebEngineContextMenuData.MediaFlag = ...  # 0x20
    CanSelectAll: QWebEngineContextMenuData.EditFlag = ...  # 0x40
    MediaCanToggleControls: QWebEngineContextMenuData.MediaFlag = ...  # 0x40
    CanTranslate: QWebEngineContextMenuData.EditFlag = ...  # 0x80
    MediaControls: QWebEngineContextMenuData.MediaFlag = ...  # 0x80
    CanEditRichly: QWebEngineContextMenuData.EditFlag = ...  # 0x100
    MediaCanPrint: QWebEngineContextMenuData.MediaFlag = ...  # 0x100
    MediaCanRotate: QWebEngineContextMenuData.MediaFlag = ...  # 0x200

    class EditFlag(object):
        CanUndo: QWebEngineContextMenuData.EditFlag = ...  # 0x1
        CanRedo: QWebEngineContextMenuData.EditFlag = ...  # 0x2
        CanCut: QWebEngineContextMenuData.EditFlag = ...  # 0x4
        CanCopy: QWebEngineContextMenuData.EditFlag = ...  # 0x8
        CanPaste: QWebEngineContextMenuData.EditFlag = ...  # 0x10
        CanDelete: QWebEngineContextMenuData.EditFlag = ...  # 0x20
        CanSelectAll: QWebEngineContextMenuData.EditFlag = ...  # 0x40
        CanTranslate: QWebEngineContextMenuData.EditFlag = ...  # 0x80
        CanEditRichly: QWebEngineContextMenuData.EditFlag = ...  # 0x100

        def __index__(self) -> int: ...
        def __init__(self, value: typing.Union[int, EditFlag] = ...) -> None: ...
        def __or__(self, other: typing.Union[int, EditFlag]) -> EditFlags: ...
        def __and__(self, other: typing.Union[int, EditFlag]) -> EditFlags: ...
        def __xor__(self, other: typing.Union[int, EditFlag]) -> EditFlags: ...
        def __ror__(self, other: typing.Union[int, EditFlag]) -> EditFlags: ...
        def __rand__(self, other: typing.Union[int, EditFlag]) -> EditFlags: ...
        def __rxor__(self, other: typing.Union[int, EditFlag]) -> EditFlags: ...
        def __ior__(self, other: typing.Union[int, EditFlag]) -> EditFlags: ...
        def __iand__(self, other: typing.Union[int, EditFlag]) -> EditFlags: ...
        def __ixor__(self, other: typing.Union[int, EditFlag]) -> EditFlags: ...
        def __invert__(self) -> EditFlags: ...

    class EditFlags(object):
        def __index__(self) -> int: ...
        def __init__(
            self, value: typing.Union[int, EditFlag, EditFlags] = ...
        ) -> None: ...
        def __or__(
            self, other: typing.Union[int, EditFlag, EditFlags]
        ) -> EditFlags: ...
        def __and__(
            self, other: typing.Union[int, EditFlag, EditFlags]
        ) -> EditFlags: ...
        def __xor__(
            self, other: typing.Union[int, EditFlag, EditFlags]
        ) -> EditFlags: ...
        def __ror__(
            self, other: typing.Union[int, EditFlag, EditFlags]
        ) -> EditFlags: ...
        def __rand__(
            self, other: typing.Union[int, EditFlag, EditFlags]
        ) -> EditFlags: ...
        def __rxor__(
            self, other: typing.Union[int, EditFlag, EditFlags]
        ) -> EditFlags: ...
        def __ior__(
            self, other: typing.Union[int, EditFlag, EditFlags]
        ) -> EditFlags: ...
        def __iand__(
            self, other: typing.Union[int, EditFlag, EditFlags]
        ) -> EditFlags: ...
        def __ixor__(
            self, other: typing.Union[int, EditFlag, EditFlags]
        ) -> EditFlags: ...
        def __invert__(self) -> EditFlags: ...

    class MediaFlag(object):
        MediaInError: QWebEngineContextMenuData.MediaFlag = ...  # 0x1
        MediaPaused: QWebEngineContextMenuData.MediaFlag = ...  # 0x2
        MediaMuted: QWebEngineContextMenuData.MediaFlag = ...  # 0x4
        MediaLoop: QWebEngineContextMenuData.MediaFlag = ...  # 0x8
        MediaCanSave: QWebEngineContextMenuData.MediaFlag = ...  # 0x10
        MediaHasAudio: QWebEngineContextMenuData.MediaFlag = ...  # 0x20
        MediaCanToggleControls: QWebEngineContextMenuData.MediaFlag = ...  # 0x40
        MediaControls: QWebEngineContextMenuData.MediaFlag = ...  # 0x80
        MediaCanPrint: QWebEngineContextMenuData.MediaFlag = ...  # 0x100
        MediaCanRotate: QWebEngineContextMenuData.MediaFlag = ...  # 0x200

        def __index__(self) -> int: ...
        def __init__(self, value: typing.Union[int, MediaFlag] = ...) -> None: ...
        def __or__(self, other: typing.Union[int, MediaFlag]) -> MediaFlags: ...
        def __and__(self, other: typing.Union[int, MediaFlag]) -> MediaFlags: ...
        def __xor__(self, other: typing.Union[int, MediaFlag]) -> MediaFlags: ...
        def __ror__(self, other: typing.Union[int, MediaFlag]) -> MediaFlags: ...
        def __rand__(self, other: typing.Union[int, MediaFlag]) -> MediaFlags: ...
        def __rxor__(self, other: typing.Union[int, MediaFlag]) -> MediaFlags: ...
        def __ior__(self, other: typing.Union[int, MediaFlag]) -> MediaFlags: ...
        def __iand__(self, other: typing.Union[int, MediaFlag]) -> MediaFlags: ...
        def __ixor__(self, other: typing.Union[int, MediaFlag]) -> MediaFlags: ...
        def __invert__(self) -> MediaFlags: ...

    class MediaFlags(object):
        def __index__(self) -> int: ...
        def __init__(
            self, value: typing.Union[int, MediaFlag, MediaFlags] = ...
        ) -> None: ...
        def __or__(
            self, other: typing.Union[int, MediaFlag, MediaFlags]
        ) -> MediaFlags: ...
        def __and__(
            self, other: typing.Union[int, MediaFlag, MediaFlags]
        ) -> MediaFlags: ...
        def __xor__(
            self, other: typing.Union[int, MediaFlag, MediaFlags]
        ) -> MediaFlags: ...
        def __ror__(
            self, other: typing.Union[int, MediaFlag, MediaFlags]
        ) -> MediaFlags: ...
        def __rand__(
            self, other: typing.Union[int, MediaFlag, MediaFlags]
        ) -> MediaFlags: ...
        def __rxor__(
            self, other: typing.Union[int, MediaFlag, MediaFlags]
        ) -> MediaFlags: ...
        def __ior__(
            self, other: typing.Union[int, MediaFlag, MediaFlags]
        ) -> MediaFlags: ...
        def __iand__(
            self, other: typing.Union[int, MediaFlag, MediaFlags]
        ) -> MediaFlags: ...
        def __ixor__(
            self, other: typing.Union[int, MediaFlag, MediaFlags]
        ) -> MediaFlags: ...
        def __invert__(self) -> MediaFlags: ...

    class MediaType(object):
        MediaTypeNone: QWebEngineContextMenuData.MediaType = ...  # 0x0
        MediaTypeImage: QWebEngineContextMenuData.MediaType = ...  # 0x1
        MediaTypeVideo: QWebEngineContextMenuData.MediaType = ...  # 0x2
        MediaTypeAudio: QWebEngineContextMenuData.MediaType = ...  # 0x3
        MediaTypeCanvas: QWebEngineContextMenuData.MediaType = ...  # 0x4
        MediaTypeFile: QWebEngineContextMenuData.MediaType = ...  # 0x5
        MediaTypePlugin: QWebEngineContextMenuData.MediaType = ...  # 0x6
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(
        self, other: PySide2.QtWebEngineWidgets.QWebEngineContextMenuData
    ) -> None: ...
    @staticmethod
    def __copy__() -> None: ...
    def editFlags(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.EditFlags: ...
    def isContentEditable(self) -> bool: ...
    def isValid(self) -> bool: ...
    def linkText(self) -> str: ...
    def linkUrl(self) -> PySide2.QtCore.QUrl: ...
    def mediaFlags(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaFlags: ...
    def mediaType(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData.MediaType: ...
    def mediaUrl(self) -> PySide2.QtCore.QUrl: ...
    def misspelledWord(self) -> str: ...
    def position(self) -> PySide2.QtCore.QPoint: ...
    def selectedText(self) -> str: ...
    def spellCheckerSuggestions(self) -> typing.List: ...

class QWebEngineDownloadItem(PySide2.QtCore.QObject):
    downloadProgress: PySide2.QtCore.Signal
    finished: PySide2.QtCore.Signal
    isPausedChanged: PySide2.QtCore.Signal
    stateChanged: PySide2.QtCore.Signal

    UnknownSaveFormat: QWebEngineDownloadItem.SavePageFormat = ...  # -0x1
    Attachment: QWebEngineDownloadItem.DownloadType = ...  # 0x0
    DownloadRequested: QWebEngineDownloadItem.DownloadState = ...  # 0x0
    NoReason: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x0
    SingleHtmlSaveFormat: QWebEngineDownloadItem.SavePageFormat = ...  # 0x0
    CompleteHtmlSaveFormat: QWebEngineDownloadItem.SavePageFormat = ...  # 0x1
    DownloadAttribute: QWebEngineDownloadItem.DownloadType = ...  # 0x1
    DownloadInProgress: QWebEngineDownloadItem.DownloadState = ...  # 0x1
    FileFailed: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x1
    DownloadCompleted: QWebEngineDownloadItem.DownloadState = ...  # 0x2
    FileAccessDenied: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x2
    MimeHtmlSaveFormat: QWebEngineDownloadItem.SavePageFormat = ...  # 0x2
    UserRequested: QWebEngineDownloadItem.DownloadType = ...  # 0x2
    DownloadCancelled: QWebEngineDownloadItem.DownloadState = ...  # 0x3
    FileNoSpace: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x3
    SavePage: QWebEngineDownloadItem.DownloadType = ...  # 0x3
    DownloadInterrupted: QWebEngineDownloadItem.DownloadState = ...  # 0x4
    FileNameTooLong: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x5
    FileTooLarge: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x6
    FileVirusInfected: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x7
    FileTransientError: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0xa
    FileBlocked: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0xb
    FileSecurityCheckFailed: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0xc
    FileTooShort: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0xd
    FileHashMismatch: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0xe
    NetworkFailed: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x14
    NetworkTimeout: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x15
    NetworkDisconnected: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x16
    NetworkServerDown: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x17
    NetworkInvalidRequest: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x18
    ServerFailed: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x1e
    ServerBadContent: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x21
    ServerUnauthorized: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x22
    ServerCertProblem: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x23
    ServerForbidden: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x24
    ServerUnreachable: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x25
    UserCanceled: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x28

    class DownloadInterruptReason(object):
        NoReason: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x0
        FileFailed: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x1
        FileAccessDenied: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x2
        FileNoSpace: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x3
        FileNameTooLong: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x5
        FileTooLarge: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x6
        FileVirusInfected: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x7
        FileTransientError: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0xa
        FileBlocked: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0xb
        FileSecurityCheckFailed: QWebEngineDownloadItem.DownloadInterruptReason = (
            ...
        )  # 0xc
        FileTooShort: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0xd
        FileHashMismatch: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0xe
        NetworkFailed: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x14
        NetworkTimeout: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x15
        NetworkDisconnected: QWebEngineDownloadItem.DownloadInterruptReason = (
            ...
        )  # 0x16
        NetworkServerDown: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x17
        NetworkInvalidRequest: QWebEngineDownloadItem.DownloadInterruptReason = (
            ...
        )  # 0x18
        ServerFailed: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x1e
        ServerBadContent: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x21
        ServerUnauthorized: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x22
        ServerCertProblem: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x23
        ServerForbidden: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x24
        ServerUnreachable: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x25
        UserCanceled: QWebEngineDownloadItem.DownloadInterruptReason = ...  # 0x28

    class DownloadState(object):
        DownloadRequested: QWebEngineDownloadItem.DownloadState = ...  # 0x0
        DownloadInProgress: QWebEngineDownloadItem.DownloadState = ...  # 0x1
        DownloadCompleted: QWebEngineDownloadItem.DownloadState = ...  # 0x2
        DownloadCancelled: QWebEngineDownloadItem.DownloadState = ...  # 0x3
        DownloadInterrupted: QWebEngineDownloadItem.DownloadState = ...  # 0x4

    class DownloadType(object):
        Attachment: QWebEngineDownloadItem.DownloadType = ...  # 0x0
        DownloadAttribute: QWebEngineDownloadItem.DownloadType = ...  # 0x1
        UserRequested: QWebEngineDownloadItem.DownloadType = ...  # 0x2
        SavePage: QWebEngineDownloadItem.DownloadType = ...  # 0x3

    class SavePageFormat(object):
        UnknownSaveFormat: QWebEngineDownloadItem.SavePageFormat = ...  # -0x1
        SingleHtmlSaveFormat: QWebEngineDownloadItem.SavePageFormat = ...  # 0x0
        CompleteHtmlSaveFormat: QWebEngineDownloadItem.SavePageFormat = ...  # 0x1
        MimeHtmlSaveFormat: QWebEngineDownloadItem.SavePageFormat = ...  # 0x2
    def accept(self) -> None: ...
    def cancel(self) -> None: ...
    def downloadDirectory(self) -> str: ...
    def downloadFileName(self) -> str: ...
    def id(self) -> int: ...
    def interruptReason(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadInterruptReason: ...
    def interruptReasonString(self) -> str: ...
    def isFinished(self) -> bool: ...
    def isPaused(self) -> bool: ...
    def isSavePageDownload(self) -> bool: ...
    def mimeType(self) -> str: ...
    def page(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def path(self) -> str: ...
    def pause(self) -> None: ...
    def receivedBytes(self) -> int: ...
    def resume(self) -> None: ...
    def savePageFormat(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat: ...
    def setDownloadDirectory(self, directory: str) -> None: ...
    def setDownloadFileName(self, fileName: str) -> None: ...
    def setPath(self, path: str) -> None: ...
    def setSavePageFormat(
        self, format: PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat
    ) -> None: ...
    def state(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadState: ...
    def suggestedFileName(self) -> str: ...
    def totalBytes(self) -> int: ...
    def type(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.DownloadType: ...
    def url(self) -> PySide2.QtCore.QUrl: ...

class QWebEngineFullScreenRequest(Shiboken.Object):
    def accept(self) -> None: ...
    def origin(self) -> PySide2.QtCore.QUrl: ...
    def reject(self) -> None: ...
    def toggleOn(self) -> bool: ...

class QWebEngineHistory(Shiboken.Object):
    def __lshift__(
        self, stream: PySide2.QtCore.QDataStream
    ) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(
        self, stream: PySide2.QtCore.QDataStream
    ) -> PySide2.QtCore.QDataStream: ...
    def back(self) -> None: ...
    def backItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def backItems(self, maxItems: int) -> typing.List: ...
    def canGoBack(self) -> bool: ...
    def canGoForward(self) -> bool: ...
    def clear(self) -> None: ...
    def count(self) -> int: ...
    def currentItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def currentItemIndex(self) -> int: ...
    def forward(self) -> None: ...
    def forwardItem(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def forwardItems(self, maxItems: int) -> typing.List: ...
    def goToItem(
        self, item: PySide2.QtWebEngineWidgets.QWebEngineHistoryItem
    ) -> None: ...
    def itemAt(self, i: int) -> PySide2.QtWebEngineWidgets.QWebEngineHistoryItem: ...
    def items(self) -> typing.List: ...

class QWebEngineHistoryItem(Shiboken.Object):
    def __init__(
        self, other: PySide2.QtWebEngineWidgets.QWebEngineHistoryItem
    ) -> None: ...
    @staticmethod
    def __copy__() -> None: ...
    def iconUrl(self) -> PySide2.QtCore.QUrl: ...
    def isValid(self) -> bool: ...
    def lastVisited(self) -> PySide2.QtCore.QDateTime: ...
    def originalUrl(self) -> PySide2.QtCore.QUrl: ...
    def swap(self, other: PySide2.QtWebEngineWidgets.QWebEngineHistoryItem) -> None: ...
    def title(self) -> str: ...
    def url(self) -> PySide2.QtCore.QUrl: ...

class QWebEnginePage(PySide2.QtCore.QObject):
    audioMutedChanged: PySide2.QtCore.Signal
    authenticationRequired: PySide2.QtCore.Signal
    contentsSizeChanged: PySide2.QtCore.Signal
    featurePermissionRequestCanceled: PySide2.QtCore.Signal
    featurePermissionRequested: PySide2.QtCore.Signal
    findTextFinished: PySide2.QtCore.Signal
    fullScreenRequested: PySide2.QtCore.Signal
    geometryChangeRequested: PySide2.QtCore.Signal
    iconChanged: PySide2.QtCore.Signal
    iconUrlChanged: PySide2.QtCore.Signal
    lifecycleStateChanged: PySide2.QtCore.Signal
    linkHovered: PySide2.QtCore.Signal
    loadFinished: PySide2.QtCore.Signal
    loadProgress: PySide2.QtCore.Signal
    loadStarted: PySide2.QtCore.Signal
    pdfPrintingFinished: PySide2.QtCore.Signal
    printRequested: PySide2.QtCore.Signal
    proxyAuthenticationRequired: PySide2.QtCore.Signal
    quotaRequested: PySide2.QtCore.Signal
    recentlyAudibleChanged: PySide2.QtCore.Signal
    recommendedStateChanged: PySide2.QtCore.Signal
    registerProtocolHandlerRequested: PySide2.QtCore.Signal
    renderProcessPidChanged: PySide2.QtCore.Signal
    renderProcessTerminated: PySide2.QtCore.Signal
    scrollPositionChanged: PySide2.QtCore.Signal
    selectClientCertificate: PySide2.QtCore.Signal
    selectionChanged: PySide2.QtCore.Signal
    titleChanged: PySide2.QtCore.Signal
    urlChanged: PySide2.QtCore.Signal
    visibleChanged: PySide2.QtCore.Signal
    windowCloseRequested: PySide2.QtCore.Signal

    NoWebAction: QWebEnginePage.WebAction = ...  # -0x1
    Back: QWebEnginePage.WebAction = ...  # 0x0
    FileSelectOpen: QWebEnginePage.FileSelectionMode = ...  # 0x0
    InfoMessageLevel: QWebEnginePage.JavaScriptConsoleMessageLevel = ...  # 0x0
    NavigationTypeLinkClicked: QWebEnginePage.NavigationType = ...  # 0x0
    NormalTerminationStatus: QWebEnginePage.RenderProcessTerminationStatus = ...  # 0x0
    Notifications: QWebEnginePage.Feature = ...  # 0x0
    PermissionUnknown: QWebEnginePage.PermissionPolicy = ...  # 0x0
    WebBrowserWindow: QWebEnginePage.WebWindowType = ...  # 0x0
    AbnormalTerminationStatus: QWebEnginePage.RenderProcessTerminationStatus = (
        ...
    )  # 0x1
    FileSelectOpenMultiple: QWebEnginePage.FileSelectionMode = ...  # 0x1
    FindBackward: QWebEnginePage.FindFlag = ...  # 0x1
    Forward: QWebEnginePage.WebAction = ...  # 0x1
    Geolocation: QWebEnginePage.Feature = ...  # 0x1
    NavigationTypeTyped: QWebEnginePage.NavigationType = ...  # 0x1
    PermissionGrantedByUser: QWebEnginePage.PermissionPolicy = ...  # 0x1
    WarningMessageLevel: QWebEnginePage.JavaScriptConsoleMessageLevel = ...  # 0x1
    WebBrowserTab: QWebEnginePage.WebWindowType = ...  # 0x1
    CrashedTerminationStatus: QWebEnginePage.RenderProcessTerminationStatus = ...  # 0x2
    ErrorMessageLevel: QWebEnginePage.JavaScriptConsoleMessageLevel = ...  # 0x2
    FindCaseSensitively: QWebEnginePage.FindFlag = ...  # 0x2
    MediaAudioCapture: QWebEnginePage.Feature = ...  # 0x2
    NavigationTypeFormSubmitted: QWebEnginePage.NavigationType = ...  # 0x2
    PermissionDeniedByUser: QWebEnginePage.PermissionPolicy = ...  # 0x2
    Stop: QWebEnginePage.WebAction = ...  # 0x2
    WebDialog: QWebEnginePage.WebWindowType = ...  # 0x2
    KilledTerminationStatus: QWebEnginePage.RenderProcessTerminationStatus = ...  # 0x3
    MediaVideoCapture: QWebEnginePage.Feature = ...  # 0x3
    NavigationTypeBackForward: QWebEnginePage.NavigationType = ...  # 0x3
    Reload: QWebEnginePage.WebAction = ...  # 0x3
    WebBrowserBackgroundTab: QWebEnginePage.WebWindowType = ...  # 0x3
    Cut: QWebEnginePage.WebAction = ...  # 0x4
    MediaAudioVideoCapture: QWebEnginePage.Feature = ...  # 0x4
    NavigationTypeReload: QWebEnginePage.NavigationType = ...  # 0x4
    Copy: QWebEnginePage.WebAction = ...  # 0x5
    MouseLock: QWebEnginePage.Feature = ...  # 0x5
    NavigationTypeOther: QWebEnginePage.NavigationType = ...  # 0x5
    DesktopVideoCapture: QWebEnginePage.Feature = ...  # 0x6
    NavigationTypeRedirect: QWebEnginePage.NavigationType = ...  # 0x6
    Paste: QWebEnginePage.WebAction = ...  # 0x6
    DesktopAudioVideoCapture: QWebEnginePage.Feature = ...  # 0x7
    Undo: QWebEnginePage.WebAction = ...  # 0x7
    Redo: QWebEnginePage.WebAction = ...  # 0x8
    SelectAll: QWebEnginePage.WebAction = ...  # 0x9
    ReloadAndBypassCache: QWebEnginePage.WebAction = ...  # 0xa
    PasteAndMatchStyle: QWebEnginePage.WebAction = ...  # 0xb
    OpenLinkInThisWindow: QWebEnginePage.WebAction = ...  # 0xc
    OpenLinkInNewWindow: QWebEnginePage.WebAction = ...  # 0xd
    OpenLinkInNewTab: QWebEnginePage.WebAction = ...  # 0xe
    CopyLinkToClipboard: QWebEnginePage.WebAction = ...  # 0xf
    DownloadLinkToDisk: QWebEnginePage.WebAction = ...  # 0x10
    CopyImageToClipboard: QWebEnginePage.WebAction = ...  # 0x11
    CopyImageUrlToClipboard: QWebEnginePage.WebAction = ...  # 0x12
    DownloadImageToDisk: QWebEnginePage.WebAction = ...  # 0x13
    CopyMediaUrlToClipboard: QWebEnginePage.WebAction = ...  # 0x14
    ToggleMediaControls: QWebEnginePage.WebAction = ...  # 0x15
    ToggleMediaLoop: QWebEnginePage.WebAction = ...  # 0x16
    ToggleMediaPlayPause: QWebEnginePage.WebAction = ...  # 0x17
    ToggleMediaMute: QWebEnginePage.WebAction = ...  # 0x18
    DownloadMediaToDisk: QWebEnginePage.WebAction = ...  # 0x19
    InspectElement: QWebEnginePage.WebAction = ...  # 0x1a
    ExitFullScreen: QWebEnginePage.WebAction = ...  # 0x1b
    RequestClose: QWebEnginePage.WebAction = ...  # 0x1c
    Unselect: QWebEnginePage.WebAction = ...  # 0x1d
    SavePage: QWebEnginePage.WebAction = ...  # 0x1e
    OpenLinkInNewBackgroundTab: QWebEnginePage.WebAction = ...  # 0x1f
    ViewSource: QWebEnginePage.WebAction = ...  # 0x20
    ToggleBold: QWebEnginePage.WebAction = ...  # 0x21
    ToggleItalic: QWebEnginePage.WebAction = ...  # 0x22
    ToggleUnderline: QWebEnginePage.WebAction = ...  # 0x23
    ToggleStrikethrough: QWebEnginePage.WebAction = ...  # 0x24
    AlignLeft: QWebEnginePage.WebAction = ...  # 0x25
    AlignCenter: QWebEnginePage.WebAction = ...  # 0x26
    AlignRight: QWebEnginePage.WebAction = ...  # 0x27
    AlignJustified: QWebEnginePage.WebAction = ...  # 0x28
    Indent: QWebEnginePage.WebAction = ...  # 0x29
    Outdent: QWebEnginePage.WebAction = ...  # 0x2a
    InsertOrderedList: QWebEnginePage.WebAction = ...  # 0x2b
    InsertUnorderedList: QWebEnginePage.WebAction = ...  # 0x2c
    WebActionCount: QWebEnginePage.WebAction = ...  # 0x2d

    class Feature(object):
        Notifications: QWebEnginePage.Feature = ...  # 0x0
        Geolocation: QWebEnginePage.Feature = ...  # 0x1
        MediaAudioCapture: QWebEnginePage.Feature = ...  # 0x2
        MediaVideoCapture: QWebEnginePage.Feature = ...  # 0x3
        MediaAudioVideoCapture: QWebEnginePage.Feature = ...  # 0x4
        MouseLock: QWebEnginePage.Feature = ...  # 0x5
        DesktopVideoCapture: QWebEnginePage.Feature = ...  # 0x6
        DesktopAudioVideoCapture: QWebEnginePage.Feature = ...  # 0x7

    class FileSelectionMode(object):
        FileSelectOpen: QWebEnginePage.FileSelectionMode = ...  # 0x0
        FileSelectOpenMultiple: QWebEnginePage.FileSelectionMode = ...  # 0x1

    class FindFlag(object):
        FindBackward: QWebEnginePage.FindFlag = ...  # 0x1
        FindCaseSensitively: QWebEnginePage.FindFlag = ...  # 0x2

        def __index__(self) -> int: ...
        def __init__(self, value: typing.Union[int, FindFlag] = ...) -> None: ...
        def __or__(self, other: typing.Union[int, FindFlag]) -> FindFlags: ...
        def __and__(self, other: typing.Union[int, FindFlag]) -> FindFlags: ...
        def __xor__(self, other: typing.Union[int, FindFlag]) -> FindFlags: ...
        def __ror__(self, other: typing.Union[int, FindFlag]) -> FindFlags: ...
        def __rand__(self, other: typing.Union[int, FindFlag]) -> FindFlags: ...
        def __rxor__(self, other: typing.Union[int, FindFlag]) -> FindFlags: ...
        def __ior__(self, other: typing.Union[int, FindFlag]) -> FindFlags: ...
        def __iand__(self, other: typing.Union[int, FindFlag]) -> FindFlags: ...
        def __ixor__(self, other: typing.Union[int, FindFlag]) -> FindFlags: ...
        def __invert__(self) -> FindFlags: ...

    class FindFlags(object):
        def __index__(self) -> int: ...
        def __init__(
            self, value: typing.Union[int, FindFlag, FindFlags] = ...
        ) -> None: ...
        def __or__(
            self, other: typing.Union[int, FindFlag, FindFlags]
        ) -> FindFlags: ...
        def __and__(
            self, other: typing.Union[int, FindFlag, FindFlags]
        ) -> FindFlags: ...
        def __xor__(
            self, other: typing.Union[int, FindFlag, FindFlags]
        ) -> FindFlags: ...
        def __ror__(
            self, other: typing.Union[int, FindFlag, FindFlags]
        ) -> FindFlags: ...
        def __rand__(
            self, other: typing.Union[int, FindFlag, FindFlags]
        ) -> FindFlags: ...
        def __rxor__(
            self, other: typing.Union[int, FindFlag, FindFlags]
        ) -> FindFlags: ...
        def __ior__(
            self, other: typing.Union[int, FindFlag, FindFlags]
        ) -> FindFlags: ...
        def __iand__(
            self, other: typing.Union[int, FindFlag, FindFlags]
        ) -> FindFlags: ...
        def __ixor__(
            self, other: typing.Union[int, FindFlag, FindFlags]
        ) -> FindFlags: ...
        def __invert__(self) -> FindFlags: ...

    class JavaScriptConsoleMessageLevel(object):
        InfoMessageLevel: QWebEnginePage.JavaScriptConsoleMessageLevel = ...  # 0x0
        WarningMessageLevel: QWebEnginePage.JavaScriptConsoleMessageLevel = ...  # 0x1
        ErrorMessageLevel: QWebEnginePage.JavaScriptConsoleMessageLevel = ...  # 0x2

    class LifecycleState(object):
        Active: QWebEnginePage.LifecycleState = ...  # 0x0
        Frozen: QWebEnginePage.LifecycleState = ...  # 0x1
        Discarded: QWebEnginePage.LifecycleState = ...  # 0x2

    class NavigationType(object):
        NavigationTypeLinkClicked: QWebEnginePage.NavigationType = ...  # 0x0
        NavigationTypeTyped: QWebEnginePage.NavigationType = ...  # 0x1
        NavigationTypeFormSubmitted: QWebEnginePage.NavigationType = ...  # 0x2
        NavigationTypeBackForward: QWebEnginePage.NavigationType = ...  # 0x3
        NavigationTypeReload: QWebEnginePage.NavigationType = ...  # 0x4
        NavigationTypeOther: QWebEnginePage.NavigationType = ...  # 0x5
        NavigationTypeRedirect: QWebEnginePage.NavigationType = ...  # 0x6

    class PermissionPolicy(object):
        PermissionUnknown: QWebEnginePage.PermissionPolicy = ...  # 0x0
        PermissionGrantedByUser: QWebEnginePage.PermissionPolicy = ...  # 0x1
        PermissionDeniedByUser: QWebEnginePage.PermissionPolicy = ...  # 0x2

    class RenderProcessTerminationStatus(object):
        NormalTerminationStatus: QWebEnginePage.RenderProcessTerminationStatus = (
            ...
        )  # 0x0
        AbnormalTerminationStatus: QWebEnginePage.RenderProcessTerminationStatus = (
            ...
        )  # 0x1
        CrashedTerminationStatus: QWebEnginePage.RenderProcessTerminationStatus = (
            ...
        )  # 0x2
        KilledTerminationStatus: QWebEnginePage.RenderProcessTerminationStatus = (
            ...
        )  # 0x3

    class WebAction(object):
        NoWebAction: QWebEnginePage.WebAction = ...  # -0x1
        Back: QWebEnginePage.WebAction = ...  # 0x0
        Forward: QWebEnginePage.WebAction = ...  # 0x1
        Stop: QWebEnginePage.WebAction = ...  # 0x2
        Reload: QWebEnginePage.WebAction = ...  # 0x3
        Cut: QWebEnginePage.WebAction = ...  # 0x4
        Copy: QWebEnginePage.WebAction = ...  # 0x5
        Paste: QWebEnginePage.WebAction = ...  # 0x6
        Undo: QWebEnginePage.WebAction = ...  # 0x7
        Redo: QWebEnginePage.WebAction = ...  # 0x8
        SelectAll: QWebEnginePage.WebAction = ...  # 0x9
        ReloadAndBypassCache: QWebEnginePage.WebAction = ...  # 0xa
        PasteAndMatchStyle: QWebEnginePage.WebAction = ...  # 0xb
        OpenLinkInThisWindow: QWebEnginePage.WebAction = ...  # 0xc
        OpenLinkInNewWindow: QWebEnginePage.WebAction = ...  # 0xd
        OpenLinkInNewTab: QWebEnginePage.WebAction = ...  # 0xe
        CopyLinkToClipboard: QWebEnginePage.WebAction = ...  # 0xf
        DownloadLinkToDisk: QWebEnginePage.WebAction = ...  # 0x10
        CopyImageToClipboard: QWebEnginePage.WebAction = ...  # 0x11
        CopyImageUrlToClipboard: QWebEnginePage.WebAction = ...  # 0x12
        DownloadImageToDisk: QWebEnginePage.WebAction = ...  # 0x13
        CopyMediaUrlToClipboard: QWebEnginePage.WebAction = ...  # 0x14
        ToggleMediaControls: QWebEnginePage.WebAction = ...  # 0x15
        ToggleMediaLoop: QWebEnginePage.WebAction = ...  # 0x16
        ToggleMediaPlayPause: QWebEnginePage.WebAction = ...  # 0x17
        ToggleMediaMute: QWebEnginePage.WebAction = ...  # 0x18
        DownloadMediaToDisk: QWebEnginePage.WebAction = ...  # 0x19
        InspectElement: QWebEnginePage.WebAction = ...  # 0x1a
        ExitFullScreen: QWebEnginePage.WebAction = ...  # 0x1b
        RequestClose: QWebEnginePage.WebAction = ...  # 0x1c
        Unselect: QWebEnginePage.WebAction = ...  # 0x1d
        SavePage: QWebEnginePage.WebAction = ...  # 0x1e
        OpenLinkInNewBackgroundTab: QWebEnginePage.WebAction = ...  # 0x1f
        ViewSource: QWebEnginePage.WebAction = ...  # 0x20
        ToggleBold: QWebEnginePage.WebAction = ...  # 0x21
        ToggleItalic: QWebEnginePage.WebAction = ...  # 0x22
        ToggleUnderline: QWebEnginePage.WebAction = ...  # 0x23
        ToggleStrikethrough: QWebEnginePage.WebAction = ...  # 0x24
        AlignLeft: QWebEnginePage.WebAction = ...  # 0x25
        AlignCenter: QWebEnginePage.WebAction = ...  # 0x26
        AlignRight: QWebEnginePage.WebAction = ...  # 0x27
        AlignJustified: QWebEnginePage.WebAction = ...  # 0x28
        Indent: QWebEnginePage.WebAction = ...  # 0x29
        Outdent: QWebEnginePage.WebAction = ...  # 0x2a
        InsertOrderedList: QWebEnginePage.WebAction = ...  # 0x2b
        InsertUnorderedList: QWebEnginePage.WebAction = ...  # 0x2c
        WebActionCount: QWebEnginePage.WebAction = ...  # 0x2d

    class WebWindowType(object):
        WebBrowserWindow: QWebEnginePage.WebWindowType = ...  # 0x0
        WebBrowserTab: QWebEnginePage.WebWindowType = ...  # 0x1
        WebDialog: QWebEnginePage.WebWindowType = ...  # 0x2
        WebBrowserBackgroundTab: QWebEnginePage.WebWindowType = ...  # 0x3
    @typing.overload
    def __init__(
        self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        profile: PySide2.QtWebEngineWidgets.QWebEngineProfile,
        parent: typing.Optional[PySide2.QtCore.QObject] = ...,
    ) -> None: ...
    def acceptNavigationRequest(
        self,
        url: PySide2.QtCore.QUrl,
        type: PySide2.QtWebEngineWidgets.QWebEnginePage.NavigationType,
        isMainFrame: bool,
    ) -> bool: ...
    def action(
        self, action: PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction
    ) -> PySide2.QtWidgets.QAction: ...
    def backgroundColor(self) -> PySide2.QtGui.QColor: ...
    def certificateError(
        self, certificateError: PySide2.QtWebEngineWidgets.QWebEngineCertificateError
    ) -> bool: ...
    def chooseFiles(
        self,
        mode: PySide2.QtWebEngineWidgets.QWebEnginePage.FileSelectionMode,
        oldFiles: typing.Sequence,
        acceptedMimeTypes: typing.Sequence,
    ) -> typing.List: ...
    def contentsSize(self) -> PySide2.QtCore.QSizeF: ...
    def contextMenuData(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineContextMenuData: ...
    def createStandardContextMenu(self) -> PySide2.QtWidgets.QMenu: ...
    def createWindow(
        self, type: PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType
    ) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def devToolsPage(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def download(self, url: PySide2.QtCore.QUrl, filename: str = ...) -> None: ...
    def event(self, arg__1: PySide2.QtCore.QEvent) -> bool: ...
    @typing.overload
    def findText(
        self,
        arg__1: str,
        arg__2: PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags,
        arg__3: object,
    ) -> None: ...
    @typing.overload
    def findText(
        self,
        subString: str,
        options: PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags = ...,
    ) -> None: ...
    def hasSelection(self) -> bool: ...
    def history(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistory: ...
    def icon(self) -> PySide2.QtGui.QIcon: ...
    def iconUrl(self) -> PySide2.QtCore.QUrl: ...
    def inspectedPage(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def isAudioMuted(self) -> bool: ...
    def isVisible(self) -> bool: ...
    def javaScriptAlert(
        self, securityOrigin: PySide2.QtCore.QUrl, msg: str
    ) -> None: ...
    def javaScriptConfirm(
        self, securityOrigin: PySide2.QtCore.QUrl, msg: str
    ) -> bool: ...
    def javaScriptConsoleMessage(
        self,
        level: PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel,
        message: str,
        lineNumber: int,
        sourceID: str,
    ) -> None: ...
    def javaScriptPrompt(
        self, securityOrigin: PySide2.QtCore.QUrl, msg: str, defaultValue: str
    ) -> typing.Tuple: ...
    def lifecycleState(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEnginePage.LifecycleState: ...
    @typing.overload
    def load(self, request: PySide2.QtWebEngineCore.QWebEngineHttpRequest) -> None: ...
    @typing.overload
    def load(self, url: PySide2.QtCore.QUrl) -> None: ...
    def print(
        self, arg__1: PySide2.QtPrintSupport.QPrinter, arg__2: object
    ) -> None: ...
    @typing.overload
    def printToPdf(self, arg__1: object, arg__2: PySide2.QtGui.QPageLayout) -> None: ...
    @typing.overload
    def printToPdf(
        self, filePath: str, layout: PySide2.QtGui.QPageLayout = ...
    ) -> None: ...
    def profile(self) -> PySide2.QtWebEngineWidgets.QWebEngineProfile: ...
    def recentlyAudible(self) -> bool: ...
    def recommendedState(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEnginePage.LifecycleState: ...
    def renderProcessPid(self) -> int: ...
    def replaceMisspelledWord(self, replacement: str) -> None: ...
    def requestedUrl(self) -> PySide2.QtCore.QUrl: ...
    @typing.overload
    def runJavaScript(self, arg__1: str, arg__2: int, arg__3: object) -> None: ...
    @typing.overload
    def runJavaScript(self, scriptSource: str) -> None: ...
    @typing.overload
    def runJavaScript(self, scriptSource: str, worldId: int) -> None: ...
    def save(
        self,
        filePath: str,
        format: PySide2.QtWebEngineWidgets.QWebEngineDownloadItem.SavePageFormat = ...,
    ) -> None: ...
    def scripts(self) -> PySide2.QtWebEngineWidgets.QWebEngineScriptCollection: ...
    def scrollPosition(self) -> PySide2.QtCore.QPointF: ...
    def selectedText(self) -> str: ...
    def setAudioMuted(self, muted: bool) -> None: ...
    def setBackgroundColor(
        self,
        color: Union[PySide2.QtGui.QColor, PySide2.QtCore.Qt.GlobalColor, str, int],
    ) -> None: ...
    def setContent(
        self,
        data: PySide2.QtCore.QByteArray,
        mimeType: str = ...,
        baseUrl: PySide2.QtCore.QUrl = ...,
    ) -> None: ...
    def setDevToolsPage(
        self, page: PySide2.QtWebEngineWidgets.QWebEnginePage
    ) -> None: ...
    def setFeaturePermission(
        self,
        securityOrigin: PySide2.QtCore.QUrl,
        feature: PySide2.QtWebEngineWidgets.QWebEnginePage.Feature,
        policy: PySide2.QtWebEngineWidgets.QWebEnginePage.PermissionPolicy,
    ) -> None: ...
    def setHtml(self, html: str, baseUrl: PySide2.QtCore.QUrl = ...) -> None: ...
    def setInspectedPage(
        self, page: PySide2.QtWebEngineWidgets.QWebEnginePage
    ) -> None: ...
    def setLifecycleState(
        self, state: PySide2.QtWebEngineWidgets.QWebEnginePage.LifecycleState
    ) -> None: ...
    def setUrl(self, url: PySide2.QtCore.QUrl) -> None: ...
    def setUrlRequestInterceptor(
        self, interceptor: PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor
    ) -> None: ...
    def setView(self, view: PySide2.QtWidgets.QWidget) -> None: ...
    def setVisible(self, visible: bool) -> None: ...
    @typing.overload
    def setWebChannel(self, arg__1: PySide2.QtWebChannel.QWebChannel) -> None: ...
    @typing.overload
    def setWebChannel(
        self, arg__1: PySide2.QtWebChannel.QWebChannel, worldId: int
    ) -> None: ...
    def setZoomFactor(self, factor: float) -> None: ...
    def settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def title(self) -> str: ...
    def toHtml(self, arg__1: object) -> None: ...
    def toPlainText(self, arg__1: object) -> None: ...
    def triggerAction(
        self,
        action: PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction,
        checked: bool = ...,
    ) -> None: ...
    def url(self) -> PySide2.QtCore.QUrl: ...
    def view(self) -> PySide2.QtWidgets.QWidget: ...
    def webChannel(self) -> PySide2.QtWebChannel.QWebChannel: ...
    def zoomFactor(self) -> float: ...

class QWebEngineProfile(PySide2.QtCore.QObject):
    downloadRequested: PySide2.QtCore.Signal

    MemoryHttpCache: QWebEngineProfile.HttpCacheType = ...  # 0x0
    NoPersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...  # 0x0
    AllowPersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...  # 0x1
    DiskHttpCache: QWebEngineProfile.HttpCacheType = ...  # 0x1
    ForcePersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...  # 0x2
    NoCache: QWebEngineProfile.HttpCacheType = ...  # 0x2

    class HttpCacheType(object):
        MemoryHttpCache: QWebEngineProfile.HttpCacheType = ...  # 0x0
        DiskHttpCache: QWebEngineProfile.HttpCacheType = ...  # 0x1
        NoCache: QWebEngineProfile.HttpCacheType = ...  # 0x2

    class PersistentCookiesPolicy(object):
        NoPersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...  # 0x0
        AllowPersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...  # 0x1
        ForcePersistentCookies: QWebEngineProfile.PersistentCookiesPolicy = ...  # 0x2
    @typing.overload
    def __init__(
        self, name: str, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
    ) -> None: ...
    def cachePath(self) -> str: ...
    def clearAllVisitedLinks(self) -> None: ...
    def clearHttpCache(self) -> None: ...
    def clearVisitedLinks(self, urls: typing.Sequence) -> None: ...
    def cookieStore(self) -> PySide2.QtWebEngineCore.QWebEngineCookieStore: ...
    @staticmethod
    def defaultProfile() -> PySide2.QtWebEngineWidgets.QWebEngineProfile: ...
    def downloadPath(self) -> str: ...
    def httpAcceptLanguage(self) -> str: ...
    def httpCacheMaximumSize(self) -> int: ...
    def httpCacheType(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType: ...
    def httpUserAgent(self) -> str: ...
    def installUrlSchemeHandler(
        self,
        scheme: PySide2.QtCore.QByteArray,
        arg__2: PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler,
    ) -> None: ...
    def isOffTheRecord(self) -> bool: ...
    def isSpellCheckEnabled(self) -> bool: ...
    def isUsedForGlobalCertificateVerification(self) -> bool: ...
    def persistentCookiesPolicy(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy: ...
    def persistentStoragePath(self) -> str: ...
    def removeAllUrlSchemeHandlers(self) -> None: ...
    def removeUrlScheme(self, scheme: PySide2.QtCore.QByteArray) -> None: ...
    def removeUrlSchemeHandler(
        self, arg__1: PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler
    ) -> None: ...
    def scripts(self) -> PySide2.QtWebEngineWidgets.QWebEngineScriptCollection: ...
    def setCachePath(self, path: str) -> None: ...
    def setDownloadPath(self, path: str) -> None: ...
    def setHttpAcceptLanguage(self, httpAcceptLanguage: str) -> None: ...
    def setHttpCacheMaximumSize(self, maxSize: int) -> None: ...
    def setHttpCacheType(
        self, arg__1: PySide2.QtWebEngineWidgets.QWebEngineProfile.HttpCacheType
    ) -> None: ...
    def setHttpUserAgent(self, userAgent: str) -> None: ...
    def setPersistentCookiesPolicy(
        self,
        arg__1: PySide2.QtWebEngineWidgets.QWebEngineProfile.PersistentCookiesPolicy,
    ) -> None: ...
    def setPersistentStoragePath(self, path: str) -> None: ...
    def setRequestInterceptor(
        self, interceptor: PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor
    ) -> None: ...
    def setSpellCheckEnabled(self, enabled: bool) -> None: ...
    def setSpellCheckLanguages(self, languages: typing.Sequence) -> None: ...
    def setUrlRequestInterceptor(
        self, interceptor: PySide2.QtWebEngineCore.QWebEngineUrlRequestInterceptor
    ) -> None: ...
    def setUseForGlobalCertificateVerification(self, enabled: bool = ...) -> None: ...
    def settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def spellCheckLanguages(self) -> typing.List: ...
    def storageName(self) -> str: ...
    def urlSchemeHandler(
        self, arg__1: PySide2.QtCore.QByteArray
    ) -> PySide2.QtWebEngineCore.QWebEngineUrlSchemeHandler: ...
    def visitedLinksContainsUrl(self, url: PySide2.QtCore.QUrl) -> bool: ...

class QWebEngineScript(Shiboken.Object):
    Deferred: QWebEngineScript.InjectionPoint = ...  # 0x0
    MainWorld: QWebEngineScript.ScriptWorldId = ...  # 0x0
    ApplicationWorld: QWebEngineScript.ScriptWorldId = ...  # 0x1
    DocumentReady: QWebEngineScript.InjectionPoint = ...  # 0x1
    DocumentCreation: QWebEngineScript.InjectionPoint = ...  # 0x2
    UserWorld: QWebEngineScript.ScriptWorldId = ...  # 0x2

    class InjectionPoint(object):
        Deferred: QWebEngineScript.InjectionPoint = ...  # 0x0
        DocumentReady: QWebEngineScript.InjectionPoint = ...  # 0x1
        DocumentCreation: QWebEngineScript.InjectionPoint = ...  # 0x2

    class ScriptWorldId(object):
        MainWorld: QWebEngineScript.ScriptWorldId = ...  # 0x0
        ApplicationWorld: QWebEngineScript.ScriptWorldId = ...  # 0x1
        UserWorld: QWebEngineScript.ScriptWorldId = ...  # 0x2
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: PySide2.QtWebEngineWidgets.QWebEngineScript) -> None: ...
    @staticmethod
    def __copy__() -> None: ...
    def injectionPoint(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint: ...
    def isNull(self) -> bool: ...
    def name(self) -> str: ...
    def runsOnSubFrames(self) -> bool: ...
    def setInjectionPoint(
        self, arg__1: PySide2.QtWebEngineWidgets.QWebEngineScript.InjectionPoint
    ) -> None: ...
    def setName(self, arg__1: str) -> None: ...
    def setRunsOnSubFrames(self, on: bool) -> None: ...
    def setSourceCode(self, arg__1: str) -> None: ...
    def setWorldId(self, arg__1: int) -> None: ...
    def sourceCode(self) -> str: ...
    def swap(self, other: PySide2.QtWebEngineWidgets.QWebEngineScript) -> None: ...
    def worldId(self) -> int: ...

class QWebEngineScriptCollection(Shiboken.Object):
    def clear(self) -> None: ...
    def contains(self, value: PySide2.QtWebEngineWidgets.QWebEngineScript) -> bool: ...
    def count(self) -> int: ...
    def findScript(self, name: str) -> PySide2.QtWebEngineWidgets.QWebEngineScript: ...
    def findScripts(self, name: str) -> typing.List: ...
    @typing.overload
    def insert(self, arg__1: PySide2.QtWebEngineWidgets.QWebEngineScript) -> None: ...
    @typing.overload
    def insert(self, list: typing.Sequence) -> None: ...
    def isEmpty(self) -> bool: ...
    def remove(self, arg__1: PySide2.QtWebEngineWidgets.QWebEngineScript) -> bool: ...
    def size(self) -> int: ...
    def toList(self) -> typing.List: ...

class QWebEngineSettings(Shiboken.Object):
    AutoLoadImages: QWebEngineSettings.WebAttribute = ...  # 0x0
    MinimumFontSize: QWebEngineSettings.FontSize = ...  # 0x0
    StandardFont: QWebEngineSettings.FontFamily = ...  # 0x0
    DisallowUnknownUrlSchemes: QWebEngineSettings.UnknownUrlSchemePolicy = ...  # 0x1
    FixedFont: QWebEngineSettings.FontFamily = ...  # 0x1
    JavascriptEnabled: QWebEngineSettings.WebAttribute = ...  # 0x1
    MinimumLogicalFontSize: QWebEngineSettings.FontSize = ...  # 0x1
    AllowUnknownUrlSchemesFromUserInteraction: QWebEngineSettings.UnknownUrlSchemePolicy = (
        ...
    )  # 0x2
    DefaultFontSize: QWebEngineSettings.FontSize = ...  # 0x2
    JavascriptCanOpenWindows: QWebEngineSettings.WebAttribute = ...  # 0x2
    SerifFont: QWebEngineSettings.FontFamily = ...  # 0x2
    AllowAllUnknownUrlSchemes: QWebEngineSettings.UnknownUrlSchemePolicy = ...  # 0x3
    DefaultFixedFontSize: QWebEngineSettings.FontSize = ...  # 0x3
    JavascriptCanAccessClipboard: QWebEngineSettings.WebAttribute = ...  # 0x3
    SansSerifFont: QWebEngineSettings.FontFamily = ...  # 0x3
    CursiveFont: QWebEngineSettings.FontFamily = ...  # 0x4
    LinksIncludedInFocusChain: QWebEngineSettings.WebAttribute = ...  # 0x4
    FantasyFont: QWebEngineSettings.FontFamily = ...  # 0x5
    LocalStorageEnabled: QWebEngineSettings.WebAttribute = ...  # 0x5
    LocalContentCanAccessRemoteUrls: QWebEngineSettings.WebAttribute = ...  # 0x6
    PictographFont: QWebEngineSettings.FontFamily = ...  # 0x6
    XSSAuditingEnabled: QWebEngineSettings.WebAttribute = ...  # 0x7
    SpatialNavigationEnabled: QWebEngineSettings.WebAttribute = ...  # 0x8
    LocalContentCanAccessFileUrls: QWebEngineSettings.WebAttribute = ...  # 0x9
    HyperlinkAuditingEnabled: QWebEngineSettings.WebAttribute = ...  # 0xa
    ScrollAnimatorEnabled: QWebEngineSettings.WebAttribute = ...  # 0xb
    ErrorPageEnabled: QWebEngineSettings.WebAttribute = ...  # 0xc
    PluginsEnabled: QWebEngineSettings.WebAttribute = ...  # 0xd
    FullScreenSupportEnabled: QWebEngineSettings.WebAttribute = ...  # 0xe
    ScreenCaptureEnabled: QWebEngineSettings.WebAttribute = ...  # 0xf
    WebGLEnabled: QWebEngineSettings.WebAttribute = ...  # 0x10
    Accelerated2dCanvasEnabled: QWebEngineSettings.WebAttribute = ...  # 0x11
    AutoLoadIconsForPage: QWebEngineSettings.WebAttribute = ...  # 0x12
    TouchIconsEnabled: QWebEngineSettings.WebAttribute = ...  # 0x13
    FocusOnNavigationEnabled: QWebEngineSettings.WebAttribute = ...  # 0x14
    PrintElementBackgrounds: QWebEngineSettings.WebAttribute = ...  # 0x15
    AllowRunningInsecureContent: QWebEngineSettings.WebAttribute = ...  # 0x16
    AllowGeolocationOnInsecureOrigins: QWebEngineSettings.WebAttribute = ...  # 0x17
    AllowWindowActivationFromJavaScript: QWebEngineSettings.WebAttribute = ...  # 0x18
    ShowScrollBars: QWebEngineSettings.WebAttribute = ...  # 0x19
    PlaybackRequiresUserGesture: QWebEngineSettings.WebAttribute = ...  # 0x1a
    WebRTCPublicInterfacesOnly: QWebEngineSettings.WebAttribute = ...  # 0x1b
    JavascriptCanPaste: QWebEngineSettings.WebAttribute = ...  # 0x1c
    DnsPrefetchEnabled: QWebEngineSettings.WebAttribute = ...  # 0x1d
    PdfViewerEnabled: QWebEngineSettings.WebAttribute = ...  # 0x1e

    class FontFamily(object):
        StandardFont: QWebEngineSettings.FontFamily = ...  # 0x0
        FixedFont: QWebEngineSettings.FontFamily = ...  # 0x1
        SerifFont: QWebEngineSettings.FontFamily = ...  # 0x2
        SansSerifFont: QWebEngineSettings.FontFamily = ...  # 0x3
        CursiveFont: QWebEngineSettings.FontFamily = ...  # 0x4
        FantasyFont: QWebEngineSettings.FontFamily = ...  # 0x5
        PictographFont: QWebEngineSettings.FontFamily = ...  # 0x6

    class FontSize(object):
        MinimumFontSize: QWebEngineSettings.FontSize = ...  # 0x0
        MinimumLogicalFontSize: QWebEngineSettings.FontSize = ...  # 0x1
        DefaultFontSize: QWebEngineSettings.FontSize = ...  # 0x2
        DefaultFixedFontSize: QWebEngineSettings.FontSize = ...  # 0x3

    class UnknownUrlSchemePolicy(object):
        DisallowUnknownUrlSchemes: QWebEngineSettings.UnknownUrlSchemePolicy = (
            ...
        )  # 0x1
        AllowUnknownUrlSchemesFromUserInteraction: QWebEngineSettings.UnknownUrlSchemePolicy = (
            ...
        )  # 0x2
        AllowAllUnknownUrlSchemes: QWebEngineSettings.UnknownUrlSchemePolicy = (
            ...
        )  # 0x3

    class WebAttribute(object):
        AutoLoadImages: QWebEngineSettings.WebAttribute = ...  # 0x0
        JavascriptEnabled: QWebEngineSettings.WebAttribute = ...  # 0x1
        JavascriptCanOpenWindows: QWebEngineSettings.WebAttribute = ...  # 0x2
        JavascriptCanAccessClipboard: QWebEngineSettings.WebAttribute = ...  # 0x3
        LinksIncludedInFocusChain: QWebEngineSettings.WebAttribute = ...  # 0x4
        LocalStorageEnabled: QWebEngineSettings.WebAttribute = ...  # 0x5
        LocalContentCanAccessRemoteUrls: QWebEngineSettings.WebAttribute = ...  # 0x6
        XSSAuditingEnabled: QWebEngineSettings.WebAttribute = ...  # 0x7
        SpatialNavigationEnabled: QWebEngineSettings.WebAttribute = ...  # 0x8
        LocalContentCanAccessFileUrls: QWebEngineSettings.WebAttribute = ...  # 0x9
        HyperlinkAuditingEnabled: QWebEngineSettings.WebAttribute = ...  # 0xa
        ScrollAnimatorEnabled: QWebEngineSettings.WebAttribute = ...  # 0xb
        ErrorPageEnabled: QWebEngineSettings.WebAttribute = ...  # 0xc
        PluginsEnabled: QWebEngineSettings.WebAttribute = ...  # 0xd
        FullScreenSupportEnabled: QWebEngineSettings.WebAttribute = ...  # 0xe
        ScreenCaptureEnabled: QWebEngineSettings.WebAttribute = ...  # 0xf
        WebGLEnabled: QWebEngineSettings.WebAttribute = ...  # 0x10
        Accelerated2dCanvasEnabled: QWebEngineSettings.WebAttribute = ...  # 0x11
        AutoLoadIconsForPage: QWebEngineSettings.WebAttribute = ...  # 0x12
        TouchIconsEnabled: QWebEngineSettings.WebAttribute = ...  # 0x13
        FocusOnNavigationEnabled: QWebEngineSettings.WebAttribute = ...  # 0x14
        PrintElementBackgrounds: QWebEngineSettings.WebAttribute = ...  # 0x15
        AllowRunningInsecureContent: QWebEngineSettings.WebAttribute = ...  # 0x16
        AllowGeolocationOnInsecureOrigins: QWebEngineSettings.WebAttribute = ...  # 0x17
        AllowWindowActivationFromJavaScript: QWebEngineSettings.WebAttribute = (
            ...
        )  # 0x18
        ShowScrollBars: QWebEngineSettings.WebAttribute = ...  # 0x19
        PlaybackRequiresUserGesture: QWebEngineSettings.WebAttribute = ...  # 0x1a
        WebRTCPublicInterfacesOnly: QWebEngineSettings.WebAttribute = ...  # 0x1b
        JavascriptCanPaste: QWebEngineSettings.WebAttribute = ...  # 0x1c
        DnsPrefetchEnabled: QWebEngineSettings.WebAttribute = ...  # 0x1d
        PdfViewerEnabled: QWebEngineSettings.WebAttribute = ...  # 0x1e
    @staticmethod
    def defaultSettings() -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def defaultTextEncoding(self) -> str: ...
    def fontFamily(
        self, which: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily
    ) -> str: ...
    def fontSize(
        self, type: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize
    ) -> int: ...
    @staticmethod
    def globalSettings() -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def resetAttribute(
        self, attr: PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute
    ) -> None: ...
    def resetFontFamily(
        self, which: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily
    ) -> None: ...
    def resetFontSize(
        self, type: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize
    ) -> None: ...
    def resetUnknownUrlSchemePolicy(self) -> None: ...
    def setAttribute(
        self, attr: PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute, on: bool
    ) -> None: ...
    def setDefaultTextEncoding(self, encoding: str) -> None: ...
    def setFontFamily(
        self,
        which: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontFamily,
        family: str,
    ) -> None: ...
    def setFontSize(
        self, type: PySide2.QtWebEngineWidgets.QWebEngineSettings.FontSize, size: int
    ) -> None: ...
    def setUnknownUrlSchemePolicy(
        self,
        policy: PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy,
    ) -> None: ...
    def testAttribute(
        self, attr: PySide2.QtWebEngineWidgets.QWebEngineSettings.WebAttribute
    ) -> bool: ...
    def unknownUrlSchemePolicy(
        self,
    ) -> PySide2.QtWebEngineWidgets.QWebEngineSettings.UnknownUrlSchemePolicy: ...

class QWebEngineView(PySide2.QtWidgets.QWidget):
    iconChanged: PySide2.QtCore.Signal
    iconUrlChanged: PySide2.QtCore.Signal
    loadFinished: PySide2.QtCore.Signal
    loadProgress: PySide2.QtCore.Signal
    loadStarted: PySide2.QtCore.Signal
    renderProcessTerminated: PySide2.QtCore.Signal
    selectionChanged: PySide2.QtCore.Signal
    titleChanged: PySide2.QtCore.Signal
    urlChanged: PySide2.QtCore.Signal

    def __init__(
        self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...
    ) -> None: ...
    def back(self) -> None: ...
    def closeEvent(self, arg__1: PySide2.QtGui.QCloseEvent) -> None: ...
    def contextMenuEvent(self, arg__1: PySide2.QtGui.QContextMenuEvent) -> None: ...
    def createWindow(
        self, type: PySide2.QtWebEngineWidgets.QWebEnginePage.WebWindowType
    ) -> PySide2.QtWebEngineWidgets.QWebEngineView: ...
    def dragEnterEvent(self, e: PySide2.QtGui.QDragEnterEvent) -> None: ...
    def dragLeaveEvent(self, e: PySide2.QtGui.QDragLeaveEvent) -> None: ...
    def dragMoveEvent(self, e: PySide2.QtGui.QDragMoveEvent) -> None: ...
    def dropEvent(self, e: PySide2.QtGui.QDropEvent) -> None: ...
    def event(self, arg__1: PySide2.QtCore.QEvent) -> bool: ...
    @typing.overload
    def findText(
        self,
        arg__1: str,
        arg__2: PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags,
        arg__3: object,
    ) -> None: ...
    @typing.overload
    def findText(
        self,
        subString: str,
        options: PySide2.QtWebEngineWidgets.QWebEnginePage.FindFlags = ...,
    ) -> None: ...
    def forward(self) -> None: ...
    def hasSelection(self) -> bool: ...
    def hideEvent(self, arg__1: PySide2.QtGui.QHideEvent) -> None: ...
    def history(self) -> PySide2.QtWebEngineWidgets.QWebEngineHistory: ...
    def icon(self) -> PySide2.QtGui.QIcon: ...
    def iconUrl(self) -> PySide2.QtCore.QUrl: ...
    @typing.overload
    def load(self, request: PySide2.QtWebEngineCore.QWebEngineHttpRequest) -> None: ...
    @typing.overload
    def load(self, url: PySide2.QtCore.QUrl) -> None: ...
    def page(self) -> PySide2.QtWebEngineWidgets.QWebEnginePage: ...
    def pageAction(
        self, action: PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction
    ) -> PySide2.QtWidgets.QAction: ...
    def reload(self) -> None: ...
    def selectedText(self) -> str: ...
    def setContent(
        self,
        data: PySide2.QtCore.QByteArray,
        mimeType: str = ...,
        baseUrl: PySide2.QtCore.QUrl = ...,
    ) -> None: ...
    def setHtml(self, html: str, baseUrl: PySide2.QtCore.QUrl = ...) -> None: ...
    def setPage(self, page: PySide2.QtWebEngineWidgets.QWebEnginePage) -> None: ...
    def setUrl(self, url: PySide2.QtCore.QUrl) -> None: ...
    def setZoomFactor(self, factor: float) -> None: ...
    def settings(self) -> PySide2.QtWebEngineWidgets.QWebEngineSettings: ...
    def showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None: ...
    def sizeHint(self) -> PySide2.QtCore.QSize: ...
    def stop(self) -> None: ...
    def title(self) -> str: ...
    def triggerPageAction(
        self,
        action: PySide2.QtWebEngineWidgets.QWebEnginePage.WebAction,
        checked: bool = ...,
    ) -> None: ...
    def url(self) -> PySide2.QtCore.QUrl: ...
    def zoomFactor(self) -> float: ...

# eof
