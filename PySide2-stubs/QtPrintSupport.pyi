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
PySide2.QtPrintSupport, except for defaults which are replaced by "...".
"""

import sys

# Module PySide2.QtPrintSupport
import PySide2
import typing

import shiboken2 as Shiboken

import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtWidgets
import PySide2.QtPrintSupport

class QAbstractPrintDialog(PySide2.QtWidgets.QDialog):
    AllPages: QAbstractPrintDialog.PrintRange = ...  # 0x0
    None_: QAbstractPrintDialog.PrintDialogOption = ...  # 0x0
    PrintToFile: QAbstractPrintDialog.PrintDialogOption = ...  # 0x1
    Selection: QAbstractPrintDialog.PrintRange = ...  # 0x1
    PageRange: QAbstractPrintDialog.PrintRange = ...  # 0x2
    PrintSelection: QAbstractPrintDialog.PrintDialogOption = ...  # 0x2
    CurrentPage: QAbstractPrintDialog.PrintRange = ...  # 0x3
    PrintPageRange: QAbstractPrintDialog.PrintDialogOption = ...  # 0x4
    PrintShowPageSize: QAbstractPrintDialog.PrintDialogOption = ...  # 0x8
    PrintCollateCopies: QAbstractPrintDialog.PrintDialogOption = ...  # 0x10
    DontUseSheet: QAbstractPrintDialog.PrintDialogOption = ...  # 0x20
    PrintCurrentPage: QAbstractPrintDialog.PrintDialogOption = ...  # 0x40

    class PrintDialogOption(object):
        None_: QAbstractPrintDialog.PrintDialogOption = ...  # 0x0
        PrintToFile: QAbstractPrintDialog.PrintDialogOption = ...  # 0x1
        PrintSelection: QAbstractPrintDialog.PrintDialogOption = ...  # 0x2
        PrintPageRange: QAbstractPrintDialog.PrintDialogOption = ...  # 0x4
        PrintShowPageSize: QAbstractPrintDialog.PrintDialogOption = ...  # 0x8
        PrintCollateCopies: QAbstractPrintDialog.PrintDialogOption = ...  # 0x10
        DontUseSheet: QAbstractPrintDialog.PrintDialogOption = ...  # 0x20
        PrintCurrentPage: QAbstractPrintDialog.PrintDialogOption = ...  # 0x40

        def __index__(self) -> int: ...
        def __init__(
            self, value: typing.Union[int, PrintDialogOption] = ...
        ) -> None: ...
        def __or__(
            self, other: typing.Union[int, PrintDialogOption]
        ) -> PrintDialogOptions: ...
        def __and__(
            self, other: typing.Union[int, PrintDialogOption]
        ) -> PrintDialogOptions: ...
        def __xor__(
            self, other: typing.Union[int, PrintDialogOption]
        ) -> PrintDialogOptions: ...
        def __ror__(
            self, other: typing.Union[int, PrintDialogOption]
        ) -> PrintDialogOptions: ...
        def __rand__(
            self, other: typing.Union[int, PrintDialogOption]
        ) -> PrintDialogOptions: ...
        def __rxor__(
            self, other: typing.Union[int, PrintDialogOption]
        ) -> PrintDialogOptions: ...
        def __ior__(
            self, other: typing.Union[int, PrintDialogOption]
        ) -> PrintDialogOptions: ...
        def __iand__(
            self, other: typing.Union[int, PrintDialogOption]
        ) -> PrintDialogOptions: ...
        def __ixor__(
            self, other: typing.Union[int, PrintDialogOption]
        ) -> PrintDialogOptions: ...
        def __invert__(self) -> PrintDialogOptions: ...

    class PrintDialogOptions(object):
        def __index__(self) -> int: ...
        def __init__(
            self, value: typing.Union[int, PrintDialogOption, PrintDialogOptions] = ...
        ) -> None: ...
        def __or__(
            self, other: typing.Union[int, PrintDialogOption, PrintDialogOptions]
        ) -> PrintDialogOptions: ...
        def __and__(
            self, other: typing.Union[int, PrintDialogOption, PrintDialogOptions]
        ) -> PrintDialogOptions: ...
        def __xor__(
            self, other: typing.Union[int, PrintDialogOption, PrintDialogOptions]
        ) -> PrintDialogOptions: ...
        def __ror__(
            self, other: typing.Union[int, PrintDialogOption, PrintDialogOptions]
        ) -> PrintDialogOptions: ...
        def __rand__(
            self, other: typing.Union[int, PrintDialogOption, PrintDialogOptions]
        ) -> PrintDialogOptions: ...
        def __rxor__(
            self, other: typing.Union[int, PrintDialogOption, PrintDialogOptions]
        ) -> PrintDialogOptions: ...
        def __ior__(
            self, other: typing.Union[int, PrintDialogOption, PrintDialogOptions]
        ) -> PrintDialogOptions: ...
        def __iand__(
            self, other: typing.Union[int, PrintDialogOption, PrintDialogOptions]
        ) -> PrintDialogOptions: ...
        def __ixor__(
            self, other: typing.Union[int, PrintDialogOption, PrintDialogOptions]
        ) -> PrintDialogOptions: ...
        def __invert__(self) -> PrintDialogOptions: ...

    class PrintRange(object):
        AllPages: QAbstractPrintDialog.PrintRange = ...  # 0x0
        Selection: QAbstractPrintDialog.PrintRange = ...  # 0x1
        PageRange: QAbstractPrintDialog.PrintRange = ...  # 0x2
        CurrentPage: QAbstractPrintDialog.PrintRange = ...  # 0x3
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
    ) -> None: ...
    def addEnabledOption(
        self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption
    ) -> None: ...
    def enabledOptions(
        self,
    ) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions: ...
    def fromPage(self) -> int: ...
    def isOptionEnabled(
        self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption
    ) -> bool: ...
    def maxPage(self) -> int: ...
    def minPage(self) -> int: ...
    def printRange(self) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange: ...
    def printer(self) -> PySide2.QtPrintSupport.QPrinter: ...
    def setEnabledOptions(
        self, options: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions
    ) -> None: ...
    def setFromTo(self, fromPage: int, toPage: int) -> None: ...
    def setMinMax(self, min: int, max: int) -> None: ...
    def setOptionTabs(self, tabs: typing.Sequence) -> None: ...
    def setPrintRange(
        self, range: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintRange
    ) -> None: ...
    def toPage(self) -> int: ...

class QPageSetupDialog(PySide2.QtWidgets.QDialog):
    @typing.overload
    def __init__(
        self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
    ) -> None: ...
    def done(self, result: int) -> None: ...
    def exec_(self) -> int: ...
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    def open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None: ...
    def printer(self) -> PySide2.QtPrintSupport.QPrinter: ...
    if sys.platform() == "win32":
        def setVisible(self, visible: bool) -> None: ...

class QPrintDialog(PySide2.QtPrintSupport.QAbstractPrintDialog):
    accepted: PySide2.QtCore.Signal

    @typing.overload
    def __init__(
        self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
    ) -> None: ...

    if sys.platform() == "darwin" or sys.platform() == "linux":
        def accept(self) -> None: ...

    def done(self, result: int) -> None: ...
    def exec_(self) -> int: ...
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    def open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None: ...
    def options(
        self,
    ) -> PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions: ...
    def setOption(
        self,
        option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption,
        on: bool = ...,
    ) -> None: ...
    def setOptions(
        self, options: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOptions
    ) -> None: ...
    def setVisible(self, visible: bool) -> None: ...
    def testOption(
        self, option: PySide2.QtPrintSupport.QAbstractPrintDialog.PrintDialogOption
    ) -> bool: ...

class QPrintEngine(Shiboken.Object):
    PPK_CollateCopies: QPrintEngine.PrintEnginePropertyKey = ...  # 0x0
    PPK_ColorMode: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1
    PPK_Creator: QPrintEngine.PrintEnginePropertyKey = ...  # 0x2
    PPK_DocumentName: QPrintEngine.PrintEnginePropertyKey = ...  # 0x3
    PPK_FullPage: QPrintEngine.PrintEnginePropertyKey = ...  # 0x4
    PPK_NumberOfCopies: QPrintEngine.PrintEnginePropertyKey = ...  # 0x5
    PPK_Orientation: QPrintEngine.PrintEnginePropertyKey = ...  # 0x6
    PPK_OutputFileName: QPrintEngine.PrintEnginePropertyKey = ...  # 0x7
    PPK_PageOrder: QPrintEngine.PrintEnginePropertyKey = ...  # 0x8
    PPK_PageRect: QPrintEngine.PrintEnginePropertyKey = ...  # 0x9
    PPK_PageSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0xa
    PPK_PaperSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0xa
    PPK_PaperRect: QPrintEngine.PrintEnginePropertyKey = ...  # 0xb
    PPK_PaperSource: QPrintEngine.PrintEnginePropertyKey = ...  # 0xc
    PPK_PrinterName: QPrintEngine.PrintEnginePropertyKey = ...  # 0xd
    PPK_PrinterProgram: QPrintEngine.PrintEnginePropertyKey = ...  # 0xe
    PPK_Resolution: QPrintEngine.PrintEnginePropertyKey = ...  # 0xf
    PPK_SelectionOption: QPrintEngine.PrintEnginePropertyKey = ...  # 0x10
    PPK_SupportedResolutions: QPrintEngine.PrintEnginePropertyKey = ...  # 0x11
    PPK_WindowsPageSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0x12
    PPK_FontEmbedding: QPrintEngine.PrintEnginePropertyKey = ...  # 0x13
    PPK_Duplex: QPrintEngine.PrintEnginePropertyKey = ...  # 0x14
    PPK_PaperSources: QPrintEngine.PrintEnginePropertyKey = ...  # 0x15
    PPK_CustomPaperSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0x16
    PPK_PageMargins: QPrintEngine.PrintEnginePropertyKey = ...  # 0x17
    PPK_CopyCount: QPrintEngine.PrintEnginePropertyKey = ...  # 0x18
    PPK_SupportsMultipleCopies: QPrintEngine.PrintEnginePropertyKey = ...  # 0x19
    PPK_PaperName: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1a
    PPK_QPageSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1b
    PPK_QPageMargins: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1c
    PPK_QPageLayout: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1d
    PPK_CustomBase: QPrintEngine.PrintEnginePropertyKey = ...  # 0xff00

    class PrintEnginePropertyKey(object):
        PPK_CollateCopies: QPrintEngine.PrintEnginePropertyKey = ...  # 0x0
        PPK_ColorMode: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1
        PPK_Creator: QPrintEngine.PrintEnginePropertyKey = ...  # 0x2
        PPK_DocumentName: QPrintEngine.PrintEnginePropertyKey = ...  # 0x3
        PPK_FullPage: QPrintEngine.PrintEnginePropertyKey = ...  # 0x4
        PPK_NumberOfCopies: QPrintEngine.PrintEnginePropertyKey = ...  # 0x5
        PPK_Orientation: QPrintEngine.PrintEnginePropertyKey = ...  # 0x6
        PPK_OutputFileName: QPrintEngine.PrintEnginePropertyKey = ...  # 0x7
        PPK_PageOrder: QPrintEngine.PrintEnginePropertyKey = ...  # 0x8
        PPK_PageRect: QPrintEngine.PrintEnginePropertyKey = ...  # 0x9
        PPK_PageSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0xa
        PPK_PaperSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0xa
        PPK_PaperRect: QPrintEngine.PrintEnginePropertyKey = ...  # 0xb
        PPK_PaperSource: QPrintEngine.PrintEnginePropertyKey = ...  # 0xc
        PPK_PrinterName: QPrintEngine.PrintEnginePropertyKey = ...  # 0xd
        PPK_PrinterProgram: QPrintEngine.PrintEnginePropertyKey = ...  # 0xe
        PPK_Resolution: QPrintEngine.PrintEnginePropertyKey = ...  # 0xf
        PPK_SelectionOption: QPrintEngine.PrintEnginePropertyKey = ...  # 0x10
        PPK_SupportedResolutions: QPrintEngine.PrintEnginePropertyKey = ...  # 0x11
        PPK_WindowsPageSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0x12
        PPK_FontEmbedding: QPrintEngine.PrintEnginePropertyKey = ...  # 0x13
        PPK_Duplex: QPrintEngine.PrintEnginePropertyKey = ...  # 0x14
        PPK_PaperSources: QPrintEngine.PrintEnginePropertyKey = ...  # 0x15
        PPK_CustomPaperSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0x16
        PPK_PageMargins: QPrintEngine.PrintEnginePropertyKey = ...  # 0x17
        PPK_CopyCount: QPrintEngine.PrintEnginePropertyKey = ...  # 0x18
        PPK_SupportsMultipleCopies: QPrintEngine.PrintEnginePropertyKey = ...  # 0x19
        PPK_PaperName: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1a
        PPK_QPageSize: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1b
        PPK_QPageMargins: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1c
        PPK_QPageLayout: QPrintEngine.PrintEnginePropertyKey = ...  # 0x1d
        PPK_CustomBase: QPrintEngine.PrintEnginePropertyKey = ...  # 0xff00
    def __init__(self) -> None: ...
    def abort(self) -> bool: ...
    def metric(self, arg__1: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def newPage(self) -> bool: ...
    def printerState(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState: ...
    def property(
        self, key: PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey
    ) -> typing.Any: ...
    def setProperty(
        self,
        key: PySide2.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey,
        value: typing.Any,
    ) -> None: ...

class QPrintPreviewDialog(PySide2.QtWidgets.QDialog):
    paintRequested: PySide2.QtCore.Signal

    @typing.overload
    def __init__(
        self,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        flags: PySide2.QtCore.Qt.WindowFlags = ...,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        flags: PySide2.QtCore.Qt.WindowFlags = ...,
    ) -> None: ...
    def done(self, result: int) -> None: ...
    @typing.overload
    def open(self) -> None: ...
    @typing.overload
    def open(self, receiver: PySide2.QtCore.QObject, member: bytes) -> None: ...
    def printer(self) -> PySide2.QtPrintSupport.QPrinter: ...
    def setVisible(self, visible: bool) -> None: ...

class QPrintPreviewWidget(PySide2.QtWidgets.QWidget):
    paintRequested: PySide2.QtCore.Signal
    previewChanged: PySide2.QtCore.Signal

    CustomZoom: QPrintPreviewWidget.ZoomMode = ...  # 0x0
    SinglePageView: QPrintPreviewWidget.ViewMode = ...  # 0x0
    FacingPagesView: QPrintPreviewWidget.ViewMode = ...  # 0x1
    FitToWidth: QPrintPreviewWidget.ZoomMode = ...  # 0x1
    AllPagesView: QPrintPreviewWidget.ViewMode = ...  # 0x2
    FitInView: QPrintPreviewWidget.ZoomMode = ...  # 0x2

    class ViewMode(object):
        SinglePageView: QPrintPreviewWidget.ViewMode = ...  # 0x0
        FacingPagesView: QPrintPreviewWidget.ViewMode = ...  # 0x1
        AllPagesView: QPrintPreviewWidget.ViewMode = ...  # 0x2

    class ZoomMode(object):
        CustomZoom: QPrintPreviewWidget.ZoomMode = ...  # 0x0
        FitToWidth: QPrintPreviewWidget.ZoomMode = ...  # 0x1
        FitInView: QPrintPreviewWidget.ZoomMode = ...  # 0x2
    @typing.overload
    def __init__(
        self,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        flags: PySide2.QtCore.Qt.WindowFlags = ...,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinter,
        parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        flags: PySide2.QtCore.Qt.WindowFlags = ...,
    ) -> None: ...
    def currentPage(self) -> int: ...
    def fitInView(self) -> None: ...
    def fitToWidth(self) -> None: ...
    def orientation(self) -> PySide2.QtPrintSupport.QPrinter.Orientation: ...
    def pageCount(self) -> int: ...
    def print_(self) -> None: ...
    def setAllPagesViewMode(self) -> None: ...
    def setCurrentPage(self, pageNumber: int) -> None: ...
    def setFacingPagesViewMode(self) -> None: ...
    def setLandscapeOrientation(self) -> None: ...
    def setOrientation(
        self, orientation: PySide2.QtPrintSupport.QPrinter.Orientation
    ) -> None: ...
    def setPortraitOrientation(self) -> None: ...
    def setSinglePageViewMode(self) -> None: ...
    def setViewMode(
        self, viewMode: PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode
    ) -> None: ...
    def setVisible(self, visible: bool) -> None: ...
    def setZoomFactor(self, zoomFactor: float) -> None: ...
    def setZoomMode(
        self, zoomMode: PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode
    ) -> None: ...
    def updatePreview(self) -> None: ...
    def viewMode(self) -> PySide2.QtPrintSupport.QPrintPreviewWidget.ViewMode: ...
    def zoomFactor(self) -> float: ...
    def zoomIn(self, zoom: float = ...) -> None: ...
    def zoomMode(self) -> PySide2.QtPrintSupport.QPrintPreviewWidget.ZoomMode: ...
    def zoomOut(self, zoom: float = ...) -> None: ...

class QPrinter(PySide2.QtGui.QPagedPaintDevice):
    AllPages: QPrinter.PrintRange = ...  # 0x0
    DuplexNone: QPrinter.DuplexMode = ...  # 0x0
    FirstPageFirst: QPrinter.PageOrder = ...  # 0x0
    GrayScale: QPrinter.ColorMode = ...  # 0x0
    Idle: QPrinter.PrinterState = ...  # 0x0
    Millimeter: QPrinter.Unit = ...  # 0x0
    NativeFormat: QPrinter.OutputFormat = ...  # 0x0
    OnlyOne: QPrinter.PaperSource = ...  # 0x0
    Portrait: QPrinter.Orientation = ...  # 0x0
    ScreenResolution: QPrinter.PrinterMode = ...  # 0x0
    Upper: QPrinter.PaperSource = ...  # 0x0
    Active: QPrinter.PrinterState = ...  # 0x1
    Color: QPrinter.ColorMode = ...  # 0x1
    DuplexAuto: QPrinter.DuplexMode = ...  # 0x1
    Landscape: QPrinter.Orientation = ...  # 0x1
    LastPageFirst: QPrinter.PageOrder = ...  # 0x1
    Lower: QPrinter.PaperSource = ...  # 0x1
    PdfFormat: QPrinter.OutputFormat = ...  # 0x1
    Point: QPrinter.Unit = ...  # 0x1
    PrinterResolution: QPrinter.PrinterMode = ...  # 0x1
    Selection: QPrinter.PrintRange = ...  # 0x1
    Aborted: QPrinter.PrinterState = ...  # 0x2
    DuplexLongSide: QPrinter.DuplexMode = ...  # 0x2
    HighResolution: QPrinter.PrinterMode = ...  # 0x2
    Inch: QPrinter.Unit = ...  # 0x2
    Middle: QPrinter.PaperSource = ...  # 0x2
    PageRange: QPrinter.PrintRange = ...  # 0x2
    CurrentPage: QPrinter.PrintRange = ...  # 0x3
    DuplexShortSide: QPrinter.DuplexMode = ...  # 0x3
    Error: QPrinter.PrinterState = ...  # 0x3
    Manual: QPrinter.PaperSource = ...  # 0x3
    Pica: QPrinter.Unit = ...  # 0x3
    Didot: QPrinter.Unit = ...  # 0x4
    Envelope: QPrinter.PaperSource = ...  # 0x4
    Cicero: QPrinter.Unit = ...  # 0x5
    EnvelopeManual: QPrinter.PaperSource = ...  # 0x5
    Auto: QPrinter.PaperSource = ...  # 0x6
    DevicePixel: QPrinter.Unit = ...  # 0x6
    Tractor: QPrinter.PaperSource = ...  # 0x7
    SmallFormat: QPrinter.PaperSource = ...  # 0x8
    LargeFormat: QPrinter.PaperSource = ...  # 0x9
    LargeCapacity: QPrinter.PaperSource = ...  # 0xa
    Cassette: QPrinter.PaperSource = ...  # 0xb
    FormSource: QPrinter.PaperSource = ...  # 0xc
    MaxPageSource: QPrinter.PaperSource = ...  # 0xd
    CustomSource: QPrinter.PaperSource = ...  # 0xe
    LastPaperSource: QPrinter.PaperSource = ...  # 0xe

    class ColorMode(object):
        GrayScale: QPrinter.ColorMode = ...  # 0x0
        Color: QPrinter.ColorMode = ...  # 0x1

    class DuplexMode(object):
        DuplexNone: QPrinter.DuplexMode = ...  # 0x0
        DuplexAuto: QPrinter.DuplexMode = ...  # 0x1
        DuplexLongSide: QPrinter.DuplexMode = ...  # 0x2
        DuplexShortSide: QPrinter.DuplexMode = ...  # 0x3

    class Orientation(object):
        Portrait: QPrinter.Orientation = ...  # 0x0
        Landscape: QPrinter.Orientation = ...  # 0x1

    class OutputFormat(object):
        NativeFormat: QPrinter.OutputFormat = ...  # 0x0
        PdfFormat: QPrinter.OutputFormat = ...  # 0x1

    class PageOrder(object):
        FirstPageFirst: QPrinter.PageOrder = ...  # 0x0
        LastPageFirst: QPrinter.PageOrder = ...  # 0x1

    class PaperSource(object):
        OnlyOne: QPrinter.PaperSource = ...  # 0x0
        Upper: QPrinter.PaperSource = ...  # 0x0
        Lower: QPrinter.PaperSource = ...  # 0x1
        Middle: QPrinter.PaperSource = ...  # 0x2
        Manual: QPrinter.PaperSource = ...  # 0x3
        Envelope: QPrinter.PaperSource = ...  # 0x4
        EnvelopeManual: QPrinter.PaperSource = ...  # 0x5
        Auto: QPrinter.PaperSource = ...  # 0x6
        Tractor: QPrinter.PaperSource = ...  # 0x7
        SmallFormat: QPrinter.PaperSource = ...  # 0x8
        LargeFormat: QPrinter.PaperSource = ...  # 0x9
        LargeCapacity: QPrinter.PaperSource = ...  # 0xa
        Cassette: QPrinter.PaperSource = ...  # 0xb
        FormSource: QPrinter.PaperSource = ...  # 0xc
        MaxPageSource: QPrinter.PaperSource = ...  # 0xd
        CustomSource: QPrinter.PaperSource = ...  # 0xe
        LastPaperSource: QPrinter.PaperSource = ...  # 0xe

    class PrintRange(object):
        AllPages: QPrinter.PrintRange = ...  # 0x0
        Selection: QPrinter.PrintRange = ...  # 0x1
        PageRange: QPrinter.PrintRange = ...  # 0x2
        CurrentPage: QPrinter.PrintRange = ...  # 0x3

    class PrinterMode(object):
        ScreenResolution: QPrinter.PrinterMode = ...  # 0x0
        PrinterResolution: QPrinter.PrinterMode = ...  # 0x1
        HighResolution: QPrinter.PrinterMode = ...  # 0x2

    class PrinterState(object):
        Idle: QPrinter.PrinterState = ...  # 0x0
        Active: QPrinter.PrinterState = ...  # 0x1
        Aborted: QPrinter.PrinterState = ...  # 0x2
        Error: QPrinter.PrinterState = ...  # 0x3

    class Unit(object):
        Millimeter: QPrinter.Unit = ...  # 0x0
        Point: QPrinter.Unit = ...  # 0x1
        Inch: QPrinter.Unit = ...  # 0x2
        Pica: QPrinter.Unit = ...  # 0x3
        Didot: QPrinter.Unit = ...  # 0x4
        Cicero: QPrinter.Unit = ...  # 0x5
        DevicePixel: QPrinter.Unit = ...  # 0x6
    @typing.overload
    def __init__(
        self, mode: PySide2.QtPrintSupport.QPrinter.PrinterMode = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        printer: PySide2.QtPrintSupport.QPrinterInfo,
        mode: PySide2.QtPrintSupport.QPrinter.PrinterMode = ...,
    ) -> None: ...
    def abort(self) -> bool: ...
    def actualNumCopies(self) -> int: ...
    def collateCopies(self) -> bool: ...
    def colorMode(self) -> PySide2.QtPrintSupport.QPrinter.ColorMode: ...
    def copyCount(self) -> int: ...
    def creator(self) -> str: ...
    def devType(self) -> int: ...
    def docName(self) -> str: ...
    def doubleSidedPrinting(self) -> bool: ...
    def duplex(self) -> PySide2.QtPrintSupport.QPrinter.DuplexMode: ...
    def fontEmbeddingEnabled(self) -> bool: ...
    def fromPage(self) -> int: ...
    def fullPage(self) -> bool: ...
    def getPageMargins(
        self, unit: PySide2.QtPrintSupport.QPrinter.Unit
    ) -> typing.Tuple: ...
    def isValid(self) -> bool: ...
    def metric(self, arg__1: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def newPage(self) -> bool: ...
    def numCopies(self) -> int: ...
    def orientation(self) -> PySide2.QtPrintSupport.QPrinter.Orientation: ...
    def outputFileName(self) -> str: ...
    def outputFormat(self) -> PySide2.QtPrintSupport.QPrinter.OutputFormat: ...
    def pageOrder(self) -> PySide2.QtPrintSupport.QPrinter.PageOrder: ...
    @typing.overload
    def pageRect(self) -> PySide2.QtCore.QRect: ...
    @typing.overload
    def pageRect(
        self, arg__1: PySide2.QtPrintSupport.QPrinter.Unit
    ) -> PySide2.QtCore.QRectF: ...
    def pageSize(self) -> PySide2.QtGui.QPagedPaintDevice.PageSize: ...
    def paintEngine(self) -> PySide2.QtGui.QPaintEngine: ...
    def paperName(self) -> str: ...
    @typing.overload
    def paperRect(self) -> PySide2.QtCore.QRect: ...
    @typing.overload
    def paperRect(
        self, arg__1: PySide2.QtPrintSupport.QPrinter.Unit
    ) -> PySide2.QtCore.QRectF: ...
    @typing.overload
    def paperSize(self) -> PySide2.QtGui.QPagedPaintDevice.PageSize: ...
    @typing.overload
    def paperSize(
        self, unit: PySide2.QtPrintSupport.QPrinter.Unit
    ) -> PySide2.QtCore.QSizeF: ...
    def paperSource(self) -> PySide2.QtPrintSupport.QPrinter.PaperSource: ...
    def pdfVersion(self) -> PySide2.QtGui.QPagedPaintDevice.PdfVersion: ...
    def printEngine(self) -> PySide2.QtPrintSupport.QPrintEngine: ...
    def printProgram(self) -> str: ...
    def printRange(self) -> PySide2.QtPrintSupport.QPrinter.PrintRange: ...
    def printerName(self) -> str: ...
    def printerState(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState: ...
    def resolution(self) -> int: ...
    def setCollateCopies(self, collate: bool) -> None: ...
    def setColorMode(
        self, arg__1: PySide2.QtPrintSupport.QPrinter.ColorMode
    ) -> None: ...
    def setCopyCount(self, arg__1: int) -> None: ...
    def setCreator(self, arg__1: str) -> None: ...
    def setDocName(self, arg__1: str) -> None: ...
    def setDoubleSidedPrinting(self, enable: bool) -> None: ...
    def setDuplex(self, duplex: PySide2.QtPrintSupport.QPrinter.DuplexMode) -> None: ...
    def setEngines(
        self,
        printEngine: PySide2.QtPrintSupport.QPrintEngine,
        paintEngine: PySide2.QtGui.QPaintEngine,
    ) -> None: ...
    def setFontEmbeddingEnabled(self, enable: bool) -> None: ...
    def setFromTo(self, fromPage: int, toPage: int) -> None: ...
    def setFullPage(self, arg__1: bool) -> None: ...
    def setMargins(self, m: PySide2.QtGui.QPagedPaintDevice.Margins) -> None: ...
    def setNumCopies(self, arg__1: int) -> None: ...
    def setOrientation(
        self, arg__1: PySide2.QtPrintSupport.QPrinter.Orientation
    ) -> None: ...
    def setOutputFileName(self, arg__1: str) -> None: ...
    def setOutputFormat(
        self, format: PySide2.QtPrintSupport.QPrinter.OutputFormat
    ) -> None: ...
    @typing.overload
    def setPageMargins(
        self,
        left: float,
        top: float,
        right: float,
        bottom: float,
        unit: PySide2.QtPrintSupport.QPrinter.Unit,
    ) -> None: ...
    @typing.overload
    def setPageMargins(self, margins: PySide2.QtCore.QMarginsF) -> bool: ...
    def setPageOrder(
        self, arg__1: PySide2.QtPrintSupport.QPrinter.PageOrder
    ) -> None: ...
    @typing.overload
    def setPageSize(self, arg__1: PySide2.QtGui.QPageSize) -> bool: ...
    @typing.overload
    def setPageSize(self, arg__1: PySide2.QtGui.QPagedPaintDevice.PageSize) -> None: ...
    def setPageSizeMM(self, size: PySide2.QtCore.QSizeF) -> None: ...
    def setPaperName(self, paperName: str) -> None: ...
    @typing.overload
    def setPaperSize(
        self, arg__1: PySide2.QtGui.QPagedPaintDevice.PageSize
    ) -> None: ...
    @typing.overload
    def setPaperSize(
        self,
        paperSize: PySide2.QtCore.QSizeF,
        unit: PySide2.QtPrintSupport.QPrinter.Unit,
    ) -> None: ...
    def setPaperSource(
        self, arg__1: PySide2.QtPrintSupport.QPrinter.PaperSource
    ) -> None: ...
    def setPdfVersion(
        self, version: PySide2.QtGui.QPagedPaintDevice.PdfVersion
    ) -> None: ...
    def setPrintProgram(self, arg__1: str) -> None: ...
    def setPrintRange(
        self, range: PySide2.QtPrintSupport.QPrinter.PrintRange
    ) -> None: ...
    def setPrinterName(self, arg__1: str) -> None: ...
    def setResolution(self, arg__1: int) -> None: ...
    def setWinPageSize(self, winPageSize: int) -> None: ...
    if sys.platform() == "win32":
        def supportedPaperSources(self) -> typing.List: ...

    def supportedResolutions(self) -> typing.List: ...
    def supportsMultipleCopies(self) -> bool: ...
    def toPage(self) -> int: ...
    def winPageSize(self) -> int: ...

class QPrinterInfo(Shiboken.Object):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: PySide2.QtPrintSupport.QPrinterInfo) -> None: ...
    @typing.overload
    def __init__(self, printer: PySide2.QtPrintSupport.QPrinter) -> None: ...
    @staticmethod
    def __copy__() -> None: ...
    @staticmethod
    def availablePrinterNames() -> typing.List: ...
    @staticmethod
    def availablePrinters() -> typing.List: ...
    def defaultColorMode(self) -> PySide2.QtPrintSupport.QPrinter.ColorMode: ...
    def defaultDuplexMode(self) -> PySide2.QtPrintSupport.QPrinter.DuplexMode: ...
    def defaultPageSize(self) -> PySide2.QtGui.QPageSize: ...
    @staticmethod
    def defaultPrinter() -> PySide2.QtPrintSupport.QPrinterInfo: ...
    @staticmethod
    def defaultPrinterName() -> str: ...
    def description(self) -> str: ...
    def isDefault(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isRemote(self) -> bool: ...
    def location(self) -> str: ...
    def makeAndModel(self) -> str: ...
    def maximumPhysicalPageSize(self) -> PySide2.QtGui.QPageSize: ...
    def minimumPhysicalPageSize(self) -> PySide2.QtGui.QPageSize: ...
    @staticmethod
    def printerInfo(printerName: str) -> PySide2.QtPrintSupport.QPrinterInfo: ...
    def printerName(self) -> str: ...
    def state(self) -> PySide2.QtPrintSupport.QPrinter.PrinterState: ...
    def supportedColorModes(self) -> typing.List: ...
    def supportedDuplexModes(self) -> typing.List: ...
    def supportedPageSizes(self) -> typing.List: ...
    def supportedPaperSizes(self) -> typing.List: ...
    def supportedResolutions(self) -> typing.List: ...
    def supportedSizesWithNames(self) -> typing.List: ...
    def supportsCustomPageSizes(self) -> bool: ...

# eof
