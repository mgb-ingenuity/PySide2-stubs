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
PySide2.Qt3DRender, except for defaults which are replaced by "...".
"""

# Module PySide2.Qt3DRender
import PySide2
import typing

import shiboken2 as Shiboken

import PySide2.QtCore
import PySide2.QtGui
import PySide2.Qt3DCore
import PySide2.Qt3DRender

class Qt3DRender(Shiboken.Object):
    class API(object):
        OpenGL: Qt3DRender.API = ...  # 0x0
        Vulkan: Qt3DRender.API = ...  # 0x1
        DirectX: Qt3DRender.API = ...  # 0x2
        Metal: Qt3DRender.API = ...  # 0x3
        Null: Qt3DRender.API = ...  # 0x4

    class PropertyReaderInterface(Shiboken.Object):
        def __init__(self) -> None: ...
        def readProperty(self, v: typing.Any) -> typing.Any: ...

    class QAbstractFunctor(Shiboken.Object):
        def __init__(self) -> None: ...
        def id(self) -> int: ...

    class QAbstractLight(PySide2.Qt3DCore.QComponent):
        colorChanged: PySide2.QtCore.Signal
        intensityChanged: PySide2.QtCore.Signal

        PointLight: Qt3DRender.QAbstractLight.Type = ...  # 0x0
        DirectionalLight: Qt3DRender.QAbstractLight.Type = ...  # 0x1
        SpotLight: Qt3DRender.QAbstractLight.Type = ...  # 0x2

        class Type(object):
            PointLight: Qt3DRender.QAbstractLight.Type = ...  # 0x0
            DirectionalLight: Qt3DRender.QAbstractLight.Type = ...  # 0x1
            SpotLight: Qt3DRender.QAbstractLight.Type = ...  # 0x2
        def color(self) -> PySide2.QtGui.QColor: ...
        def intensity(self) -> float: ...
        def setColor(
            self,
            color: Union[PySide2.QtGui.QColor, PySide2.QtCore.Qt.GlobalColor, str, int],
        ) -> None: ...
        def setIntensity(self, intensity: float) -> None: ...
        def type(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractLight.Type: ...

    class QAbstractRayCaster(PySide2.Qt3DCore.QComponent):
        filterModeChanged: PySide2.QtCore.Signal
        hitsChanged: PySide2.QtCore.Signal
        runModeChanged: PySide2.QtCore.Signal

        AcceptAnyMatchingLayers: Qt3DRender.QAbstractRayCaster.FilterMode = ...  # 0x0
        Continuous: Qt3DRender.QAbstractRayCaster.RunMode = ...  # 0x0
        AcceptAllMatchingLayers: Qt3DRender.QAbstractRayCaster.FilterMode = ...  # 0x1
        SingleShot: Qt3DRender.QAbstractRayCaster.RunMode = ...  # 0x1
        DiscardAnyMatchingLayers: Qt3DRender.QAbstractRayCaster.FilterMode = ...  # 0x2
        DiscardAllMatchingLayers: Qt3DRender.QAbstractRayCaster.FilterMode = ...  # 0x3

        class FilterMode(object):
            AcceptAnyMatchingLayers: Qt3DRender.QAbstractRayCaster.FilterMode = (
                ...
            )  # 0x0
            AcceptAllMatchingLayers: Qt3DRender.QAbstractRayCaster.FilterMode = (
                ...
            )  # 0x1
            DiscardAnyMatchingLayers: Qt3DRender.QAbstractRayCaster.FilterMode = (
                ...
            )  # 0x2
            DiscardAllMatchingLayers: Qt3DRender.QAbstractRayCaster.FilterMode = (
                ...
            )  # 0x3

        class RunMode(object):
            Continuous: Qt3DRender.QAbstractRayCaster.RunMode = ...  # 0x0
            SingleShot: Qt3DRender.QAbstractRayCaster.RunMode = ...  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addLayer(self, layer: PySide2.Qt3DRender.Qt3DRender.QLayer) -> None: ...
        def filterMode(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode: ...
        def hits(self) -> typing.List: ...
        def layers(self) -> typing.List: ...
        def removeLayer(self, layer: PySide2.Qt3DRender.Qt3DRender.QLayer) -> None: ...
        def runMode(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode: ...
        def setFilterMode(
            self,
            filterMode: PySide2.Qt3DRender.Qt3DRender.QAbstractRayCaster.FilterMode,
        ) -> None: ...
        def setRunMode(
            self, runMode: PySide2.Qt3DRender.Qt3DRender.QAbstractRayCaster.RunMode
        ) -> None: ...

    class QAbstractTexture(PySide2.Qt3DCore.QNode):
        comparisonFunctionChanged: PySide2.QtCore.Signal
        comparisonModeChanged: PySide2.QtCore.Signal
        depthChanged: PySide2.QtCore.Signal
        formatChanged: PySide2.QtCore.Signal
        generateMipMapsChanged: PySide2.QtCore.Signal
        handleChanged: PySide2.QtCore.Signal
        handleTypeChanged: PySide2.QtCore.Signal
        heightChanged: PySide2.QtCore.Signal
        layersChanged: PySide2.QtCore.Signal
        magnificationFilterChanged: PySide2.QtCore.Signal
        maximumAnisotropyChanged: PySide2.QtCore.Signal
        minificationFilterChanged: PySide2.QtCore.Signal
        samplesChanged: PySide2.QtCore.Signal
        statusChanged: PySide2.QtCore.Signal
        widthChanged: PySide2.QtCore.Signal

        CompareNone: Qt3DRender.QAbstractTexture.ComparisonMode = ...  # 0x0
        NoFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x0
        NoHandle: Qt3DRender.QAbstractTexture.HandleType = ...  # 0x0
        None_: Qt3DRender.QAbstractTexture.Status = ...  # 0x0
        TargetAutomatic: Qt3DRender.QAbstractTexture.Target = ...  # 0x0
        Automatic: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1
        Loading: Qt3DRender.QAbstractTexture.Status = ...  # 0x1
        OpenGLTextureId: Qt3DRender.QAbstractTexture.HandleType = ...  # 0x1
        Ready: Qt3DRender.QAbstractTexture.Status = ...  # 0x2
        Error: Qt3DRender.QAbstractTexture.Status = ...  # 0x3
        CompareNever: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x200
        CompareLess: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x201
        CompareEqual: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x202
        CompareLessEqual: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x203
        CompareGreater: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x204
        CommpareNotEqual: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x205
        CompareGreaterEqual: Qt3DRender.QAbstractTexture.ComparisonFunction = (
            ...
        )  # 0x206
        CompareAlways: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x207
        Target1D: Qt3DRender.QAbstractTexture.Target = ...  # 0xde0
        Target2D: Qt3DRender.QAbstractTexture.Target = ...  # 0xde1
        DepthFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1902
        AlphaFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1906
        RGBFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1907
        RGBAFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1908
        LuminanceFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1909
        LuminanceAlphaFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x190a
        Nearest: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2600
        Linear: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2601
        NearestMipMapNearest: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2700
        LinearMipMapNearest: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2701
        NearestMipMapLinear: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2702
        LinearMipMapLinear: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2703
        RG3B2: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x2a10
        RGB8_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8051
        RGB16_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8054
        RGBA4: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8056
        RGB5A1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8057
        RGBA8_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8058
        RGB10A2: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8059
        RGBA16_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x805b
        Target3D: Qt3DRender.QAbstractTexture.Target = ...  # 0x806f
        D16: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x81a5
        D24: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x81a6
        D32: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x81a7
        R8_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8229
        R16_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822a
        RG8_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822b
        RG16_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822c
        R16F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822d
        R32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822e
        RG16F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822f
        RG32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8230
        R8I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8231
        R8U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8232
        R16I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8233
        R16U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8234
        R32I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8235
        R32U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8236
        RG8I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8237
        RG8U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8238
        RG16I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8239
        RG16U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x823a
        RG32I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x823b
        RG32U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x823c
        RGB_DXT1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x83f0
        RGBA_DXT1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x83f1
        RGBA_DXT3: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x83f2
        RGBA_DXT5: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x83f3
        TargetRectangle: Qt3DRender.QAbstractTexture.Target = ...  # 0x84f5
        TargetCubeMap: Qt3DRender.QAbstractTexture.Target = ...  # 0x8513
        CubeMapPositiveX: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8515
        CubeMapNegativeX: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8516
        CubeMapPositiveY: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8517
        CubeMapNegativeY: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8518
        CubeMapPositiveZ: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8519
        CubeMapNegativeZ: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x851a
        AllFaces: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x851b
        RGBA32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8814
        RGB32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8815
        RGBA16F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x881a
        RGB16F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x881b
        CompareRefToTexture: Qt3DRender.QAbstractTexture.ComparisonMode = ...  # 0x884e
        D24S8: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x88f0
        Target1DArray: Qt3DRender.QAbstractTexture.Target = ...  # 0x8c18
        Target2DArray: Qt3DRender.QAbstractTexture.Target = ...  # 0x8c1a
        TargetBuffer: Qt3DRender.QAbstractTexture.Target = ...  # 0x8c2a
        RG11B10F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c3a
        RGB9E5: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c3d
        SRGB8: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c41
        SRGB8_Alpha8: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c43
        SRGB_DXT1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c4c
        SRGB_Alpha_DXT1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c4d
        SRGB_Alpha_DXT3: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c4e
        SRGB_Alpha_DXT5: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c4f
        D32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8cac
        D32FS8X24: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8cad
        R5G6B5: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d62
        RGB8_ETC1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d64
        RGBA32U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d70
        RGB32U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d71
        RGBA16U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d76
        RGB16U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d77
        RGBA8U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d7c
        RGB8U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d7d
        RGBA32I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d82
        RGB32I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d83
        RGBA16I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d88
        RGB16I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d89
        RGBA8I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d8e
        RGB8I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d8f
        R_ATI1N_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8dbb
        R_ATI1N_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8dbc
        RG_ATI2N_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8dbd
        RG_ATI2N_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8dbe
        RGB_BP_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8e8c
        SRGB_BP_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8e8d
        RGB_BP_SIGNED_FLOAT: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8e8e
        RGB_BP_UNSIGNED_FLOAT: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8e8f
        R8_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f94
        RG8_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f95
        RGB8_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f96
        RGBA8_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f97
        R16_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f98
        RG16_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f99
        RGB16_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f9a
        RGBA16_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f9b
        TargetCubeMapArray: Qt3DRender.QAbstractTexture.Target = ...  # 0x9009
        RGB10A2U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x906f
        Target2DMultisample: Qt3DRender.QAbstractTexture.Target = ...  # 0x9100
        Target2DMultisampleArray: Qt3DRender.QAbstractTexture.Target = ...  # 0x9102
        R11_EAC_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9270
        R11_EAC_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9271
        RG11_EAC_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9272
        RG11_EAC_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9273
        RGB8_ETC2: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9274
        SRGB8_ETC2: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9275
        RGB8_PunchThrough_Alpha1_ETC2: Qt3DRender.QAbstractTexture.TextureFormat = (
            ...
        )  # 0x9276
        SRGB8_PunchThrough_Alpha1_ETC2: Qt3DRender.QAbstractTexture.TextureFormat = (
            ...
        )  # 0x9277
        RGBA8_ETC2_EAC: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9278
        SRGB8_Alpha8_ETC2_EAC: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9279

        class ComparisonFunction(object):
            CompareNever: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x200
            CompareLess: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x201
            CompareEqual: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x202
            CompareLessEqual: Qt3DRender.QAbstractTexture.ComparisonFunction = (
                ...
            )  # 0x203
            CompareGreater: Qt3DRender.QAbstractTexture.ComparisonFunction = (
                ...
            )  # 0x204
            CommpareNotEqual: Qt3DRender.QAbstractTexture.ComparisonFunction = (
                ...
            )  # 0x205
            CompareGreaterEqual: Qt3DRender.QAbstractTexture.ComparisonFunction = (
                ...
            )  # 0x206
            CompareAlways: Qt3DRender.QAbstractTexture.ComparisonFunction = ...  # 0x207

        class ComparisonMode(object):
            CompareNone: Qt3DRender.QAbstractTexture.ComparisonMode = ...  # 0x0
            CompareRefToTexture: Qt3DRender.QAbstractTexture.ComparisonMode = (
                ...
            )  # 0x884e

        class CubeMapFace(object):
            CubeMapPositiveX: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8515
            CubeMapNegativeX: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8516
            CubeMapPositiveY: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8517
            CubeMapNegativeY: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8518
            CubeMapPositiveZ: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x8519
            CubeMapNegativeZ: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x851a
            AllFaces: Qt3DRender.QAbstractTexture.CubeMapFace = ...  # 0x851b

        class Filter(object):
            Nearest: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2600
            Linear: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2601
            NearestMipMapNearest: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2700
            LinearMipMapNearest: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2701
            NearestMipMapLinear: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2702
            LinearMipMapLinear: Qt3DRender.QAbstractTexture.Filter = ...  # 0x2703

        class HandleType(object):
            NoHandle: Qt3DRender.QAbstractTexture.HandleType = ...  # 0x0
            OpenGLTextureId: Qt3DRender.QAbstractTexture.HandleType = ...  # 0x1

        class Status(object):
            None_: Qt3DRender.QAbstractTexture.Status = ...  # 0x0
            Loading: Qt3DRender.QAbstractTexture.Status = ...  # 0x1
            Ready: Qt3DRender.QAbstractTexture.Status = ...  # 0x2
            Error: Qt3DRender.QAbstractTexture.Status = ...  # 0x3

        class Target(object):
            TargetAutomatic: Qt3DRender.QAbstractTexture.Target = ...  # 0x0
            Target1D: Qt3DRender.QAbstractTexture.Target = ...  # 0xde0
            Target2D: Qt3DRender.QAbstractTexture.Target = ...  # 0xde1
            Target3D: Qt3DRender.QAbstractTexture.Target = ...  # 0x806f
            TargetRectangle: Qt3DRender.QAbstractTexture.Target = ...  # 0x84f5
            TargetCubeMap: Qt3DRender.QAbstractTexture.Target = ...  # 0x8513
            Target1DArray: Qt3DRender.QAbstractTexture.Target = ...  # 0x8c18
            Target2DArray: Qt3DRender.QAbstractTexture.Target = ...  # 0x8c1a
            TargetBuffer: Qt3DRender.QAbstractTexture.Target = ...  # 0x8c2a
            TargetCubeMapArray: Qt3DRender.QAbstractTexture.Target = ...  # 0x9009
            Target2DMultisample: Qt3DRender.QAbstractTexture.Target = ...  # 0x9100
            Target2DMultisampleArray: Qt3DRender.QAbstractTexture.Target = ...  # 0x9102

        class TextureFormat(object):
            NoFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x0
            Automatic: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1
            DepthFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1902
            AlphaFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1906
            RGBFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1907
            RGBAFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1908
            LuminanceFormat: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x1909
            LuminanceAlphaFormat: Qt3DRender.QAbstractTexture.TextureFormat = (
                ...
            )  # 0x190a
            RG3B2: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x2a10
            RGB8_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8051
            RGB16_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8054
            RGBA4: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8056
            RGB5A1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8057
            RGBA8_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8058
            RGB10A2: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8059
            RGBA16_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x805b
            D16: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x81a5
            D24: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x81a6
            D32: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x81a7
            R8_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8229
            R16_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822a
            RG8_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822b
            RG16_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822c
            R16F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822d
            R32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822e
            RG16F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x822f
            RG32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8230
            R8I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8231
            R8U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8232
            R16I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8233
            R16U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8234
            R32I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8235
            R32U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8236
            RG8I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8237
            RG8U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8238
            RG16I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8239
            RG16U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x823a
            RG32I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x823b
            RG32U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x823c
            RGB_DXT1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x83f0
            RGBA_DXT1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x83f1
            RGBA_DXT3: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x83f2
            RGBA_DXT5: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x83f3
            RGBA32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8814
            RGB32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8815
            RGBA16F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x881a
            RGB16F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x881b
            D24S8: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x88f0
            RG11B10F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c3a
            RGB9E5: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c3d
            SRGB8: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c41
            SRGB8_Alpha8: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c43
            SRGB_DXT1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c4c
            SRGB_Alpha_DXT1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c4d
            SRGB_Alpha_DXT3: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c4e
            SRGB_Alpha_DXT5: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8c4f
            D32F: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8cac
            D32FS8X24: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8cad
            R5G6B5: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d62
            RGB8_ETC1: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d64
            RGBA32U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d70
            RGB32U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d71
            RGBA16U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d76
            RGB16U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d77
            RGBA8U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d7c
            RGB8U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d7d
            RGBA32I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d82
            RGB32I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d83
            RGBA16I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d88
            RGB16I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d89
            RGBA8I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d8e
            RGB8I: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8d8f
            R_ATI1N_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8dbb
            R_ATI1N_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8dbc
            RG_ATI2N_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8dbd
            RG_ATI2N_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8dbe
            RGB_BP_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8e8c
            SRGB_BP_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8e8d
            RGB_BP_SIGNED_FLOAT: Qt3DRender.QAbstractTexture.TextureFormat = (
                ...
            )  # 0x8e8e
            RGB_BP_UNSIGNED_FLOAT: Qt3DRender.QAbstractTexture.TextureFormat = (
                ...
            )  # 0x8e8f
            R8_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f94
            RG8_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f95
            RGB8_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f96
            RGBA8_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f97
            R16_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f98
            RG16_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f99
            RGB16_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f9a
            RGBA16_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x8f9b
            RGB10A2U: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x906f
            R11_EAC_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9270
            R11_EAC_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9271
            RG11_EAC_UNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9272
            RG11_EAC_SNorm: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9273
            RGB8_ETC2: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9274
            SRGB8_ETC2: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9275
            RGB8_PunchThrough_Alpha1_ETC2: Qt3DRender.QAbstractTexture.TextureFormat = (
                ...
            )  # 0x9276
            SRGB8_PunchThrough_Alpha1_ETC2: Qt3DRender.QAbstractTexture.TextureFormat = (
                ...
            )  # 0x9277
            RGBA8_ETC2_EAC: Qt3DRender.QAbstractTexture.TextureFormat = ...  # 0x9278
            SRGB8_Alpha8_ETC2_EAC: Qt3DRender.QAbstractTexture.TextureFormat = (
                ...
            )  # 0x9279
        @typing.overload
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            target: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Target,
            parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...,
        ) -> None: ...
        def addTextureImage(
            self, textureImage: PySide2.Qt3DRender.Qt3DRender.QAbstractTextureImage
        ) -> None: ...
        def comparisonFunction(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction: ...
        def comparisonMode(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode: ...
        def depth(self) -> int: ...
        def format(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat: ...
        def generateMipMaps(self) -> bool: ...
        def handle(self) -> typing.Any: ...
        def handleType(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.HandleType: ...
        def height(self) -> int: ...
        def layers(self) -> int: ...
        def magnificationFilter(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Filter: ...
        def maximumAnisotropy(self) -> float: ...
        def minificationFilter(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Filter: ...
        def removeTextureImage(
            self, textureImage: PySide2.Qt3DRender.Qt3DRender.QAbstractTextureImage
        ) -> None: ...
        def samples(self) -> int: ...
        def setComparisonFunction(
            self,
            function: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction,
        ) -> None: ...
        def setComparisonMode(
            self, mode: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode
        ) -> None: ...
        def setDepth(self, depth: int) -> None: ...
        def setFormat(
            self, format: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat
        ) -> None: ...
        def setGenerateMipMaps(self, gen: bool) -> None: ...
        def setHandle(self, handle: typing.Any) -> None: ...
        def setHandleType(
            self, type: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.HandleType
        ) -> None: ...
        def setHeight(self, height: int) -> None: ...
        def setLayers(self, layers: int) -> None: ...
        def setMagnificationFilter(
            self, f: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Filter
        ) -> None: ...
        def setMaximumAnisotropy(self, anisotropy: float) -> None: ...
        def setMinificationFilter(
            self, f: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Filter
        ) -> None: ...
        def setSamples(self, samples: int) -> None: ...
        def setSize(self, width: int, height: int = ..., depth: int = ...) -> None: ...
        def setStatus(
            self, status: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Status
        ) -> None: ...
        def setWidth(self, width: int) -> None: ...
        def setWrapMode(
            self, wrapMode: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode
        ) -> None: ...
        def status(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Status: ...
        def target(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Target: ...
        def textureImages(self) -> typing.List: ...
        def width(self) -> int: ...
        def wrapMode(self) -> PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode: ...

    class QAbstractTextureImage(PySide2.Qt3DCore.QNode):
        faceChanged: PySide2.QtCore.Signal
        layerChanged: PySide2.QtCore.Signal
        mipLevelChanged: PySide2.QtCore.Signal

        def face(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace: ...
        def layer(self) -> int: ...
        def mipLevel(self) -> int: ...
        def notifyDataGeneratorChanged(self) -> None: ...
        def setFace(
            self, face: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace
        ) -> None: ...
        def setLayer(self, layer: int) -> None: ...
        def setMipLevel(self, level: int) -> None: ...

    class QAlphaCoverage(PySide2.Qt3DRender.QRenderState):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QAlphaTest(PySide2.Qt3DRender.QRenderState):
        alphaFunctionChanged: PySide2.QtCore.Signal
        referenceValueChanged: PySide2.QtCore.Signal

        Never: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x200
        Less: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x201
        Equal: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x202
        LessOrEqual: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x203
        Greater: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x204
        NotEqual: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x205
        GreaterOrEqual: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x206
        Always: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x207

        class AlphaFunction(object):
            Never: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x200
            Less: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x201
            Equal: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x202
            LessOrEqual: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x203
            Greater: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x204
            NotEqual: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x205
            GreaterOrEqual: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x206
            Always: Qt3DRender.QAlphaTest.AlphaFunction = ...  # 0x207
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def alphaFunction(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAlphaTest.AlphaFunction: ...
        def referenceValue(self) -> float: ...
        def setAlphaFunction(
            self, alphaFunction: PySide2.Qt3DRender.Qt3DRender.QAlphaTest.AlphaFunction
        ) -> None: ...
        def setReferenceValue(self, referenceValue: float) -> None: ...

    class QAttribute(PySide2.Qt3DCore.QNode):
        attributeTypeChanged: PySide2.QtCore.Signal
        bufferChanged: PySide2.QtCore.Signal
        byteOffsetChanged: PySide2.QtCore.Signal
        byteStrideChanged: PySide2.QtCore.Signal
        countChanged: PySide2.QtCore.Signal
        dataSizeChanged: PySide2.QtCore.Signal
        dataTypeChanged: PySide2.QtCore.Signal
        divisorChanged: PySide2.QtCore.Signal
        nameChanged: PySide2.QtCore.Signal
        vertexBaseTypeChanged: PySide2.QtCore.Signal
        vertexSizeChanged: PySide2.QtCore.Signal

        Byte: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x0
        VertexAttribute: Qt3DRender.QAttribute.AttributeType = ...  # 0x0
        IndexAttribute: Qt3DRender.QAttribute.AttributeType = ...  # 0x1
        UnsignedByte: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x1
        DrawIndirectAttribute: Qt3DRender.QAttribute.AttributeType = ...  # 0x2
        Short: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x2
        UnsignedShort: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x3
        Int: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x4
        UnsignedInt: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x5
        HalfFloat: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x6
        Float: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x7
        Double: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x8

        class AttributeType(object):
            VertexAttribute: Qt3DRender.QAttribute.AttributeType = ...  # 0x0
            IndexAttribute: Qt3DRender.QAttribute.AttributeType = ...  # 0x1
            DrawIndirectAttribute: Qt3DRender.QAttribute.AttributeType = ...  # 0x2

        class VertexBaseType(object):
            Byte: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x0
            UnsignedByte: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x1
            Short: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x2
            UnsignedShort: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x3
            Int: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x4
            UnsignedInt: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x5
            HalfFloat: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x6
            Float: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x7
            Double: Qt3DRender.QAttribute.VertexBaseType = ...  # 0x8
        @typing.overload
        def __init__(
            self,
            buf: PySide2.Qt3DRender.Qt3DRender.QBuffer,
            name: str,
            vertexBaseType: PySide2.Qt3DRender.Qt3DRender.QAttribute.VertexBaseType,
            vertexSize: int,
            count: int,
            offset: int = ...,
            stride: int = ...,
            parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...,
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            buf: PySide2.Qt3DRender.Qt3DRender.QBuffer,
            vertexBaseType: PySide2.Qt3DRender.Qt3DRender.QAttribute.VertexBaseType,
            vertexSize: int,
            count: int,
            offset: int = ...,
            stride: int = ...,
            parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...,
        ) -> None: ...
        @typing.overload
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def attributeType(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAttribute.AttributeType: ...
        def buffer(self) -> PySide2.Qt3DRender.Qt3DRender.QBuffer: ...
        def byteOffset(self) -> int: ...
        def byteStride(self) -> int: ...
        def count(self) -> int: ...
        @staticmethod
        def defaultColorAttributeName() -> str: ...
        @staticmethod
        def defaultJointIndicesAttributeName() -> str: ...
        @staticmethod
        def defaultJointWeightsAttributeName() -> str: ...
        @staticmethod
        def defaultNormalAttributeName() -> str: ...
        @staticmethod
        def defaultPositionAttributeName() -> str: ...
        @staticmethod
        def defaultTangentAttributeName() -> str: ...
        @staticmethod
        def defaultTextureCoordinate1AttributeName() -> str: ...
        @staticmethod
        def defaultTextureCoordinate2AttributeName() -> str: ...
        @staticmethod
        def defaultTextureCoordinateAttributeName() -> str: ...
        def divisor(self) -> int: ...
        def name(self) -> str: ...
        def setAttributeType(
            self, attributeType: PySide2.Qt3DRender.Qt3DRender.QAttribute.AttributeType
        ) -> None: ...
        def setBuffer(self, buffer: PySide2.Qt3DRender.Qt3DRender.QBuffer) -> None: ...
        def setByteOffset(self, byteOffset: int) -> None: ...
        def setByteStride(self, byteStride: int) -> None: ...
        def setCount(self, count: int) -> None: ...
        def setDataSize(self, size: int) -> None: ...
        def setDataType(
            self, type: PySide2.Qt3DRender.Qt3DRender.QAttribute.VertexBaseType
        ) -> None: ...
        def setDivisor(self, divisor: int) -> None: ...
        def setName(self, name: str) -> None: ...
        def setVertexBaseType(
            self, type: PySide2.Qt3DRender.Qt3DRender.QAttribute.VertexBaseType
        ) -> None: ...
        def setVertexSize(self, size: int) -> None: ...
        def vertexBaseType(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAttribute.VertexBaseType: ...
        def vertexSize(self) -> int: ...

    class QBlendEquation(PySide2.Qt3DRender.QRenderState):
        blendFunctionChanged: PySide2.QtCore.Signal

        Add: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x8006
        Min: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x8007
        Max: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x8008
        Subtract: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x800a
        ReverseSubtract: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x800b

        class BlendFunction(object):
            Add: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x8006
            Min: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x8007
            Max: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x8008
            Subtract: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x800a
            ReverseSubtract: Qt3DRender.QBlendEquation.BlendFunction = ...  # 0x800b
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def blendFunction(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquation.BlendFunction: ...
        def setBlendFunction(
            self,
            blendFunction: PySide2.Qt3DRender.Qt3DRender.QBlendEquation.BlendFunction,
        ) -> None: ...

    class QBlendEquationArguments(PySide2.Qt3DRender.QRenderState):
        bufferIndexChanged: PySide2.QtCore.Signal
        destinationAlphaChanged: PySide2.QtCore.Signal
        destinationRgbChanged: PySide2.QtCore.Signal
        destinationRgbaChanged: PySide2.QtCore.Signal
        sourceAlphaChanged: PySide2.QtCore.Signal
        sourceRgbChanged: PySide2.QtCore.Signal
        sourceRgbaChanged: PySide2.QtCore.Signal

        Zero: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x0
        One: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x1
        SourceColor: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x300
        OneMinusSourceColor: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x301
        SourceAlpha: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x302
        OneMinusSourceAlpha: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x303
        Source1Alpha: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x303
        DestinationAlpha: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x304
        Source1Color: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x304
        OneMinusDestinationAlpha: Qt3DRender.QBlendEquationArguments.Blending = (
            ...
        )  # 0x305
        DestinationColor: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x306
        OneMinusDestinationColor: Qt3DRender.QBlendEquationArguments.Blending = (
            ...
        )  # 0x307
        SourceAlphaSaturate: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x308
        ConstantColor: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x8001
        OneMinusConstantColor: Qt3DRender.QBlendEquationArguments.Blending = (
            ...
        )  # 0x8002
        ConstantAlpha: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x8003
        OneMinusConstantAlpha: Qt3DRender.QBlendEquationArguments.Blending = (
            ...
        )  # 0x8004
        OneMinusSource1Alpha: Qt3DRender.QBlendEquationArguments.Blending = (
            ...
        )  # 0x8005
        OneMinusSource1Color: Qt3DRender.QBlendEquationArguments.Blending = (
            ...
        )  # 0x8006
        OneMinusSource1Color0: Qt3DRender.QBlendEquationArguments.Blending = (
            ...
        )  # 0x8006

        class Blending(object):
            Zero: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x0
            One: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x1
            SourceColor: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x300
            OneMinusSourceColor: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x301
            SourceAlpha: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x302
            OneMinusSourceAlpha: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x303
            Source1Alpha: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x303
            DestinationAlpha: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x304
            Source1Color: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x304
            OneMinusDestinationAlpha: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x305
            DestinationColor: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x306
            OneMinusDestinationColor: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x307
            SourceAlphaSaturate: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x308
            ConstantColor: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x8001
            OneMinusConstantColor: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x8002
            ConstantAlpha: Qt3DRender.QBlendEquationArguments.Blending = ...  # 0x8003
            OneMinusConstantAlpha: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x8004
            OneMinusSource1Alpha: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x8005
            OneMinusSource1Color: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x8006
            OneMinusSource1Color0: Qt3DRender.QBlendEquationArguments.Blending = (
                ...
            )  # 0x8006
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def bufferIndex(self) -> int: ...
        def destinationAlpha(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def destinationRgb(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def setBufferIndex(self, index: int) -> None: ...
        def setDestinationAlpha(
            self,
            destinationAlpha: PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending,
        ) -> None: ...
        def setDestinationRgb(
            self,
            destinationRgb: PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending,
        ) -> None: ...
        def setDestinationRgba(
            self,
            destinationRgba: PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending,
        ) -> None: ...
        def setSourceAlpha(
            self,
            sourceAlpha: PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending,
        ) -> None: ...
        def setSourceRgb(
            self,
            sourceRgb: PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending,
        ) -> None: ...
        def setSourceRgba(
            self,
            sourceRgba: PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending,
        ) -> None: ...
        def sourceAlpha(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def sourceRgb(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...

    class QBlitFramebuffer(PySide2.Qt3DRender.QFrameGraphNode):
        destinationAttachmentPointChanged: PySide2.QtCore.Signal
        destinationChanged: PySide2.QtCore.Signal
        destinationRectChanged: PySide2.QtCore.Signal
        interpolationMethodChanged: PySide2.QtCore.Signal
        sourceAttachmentPointChanged: PySide2.QtCore.Signal
        sourceChanged: PySide2.QtCore.Signal
        sourceRectChanged: PySide2.QtCore.Signal

        Nearest: Qt3DRender.QBlitFramebuffer.InterpolationMethod = ...  # 0x0
        Linear: Qt3DRender.QBlitFramebuffer.InterpolationMethod = ...  # 0x1

        class InterpolationMethod(object):
            Nearest: Qt3DRender.QBlitFramebuffer.InterpolationMethod = ...  # 0x0
            Linear: Qt3DRender.QBlitFramebuffer.InterpolationMethod = ...  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def destination(self) -> PySide2.Qt3DRender.Qt3DRender.QRenderTarget: ...
        def destinationAttachmentPoint(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint: ...
        def destinationRect(self) -> PySide2.QtCore.QRectF: ...
        def interpolationMethod(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QBlitFramebuffer.InterpolationMethod: ...
        def setDestination(
            self, destination: PySide2.Qt3DRender.Qt3DRender.QRenderTarget
        ) -> None: ...
        def setDestinationAttachmentPoint(
            self,
            destinationAttachmentPoint: PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint,
        ) -> None: ...
        def setDestinationRect(
            self, destinationRect: PySide2.QtCore.QRectF
        ) -> None: ...
        def setInterpolationMethod(
            self,
            interpolationMethod: PySide2.Qt3DRender.Qt3DRender.QBlitFramebuffer.InterpolationMethod,
        ) -> None: ...
        def setSource(
            self, source: PySide2.Qt3DRender.Qt3DRender.QRenderTarget
        ) -> None: ...
        def setSourceAttachmentPoint(
            self,
            sourceAttachmentPoint: PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint,
        ) -> None: ...
        def setSourceRect(self, sourceRect: PySide2.QtCore.QRectF) -> None: ...
        def source(self) -> PySide2.Qt3DRender.Qt3DRender.QRenderTarget: ...
        def sourceAttachmentPoint(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint: ...
        def sourceRect(self) -> PySide2.QtCore.QRectF: ...

    class QBuffer(PySide2.Qt3DCore.QNode):
        accessTypeChanged: PySide2.QtCore.Signal
        dataAvailable: PySide2.QtCore.Signal
        dataChanged: PySide2.QtCore.Signal
        syncDataChanged: PySide2.QtCore.Signal
        typeChanged: PySide2.QtCore.Signal
        usageChanged: PySide2.QtCore.Signal

        Write: Qt3DRender.QBuffer.AccessType = ...  # 0x1
        Read: Qt3DRender.QBuffer.AccessType = ...  # 0x2
        ReadWrite: Qt3DRender.QBuffer.AccessType = ...  # 0x3
        VertexBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x8892
        IndexBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x8893
        StreamDraw: Qt3DRender.QBuffer.UsageType = ...  # 0x88e0
        StreamRead: Qt3DRender.QBuffer.UsageType = ...  # 0x88e1
        StreamCopy: Qt3DRender.QBuffer.UsageType = ...  # 0x88e2
        StaticDraw: Qt3DRender.QBuffer.UsageType = ...  # 0x88e4
        StaticRead: Qt3DRender.QBuffer.UsageType = ...  # 0x88e5
        StaticCopy: Qt3DRender.QBuffer.UsageType = ...  # 0x88e6
        DynamicDraw: Qt3DRender.QBuffer.UsageType = ...  # 0x88e8
        DynamicRead: Qt3DRender.QBuffer.UsageType = ...  # 0x88e9
        DynamicCopy: Qt3DRender.QBuffer.UsageType = ...  # 0x88ea
        PixelPackBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x88eb
        PixelUnpackBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x88ec
        UniformBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x8a11
        DrawIndirectBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x8f3f
        ShaderStorageBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x90d2

        class AccessType(object):
            Write: Qt3DRender.QBuffer.AccessType = ...  # 0x1
            Read: Qt3DRender.QBuffer.AccessType = ...  # 0x2
            ReadWrite: Qt3DRender.QBuffer.AccessType = ...  # 0x3

        class BufferType(object):
            VertexBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x8892
            IndexBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x8893
            PixelPackBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x88eb
            PixelUnpackBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x88ec
            UniformBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x8a11
            DrawIndirectBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x8f3f
            ShaderStorageBuffer: Qt3DRender.QBuffer.BufferType = ...  # 0x90d2

        class UsageType(object):
            StreamDraw: Qt3DRender.QBuffer.UsageType = ...  # 0x88e0
            StreamRead: Qt3DRender.QBuffer.UsageType = ...  # 0x88e1
            StreamCopy: Qt3DRender.QBuffer.UsageType = ...  # 0x88e2
            StaticDraw: Qt3DRender.QBuffer.UsageType = ...  # 0x88e4
            StaticRead: Qt3DRender.QBuffer.UsageType = ...  # 0x88e5
            StaticCopy: Qt3DRender.QBuffer.UsageType = ...  # 0x88e6
            DynamicDraw: Qt3DRender.QBuffer.UsageType = ...  # 0x88e8
            DynamicRead: Qt3DRender.QBuffer.UsageType = ...  # 0x88e9
            DynamicCopy: Qt3DRender.QBuffer.UsageType = ...  # 0x88ea
        @typing.overload
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            ty: PySide2.Qt3DRender.Qt3DRender.QBuffer.BufferType,
            parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...,
        ) -> None: ...
        def accessType(self) -> PySide2.Qt3DRender.Qt3DRender.QBuffer.AccessType: ...
        def data(self) -> PySide2.QtCore.QByteArray: ...
        def isSyncData(self) -> bool: ...
        def setAccessType(
            self, access: PySide2.Qt3DRender.Qt3DRender.QBuffer.AccessType
        ) -> None: ...
        def setData(self, bytes: PySide2.QtCore.QByteArray) -> None: ...
        def setSyncData(self, syncData: bool) -> None: ...
        def setType(
            self, type: PySide2.Qt3DRender.Qt3DRender.QBuffer.BufferType
        ) -> None: ...
        def setUsage(
            self, usage: PySide2.Qt3DRender.Qt3DRender.QBuffer.UsageType
        ) -> None: ...
        def type(self) -> PySide2.Qt3DRender.Qt3DRender.QBuffer.BufferType: ...
        def updateData(self, offset: int, bytes: PySide2.QtCore.QByteArray) -> None: ...
        def usage(self) -> PySide2.Qt3DRender.Qt3DRender.QBuffer.UsageType: ...

    class QBufferCapture(PySide2.Qt3DRender.QFrameGraphNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QBufferDataGenerator(PySide2.Qt3DRender.QAbstractFunctor):
        def __init__(self) -> None: ...

    class QCamera(PySide2.Qt3DCore.QEntity):
        aspectRatioChanged: PySide2.QtCore.Signal
        bottomChanged: PySide2.QtCore.Signal
        exposureChanged: PySide2.QtCore.Signal
        farPlaneChanged: PySide2.QtCore.Signal
        fieldOfViewChanged: PySide2.QtCore.Signal
        leftChanged: PySide2.QtCore.Signal
        nearPlaneChanged: PySide2.QtCore.Signal
        positionChanged: PySide2.QtCore.Signal
        projectionMatrixChanged: PySide2.QtCore.Signal
        projectionTypeChanged: PySide2.QtCore.Signal
        rightChanged: PySide2.QtCore.Signal
        topChanged: PySide2.QtCore.Signal
        upVectorChanged: PySide2.QtCore.Signal
        viewCenterChanged: PySide2.QtCore.Signal
        viewMatrixChanged: PySide2.QtCore.Signal
        viewVectorChanged: PySide2.QtCore.Signal

        TranslateViewCenter: Qt3DRender.QCamera.CameraTranslationOption = ...  # 0x0
        DontTranslateViewCenter: Qt3DRender.QCamera.CameraTranslationOption = ...  # 0x1

        class CameraTranslationOption(object):
            TranslateViewCenter: Qt3DRender.QCamera.CameraTranslationOption = ...  # 0x0
            DontTranslateViewCenter: Qt3DRender.QCamera.CameraTranslationOption = (
                ...
            )  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def aspectRatio(self) -> float: ...
        def bottom(self) -> float: ...
        def exposure(self) -> float: ...
        def farPlane(self) -> float: ...
        def fieldOfView(self) -> float: ...
        def left(self) -> float: ...
        def lens(self) -> PySide2.Qt3DRender.Qt3DRender.QCameraLens: ...
        def nearPlane(self) -> float: ...
        @typing.overload
        def pan(self, angle: float) -> None: ...
        @typing.overload
        def pan(self, angle: float, axis: PySide2.QtGui.QVector3D) -> None: ...
        @typing.overload
        def panAboutViewCenter(self, angle: float) -> None: ...
        @typing.overload
        def panAboutViewCenter(
            self, angle: float, axis: PySide2.QtGui.QVector3D
        ) -> None: ...
        def panRotation(self, angle: float) -> PySide2.QtGui.QQuaternion: ...
        def position(self) -> PySide2.QtGui.QVector3D: ...
        def projectionMatrix(self) -> PySide2.QtGui.QMatrix4x4: ...
        def projectionType(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType: ...
        def right(self) -> float: ...
        def roll(self, angle: float) -> None: ...
        def rollAboutViewCenter(self, angle: float) -> None: ...
        def rollRotation(self, angle: float) -> PySide2.QtGui.QQuaternion: ...
        def rotate(self, q: PySide2.QtGui.QQuaternion) -> None: ...
        def rotateAboutViewCenter(self, q: PySide2.QtGui.QQuaternion) -> None: ...
        def rotation(
            self, angle: float, axis: PySide2.QtGui.QVector3D
        ) -> PySide2.QtGui.QQuaternion: ...
        def setAspectRatio(self, aspectRatio: float) -> None: ...
        def setBottom(self, bottom: float) -> None: ...
        def setExposure(self, exposure: float) -> None: ...
        def setFarPlane(self, farPlane: float) -> None: ...
        def setFieldOfView(self, fieldOfView: float) -> None: ...
        def setLeft(self, left: float) -> None: ...
        def setNearPlane(self, nearPlane: float) -> None: ...
        def setPosition(self, position: PySide2.QtGui.QVector3D) -> None: ...
        def setProjectionMatrix(
            self, projectionMatrix: PySide2.QtGui.QMatrix4x4
        ) -> None: ...
        def setProjectionType(
            self, type: PySide2.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType
        ) -> None: ...
        def setRight(self, right: float) -> None: ...
        def setTop(self, top: float) -> None: ...
        def setUpVector(self, upVector: PySide2.QtGui.QVector3D) -> None: ...
        def setViewCenter(self, viewCenter: PySide2.QtGui.QVector3D) -> None: ...
        def tilt(self, angle: float) -> None: ...
        def tiltAboutViewCenter(self, angle: float) -> None: ...
        def tiltRotation(self, angle: float) -> PySide2.QtGui.QQuaternion: ...
        def top(self) -> float: ...
        def transform(self) -> PySide2.Qt3DCore.Qt3DCore.QTransform: ...
        def translate(
            self,
            vLocal: PySide2.QtGui.QVector3D,
            option: PySide2.Qt3DRender.Qt3DRender.QCamera.CameraTranslationOption = ...,
        ) -> None: ...
        def translateWorld(
            self,
            vWorld: PySide2.QtGui.QVector3D,
            option: PySide2.Qt3DRender.Qt3DRender.QCamera.CameraTranslationOption = ...,
        ) -> None: ...
        def upVector(self) -> PySide2.QtGui.QVector3D: ...
        def viewAll(self) -> None: ...
        def viewCenter(self) -> PySide2.QtGui.QVector3D: ...
        def viewEntity(self, entity: PySide2.Qt3DCore.Qt3DCore.QEntity) -> None: ...
        def viewMatrix(self) -> PySide2.QtGui.QMatrix4x4: ...
        def viewSphere(
            self, center: PySide2.QtGui.QVector3D, radius: float
        ) -> None: ...
        def viewVector(self) -> PySide2.QtGui.QVector3D: ...

    class QCameraLens(PySide2.Qt3DCore.QComponent):
        aspectRatioChanged: PySide2.QtCore.Signal
        bottomChanged: PySide2.QtCore.Signal
        exposureChanged: PySide2.QtCore.Signal
        farPlaneChanged: PySide2.QtCore.Signal
        fieldOfViewChanged: PySide2.QtCore.Signal
        leftChanged: PySide2.QtCore.Signal
        nearPlaneChanged: PySide2.QtCore.Signal
        projectionMatrixChanged: PySide2.QtCore.Signal
        projectionTypeChanged: PySide2.QtCore.Signal
        rightChanged: PySide2.QtCore.Signal
        topChanged: PySide2.QtCore.Signal
        viewSphere: PySide2.QtCore.Signal

        OrthographicProjection: Qt3DRender.QCameraLens.ProjectionType = ...  # 0x0
        PerspectiveProjection: Qt3DRender.QCameraLens.ProjectionType = ...  # 0x1
        FrustumProjection: Qt3DRender.QCameraLens.ProjectionType = ...  # 0x2
        CustomProjection: Qt3DRender.QCameraLens.ProjectionType = ...  # 0x3

        class ProjectionType(object):
            OrthographicProjection: Qt3DRender.QCameraLens.ProjectionType = ...  # 0x0
            PerspectiveProjection: Qt3DRender.QCameraLens.ProjectionType = ...  # 0x1
            FrustumProjection: Qt3DRender.QCameraLens.ProjectionType = ...  # 0x2
            CustomProjection: Qt3DRender.QCameraLens.ProjectionType = ...  # 0x3
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def aspectRatio(self) -> float: ...
        def bottom(self) -> float: ...
        def exposure(self) -> float: ...
        def farPlane(self) -> float: ...
        def fieldOfView(self) -> float: ...
        def left(self) -> float: ...
        def nearPlane(self) -> float: ...
        def projectionMatrix(self) -> PySide2.QtGui.QMatrix4x4: ...
        def projectionType(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType: ...
        def right(self) -> float: ...
        def setAspectRatio(self, aspectRatio: float) -> None: ...
        def setBottom(self, bottom: float) -> None: ...
        def setExposure(self, exposure: float) -> None: ...
        def setFarPlane(self, farPlane: float) -> None: ...
        def setFieldOfView(self, fieldOfView: float) -> None: ...
        def setFrustumProjection(
            self,
            left: float,
            right: float,
            bottom: float,
            top: float,
            nearPlane: float,
            farPlane: float,
        ) -> None: ...
        def setLeft(self, left: float) -> None: ...
        def setNearPlane(self, nearPlane: float) -> None: ...
        def setOrthographicProjection(
            self,
            left: float,
            right: float,
            bottom: float,
            top: float,
            nearPlane: float,
            farPlane: float,
        ) -> None: ...
        def setPerspectiveProjection(
            self, fieldOfView: float, aspect: float, nearPlane: float, farPlane: float
        ) -> None: ...
        def setProjectionMatrix(
            self, projectionMatrix: PySide2.QtGui.QMatrix4x4
        ) -> None: ...
        def setProjectionType(
            self,
            projectionType: PySide2.Qt3DRender.Qt3DRender.QCameraLens.ProjectionType,
        ) -> None: ...
        def setRight(self, right: float) -> None: ...
        def setTop(self, top: float) -> None: ...
        def top(self) -> float: ...
        def viewAll(self, cameraId: PySide2.Qt3DCore.Qt3DCore.QNodeId) -> None: ...
        def viewEntity(
            self,
            entityId: PySide2.Qt3DCore.Qt3DCore.QNodeId,
            cameraId: PySide2.Qt3DCore.Qt3DCore.QNodeId,
        ) -> None: ...

    class QCameraSelector(PySide2.Qt3DRender.QFrameGraphNode):
        cameraChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def camera(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def setCamera(self, camera: PySide2.Qt3DCore.Qt3DCore.QEntity) -> None: ...

    class QClearBuffers(PySide2.Qt3DRender.QFrameGraphNode):
        buffersChanged: PySide2.QtCore.Signal
        clearColorChanged: PySide2.QtCore.Signal
        clearDepthValueChanged: PySide2.QtCore.Signal
        clearStencilValueChanged: PySide2.QtCore.Signal
        colorBufferChanged: PySide2.QtCore.Signal

        AllBuffers: Qt3DRender.QClearBuffers.BufferType = ...  # -0x1
        None_: Qt3DRender.QClearBuffers.BufferType = ...  # 0x0
        ColorBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x1
        DepthBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x2
        ColorDepthBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x3
        StencilBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x4
        DepthStencilBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x6
        ColorDepthStencilBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x7

        class BufferType(object):
            AllBuffers: Qt3DRender.QClearBuffers.BufferType = ...  # -0x1
            None_: Qt3DRender.QClearBuffers.BufferType = ...  # 0x0
            ColorBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x1
            DepthBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x2
            ColorDepthBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x3
            StencilBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x4
            DepthStencilBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x6
            ColorDepthStencilBuffer: Qt3DRender.QClearBuffers.BufferType = ...  # 0x7

            def __index__(self) -> int: ...
            def __init__(self, value: typing.Union[int, BufferType] = ...) -> None: ...
            def __or__(
                self, other: typing.Union[int, BufferType]
            ) -> BufferTypeFlags: ...
            def __and__(
                self, other: typing.Union[int, BufferType]
            ) -> BufferTypeFlags: ...
            def __xor__(
                self, other: typing.Union[int, BufferType]
            ) -> BufferTypeFlags: ...
            def __ror__(
                self, other: typing.Union[int, BufferType]
            ) -> BufferTypeFlags: ...
            def __rand__(
                self, other: typing.Union[int, BufferType]
            ) -> BufferTypeFlags: ...
            def __rxor__(
                self, other: typing.Union[int, BufferType]
            ) -> BufferTypeFlags: ...
            def __ior__(
                self, other: typing.Union[int, BufferType]
            ) -> BufferTypeFlags: ...
            def __iand__(
                self, other: typing.Union[int, BufferType]
            ) -> BufferTypeFlags: ...
            def __ixor__(
                self, other: typing.Union[int, BufferType]
            ) -> BufferTypeFlags: ...
            def __invert__(self) -> BufferTypeFlags: ...

        class BufferTypeFlags(object):
            def __index__(self) -> int: ...
            def __init__(
                self, value: typing.Union[int, BufferType, BufferTypeFlags] = ...
            ) -> None: ...
            def __or__(
                self, other: typing.Union[int, BufferType, BufferTypeFlags]
            ) -> BufferTypeFlags: ...
            def __and__(
                self, other: typing.Union[int, BufferType, BufferTypeFlags]
            ) -> BufferTypeFlags: ...
            def __xor__(
                self, other: typing.Union[int, BufferType, BufferTypeFlags]
            ) -> BufferTypeFlags: ...
            def __ror__(
                self, other: typing.Union[int, BufferType, BufferTypeFlags]
            ) -> BufferTypeFlags: ...
            def __rand__(
                self, other: typing.Union[int, BufferType, BufferTypeFlags]
            ) -> BufferTypeFlags: ...
            def __rxor__(
                self, other: typing.Union[int, BufferType, BufferTypeFlags]
            ) -> BufferTypeFlags: ...
            def __ior__(
                self, other: typing.Union[int, BufferType, BufferTypeFlags]
            ) -> BufferTypeFlags: ...
            def __iand__(
                self, other: typing.Union[int, BufferType, BufferTypeFlags]
            ) -> BufferTypeFlags: ...
            def __ixor__(
                self, other: typing.Union[int, BufferType, BufferTypeFlags]
            ) -> BufferTypeFlags: ...
            def __invert__(self) -> BufferTypeFlags: ...

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def buffers(self) -> PySide2.Qt3DRender.Qt3DRender.QClearBuffers.BufferType: ...
        def clearColor(self) -> PySide2.QtGui.QColor: ...
        def clearDepthValue(self) -> float: ...
        def clearStencilValue(self) -> int: ...
        def colorBuffer(self) -> PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput: ...
        def setBuffers(
            self, buffers: PySide2.Qt3DRender.Qt3DRender.QClearBuffers.BufferType
        ) -> None: ...
        def setClearColor(
            self,
            color: Union[PySide2.QtGui.QColor, PySide2.QtCore.Qt.GlobalColor, str, int],
        ) -> None: ...
        def setClearDepthValue(self, clearDepthValue: float) -> None: ...
        def setClearStencilValue(self, clearStencilValue: int) -> None: ...
        def setColorBuffer(
            self, buffer: PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput
        ) -> None: ...

    class QClipPlane(PySide2.Qt3DRender.QRenderState):
        distanceChanged: PySide2.QtCore.Signal
        normalChanged: PySide2.QtCore.Signal
        planeIndexChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def distance(self) -> float: ...
        def normal(self) -> PySide2.QtGui.QVector3D: ...
        def planeIndex(self) -> int: ...
        def setDistance(self, arg__1: float) -> None: ...
        def setNormal(self, arg__1: PySide2.QtGui.QVector3D) -> None: ...
        def setPlaneIndex(self, arg__1: int) -> None: ...

    class QColorMask(PySide2.Qt3DRender.QRenderState):
        alphaMaskedChanged: PySide2.QtCore.Signal
        blueMaskedChanged: PySide2.QtCore.Signal
        greenMaskedChanged: PySide2.QtCore.Signal
        redMaskedChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def isAlphaMasked(self) -> bool: ...
        def isBlueMasked(self) -> bool: ...
        def isGreenMasked(self) -> bool: ...
        def isRedMasked(self) -> bool: ...
        def setAlphaMasked(self, alphaMasked: bool) -> None: ...
        def setBlueMasked(self, blueMasked: bool) -> None: ...
        def setGreenMasked(self, greenMasked: bool) -> None: ...
        def setRedMasked(self, redMasked: bool) -> None: ...

    class QComputeCommand(PySide2.Qt3DCore.QComponent):
        runTypeChanged: PySide2.QtCore.Signal
        workGroupXChanged: PySide2.QtCore.Signal
        workGroupYChanged: PySide2.QtCore.Signal
        workGroupZChanged: PySide2.QtCore.Signal

        Continuous: Qt3DRender.QComputeCommand.RunType = ...  # 0x0
        Manual: Qt3DRender.QComputeCommand.RunType = ...  # 0x1

        class RunType(object):
            Continuous: Qt3DRender.QComputeCommand.RunType = ...  # 0x0
            Manual: Qt3DRender.QComputeCommand.RunType = ...  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def runType(self) -> PySide2.Qt3DRender.Qt3DRender.QComputeCommand.RunType: ...
        def setRunType(
            self, runType: PySide2.Qt3DRender.Qt3DRender.QComputeCommand.RunType
        ) -> None: ...
        def setWorkGroupX(self, workGroupX: int) -> None: ...
        def setWorkGroupY(self, workGroupY: int) -> None: ...
        def setWorkGroupZ(self, workGroupZ: int) -> None: ...
        @typing.overload
        def trigger(self, frameCount: int = ...) -> None: ...
        @typing.overload
        def trigger(
            self,
            workGroupX: int,
            workGroupY: int,
            workGroupZ: int,
            frameCount: int = ...,
        ) -> None: ...
        def workGroupX(self) -> int: ...
        def workGroupY(self) -> int: ...
        def workGroupZ(self) -> int: ...

    class QCullFace(PySide2.Qt3DRender.QRenderState):
        modeChanged: PySide2.QtCore.Signal

        NoCulling: Qt3DRender.QCullFace.CullingMode = ...  # 0x0
        Front: Qt3DRender.QCullFace.CullingMode = ...  # 0x404
        Back: Qt3DRender.QCullFace.CullingMode = ...  # 0x405
        FrontAndBack: Qt3DRender.QCullFace.CullingMode = ...  # 0x408

        class CullingMode(object):
            NoCulling: Qt3DRender.QCullFace.CullingMode = ...  # 0x0
            Front: Qt3DRender.QCullFace.CullingMode = ...  # 0x404
            Back: Qt3DRender.QCullFace.CullingMode = ...  # 0x405
            FrontAndBack: Qt3DRender.QCullFace.CullingMode = ...  # 0x408
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def mode(self) -> PySide2.Qt3DRender.Qt3DRender.QCullFace.CullingMode: ...
        def setMode(
            self, mode: PySide2.Qt3DRender.Qt3DRender.QCullFace.CullingMode
        ) -> None: ...

    class QDepthTest(PySide2.Qt3DRender.QRenderState):
        depthFunctionChanged: PySide2.QtCore.Signal

        Never: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x200
        Less: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x201
        Equal: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x202
        LessOrEqual: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x203
        Greater: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x204
        NotEqual: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x205
        GreaterOrEqual: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x206
        Always: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x207

        class DepthFunction(object):
            Never: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x200
            Less: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x201
            Equal: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x202
            LessOrEqual: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x203
            Greater: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x204
            NotEqual: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x205
            GreaterOrEqual: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x206
            Always: Qt3DRender.QDepthTest.DepthFunction = ...  # 0x207
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def depthFunction(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QDepthTest.DepthFunction: ...
        def setDepthFunction(
            self, depthFunction: PySide2.Qt3DRender.Qt3DRender.QDepthTest.DepthFunction
        ) -> None: ...

    class QDirectionalLight(PySide2.Qt3DRender.QAbstractLight):
        worldDirectionChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def setWorldDirection(
            self, worldDirection: PySide2.QtGui.QVector3D
        ) -> None: ...
        def worldDirection(self) -> PySide2.QtGui.QVector3D: ...

    class QDispatchCompute(PySide2.Qt3DRender.QFrameGraphNode):
        workGroupXChanged: PySide2.QtCore.Signal
        workGroupYChanged: PySide2.QtCore.Signal
        workGroupZChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def setWorkGroupX(self, workGroupX: int) -> None: ...
        def setWorkGroupY(self, workGroupY: int) -> None: ...
        def setWorkGroupZ(self, workGroupZ: int) -> None: ...
        def workGroupX(self) -> int: ...
        def workGroupY(self) -> int: ...
        def workGroupZ(self) -> int: ...

    class QDithering(PySide2.Qt3DRender.QRenderState):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QEffect(PySide2.Qt3DCore.QNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addParameter(
            self, parameter: PySide2.Qt3DRender.Qt3DRender.QParameter
        ) -> None: ...
        def addTechnique(self, t: PySide2.Qt3DRender.Qt3DRender.QTechnique) -> None: ...
        def parameters(self) -> typing.List: ...
        def removeParameter(
            self, parameter: PySide2.Qt3DRender.Qt3DRender.QParameter
        ) -> None: ...
        def removeTechnique(
            self, t: PySide2.Qt3DRender.Qt3DRender.QTechnique
        ) -> None: ...
        def techniques(self) -> typing.List: ...

    class QEnvironmentLight(PySide2.Qt3DCore.QComponent):
        irradianceChanged: PySide2.QtCore.Signal
        specularChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def irradiance(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setIrradiance(
            self, irradiance: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture
        ) -> None: ...
        def setSpecular(
            self, specular: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture
        ) -> None: ...
        def specular(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...

    class QFilterKey(PySide2.Qt3DCore.QNode):
        nameChanged: PySide2.QtCore.Signal
        valueChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def name(self) -> str: ...
        def setName(self, customType: str) -> None: ...
        def setValue(self, value: typing.Any) -> None: ...
        def value(self) -> typing.Any: ...

    class QFrameGraphNode(PySide2.Qt3DCore.QNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def parentFrameGraphNode(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QFrameGraphNode: ...

    class QFrameGraphNodeCreatedChangeBase(PySide2.Qt3DCore.QNodeCreatedChangeBase):
        def __init__(
            self, node: PySide2.Qt3DRender.Qt3DRender.QFrameGraphNode
        ) -> None: ...
        def parentFrameGraphNodeId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...

    class QFrontFace(PySide2.Qt3DRender.QRenderState):
        directionChanged: PySide2.QtCore.Signal

        ClockWise: Qt3DRender.QFrontFace.WindingDirection = ...  # 0x900
        CounterClockWise: Qt3DRender.QFrontFace.WindingDirection = ...  # 0x901

        class WindingDirection(object):
            ClockWise: Qt3DRender.QFrontFace.WindingDirection = ...  # 0x900
            CounterClockWise: Qt3DRender.QFrontFace.WindingDirection = ...  # 0x901
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def direction(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QFrontFace.WindingDirection: ...
        def setDirection(
            self, direction: PySide2.Qt3DRender.Qt3DRender.QFrontFace.WindingDirection
        ) -> None: ...

    class QFrustumCulling(PySide2.Qt3DRender.QFrameGraphNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QGeometry(PySide2.Qt3DCore.QNode):
        boundingVolumePositionAttributeChanged: PySide2.QtCore.Signal
        maxExtentChanged: PySide2.QtCore.Signal
        minExtentChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addAttribute(
            self, attribute: PySide2.Qt3DRender.Qt3DRender.QAttribute
        ) -> None: ...
        def attributes(self) -> typing.List: ...
        def boundingVolumePositionAttribute(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def maxExtent(self) -> PySide2.QtGui.QVector3D: ...
        def minExtent(self) -> PySide2.QtGui.QVector3D: ...
        def removeAttribute(
            self, attribute: PySide2.Qt3DRender.Qt3DRender.QAttribute
        ) -> None: ...
        def setBoundingVolumePositionAttribute(
            self,
            boundingVolumePositionAttribute: PySide2.Qt3DRender.Qt3DRender.QAttribute,
        ) -> None: ...

    class QGeometryFactory(PySide2.Qt3DRender.QAbstractFunctor):
        def __init__(self) -> None: ...

    class QGeometryRenderer(PySide2.Qt3DCore.QComponent):
        firstInstanceChanged: PySide2.QtCore.Signal
        firstVertexChanged: PySide2.QtCore.Signal
        geometryChanged: PySide2.QtCore.Signal
        indexBufferByteOffsetChanged: PySide2.QtCore.Signal
        indexOffsetChanged: PySide2.QtCore.Signal
        instanceCountChanged: PySide2.QtCore.Signal
        primitiveRestartEnabledChanged: PySide2.QtCore.Signal
        primitiveTypeChanged: PySide2.QtCore.Signal
        restartIndexValueChanged: PySide2.QtCore.Signal
        vertexCountChanged: PySide2.QtCore.Signal
        verticesPerPatchChanged: PySide2.QtCore.Signal

        Points: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x0
        Lines: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x1
        LineLoop: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x2
        LineStrip: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x3
        Triangles: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x4
        TriangleStrip: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x5
        TriangleFan: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x6
        LinesAdjacency: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0xa
        LineStripAdjacency: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0xb
        TrianglesAdjacency: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0xc
        TriangleStripAdjacency: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0xd
        Patches: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0xe

        class PrimitiveType(object):
            Points: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x0
            Lines: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x1
            LineLoop: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x2
            LineStrip: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x3
            Triangles: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x4
            TriangleStrip: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x5
            TriangleFan: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0x6
            LinesAdjacency: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0xa
            LineStripAdjacency: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0xb
            TrianglesAdjacency: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0xc
            TriangleStripAdjacency: Qt3DRender.QGeometryRenderer.PrimitiveType = (
                ...
            )  # 0xd
            Patches: Qt3DRender.QGeometryRenderer.PrimitiveType = ...  # 0xe
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def firstInstance(self) -> int: ...
        def firstVertex(self) -> int: ...
        def geometry(self) -> PySide2.Qt3DRender.Qt3DRender.QGeometry: ...
        def indexBufferByteOffset(self) -> int: ...
        def indexOffset(self) -> int: ...
        def instanceCount(self) -> int: ...
        def primitiveRestartEnabled(self) -> bool: ...
        def primitiveType(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType: ...
        def restartIndexValue(self) -> int: ...
        def setFirstInstance(self, firstInstance: int) -> None: ...
        def setFirstVertex(self, firstVertex: int) -> None: ...
        def setGeometry(
            self, geometry: PySide2.Qt3DRender.Qt3DRender.QGeometry
        ) -> None: ...
        def setIndexBufferByteOffset(self, offset: int) -> None: ...
        def setIndexOffset(self, indexOffset: int) -> None: ...
        def setInstanceCount(self, instanceCount: int) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled: bool) -> None: ...
        def setPrimitiveType(
            self,
            primitiveType: PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType,
        ) -> None: ...
        def setRestartIndexValue(self, index: int) -> None: ...
        def setVertexCount(self, vertexCount: int) -> None: ...
        def setVerticesPerPatch(self, verticesPerPatch: int) -> None: ...
        def vertexCount(self) -> int: ...
        def verticesPerPatch(self) -> int: ...

    class QGraphicsApiFilter(PySide2.QtCore.QObject):
        apiChanged: PySide2.QtCore.Signal
        extensionsChanged: PySide2.QtCore.Signal
        graphicsApiFilterChanged: PySide2.QtCore.Signal
        majorVersionChanged: PySide2.QtCore.Signal
        minorVersionChanged: PySide2.QtCore.Signal
        profileChanged: PySide2.QtCore.Signal
        vendorChanged: PySide2.QtCore.Signal

        NoProfile: Qt3DRender.QGraphicsApiFilter.OpenGLProfile = ...  # 0x0
        CoreProfile: Qt3DRender.QGraphicsApiFilter.OpenGLProfile = ...  # 0x1
        OpenGL: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x1
        CompatibilityProfile: Qt3DRender.QGraphicsApiFilter.OpenGLProfile = ...  # 0x2
        OpenGLES: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x2
        Vulkan: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x3
        DirectX: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x4
        RHI: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x5

        class Api(object):
            OpenGL: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x1
            OpenGLES: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x2
            Vulkan: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x3
            DirectX: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x4
            RHI: Qt3DRender.QGraphicsApiFilter.Api = ...  # 0x5

        class OpenGLProfile(object):
            NoProfile: Qt3DRender.QGraphicsApiFilter.OpenGLProfile = ...  # 0x0
            CoreProfile: Qt3DRender.QGraphicsApiFilter.OpenGLProfile = ...  # 0x1
            CompatibilityProfile: Qt3DRender.QGraphicsApiFilter.OpenGLProfile = (
                ...
            )  # 0x2
        def __init__(
            self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
        ) -> None: ...
        def api(self) -> PySide2.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api: ...
        def extensions(self) -> typing.List: ...
        def majorVersion(self) -> int: ...
        def minorVersion(self) -> int: ...
        def profile(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile: ...
        def setApi(
            self, api: PySide2.Qt3DRender.Qt3DRender.QGraphicsApiFilter.Api
        ) -> None: ...
        def setExtensions(self, extensions: typing.Sequence) -> None: ...
        def setMajorVersion(self, majorVersion: int) -> None: ...
        def setMinorVersion(self, minorVersion: int) -> None: ...
        def setProfile(
            self,
            profile: PySide2.Qt3DRender.Qt3DRender.QGraphicsApiFilter.OpenGLProfile,
        ) -> None: ...
        def setVendor(self, vendor: str) -> None: ...
        def vendor(self) -> str: ...

    class QLayer(PySide2.Qt3DCore.QComponent):
        recursiveChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def recursive(self) -> bool: ...
        def setRecursive(self, recursive: bool) -> None: ...

    class QLayerFilter(PySide2.Qt3DRender.QFrameGraphNode):
        filterModeChanged: PySide2.QtCore.Signal

        AcceptAnyMatchingLayers: Qt3DRender.QLayerFilter.FilterMode = ...  # 0x0
        AcceptAllMatchingLayers: Qt3DRender.QLayerFilter.FilterMode = ...  # 0x1
        DiscardAnyMatchingLayers: Qt3DRender.QLayerFilter.FilterMode = ...  # 0x2
        DiscardAllMatchingLayers: Qt3DRender.QLayerFilter.FilterMode = ...  # 0x3

        class FilterMode(object):
            AcceptAnyMatchingLayers: Qt3DRender.QLayerFilter.FilterMode = ...  # 0x0
            AcceptAllMatchingLayers: Qt3DRender.QLayerFilter.FilterMode = ...  # 0x1
            DiscardAnyMatchingLayers: Qt3DRender.QLayerFilter.FilterMode = ...  # 0x2
            DiscardAllMatchingLayers: Qt3DRender.QLayerFilter.FilterMode = ...  # 0x3
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addLayer(self, layer: PySide2.Qt3DRender.Qt3DRender.QLayer) -> None: ...
        def filterMode(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QLayerFilter.FilterMode: ...
        def layers(self) -> typing.List: ...
        def removeLayer(self, layer: PySide2.Qt3DRender.Qt3DRender.QLayer) -> None: ...
        def setFilterMode(
            self, filterMode: PySide2.Qt3DRender.Qt3DRender.QLayerFilter.FilterMode
        ) -> None: ...

    class QLevelOfDetail(PySide2.Qt3DCore.QComponent):
        cameraChanged: PySide2.QtCore.Signal
        currentIndexChanged: PySide2.QtCore.Signal
        thresholdTypeChanged: PySide2.QtCore.Signal
        thresholdsChanged: PySide2.QtCore.Signal
        volumeOverrideChanged: PySide2.QtCore.Signal

        DistanceToCameraThreshold: Qt3DRender.QLevelOfDetail.ThresholdType = ...  # 0x0
        ProjectedScreenPixelSizeThreshold: Qt3DRender.QLevelOfDetail.ThresholdType = (
            ...
        )  # 0x1

        class ThresholdType(object):
            DistanceToCameraThreshold: Qt3DRender.QLevelOfDetail.ThresholdType = (
                ...
            )  # 0x0
            ProjectedScreenPixelSizeThreshold: Qt3DRender.QLevelOfDetail.ThresholdType = (
                ...
            )  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def camera(self) -> PySide2.Qt3DRender.Qt3DRender.QCamera: ...
        def createBoundingSphere(
            self, center: PySide2.QtGui.QVector3D, radius: float
        ) -> PySide2.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere: ...
        def currentIndex(self) -> int: ...
        def setCamera(self, camera: PySide2.Qt3DRender.Qt3DRender.QCamera) -> None: ...
        def setCurrentIndex(self, currentIndex: int) -> None: ...
        def setThresholdType(
            self,
            thresholdType: PySide2.Qt3DRender.Qt3DRender.QLevelOfDetail.ThresholdType,
        ) -> None: ...
        def setThresholds(self, thresholds: typing.List) -> None: ...
        def setVolumeOverride(
            self,
            volumeOverride: PySide2.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere,
        ) -> None: ...
        def thresholdType(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QLevelOfDetail.ThresholdType: ...
        def thresholds(self) -> typing.List: ...
        def volumeOverride(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere: ...

    class QLevelOfDetailBoundingSphere(Shiboken.Object):
        @typing.overload
        def __init__(
            self, center: PySide2.QtGui.QVector3D = ..., radius: float = ...
        ) -> None: ...
        @typing.overload
        def __init__(
            self, other: PySide2.Qt3DRender.Qt3DRender.QLevelOfDetailBoundingSphere
        ) -> None: ...
        def center(self) -> PySide2.QtGui.QVector3D: ...
        def isEmpty(self) -> bool: ...
        def radius(self) -> float: ...

    class QLevelOfDetailSwitch(PySide2.Qt3DRender.QLevelOfDetail):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QLineWidth(PySide2.Qt3DRender.QRenderState):
        smoothChanged: PySide2.QtCore.Signal
        valueChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def setSmooth(self, enabled: bool) -> None: ...
        def setValue(self, value: float) -> None: ...
        def smooth(self) -> bool: ...
        def value(self) -> float: ...

    class QMaterial(PySide2.Qt3DCore.QComponent):
        effectChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addParameter(
            self, parameter: PySide2.Qt3DRender.Qt3DRender.QParameter
        ) -> None: ...
        def effect(self) -> PySide2.Qt3DRender.Qt3DRender.QEffect: ...
        def parameters(self) -> typing.List: ...
        def removeParameter(
            self, parameter: PySide2.Qt3DRender.Qt3DRender.QParameter
        ) -> None: ...
        def setEffect(self, effect: PySide2.Qt3DRender.Qt3DRender.QEffect) -> None: ...

    class QMemoryBarrier(PySide2.Qt3DRender.QFrameGraphNode):
        waitOperationsChanged: PySide2.QtCore.Signal

        All: Qt3DRender.QMemoryBarrier.Operation = ...  # -0x1
        None_: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x0
        VertexAttributeArray: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x1
        ElementArray: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x2
        Uniform: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x4
        TextureFetch: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x8
        ShaderImageAccess: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x10
        Command: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x20
        PixelBuffer: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x40
        TextureUpdate: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x80
        BufferUpdate: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x100
        FrameBuffer: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x200
        TransformFeedback: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x400
        AtomicCounter: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x800
        ShaderStorage: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x1000
        QueryBuffer: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x2000

        class Operation(object):
            All: Qt3DRender.QMemoryBarrier.Operation = ...  # -0x1
            None_: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x0
            VertexAttributeArray: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x1
            ElementArray: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x2
            Uniform: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x4
            TextureFetch: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x8
            ShaderImageAccess: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x10
            Command: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x20
            PixelBuffer: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x40
            TextureUpdate: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x80
            BufferUpdate: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x100
            FrameBuffer: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x200
            TransformFeedback: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x400
            AtomicCounter: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x800
            ShaderStorage: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x1000
            QueryBuffer: Qt3DRender.QMemoryBarrier.Operation = ...  # 0x2000

            def __index__(self) -> int: ...
            def __init__(self, value: typing.Union[int, Operation] = ...) -> None: ...
            def __or__(self, other: typing.Union[int, Operation]) -> Operations: ...
            def __and__(self, other: typing.Union[int, Operation]) -> Operations: ...
            def __xor__(self, other: typing.Union[int, Operation]) -> Operations: ...
            def __ror__(self, other: typing.Union[int, Operation]) -> Operations: ...
            def __rand__(self, other: typing.Union[int, Operation]) -> Operations: ...
            def __rxor__(self, other: typing.Union[int, Operation]) -> Operations: ...
            def __ior__(self, other: typing.Union[int, Operation]) -> Operations: ...
            def __iand__(self, other: typing.Union[int, Operation]) -> Operations: ...
            def __ixor__(self, other: typing.Union[int, Operation]) -> Operations: ...
            def __invert__(self) -> Operations: ...

        class Operations(object):
            def __index__(self) -> int: ...
            def __init__(
                self, value: typing.Union[int, Operation, Operations] = ...
            ) -> None: ...
            def __or__(
                self, other: typing.Union[int, Operation, Operations]
            ) -> Operations: ...
            def __and__(
                self, other: typing.Union[int, Operation, Operations]
            ) -> Operations: ...
            def __xor__(
                self, other: typing.Union[int, Operation, Operations]
            ) -> Operations: ...
            def __ror__(
                self, other: typing.Union[int, Operation, Operations]
            ) -> Operations: ...
            def __rand__(
                self, other: typing.Union[int, Operation, Operations]
            ) -> Operations: ...
            def __rxor__(
                self, other: typing.Union[int, Operation, Operations]
            ) -> Operations: ...
            def __ior__(
                self, other: typing.Union[int, Operation, Operations]
            ) -> Operations: ...
            def __iand__(
                self, other: typing.Union[int, Operation, Operations]
            ) -> Operations: ...
            def __ixor__(
                self, other: typing.Union[int, Operation, Operations]
            ) -> Operations: ...
            def __invert__(self) -> Operations: ...

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def setWaitOperations(
            self, operations: PySide2.Qt3DRender.Qt3DRender.QMemoryBarrier.Operations
        ) -> None: ...
        def waitOperations(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QMemoryBarrier.Operations: ...

    class QMesh(PySide2.Qt3DRender.QGeometryRenderer):
        meshNameChanged: PySide2.QtCore.Signal
        sourceChanged: PySide2.QtCore.Signal
        statusChanged: PySide2.QtCore.Signal

        None_: Qt3DRender.QMesh.Status = ...  # 0x0
        Loading: Qt3DRender.QMesh.Status = ...  # 0x1
        Ready: Qt3DRender.QMesh.Status = ...  # 0x2
        Error: Qt3DRender.QMesh.Status = ...  # 0x3

        class Status(object):
            None_: Qt3DRender.QMesh.Status = ...  # 0x0
            Loading: Qt3DRender.QMesh.Status = ...  # 0x1
            Ready: Qt3DRender.QMesh.Status = ...  # 0x2
            Error: Qt3DRender.QMesh.Status = ...  # 0x3
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def meshName(self) -> str: ...
        def setMeshName(self, meshName: str) -> None: ...
        def setSource(self, source: PySide2.QtCore.QUrl) -> None: ...
        def source(self) -> PySide2.QtCore.QUrl: ...
        def status(self) -> PySide2.Qt3DRender.Qt3DRender.QMesh.Status: ...

    class QMultiSampleAntiAliasing(PySide2.Qt3DRender.QRenderState):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QNoDepthMask(PySide2.Qt3DRender.QRenderState):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QNoDraw(PySide2.Qt3DRender.QFrameGraphNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QNoPicking(PySide2.Qt3DRender.QFrameGraphNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QObjectPicker(PySide2.Qt3DCore.QComponent):
        clicked: PySide2.QtCore.Signal
        containsMouseChanged: PySide2.QtCore.Signal
        dragEnabledChanged: PySide2.QtCore.Signal
        entered: PySide2.QtCore.Signal
        exited: PySide2.QtCore.Signal
        hoverEnabledChanged: PySide2.QtCore.Signal
        moved: PySide2.QtCore.Signal
        pressed: PySide2.QtCore.Signal
        pressedChanged: PySide2.QtCore.Signal
        priorityChanged: PySide2.QtCore.Signal
        released: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def containsMouse(self) -> bool: ...
        def isDragEnabled(self) -> bool: ...
        def isHoverEnabled(self) -> bool: ...
        def isPressed(self) -> bool: ...
        def priority(self) -> int: ...
        def setDragEnabled(self, dragEnabled: bool) -> None: ...
        def setHoverEnabled(self, hoverEnabled: bool) -> None: ...
        def setPriority(self, priority: int) -> None: ...

    class QPaintedTextureImage(PySide2.Qt3DRender.QAbstractTextureImage):
        heightChanged: PySide2.QtCore.Signal
        sizeChanged: PySide2.QtCore.Signal
        widthChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def height(self) -> int: ...
        def paint(self, painter: PySide2.QtGui.QPainter) -> None: ...
        def setHeight(self, h: int) -> None: ...
        def setSize(self, size: PySide2.QtCore.QSize) -> None: ...
        def setWidth(self, w: int) -> None: ...
        def size(self) -> PySide2.QtCore.QSize: ...
        def update(self, rect: PySide2.QtCore.QRect = ...) -> None: ...
        def width(self) -> int: ...

    class QParameter(PySide2.Qt3DCore.QNode):
        nameChanged: PySide2.QtCore.Signal
        valueChanged: PySide2.QtCore.Signal

        @typing.overload
        def __init__(
            self,
            name: str,
            texture: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture,
            parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...,
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            name: str,
            value: typing.Any,
            parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...,
        ) -> None: ...
        @typing.overload
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def name(self) -> str: ...
        def setName(self, name: str) -> None: ...
        def setValue(self, dv: typing.Any) -> None: ...
        def value(self) -> typing.Any: ...

    class QPickEvent(PySide2.QtCore.QObject):
        acceptedChanged: PySide2.QtCore.Signal

        NoButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x0
        NoModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x0
        LeftButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x1
        RightButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x2
        MiddleButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x4
        BackButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x8
        ShiftModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x2000000
        ControlModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x4000000
        AltModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x8000000
        MetaModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x10000000
        KeypadModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x20000000

        class Buttons(object):
            NoButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x0
            LeftButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x1
            RightButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x2
            MiddleButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x4
            BackButton: Qt3DRender.QPickEvent.Buttons = ...  # 0x8

        class Modifiers(object):
            NoModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x0
            ShiftModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x2000000
            ControlModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x4000000
            AltModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x8000000
            MetaModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x10000000
            KeypadModifier: Qt3DRender.QPickEvent.Modifiers = ...  # 0x20000000
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(
            self,
            position: PySide2.QtCore.QPointF,
            worldIntersection: PySide2.QtGui.QVector3D,
            localIntersection: PySide2.QtGui.QVector3D,
            distance: float,
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            position: PySide2.QtCore.QPointF,
            worldIntersection: PySide2.QtGui.QVector3D,
            localIntersection: PySide2.QtGui.QVector3D,
            distance: float,
            button: PySide2.Qt3DRender.Qt3DRender.QPickEvent.Buttons,
            buttons: int,
            modifiers: int,
        ) -> None: ...
        def button(self) -> PySide2.Qt3DRender.Qt3DRender.QPickEvent.Buttons: ...
        def buttons(self) -> int: ...
        def distance(self) -> float: ...
        def entity(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def isAccepted(self) -> bool: ...
        def localIntersection(self) -> PySide2.QtGui.QVector3D: ...
        def modifiers(self) -> int: ...
        def position(self) -> PySide2.QtCore.QPointF: ...
        def setAccepted(self, accepted: bool) -> None: ...
        def viewport(self) -> PySide2.Qt3DRender.Qt3DRender.QViewport: ...
        def worldIntersection(self) -> PySide2.QtGui.QVector3D: ...

    class QPickLineEvent(PySide2.Qt3DRender.QPickEvent):
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(
            self,
            position: PySide2.QtCore.QPointF,
            worldIntersection: PySide2.QtGui.QVector3D,
            localIntersection: PySide2.QtGui.QVector3D,
            distance: float,
            edgeIndex: int,
            vertex1Index: int,
            vertex2Index: int,
            button: PySide2.Qt3DRender.Qt3DRender.QPickEvent.Buttons,
            buttons: int,
            modifiers: int,
        ) -> None: ...
        def edgeIndex(self) -> int: ...
        def vertex1Index(self) -> int: ...
        def vertex2Index(self) -> int: ...

    class QPickPointEvent(PySide2.Qt3DRender.QPickEvent):
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(
            self,
            position: PySide2.QtCore.QPointF,
            worldIntersection: PySide2.QtGui.QVector3D,
            localIntersection: PySide2.QtGui.QVector3D,
            distance: float,
            pointIndex: int,
            button: PySide2.Qt3DRender.Qt3DRender.QPickEvent.Buttons,
            buttons: int,
            modifiers: int,
        ) -> None: ...
        def pointIndex(self) -> int: ...

    class QPickTriangleEvent(PySide2.Qt3DRender.QPickEvent):
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(
            self,
            position: PySide2.QtCore.QPointF,
            worldIntersection: PySide2.QtGui.QVector3D,
            localIntersection: PySide2.QtGui.QVector3D,
            distance: float,
            triangleIndex: int,
            vertex1Index: int,
            vertex2Index: int,
            vertex3Index: int,
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            position: PySide2.QtCore.QPointF,
            worldIntersection: PySide2.QtGui.QVector3D,
            localIntersection: PySide2.QtGui.QVector3D,
            distance: float,
            triangleIndex: int,
            vertex1Index: int,
            vertex2Index: int,
            vertex3Index: int,
            button: PySide2.Qt3DRender.Qt3DRender.QPickEvent.Buttons,
            buttons: int,
            modifiers: int,
            uvw: PySide2.QtGui.QVector3D,
        ) -> None: ...
        def triangleIndex(self) -> int: ...
        def uvw(self) -> PySide2.QtGui.QVector3D: ...
        def vertex1Index(self) -> int: ...
        def vertex2Index(self) -> int: ...
        def vertex3Index(self) -> int: ...

    class QPickingSettings(PySide2.Qt3DCore.QNode):
        faceOrientationPickingModeChanged: PySide2.QtCore.Signal
        pickMethodChanged: PySide2.QtCore.Signal
        pickResultModeChanged: PySide2.QtCore.Signal
        worldSpaceToleranceChanged: PySide2.QtCore.Signal

        BoundingVolumePicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x0
        NearestPick: Qt3DRender.QPickingSettings.PickResultMode = ...  # 0x0
        AllPicks: Qt3DRender.QPickingSettings.PickResultMode = ...  # 0x1
        FrontFace: Qt3DRender.QPickingSettings.FaceOrientationPickingMode = ...  # 0x1
        TrianglePicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x1
        BackFace: Qt3DRender.QPickingSettings.FaceOrientationPickingMode = ...  # 0x2
        LinePicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x2
        NearestPriorityPick: Qt3DRender.QPickingSettings.PickResultMode = ...  # 0x2
        FrontAndBackFace: Qt3DRender.QPickingSettings.FaceOrientationPickingMode = (
            ...
        )  # 0x3
        PointPicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x4
        PrimitivePicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x7

        class FaceOrientationPickingMode(object):
            FrontFace: Qt3DRender.QPickingSettings.FaceOrientationPickingMode = (
                ...
            )  # 0x1
            BackFace: Qt3DRender.QPickingSettings.FaceOrientationPickingMode = (
                ...
            )  # 0x2
            FrontAndBackFace: Qt3DRender.QPickingSettings.FaceOrientationPickingMode = (
                ...
            )  # 0x3

        class PickMethod(object):
            BoundingVolumePicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x0
            TrianglePicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x1
            LinePicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x2
            PointPicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x4
            PrimitivePicking: Qt3DRender.QPickingSettings.PickMethod = ...  # 0x7

        class PickResultMode(object):
            NearestPick: Qt3DRender.QPickingSettings.PickResultMode = ...  # 0x0
            AllPicks: Qt3DRender.QPickingSettings.PickResultMode = ...  # 0x1
            NearestPriorityPick: Qt3DRender.QPickingSettings.PickResultMode = ...  # 0x2
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def faceOrientationPickingMode(
            self,
        ) -> (
            PySide2.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode
        ): ...
        def pickMethod(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod: ...
        def pickResultMode(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode: ...
        def setFaceOrientationPickingMode(
            self,
            faceOrientationPickingMode: PySide2.Qt3DRender.Qt3DRender.QPickingSettings.FaceOrientationPickingMode,
        ) -> None: ...
        def setPickMethod(
            self, pickMethod: PySide2.Qt3DRender.Qt3DRender.QPickingSettings.PickMethod
        ) -> None: ...
        def setPickResultMode(
            self,
            pickResultMode: PySide2.Qt3DRender.Qt3DRender.QPickingSettings.PickResultMode,
        ) -> None: ...
        def setWorldSpaceTolerance(self, worldSpaceTolerance: float) -> None: ...
        def worldSpaceTolerance(self) -> float: ...

    class QPointLight(PySide2.Qt3DRender.QAbstractLight):
        constantAttenuationChanged: PySide2.QtCore.Signal
        linearAttenuationChanged: PySide2.QtCore.Signal
        quadraticAttenuationChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def constantAttenuation(self) -> float: ...
        def linearAttenuation(self) -> float: ...
        def quadraticAttenuation(self) -> float: ...
        def setConstantAttenuation(self, value: float) -> None: ...
        def setLinearAttenuation(self, value: float) -> None: ...
        def setQuadraticAttenuation(self, value: float) -> None: ...

    class QPointSize(PySide2.Qt3DRender.QRenderState):
        sizeModeChanged: PySide2.QtCore.Signal
        valueChanged: PySide2.QtCore.Signal

        Fixed: Qt3DRender.QPointSize.SizeMode = ...  # 0x0
        Programmable: Qt3DRender.QPointSize.SizeMode = ...  # 0x1

        class SizeMode(object):
            Fixed: Qt3DRender.QPointSize.SizeMode = ...  # 0x0
            Programmable: Qt3DRender.QPointSize.SizeMode = ...  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def setSizeMode(
            self, sizeMode: PySide2.Qt3DRender.Qt3DRender.QPointSize.SizeMode
        ) -> None: ...
        def setValue(self, value: float) -> None: ...
        def sizeMode(self) -> PySide2.Qt3DRender.Qt3DRender.QPointSize.SizeMode: ...
        def value(self) -> float: ...

    class QPolygonOffset(PySide2.Qt3DRender.QRenderState):
        depthStepsChanged: PySide2.QtCore.Signal
        scaleFactorChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def depthSteps(self) -> float: ...
        def scaleFactor(self) -> float: ...
        def setDepthSteps(self, depthSteps: float) -> None: ...
        def setScaleFactor(self, scaleFactor: float) -> None: ...

    class QProximityFilter(PySide2.Qt3DRender.QFrameGraphNode):
        distanceThresholdChanged: PySide2.QtCore.Signal
        entityChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def distanceThreshold(self) -> float: ...
        def entity(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def setDistanceThreshold(self, distanceThreshold: float) -> None: ...
        def setEntity(self, entity: PySide2.Qt3DCore.Qt3DCore.QEntity) -> None: ...

    class QRayCaster(PySide2.Qt3DRender.QAbstractRayCaster):
        directionChanged: PySide2.QtCore.Signal
        lengthChanged: PySide2.QtCore.Signal
        originChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def direction(self) -> PySide2.QtGui.QVector3D: ...
        def length(self) -> float: ...
        def origin(self) -> PySide2.QtGui.QVector3D: ...
        def setDirection(self, direction: PySide2.QtGui.QVector3D) -> None: ...
        def setLength(self, length: float) -> None: ...
        def setOrigin(self, origin: PySide2.QtGui.QVector3D) -> None: ...
        @typing.overload
        def trigger(self) -> None: ...
        @typing.overload
        def trigger(
            self,
            origin: PySide2.QtGui.QVector3D,
            direction: PySide2.QtGui.QVector3D,
            length: float,
        ) -> None: ...

    class QRayCasterHit(Shiboken.Object):
        TriangleHit: Qt3DRender.QRayCasterHit.HitType = ...  # 0x0
        LineHit: Qt3DRender.QRayCasterHit.HitType = ...  # 0x1
        PointHit: Qt3DRender.QRayCasterHit.HitType = ...  # 0x2
        EntityHit: Qt3DRender.QRayCasterHit.HitType = ...  # 0x3

        class HitType(object):
            TriangleHit: Qt3DRender.QRayCasterHit.HitType = ...  # 0x0
            LineHit: Qt3DRender.QRayCasterHit.HitType = ...  # 0x1
            PointHit: Qt3DRender.QRayCasterHit.HitType = ...  # 0x2
            EntityHit: Qt3DRender.QRayCasterHit.HitType = ...  # 0x3
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(
            self, other: PySide2.Qt3DRender.Qt3DRender.QRayCasterHit
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            type: PySide2.Qt3DRender.Qt3DRender.QRayCasterHit.HitType,
            id: PySide2.Qt3DCore.Qt3DCore.QNodeId,
            distance: float,
            localIntersect: PySide2.QtGui.QVector3D,
            worldIntersect: PySide2.QtGui.QVector3D,
            primitiveIndex: int,
            v1: int,
            v2: int,
            v3: int,
        ) -> None: ...
        @staticmethod
        def __copy__() -> None: ...
        def distance(self) -> float: ...
        def entity(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def entityId(self) -> PySide2.Qt3DCore.Qt3DCore.QNodeId: ...
        def localIntersection(self) -> PySide2.QtGui.QVector3D: ...
        def primitiveIndex(self) -> int: ...
        def type(self) -> PySide2.Qt3DRender.Qt3DRender.QRayCasterHit.HitType: ...
        def vertex1Index(self) -> int: ...
        def vertex2Index(self) -> int: ...
        def vertex3Index(self) -> int: ...
        def worldIntersection(self) -> PySide2.QtGui.QVector3D: ...

    class QRenderAspect(PySide2.Qt3DCore.QAbstractAspect):
        Synchronous: Qt3DRender.QRenderAspect.RenderType = ...  # 0x0
        Threaded: Qt3DRender.QRenderAspect.RenderType = ...  # 0x1

        class RenderType(object):
            Synchronous: Qt3DRender.QRenderAspect.RenderType = ...  # 0x0
            Threaded: Qt3DRender.QRenderAspect.RenderType = ...  # 0x1
        @typing.overload
        def __init__(
            self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            type: PySide2.Qt3DRender.Qt3DRender.QRenderAspect.RenderType,
            parent: typing.Optional[PySide2.QtCore.QObject] = ...,
        ) -> None: ...

    class QRenderCapabilities(PySide2.QtCore.QObject):
        NoProfile: Qt3DRender.QRenderCapabilities.Profile = ...  # 0x0
        CoreProfile: Qt3DRender.QRenderCapabilities.Profile = ...  # 0x1
        OpenGL: Qt3DRender.QRenderCapabilities.API = ...  # 0x1
        CompatibilityProfile: Qt3DRender.QRenderCapabilities.Profile = ...  # 0x2
        OpenGLES: Qt3DRender.QRenderCapabilities.API = ...  # 0x2
        Vulkan: Qt3DRender.QRenderCapabilities.API = ...  # 0x3
        DirectX: Qt3DRender.QRenderCapabilities.API = ...  # 0x4
        RHI: Qt3DRender.QRenderCapabilities.API = ...  # 0x5

        class API(object):
            OpenGL: Qt3DRender.QRenderCapabilities.API = ...  # 0x1
            OpenGLES: Qt3DRender.QRenderCapabilities.API = ...  # 0x2
            Vulkan: Qt3DRender.QRenderCapabilities.API = ...  # 0x3
            DirectX: Qt3DRender.QRenderCapabilities.API = ...  # 0x4
            RHI: Qt3DRender.QRenderCapabilities.API = ...  # 0x5

        class Profile(object):
            NoProfile: Qt3DRender.QRenderCapabilities.Profile = ...  # 0x0
            CoreProfile: Qt3DRender.QRenderCapabilities.Profile = ...  # 0x1
            CompatibilityProfile: Qt3DRender.QRenderCapabilities.Profile = ...  # 0x2
        def __init__(
            self, parent: typing.Optional[PySide2.QtCore.QObject] = ...
        ) -> None: ...
        def api(self) -> PySide2.Qt3DRender.Qt3DRender.QRenderCapabilities.API: ...
        def driverVersion(self) -> str: ...
        def extensions(self) -> typing.List: ...
        def glslVersion(self) -> str: ...
        def isValid(self) -> bool: ...
        def majorVersion(self) -> int: ...
        def maxComputeInvocations(self) -> int: ...
        def maxComputeSharedMemorySize(self) -> int: ...
        def maxImageUnits(self) -> int: ...
        def maxSSBOBindings(self) -> int: ...
        def maxSSBOSize(self) -> int: ...
        def maxSamples(self) -> int: ...
        def maxTextureLayers(self) -> int: ...
        def maxTextureSize(self) -> int: ...
        def maxTextureUnits(self) -> int: ...
        def maxUBOBindings(self) -> int: ...
        def maxUBOSize(self) -> int: ...
        def maxWorkGroupCountX(self) -> int: ...
        def maxWorkGroupCountY(self) -> int: ...
        def maxWorkGroupCountZ(self) -> int: ...
        def maxWorkGroupSizeX(self) -> int: ...
        def maxWorkGroupSizeY(self) -> int: ...
        def maxWorkGroupSizeZ(self) -> int: ...
        def minorVersion(self) -> int: ...
        def profile(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QRenderCapabilities.Profile: ...
        def renderer(self) -> str: ...
        def supportsCompute(self) -> bool: ...
        def supportsImageStore(self) -> bool: ...
        def supportsSSBO(self) -> bool: ...
        def supportsUBO(self) -> bool: ...
        def vendor(self) -> str: ...

    class QRenderCapture(PySide2.Qt3DRender.QFrameGraphNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        @typing.overload
        def requestCapture(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QRenderCaptureReply: ...
        @typing.overload
        def requestCapture(
            self, captureId: int
        ) -> PySide2.Qt3DRender.Qt3DRender.QRenderCaptureReply: ...
        @typing.overload
        def requestCapture(
            self, rect: PySide2.QtCore.QRect
        ) -> PySide2.Qt3DRender.Qt3DRender.QRenderCaptureReply: ...

    class QRenderCaptureReply(PySide2.QtCore.QObject):
        completeChanged: PySide2.QtCore.Signal
        completed: PySide2.QtCore.Signal

        def captureId(self) -> int: ...
        def image(self) -> PySide2.QtGui.QImage: ...
        def isComplete(self) -> bool: ...
        def saveImage(self, fileName: str) -> bool: ...
        def saveToFile(self, fileName: str) -> None: ...

    class QRenderPass(PySide2.Qt3DCore.QNode):
        shaderProgramChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addFilterKey(
            self, filterKey: PySide2.Qt3DRender.Qt3DRender.QFilterKey
        ) -> None: ...
        def addParameter(self, p: PySide2.Qt3DRender.Qt3DRender.QParameter) -> None: ...
        def addRenderState(
            self, state: PySide2.Qt3DRender.Qt3DRender.QRenderState
        ) -> None: ...
        def filterKeys(self) -> typing.List: ...
        def parameters(self) -> typing.List: ...
        def removeFilterKey(
            self, filterKey: PySide2.Qt3DRender.Qt3DRender.QFilterKey
        ) -> None: ...
        def removeParameter(
            self, p: PySide2.Qt3DRender.Qt3DRender.QParameter
        ) -> None: ...
        def removeRenderState(
            self, state: PySide2.Qt3DRender.Qt3DRender.QRenderState
        ) -> None: ...
        def renderStates(self) -> typing.List: ...
        def setShaderProgram(
            self, shaderProgram: PySide2.Qt3DRender.Qt3DRender.QShaderProgram
        ) -> None: ...
        def shaderProgram(self) -> PySide2.Qt3DRender.Qt3DRender.QShaderProgram: ...

    class QRenderPassFilter(PySide2.Qt3DRender.QFrameGraphNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addMatch(
            self, filterKey: PySide2.Qt3DRender.Qt3DRender.QFilterKey
        ) -> None: ...
        def addParameter(
            self, parameter: PySide2.Qt3DRender.Qt3DRender.QParameter
        ) -> None: ...
        def matchAny(self) -> typing.List: ...
        def parameters(self) -> typing.List: ...
        def removeMatch(
            self, filterKey: PySide2.Qt3DRender.Qt3DRender.QFilterKey
        ) -> None: ...
        def removeParameter(
            self, parameter: PySide2.Qt3DRender.Qt3DRender.QParameter
        ) -> None: ...

    class QRenderSettings(PySide2.Qt3DCore.QComponent):
        activeFrameGraphChanged: PySide2.QtCore.Signal
        renderPolicyChanged: PySide2.QtCore.Signal

        OnDemand: Qt3DRender.QRenderSettings.RenderPolicy = ...  # 0x0
        Always: Qt3DRender.QRenderSettings.RenderPolicy = ...  # 0x1

        class RenderPolicy(object):
            OnDemand: Qt3DRender.QRenderSettings.RenderPolicy = ...  # 0x0
            Always: Qt3DRender.QRenderSettings.RenderPolicy = ...  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def activeFrameGraph(self) -> PySide2.Qt3DRender.Qt3DRender.QFrameGraphNode: ...
        def pickingSettings(self) -> PySide2.Qt3DRender.Qt3DRender.QPickingSettings: ...
        def renderCapabilities(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QRenderCapabilities: ...
        def renderPolicy(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QRenderSettings.RenderPolicy: ...
        def setActiveFrameGraph(
            self, activeFrameGraph: PySide2.Qt3DRender.Qt3DRender.QFrameGraphNode
        ) -> None: ...
        def setRenderPolicy(
            self,
            renderPolicy: PySide2.Qt3DRender.Qt3DRender.QRenderSettings.RenderPolicy,
        ) -> None: ...

    class QRenderState(PySide2.Qt3DCore.QNode): ...

    class QRenderStateSet(PySide2.Qt3DRender.QFrameGraphNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addRenderState(
            self, state: PySide2.Qt3DRender.Qt3DRender.QRenderState
        ) -> None: ...
        def removeRenderState(
            self, state: PySide2.Qt3DRender.Qt3DRender.QRenderState
        ) -> None: ...
        def renderStates(self) -> typing.List: ...

    class QRenderSurfaceSelector(PySide2.Qt3DRender.QFrameGraphNode):
        externalRenderTargetSizeChanged: PySide2.QtCore.Signal
        surfaceChanged: PySide2.QtCore.Signal
        surfacePixelRatioChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def externalRenderTargetSize(self) -> PySide2.QtCore.QSize: ...
        def setExternalRenderTargetSize(self, size: PySide2.QtCore.QSize) -> None: ...
        def setSurface(self, surfaceObject: PySide2.QtCore.QObject) -> None: ...
        def setSurfacePixelRatio(self, ratio: float) -> None: ...
        def surface(self) -> PySide2.QtCore.QObject: ...
        def surfacePixelRatio(self) -> float: ...

    class QRenderTarget(PySide2.Qt3DCore.QComponent):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addOutput(
            self, output: PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput
        ) -> None: ...
        def outputs(self) -> typing.List: ...
        def removeOutput(
            self, output: PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput
        ) -> None: ...

    class QRenderTargetOutput(PySide2.Qt3DCore.QNode):
        attachmentPointChanged: PySide2.QtCore.Signal
        faceChanged: PySide2.QtCore.Signal
        layerChanged: PySide2.QtCore.Signal
        mipLevelChanged: PySide2.QtCore.Signal
        textureChanged: PySide2.QtCore.Signal

        Color0: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x0
        Color1: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x1
        Color2: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x2
        Color3: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x3
        Color4: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x4
        Color5: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x5
        Color6: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x6
        Color7: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x7
        Color8: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x8
        Color9: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x9
        Color10: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xa
        Color11: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xb
        Color12: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xc
        Color13: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xd
        Color14: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xe
        Color15: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xf
        Depth: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x10
        Stencil: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x11
        DepthStencil: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x12

        class AttachmentPoint(object):
            Color0: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x0
            Color1: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x1
            Color2: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x2
            Color3: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x3
            Color4: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x4
            Color5: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x5
            Color6: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x6
            Color7: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x7
            Color8: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x8
            Color9: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x9
            Color10: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xa
            Color11: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xb
            Color12: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xc
            Color13: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xd
            Color14: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xe
            Color15: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0xf
            Depth: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x10
            Stencil: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x11
            DepthStencil: Qt3DRender.QRenderTargetOutput.AttachmentPoint = ...  # 0x12
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def attachmentPoint(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint: ...
        def face(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace: ...
        def layer(self) -> int: ...
        def mipLevel(self) -> int: ...
        def setAttachmentPoint(
            self,
            attachmentPoint: PySide2.Qt3DRender.Qt3DRender.QRenderTargetOutput.AttachmentPoint,
        ) -> None: ...
        def setFace(
            self, face: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.CubeMapFace
        ) -> None: ...
        def setLayer(self, layer: int) -> None: ...
        def setMipLevel(self, level: int) -> None: ...
        def setTexture(
            self, texture: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture
        ) -> None: ...
        def texture(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...

    class QRenderTargetSelector(PySide2.Qt3DRender.QFrameGraphNode):
        targetChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def outputs(self) -> typing.List: ...
        def setOutputs(self, buffers: typing.List) -> None: ...
        def setTarget(
            self, target: PySide2.Qt3DRender.Qt3DRender.QRenderTarget
        ) -> None: ...
        def target(self) -> PySide2.Qt3DRender.Qt3DRender.QRenderTarget: ...

    class QSceneLoader(PySide2.Qt3DCore.QComponent):
        sourceChanged: PySide2.QtCore.Signal
        statusChanged: PySide2.QtCore.Signal

        None_: Qt3DRender.QSceneLoader.Status = ...  # 0x0
        UnknownComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x0
        GeometryRendererComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x1
        Loading: Qt3DRender.QSceneLoader.Status = ...  # 0x1
        Ready: Qt3DRender.QSceneLoader.Status = ...  # 0x2
        TransformComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x2
        Error: Qt3DRender.QSceneLoader.Status = ...  # 0x3
        MaterialComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x3
        LightComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x4
        CameraLensComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x5

        class ComponentType(object):
            UnknownComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x0
            GeometryRendererComponent: Qt3DRender.QSceneLoader.ComponentType = (
                ...
            )  # 0x1
            TransformComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x2
            MaterialComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x3
            LightComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x4
            CameraLensComponent: Qt3DRender.QSceneLoader.ComponentType = ...  # 0x5

        class Status(object):
            None_: Qt3DRender.QSceneLoader.Status = ...  # 0x0
            Loading: Qt3DRender.QSceneLoader.Status = ...  # 0x1
            Ready: Qt3DRender.QSceneLoader.Status = ...  # 0x2
            Error: Qt3DRender.QSceneLoader.Status = ...  # 0x3
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def component(
            self,
            entityName: str,
            componentType: PySide2.Qt3DRender.Qt3DRender.QSceneLoader.ComponentType,
        ) -> PySide2.Qt3DCore.Qt3DCore.QComponent: ...
        def entity(self, entityName: str) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def entityNames(self) -> typing.List: ...
        def setSource(self, arg: PySide2.QtCore.QUrl) -> None: ...
        def setStatus(
            self, status: PySide2.Qt3DRender.Qt3DRender.QSceneLoader.Status
        ) -> None: ...
        def source(self) -> PySide2.QtCore.QUrl: ...
        def status(self) -> PySide2.Qt3DRender.Qt3DRender.QSceneLoader.Status: ...

    class QScissorTest(PySide2.Qt3DRender.QRenderState):
        bottomChanged: PySide2.QtCore.Signal
        heightChanged: PySide2.QtCore.Signal
        leftChanged: PySide2.QtCore.Signal
        widthChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def bottom(self) -> int: ...
        def height(self) -> int: ...
        def left(self) -> int: ...
        def setBottom(self, bottom: int) -> None: ...
        def setHeight(self, height: int) -> None: ...
        def setLeft(self, left: int) -> None: ...
        def setWidth(self, width: int) -> None: ...
        def width(self) -> int: ...

    class QScreenRayCaster(PySide2.Qt3DRender.QAbstractRayCaster):
        positionChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def position(self) -> PySide2.QtCore.QPoint: ...
        def setPosition(self, position: PySide2.QtCore.QPoint) -> None: ...
        @typing.overload
        def trigger(self) -> None: ...
        @typing.overload
        def trigger(self, position: PySide2.QtCore.QPoint) -> None: ...

    class QSeamlessCubemap(PySide2.Qt3DRender.QRenderState):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QSetFence(PySide2.Qt3DRender.QFrameGraphNode):
        handleChanged: PySide2.QtCore.Signal
        handleTypeChanged: PySide2.QtCore.Signal

        NoHandle: Qt3DRender.QSetFence.HandleType = ...  # 0x0
        OpenGLFenceId: Qt3DRender.QSetFence.HandleType = ...  # 0x1

        class HandleType(object):
            NoHandle: Qt3DRender.QSetFence.HandleType = ...  # 0x0
            OpenGLFenceId: Qt3DRender.QSetFence.HandleType = ...  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def handle(self) -> typing.Any: ...
        def handleType(self) -> PySide2.Qt3DRender.Qt3DRender.QSetFence.HandleType: ...

    class QShaderData(PySide2.Qt3DCore.QComponent):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def event(self, event: PySide2.QtCore.QEvent) -> bool: ...

    class QShaderImage(PySide2.Qt3DCore.QNode):
        accessChanged: PySide2.QtCore.Signal
        formatChanged: PySide2.QtCore.Signal
        layerChanged: PySide2.QtCore.Signal
        layeredChanged: PySide2.QtCore.Signal
        mipLevelChanged: PySide2.QtCore.Signal
        textureChanged: PySide2.QtCore.Signal

        NoFormat: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x0
        ReadOnly: Qt3DRender.QShaderImage.Access = ...  # 0x0
        Automatic: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x1
        WriteOnly: Qt3DRender.QShaderImage.Access = ...  # 0x1
        ReadWrite: Qt3DRender.QShaderImage.Access = ...  # 0x2
        RGBA8_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8058
        RGB10A2: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8059
        RGBA16_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x805b
        R8_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8229
        R16_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822a
        RG8_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822b
        RG16_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822c
        R16F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822d
        R32F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822e
        RG16F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822f
        RG32F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8230
        R8I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8231
        R8U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8232
        R16I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8233
        R16U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8234
        R32I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8235
        R32U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8236
        RG8I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8237
        RG8U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8238
        RG16I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8239
        RG16U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x823a
        RG32I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x823b
        RG32U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x823c
        RGBA32F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8814
        RGBA16F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x881a
        RG11B10F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8c3a
        RGBA32U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d70
        RGBA16U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d76
        RGBA8U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d7c
        RGBA32I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d82
        RGBA16I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d88
        RGBA8I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d8e
        R8_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f94
        RG8_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f95
        RGBA8_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f97
        R16_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f98
        RG16_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f99
        RGBA16_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f9b
        RGB10A2U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x906f

        class Access(object):
            ReadOnly: Qt3DRender.QShaderImage.Access = ...  # 0x0
            WriteOnly: Qt3DRender.QShaderImage.Access = ...  # 0x1
            ReadWrite: Qt3DRender.QShaderImage.Access = ...  # 0x2

        class ImageFormat(object):
            NoFormat: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x0
            Automatic: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x1
            RGBA8_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8058
            RGB10A2: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8059
            RGBA16_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x805b
            R8_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8229
            R16_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822a
            RG8_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822b
            RG16_UNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822c
            R16F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822d
            R32F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822e
            RG16F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x822f
            RG32F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8230
            R8I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8231
            R8U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8232
            R16I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8233
            R16U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8234
            R32I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8235
            R32U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8236
            RG8I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8237
            RG8U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8238
            RG16I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8239
            RG16U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x823a
            RG32I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x823b
            RG32U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x823c
            RGBA32F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8814
            RGBA16F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x881a
            RG11B10F: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8c3a
            RGBA32U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d70
            RGBA16U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d76
            RGBA8U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d7c
            RGBA32I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d82
            RGBA16I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d88
            RGBA8I: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8d8e
            R8_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f94
            RG8_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f95
            RGBA8_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f97
            R16_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f98
            RG16_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f99
            RGBA16_SNorm: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x8f9b
            RGB10A2U: Qt3DRender.QShaderImage.ImageFormat = ...  # 0x906f
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def access(self) -> PySide2.Qt3DRender.Qt3DRender.QShaderImage.Access: ...
        def format(self) -> PySide2.Qt3DRender.Qt3DRender.QShaderImage.ImageFormat: ...
        def layer(self) -> int: ...
        def layered(self) -> bool: ...
        def mipLevel(self) -> int: ...
        def setAccess(
            self, access: PySide2.Qt3DRender.Qt3DRender.QShaderImage.Access
        ) -> None: ...
        def setFormat(
            self, format: PySide2.Qt3DRender.Qt3DRender.QShaderImage.ImageFormat
        ) -> None: ...
        def setLayer(self, layer: int) -> None: ...
        def setLayered(self, layered: bool) -> None: ...
        def setMipLevel(self, mipLevel: int) -> None: ...
        def setTexture(
            self, texture: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture
        ) -> None: ...
        def texture(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...

    class QShaderProgram(PySide2.Qt3DCore.QNode):
        computeShaderCodeChanged: PySide2.QtCore.Signal
        formatChanged: PySide2.QtCore.Signal
        fragmentShaderCodeChanged: PySide2.QtCore.Signal
        geometryShaderCodeChanged: PySide2.QtCore.Signal
        logChanged: PySide2.QtCore.Signal
        statusChanged: PySide2.QtCore.Signal
        tessellationControlShaderCodeChanged: PySide2.QtCore.Signal
        tessellationEvaluationShaderCodeChanged: PySide2.QtCore.Signal
        vertexShaderCodeChanged: PySide2.QtCore.Signal

        GLSL: Qt3DRender.QShaderProgram.Format = ...  # 0x0
        NotReady: Qt3DRender.QShaderProgram.Status = ...  # 0x0
        Vertex: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x0
        Fragment: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x1
        Ready: Qt3DRender.QShaderProgram.Status = ...  # 0x1
        SPIRV: Qt3DRender.QShaderProgram.Format = ...  # 0x1
        Error: Qt3DRender.QShaderProgram.Status = ...  # 0x2
        TessellationControl: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x2
        TessellationEvaluation: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x3
        Geometry: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x4
        Compute: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x5

        class Format(object):
            GLSL: Qt3DRender.QShaderProgram.Format = ...  # 0x0
            SPIRV: Qt3DRender.QShaderProgram.Format = ...  # 0x1

        class ShaderType(object):
            Vertex: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x0
            Fragment: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x1
            TessellationControl: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x2
            TessellationEvaluation: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x3
            Geometry: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x4
            Compute: Qt3DRender.QShaderProgram.ShaderType = ...  # 0x5

        class Status(object):
            NotReady: Qt3DRender.QShaderProgram.Status = ...  # 0x0
            Ready: Qt3DRender.QShaderProgram.Status = ...  # 0x1
            Error: Qt3DRender.QShaderProgram.Status = ...  # 0x2
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def computeShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def format(self) -> PySide2.Qt3DRender.Qt3DRender.QShaderProgram.Format: ...
        def fragmentShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def geometryShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        @staticmethod
        def loadSource(sourceUrl: PySide2.QtCore.QUrl) -> PySide2.QtCore.QByteArray: ...
        def log(self) -> str: ...
        def setComputeShaderCode(
            self, computeShaderCode: PySide2.QtCore.QByteArray
        ) -> None: ...
        def setFormat(
            self, format: PySide2.Qt3DRender.Qt3DRender.QShaderProgram.Format
        ) -> None: ...
        def setFragmentShaderCode(
            self, fragmentShaderCode: PySide2.QtCore.QByteArray
        ) -> None: ...
        def setGeometryShaderCode(
            self, geometryShaderCode: PySide2.QtCore.QByteArray
        ) -> None: ...
        def setShaderCode(
            self,
            type: PySide2.Qt3DRender.Qt3DRender.QShaderProgram.ShaderType,
            shaderCode: PySide2.QtCore.QByteArray,
        ) -> None: ...
        def setTessellationControlShaderCode(
            self, tessellationControlShaderCode: PySide2.QtCore.QByteArray
        ) -> None: ...
        def setTessellationEvaluationShaderCode(
            self, tessellationEvaluationShaderCode: PySide2.QtCore.QByteArray
        ) -> None: ...
        def setVertexShaderCode(
            self, vertexShaderCode: PySide2.QtCore.QByteArray
        ) -> None: ...
        def shaderCode(
            self, type: PySide2.Qt3DRender.Qt3DRender.QShaderProgram.ShaderType
        ) -> PySide2.QtCore.QByteArray: ...
        def status(self) -> PySide2.Qt3DRender.Qt3DRender.QShaderProgram.Status: ...
        def tessellationControlShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def tessellationEvaluationShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def vertexShaderCode(self) -> PySide2.QtCore.QByteArray: ...

    class QShaderProgramBuilder(PySide2.Qt3DCore.QNode):
        computeShaderCodeChanged: PySide2.QtCore.Signal
        computeShaderGraphChanged: PySide2.QtCore.Signal
        enabledLayersChanged: PySide2.QtCore.Signal
        fragmentShaderCodeChanged: PySide2.QtCore.Signal
        fragmentShaderGraphChanged: PySide2.QtCore.Signal
        geometryShaderCodeChanged: PySide2.QtCore.Signal
        geometryShaderGraphChanged: PySide2.QtCore.Signal
        shaderProgramChanged: PySide2.QtCore.Signal
        tessellationControlShaderCodeChanged: PySide2.QtCore.Signal
        tessellationControlShaderGraphChanged: PySide2.QtCore.Signal
        tessellationEvaluationShaderCodeChanged: PySide2.QtCore.Signal
        tessellationEvaluationShaderGraphChanged: PySide2.QtCore.Signal
        vertexShaderCodeChanged: PySide2.QtCore.Signal
        vertexShaderGraphChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def computeShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def computeShaderGraph(self) -> PySide2.QtCore.QUrl: ...
        def enabledLayers(self) -> typing.List: ...
        def fragmentShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def fragmentShaderGraph(self) -> PySide2.QtCore.QUrl: ...
        def geometryShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def geometryShaderGraph(self) -> PySide2.QtCore.QUrl: ...
        def setComputeShaderGraph(
            self, computeShaderGraph: PySide2.QtCore.QUrl
        ) -> None: ...
        def setEnabledLayers(self, layers: typing.Sequence) -> None: ...
        def setFragmentShaderGraph(
            self, fragmentShaderGraph: PySide2.QtCore.QUrl
        ) -> None: ...
        def setGeometryShaderGraph(
            self, geometryShaderGraph: PySide2.QtCore.QUrl
        ) -> None: ...
        def setShaderProgram(
            self, program: PySide2.Qt3DRender.Qt3DRender.QShaderProgram
        ) -> None: ...
        def setTessellationControlShaderGraph(
            self, tessellationControlShaderGraph: PySide2.QtCore.QUrl
        ) -> None: ...
        def setTessellationEvaluationShaderGraph(
            self, tessellationEvaluationShaderGraph: PySide2.QtCore.QUrl
        ) -> None: ...
        def setVertexShaderGraph(
            self, vertexShaderGraph: PySide2.QtCore.QUrl
        ) -> None: ...
        def shaderProgram(self) -> PySide2.Qt3DRender.Qt3DRender.QShaderProgram: ...
        def tessellationControlShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def tessellationControlShaderGraph(self) -> PySide2.QtCore.QUrl: ...
        def tessellationEvaluationShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def tessellationEvaluationShaderGraph(self) -> PySide2.QtCore.QUrl: ...
        def vertexShaderCode(self) -> PySide2.QtCore.QByteArray: ...
        def vertexShaderGraph(self) -> PySide2.QtCore.QUrl: ...

    class QSharedGLTexture(PySide2.Qt3DRender.QAbstractTexture):
        textureIdChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def setTextureId(self, id: int) -> None: ...
        def textureId(self) -> int: ...

    class QSortPolicy(PySide2.Qt3DRender.QFrameGraphNode):
        sortTypesChanged: PySide2.QtCore.Signal

        StateChangeCost: Qt3DRender.QSortPolicy.SortType = ...  # 0x1
        BackToFront: Qt3DRender.QSortPolicy.SortType = ...  # 0x2
        Material: Qt3DRender.QSortPolicy.SortType = ...  # 0x4
        FrontToBack: Qt3DRender.QSortPolicy.SortType = ...  # 0x8
        Texture: Qt3DRender.QSortPolicy.SortType = ...  # 0x10
        Uniform: Qt3DRender.QSortPolicy.SortType = ...  # 0x20

        class SortType(object):
            StateChangeCost: Qt3DRender.QSortPolicy.SortType = ...  # 0x1
            BackToFront: Qt3DRender.QSortPolicy.SortType = ...  # 0x2
            Material: Qt3DRender.QSortPolicy.SortType = ...  # 0x4
            FrontToBack: Qt3DRender.QSortPolicy.SortType = ...  # 0x8
            Texture: Qt3DRender.QSortPolicy.SortType = ...  # 0x10
            Uniform: Qt3DRender.QSortPolicy.SortType = ...  # 0x20
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        @typing.overload
        def setSortTypes(self, sortTypes: typing.List) -> None: ...
        @typing.overload
        def setSortTypes(self, sortTypesInt: typing.List) -> None: ...
        def sortTypes(self) -> typing.List: ...
        def sortTypesInt(self) -> typing.List: ...

    class QSpotLight(PySide2.Qt3DRender.QAbstractLight):
        constantAttenuationChanged: PySide2.QtCore.Signal
        cutOffAngleChanged: PySide2.QtCore.Signal
        linearAttenuationChanged: PySide2.QtCore.Signal
        localDirectionChanged: PySide2.QtCore.Signal
        quadraticAttenuationChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def constantAttenuation(self) -> float: ...
        def cutOffAngle(self) -> float: ...
        def linearAttenuation(self) -> float: ...
        def localDirection(self) -> PySide2.QtGui.QVector3D: ...
        def quadraticAttenuation(self) -> float: ...
        def setConstantAttenuation(self, value: float) -> None: ...
        def setCutOffAngle(self, cutOffAngle: float) -> None: ...
        def setLinearAttenuation(self, value: float) -> None: ...
        def setLocalDirection(
            self, localDirection: PySide2.QtGui.QVector3D
        ) -> None: ...
        def setQuadraticAttenuation(self, value: float) -> None: ...

    class QStencilMask(PySide2.Qt3DRender.QRenderState):
        backOutputMaskChanged: PySide2.QtCore.Signal
        frontOutputMaskChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def backOutputMask(self) -> int: ...
        def frontOutputMask(self) -> int: ...
        def setBackOutputMask(self, backOutputMask: int) -> None: ...
        def setFrontOutputMask(self, frontOutputMask: int) -> None: ...

    class QStencilOperation(PySide2.Qt3DRender.QRenderState):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def back(self) -> PySide2.Qt3DRender.Qt3DRender.QStencilOperationArguments: ...
        def front(self) -> PySide2.Qt3DRender.Qt3DRender.QStencilOperationArguments: ...

    class QStencilOperationArguments(PySide2.QtCore.QObject):
        allTestsPassOperationChanged: PySide2.QtCore.Signal
        depthTestFailureOperationChanged: PySide2.QtCore.Signal
        faceModeChanged: PySide2.QtCore.Signal
        stencilTestFailureOperationChanged: PySide2.QtCore.Signal

        Zero: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x0
        Front: Qt3DRender.QStencilOperationArguments.FaceMode = ...  # 0x404
        Back: Qt3DRender.QStencilOperationArguments.FaceMode = ...  # 0x405
        FrontAndBack: Qt3DRender.QStencilOperationArguments.FaceMode = ...  # 0x408
        Invert: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x150a
        Keep: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x1e00
        Replace: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x1e01
        Increment: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x1e02
        Decrement: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x1e03
        IncrementWrap: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x8507
        DecrementWrap: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x8508

        class FaceMode(object):
            Front: Qt3DRender.QStencilOperationArguments.FaceMode = ...  # 0x404
            Back: Qt3DRender.QStencilOperationArguments.FaceMode = ...  # 0x405
            FrontAndBack: Qt3DRender.QStencilOperationArguments.FaceMode = ...  # 0x408

        class Operation(object):
            Zero: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x0
            Invert: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x150a
            Keep: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x1e00
            Replace: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x1e01
            Increment: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x1e02
            Decrement: Qt3DRender.QStencilOperationArguments.Operation = ...  # 0x1e03
            IncrementWrap: Qt3DRender.QStencilOperationArguments.Operation = (
                ...
            )  # 0x8507
            DecrementWrap: Qt3DRender.QStencilOperationArguments.Operation = (
                ...
            )  # 0x8508
        def allTestsPassOperation(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation: ...
        def depthTestFailureOperation(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation: ...
        def faceMode(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QStencilOperationArguments.FaceMode: ...
        def setAllTestsPassOperation(
            self,
            operation: PySide2.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation,
        ) -> None: ...
        def setDepthTestFailureOperation(
            self,
            operation: PySide2.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation,
        ) -> None: ...
        def setStencilTestFailureOperation(
            self,
            operation: PySide2.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation,
        ) -> None: ...
        def stencilTestFailureOperation(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QStencilOperationArguments.Operation: ...

    class QStencilTest(PySide2.Qt3DRender.QRenderState):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def back(self) -> PySide2.Qt3DRender.Qt3DRender.QStencilTestArguments: ...
        def front(self) -> PySide2.Qt3DRender.Qt3DRender.QStencilTestArguments: ...

    class QStencilTestArguments(PySide2.QtCore.QObject):
        comparisonMaskChanged: PySide2.QtCore.Signal
        faceModeChanged: PySide2.QtCore.Signal
        referenceValueChanged: PySide2.QtCore.Signal
        stencilFunctionChanged: PySide2.QtCore.Signal

        Never: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x200
        Less: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x201
        Equal: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x202
        LessOrEqual: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x203
        Greater: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x204
        NotEqual: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x205
        GreaterOrEqual: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x206
        Always: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x207
        Front: Qt3DRender.QStencilTestArguments.StencilFaceMode = ...  # 0x404
        Back: Qt3DRender.QStencilTestArguments.StencilFaceMode = ...  # 0x405
        FrontAndBack: Qt3DRender.QStencilTestArguments.StencilFaceMode = ...  # 0x408

        class StencilFaceMode(object):
            Front: Qt3DRender.QStencilTestArguments.StencilFaceMode = ...  # 0x404
            Back: Qt3DRender.QStencilTestArguments.StencilFaceMode = ...  # 0x405
            FrontAndBack: Qt3DRender.QStencilTestArguments.StencilFaceMode = (
                ...
            )  # 0x408

        class StencilFunction(object):
            Never: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x200
            Less: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x201
            Equal: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x202
            LessOrEqual: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x203
            Greater: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x204
            NotEqual: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x205
            GreaterOrEqual: Qt3DRender.QStencilTestArguments.StencilFunction = (
                ...
            )  # 0x206
            Always: Qt3DRender.QStencilTestArguments.StencilFunction = ...  # 0x207
        def comparisonMask(self) -> int: ...
        def faceMode(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QStencilTestArguments.StencilFaceMode: ...
        def referenceValue(self) -> int: ...
        def setComparisonMask(self, comparisonMask: int) -> None: ...
        def setReferenceValue(self, referenceValue: int) -> None: ...
        def setStencilFunction(
            self,
            stencilFunction: PySide2.Qt3DRender.Qt3DRender.QStencilTestArguments.StencilFunction,
        ) -> None: ...
        def stencilFunction(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QStencilTestArguments.StencilFunction: ...

    class QTechnique(PySide2.Qt3DCore.QNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addFilterKey(
            self, filterKey: PySide2.Qt3DRender.Qt3DRender.QFilterKey
        ) -> None: ...
        def addParameter(self, p: PySide2.Qt3DRender.Qt3DRender.QParameter) -> None: ...
        def addRenderPass(
            self, pass_: PySide2.Qt3DRender.Qt3DRender.QRenderPass
        ) -> None: ...
        def filterKeys(self) -> typing.List: ...
        def graphicsApiFilter(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QGraphicsApiFilter: ...
        def parameters(self) -> typing.List: ...
        def removeFilterKey(
            self, filterKey: PySide2.Qt3DRender.Qt3DRender.QFilterKey
        ) -> None: ...
        def removeParameter(
            self, p: PySide2.Qt3DRender.Qt3DRender.QParameter
        ) -> None: ...
        def removeRenderPass(
            self, pass_: PySide2.Qt3DRender.Qt3DRender.QRenderPass
        ) -> None: ...
        def renderPasses(self) -> typing.List: ...

    class QTechniqueFilter(PySide2.Qt3DRender.QFrameGraphNode):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def addMatch(
            self, filterKey: PySide2.Qt3DRender.Qt3DRender.QFilterKey
        ) -> None: ...
        def addParameter(self, p: PySide2.Qt3DRender.Qt3DRender.QParameter) -> None: ...
        def matchAll(self) -> typing.List: ...
        def parameters(self) -> typing.List: ...
        def removeMatch(
            self, filterKey: PySide2.Qt3DRender.Qt3DRender.QFilterKey
        ) -> None: ...
        def removeParameter(
            self, p: PySide2.Qt3DRender.Qt3DRender.QParameter
        ) -> None: ...

    class QTexture1D(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTexture1DArray(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTexture2D(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTexture2DArray(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTexture2DMultisample(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTexture2DMultisampleArray(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTexture3D(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTextureBuffer(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTextureCubeMap(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTextureCubeMapArray(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTextureData(Shiboken.Object):
        def __init__(self) -> None: ...
        def comparisonFunction(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction: ...
        def comparisonMode(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode: ...
        def depth(self) -> int: ...
        def format(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat: ...
        def height(self) -> int: ...
        def isAutoMipMapGenerationEnabled(self) -> bool: ...
        def layers(self) -> int: ...
        def magnificationFilter(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Filter: ...
        def maximumAnisotropy(self) -> float: ...
        def minificationFilter(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Filter: ...
        def setAutoMipMapGenerationEnabled(
            self, isAutoMipMapGenerationEnabled: bool
        ) -> None: ...
        def setComparisonFunction(
            self,
            comparisonFunction: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonFunction,
        ) -> None: ...
        def setComparisonMode(
            self,
            comparisonMode: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.ComparisonMode,
        ) -> None: ...
        def setDepth(self, depth: int) -> None: ...
        def setFormat(
            self, arg__1: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.TextureFormat
        ) -> None: ...
        def setHeight(self, height: int) -> None: ...
        def setLayers(self, layers: int) -> None: ...
        def setMagnificationFilter(
            self, filter: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Filter
        ) -> None: ...
        def setMaximumAnisotropy(self, maximumAnisotropy: float) -> None: ...
        def setMinificationFilter(
            self, filter: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Filter
        ) -> None: ...
        def setTarget(
            self, target: PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Target
        ) -> None: ...
        def setWidth(self, width: int) -> None: ...
        def setWrapModeX(
            self, wrapModeX: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode
        ) -> None: ...
        def setWrapModeY(
            self, wrapModeY: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode
        ) -> None: ...
        def setWrapModeZ(
            self, wrapModeZ: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode
        ) -> None: ...
        def target(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture.Target: ...
        def width(self) -> int: ...
        def wrapModeX(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...
        def wrapModeY(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...
        def wrapModeZ(
            self,
        ) -> PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...

    class QTextureGenerator(PySide2.Qt3DRender.QAbstractFunctor): ...

    class QTextureImage(PySide2.Qt3DRender.QAbstractTextureImage):
        mirroredChanged: PySide2.QtCore.Signal
        sourceChanged: PySide2.QtCore.Signal
        statusChanged: PySide2.QtCore.Signal

        None_: Qt3DRender.QTextureImage.Status = ...  # 0x0
        Loading: Qt3DRender.QTextureImage.Status = ...  # 0x1
        Ready: Qt3DRender.QTextureImage.Status = ...  # 0x2
        Error: Qt3DRender.QTextureImage.Status = ...  # 0x3

        class Status(object):
            None_: Qt3DRender.QTextureImage.Status = ...  # 0x0
            Loading: Qt3DRender.QTextureImage.Status = ...  # 0x1
            Ready: Qt3DRender.QTextureImage.Status = ...  # 0x2
            Error: Qt3DRender.QTextureImage.Status = ...  # 0x3
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def isMirrored(self) -> bool: ...
        def setMirrored(self, mirrored: bool) -> None: ...
        def setSource(self, source: PySide2.QtCore.QUrl) -> None: ...
        def setStatus(
            self, status: PySide2.Qt3DRender.Qt3DRender.QTextureImage.Status
        ) -> None: ...
        def source(self) -> PySide2.QtCore.QUrl: ...
        def status(self) -> PySide2.Qt3DRender.Qt3DRender.QTextureImage.Status: ...

    class QTextureImageData(Shiboken.Object):
        def __init__(self) -> None: ...
        def cleanup(self) -> None: ...
        def data(
            self, layer: int = ..., face: int = ..., mipmapLevel: int = ...
        ) -> PySide2.QtCore.QByteArray: ...
        def depth(self) -> int: ...
        def faces(self) -> int: ...
        def format(self) -> PySide2.QtGui.QOpenGLTexture.TextureFormat: ...
        def height(self) -> int: ...
        def isCompressed(self) -> bool: ...
        def layers(self) -> int: ...
        def mipLevels(self) -> int: ...
        def pixelFormat(self) -> PySide2.QtGui.QOpenGLTexture.PixelFormat: ...
        def pixelType(self) -> PySide2.QtGui.QOpenGLTexture.PixelType: ...
        def setData(
            self,
            data: PySide2.QtCore.QByteArray,
            blockSize: int,
            isCompressed: bool = ...,
        ) -> None: ...
        def setDepth(self, depth: int) -> None: ...
        def setFaces(self, faces: int) -> None: ...
        def setFormat(
            self, format: PySide2.QtGui.QOpenGLTexture.TextureFormat
        ) -> None: ...
        def setHeight(self, height: int) -> None: ...
        def setImage(self, arg__1: PySide2.QtGui.QImage) -> None: ...
        def setLayers(self, layers: int) -> None: ...
        def setMipLevels(self, mipLevels: int) -> None: ...
        def setPixelFormat(
            self, pixelFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat
        ) -> None: ...
        def setPixelType(
            self, pixelType: PySide2.QtGui.QOpenGLTexture.PixelType
        ) -> None: ...
        def setTarget(self, target: PySide2.QtGui.QOpenGLTexture.Target) -> None: ...
        def setWidth(self, width: int) -> None: ...
        def target(self) -> PySide2.QtGui.QOpenGLTexture.Target: ...
        def width(self) -> int: ...

    class QTextureImageDataGenerator(PySide2.Qt3DRender.QAbstractFunctor): ...

    class QTextureLoader(PySide2.Qt3DRender.QAbstractTexture):
        mirroredChanged: PySide2.QtCore.Signal
        sourceChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def isMirrored(self) -> bool: ...
        def setMirrored(self, mirrored: bool) -> None: ...
        def setSource(self, source: PySide2.QtCore.QUrl) -> None: ...
        def source(self) -> PySide2.QtCore.QUrl: ...

    class QTextureRectangle(PySide2.Qt3DRender.QAbstractTexture):
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...

    class QTextureWrapMode(PySide2.QtCore.QObject):
        xChanged: PySide2.QtCore.Signal
        yChanged: PySide2.QtCore.Signal
        zChanged: PySide2.QtCore.Signal

        Repeat: Qt3DRender.QTextureWrapMode.WrapMode = ...  # 0x2901
        ClampToBorder: Qt3DRender.QTextureWrapMode.WrapMode = ...  # 0x812d
        ClampToEdge: Qt3DRender.QTextureWrapMode.WrapMode = ...  # 0x812f
        MirroredRepeat: Qt3DRender.QTextureWrapMode.WrapMode = ...  # 0x8370

        class WrapMode(object):
            Repeat: Qt3DRender.QTextureWrapMode.WrapMode = ...  # 0x2901
            ClampToBorder: Qt3DRender.QTextureWrapMode.WrapMode = ...  # 0x812d
            ClampToEdge: Qt3DRender.QTextureWrapMode.WrapMode = ...  # 0x812f
            MirroredRepeat: Qt3DRender.QTextureWrapMode.WrapMode = ...  # 0x8370
        @typing.overload
        def __init__(
            self,
            wrapMode: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode = ...,
            parent: typing.Optional[PySide2.QtCore.QObject] = ...,
        ) -> None: ...
        @typing.overload
        def __init__(
            self,
            x: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode,
            y: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode,
            z: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode,
            parent: typing.Optional[PySide2.QtCore.QObject] = ...,
        ) -> None: ...
        def setX(
            self, x: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode
        ) -> None: ...
        def setY(
            self, y: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode
        ) -> None: ...
        def setZ(
            self, z: PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode
        ) -> None: ...
        def x(self) -> PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...
        def y(self) -> PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...
        def z(self) -> PySide2.Qt3DRender.Qt3DRender.QTextureWrapMode.WrapMode: ...

    class QViewport(PySide2.Qt3DRender.QFrameGraphNode):
        gammaChanged: PySide2.QtCore.Signal
        normalizedRectChanged: PySide2.QtCore.Signal

        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def gamma(self) -> float: ...
        def normalizedRect(self) -> PySide2.QtCore.QRectF: ...
        def setGamma(self, gamma: float) -> None: ...
        def setNormalizedRect(self, normalizedRect: PySide2.QtCore.QRectF) -> None: ...

    class QWaitFence(PySide2.Qt3DRender.QFrameGraphNode):
        handleChanged: PySide2.QtCore.Signal
        handleTypeChanged: PySide2.QtCore.Signal
        timeoutChanged: PySide2.QtCore.Signal
        waitOnCPUChanged: PySide2.QtCore.Signal

        NoHandle: Qt3DRender.QWaitFence.HandleType = ...  # 0x0
        OpenGLFenceId: Qt3DRender.QWaitFence.HandleType = ...  # 0x1

        class HandleType(object):
            NoHandle: Qt3DRender.QWaitFence.HandleType = ...  # 0x0
            OpenGLFenceId: Qt3DRender.QWaitFence.HandleType = ...  # 0x1
        def __init__(
            self, parent: typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode] = ...
        ) -> None: ...
        def handle(self) -> typing.Any: ...
        def handleType(self) -> PySide2.Qt3DRender.Qt3DRender.QWaitFence.HandleType: ...
        def setHandle(self, handle: typing.Any) -> None: ...
        def setHandleType(
            self, type: PySide2.Qt3DRender.Qt3DRender.QWaitFence.HandleType
        ) -> None: ...
        def setTimeout(self, timeout: int) -> None: ...
        def setWaitOnCPU(self, waitOnCPU: bool) -> None: ...
        def timeout(self) -> int: ...
        def waitOnCPU(self) -> bool: ...

# eof
