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
PySide2.Qt3DInput, except for defaults which are replaced by "...".
"""

# Module PySide2.Qt3DInput
import PySide2
try:
    import typing
except ImportError:
    from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtGui
import PySide2.Qt3DCore
import PySide2.Qt3DInput


class Qt3DInput(Shiboken.Object):

    class QAbstractActionInput(PySide2.Qt3DCore.QNode): ...

    class QAbstractAxisInput(PySide2.Qt3DCore.QNode):
        def setSourceDevice(self, sourceDevice:PySide2.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice) -> None: ...
        def sourceDevice(self) -> PySide2.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QAbstractPhysicalDevice(PySide2.Qt3DCore.QNode):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def addAxisSetting(self, axisSetting:PySide2.Qt3DInput.Qt3DInput.QAxisSetting) -> None: ...
        def axisCount(self) -> int: ...
        def axisIdentifier(self, name:str) -> int: ...
        def axisNames(self) -> typing.List: ...
        def axisSettings(self) -> typing.List: ...
        def buttonCount(self) -> int: ...
        def buttonIdentifier(self, name:str) -> int: ...
        def buttonNames(self) -> typing.List: ...
        def removeAxisSetting(self, axisSetting:PySide2.Qt3DInput.Qt3DInput.QAxisSetting) -> None: ...

    class QAction(PySide2.Qt3DCore.QNode):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def addInput(self, input:PySide2.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def inputs(self) -> typing.List: ...
        def isActive(self) -> bool: ...
        def removeInput(self, input:PySide2.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...

    class QActionInput(PySide2.Qt3DInput.QAbstractActionInput):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def buttons(self) -> typing.List: ...
        def setButtons(self, buttons:typing.List) -> None: ...
        def setSourceDevice(self, sourceDevice:PySide2.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice) -> None: ...
        def sourceDevice(self) -> PySide2.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QAnalogAxisInput(PySide2.Qt3DInput.QAbstractAxisInput):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def axis(self) -> int: ...
        def setAxis(self, axis:int) -> None: ...

    class QAxis(PySide2.Qt3DCore.QNode):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def addInput(self, input:PySide2.Qt3DInput.Qt3DInput.QAbstractAxisInput) -> None: ...
        def inputs(self) -> typing.List: ...
        def removeInput(self, input:PySide2.Qt3DInput.Qt3DInput.QAbstractAxisInput) -> None: ...
        def value(self) -> float: ...

    class QAxisAccumulator(PySide2.Qt3DCore.QComponent):
        Velocity                 : Qt3DInput.QAxisAccumulator = ... # 0x0
        Acceleration             : Qt3DInput.QAxisAccumulator = ... # 0x1

        class SourceAxisType(object):
            Velocity                 : Qt3DInput.QAxisAccumulator.SourceAxisType = ... # 0x0
            Acceleration             : Qt3DInput.QAxisAccumulator.SourceAxisType = ... # 0x1

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def scale(self) -> float: ...
        def setScale(self, scale:float) -> None: ...
        def setSourceAxis(self, sourceAxis:PySide2.Qt3DInput.Qt3DInput.QAxis) -> None: ...
        def setSourceAxisType(self, sourceAxisType:PySide2.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType) -> None: ...
        def sourceAxis(self) -> PySide2.Qt3DInput.Qt3DInput.QAxis: ...
        def sourceAxisType(self) -> PySide2.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType: ...
        def value(self) -> float: ...
        def velocity(self) -> float: ...

    class QAxisSetting(PySide2.Qt3DCore.QNode):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def axes(self) -> typing.List: ...
        def deadZoneRadius(self) -> float: ...
        def isSmoothEnabled(self) -> bool: ...
        def setAxes(self, axes:typing.List) -> None: ...
        def setDeadZoneRadius(self, deadZoneRadius:float) -> None: ...
        def setSmoothEnabled(self, enabled:bool) -> None: ...

    class QButtonAxisInput(PySide2.Qt3DInput.QAbstractAxisInput):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def acceleration(self) -> float: ...
        def buttons(self) -> typing.List: ...
        def deceleration(self) -> float: ...
        def scale(self) -> float: ...
        def setAcceleration(self, acceleration:float) -> None: ...
        def setButtons(self, buttons:typing.List) -> None: ...
        def setDeceleration(self, deceleration:float) -> None: ...
        def setScale(self, scale:float) -> None: ...

    class QInputAspect(PySide2.Qt3DCore.QAbstractAspect):

        def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

        def availablePhysicalDevices(self) -> typing.List: ...
        def createPhysicalDevice(self, name:str) -> PySide2.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QInputChord(PySide2.Qt3DInput.QAbstractActionInput):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def addChord(self, input:PySide2.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def chords(self) -> typing.List: ...
        def removeChord(self, input:PySide2.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def setTimeout(self, timeout:int) -> None: ...
        def timeout(self) -> int: ...

    class QInputSequence(PySide2.Qt3DInput.QAbstractActionInput):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def addSequence(self, input:PySide2.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def buttonInterval(self) -> int: ...
        def removeSequence(self, input:PySide2.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def sequences(self) -> typing.List: ...
        def setButtonInterval(self, buttonInterval:int) -> None: ...
        def setTimeout(self, timeout:int) -> None: ...
        def timeout(self) -> int: ...

    class QInputSettings(PySide2.Qt3DCore.QComponent):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def eventSource(self) -> PySide2.QtCore.QObject: ...
        def setEventSource(self, eventSource:PySide2.QtCore.QObject) -> None: ...

    class QKeyEvent(PySide2.QtCore.QObject):

        def __init__(self, type:PySide2.QtCore.QEvent.Type, key:int, modifiers:PySide2.QtCore.Qt.KeyboardModifiers, text:str=..., autorep:bool=..., count:int=...) -> None: ...

        def count(self) -> int: ...
        def isAccepted(self) -> bool: ...
        def isAutoRepeat(self) -> bool: ...
        def key(self) -> int: ...
        def matches(self, key_:PySide2.QtGui.QKeySequence.StandardKey) -> bool: ...
        def modifiers(self) -> int: ...
        def nativeScanCode(self) -> int: ...
        def setAccepted(self, accepted:bool) -> None: ...
        def text(self) -> str: ...
        def type(self) -> PySide2.QtCore.QEvent.Type: ...

    class QKeyboardDevice(PySide2.Qt3DInput.QAbstractPhysicalDevice):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def activeInput(self) -> PySide2.Qt3DInput.Qt3DInput.QKeyboardHandler: ...
        def axisCount(self) -> int: ...
        def axisIdentifier(self, name:str) -> int: ...
        def axisNames(self) -> typing.List: ...
        def buttonCount(self) -> int: ...
        def buttonIdentifier(self, name:str) -> int: ...
        def buttonNames(self) -> typing.List: ...

    class QKeyboardHandler(PySide2.Qt3DCore.QComponent):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def focus(self) -> bool: ...
        def setFocus(self, focus:bool) -> None: ...
        def setSourceDevice(self, keyboardDevice:PySide2.Qt3DInput.Qt3DInput.QKeyboardDevice) -> None: ...
        def sourceDevice(self) -> PySide2.Qt3DInput.Qt3DInput.QKeyboardDevice: ...

    class QLogicalDevice(PySide2.Qt3DCore.QComponent):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def actions(self) -> typing.List: ...
        def addAction(self, action:PySide2.Qt3DInput.Qt3DInput.QAction) -> None: ...
        def addAxis(self, axis:PySide2.Qt3DInput.Qt3DInput.QAxis) -> None: ...
        def axes(self) -> typing.List: ...
        def removeAction(self, action:PySide2.Qt3DInput.Qt3DInput.QAction) -> None: ...
        def removeAxis(self, axis:PySide2.Qt3DInput.Qt3DInput.QAxis) -> None: ...

    class QMouseDevice(PySide2.Qt3DInput.QAbstractPhysicalDevice):
        X                        : Qt3DInput.QMouseDevice = ... # 0x0
        Y                        : Qt3DInput.QMouseDevice = ... # 0x1
        WheelX                   : Qt3DInput.QMouseDevice = ... # 0x2
        WheelY                   : Qt3DInput.QMouseDevice = ... # 0x3

        class Axis(object):
            X                        : Qt3DInput.QMouseDevice.Axis = ... # 0x0
            Y                        : Qt3DInput.QMouseDevice.Axis = ... # 0x1
            WheelX                   : Qt3DInput.QMouseDevice.Axis = ... # 0x2
            WheelY                   : Qt3DInput.QMouseDevice.Axis = ... # 0x3

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def axisCount(self) -> int: ...
        def axisIdentifier(self, name:str) -> int: ...
        def axisNames(self) -> typing.List: ...
        def buttonCount(self) -> int: ...
        def buttonIdentifier(self, name:str) -> int: ...
        def buttonNames(self) -> typing.List: ...
        def sensitivity(self) -> float: ...
        def setSensitivity(self, value:float) -> None: ...
        def setUpdateAxesContinuously(self, updateAxesContinuously:bool) -> None: ...
        def updateAxesContinuously(self) -> bool: ...

    class QMouseEvent(PySide2.QtCore.QObject):
        NoButton                 : Qt3DInput.QMouseEvent = ... # 0x0
        NoModifier               : Qt3DInput.QMouseEvent = ... # 0x0
        LeftButton               : Qt3DInput.QMouseEvent = ... # 0x1
        RightButton              : Qt3DInput.QMouseEvent = ... # 0x2
        MiddleButton             : Qt3DInput.QMouseEvent = ... # 0x4
        BackButton               : Qt3DInput.QMouseEvent = ... # 0x8
        ShiftModifier            : Qt3DInput.QMouseEvent = ... # 0x2000000
        ControlModifier          : Qt3DInput.QMouseEvent = ... # 0x4000000
        AltModifier              : Qt3DInput.QMouseEvent = ... # 0x8000000
        MetaModifier             : Qt3DInput.QMouseEvent = ... # 0x10000000
        KeypadModifier           : Qt3DInput.QMouseEvent = ... # 0x20000000

        class Buttons(object):
            NoButton                 : Qt3DInput.QMouseEvent.Buttons = ... # 0x0
            LeftButton               : Qt3DInput.QMouseEvent.Buttons = ... # 0x1
            RightButton              : Qt3DInput.QMouseEvent.Buttons = ... # 0x2
            MiddleButton             : Qt3DInput.QMouseEvent.Buttons = ... # 0x4
            BackButton               : Qt3DInput.QMouseEvent.Buttons = ... # 0x8

        class Modifiers(object):
            NoModifier               : Qt3DInput.QMouseEvent.Modifiers = ... # 0x0
            ShiftModifier            : Qt3DInput.QMouseEvent.Modifiers = ... # 0x2000000
            ControlModifier          : Qt3DInput.QMouseEvent.Modifiers = ... # 0x4000000
            AltModifier              : Qt3DInput.QMouseEvent.Modifiers = ... # 0x8000000
            MetaModifier             : Qt3DInput.QMouseEvent.Modifiers = ... # 0x10000000
            KeypadModifier           : Qt3DInput.QMouseEvent.Modifiers = ... # 0x20000000
        def button(self) -> PySide2.Qt3DInput.Qt3DInput.QMouseEvent.Buttons: ...
        def buttons(self) -> int: ...
        def isAccepted(self) -> bool: ...
        def modifiers(self) -> PySide2.Qt3DInput.Qt3DInput.QMouseEvent.Modifiers: ...
        def setAccepted(self, accepted:bool) -> None: ...
        def type(self) -> PySide2.QtCore.QEvent.Type: ...
        def wasHeld(self) -> bool: ...
        def x(self) -> int: ...
        def y(self) -> int: ...

    class QMouseHandler(PySide2.Qt3DCore.QComponent):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def containsMouse(self) -> bool: ...
        def setContainsMouse(self, contains:bool) -> None: ...
        def setSourceDevice(self, mouseDevice:PySide2.Qt3DInput.Qt3DInput.QMouseDevice) -> None: ...
        def sourceDevice(self) -> PySide2.Qt3DInput.Qt3DInput.QMouseDevice: ...

    class QWheelEvent(PySide2.QtCore.QObject):
        NoButton                 : Qt3DInput.QWheelEvent = ... # 0x0
        NoModifier               : Qt3DInput.QWheelEvent = ... # 0x0
        LeftButton               : Qt3DInput.QWheelEvent = ... # 0x1
        RightButton              : Qt3DInput.QWheelEvent = ... # 0x2
        MiddleButton             : Qt3DInput.QWheelEvent = ... # 0x4
        BackButton               : Qt3DInput.QWheelEvent = ... # 0x8
        ShiftModifier            : Qt3DInput.QWheelEvent = ... # 0x2000000
        ControlModifier          : Qt3DInput.QWheelEvent = ... # 0x4000000
        AltModifier              : Qt3DInput.QWheelEvent = ... # 0x8000000
        MetaModifier             : Qt3DInput.QWheelEvent = ... # 0x10000000
        KeypadModifier           : Qt3DInput.QWheelEvent = ... # 0x20000000

        class Buttons(object):
            NoButton                 : Qt3DInput.QWheelEvent.Buttons = ... # 0x0
            LeftButton               : Qt3DInput.QWheelEvent.Buttons = ... # 0x1
            RightButton              : Qt3DInput.QWheelEvent.Buttons = ... # 0x2
            MiddleButton             : Qt3DInput.QWheelEvent.Buttons = ... # 0x4
            BackButton               : Qt3DInput.QWheelEvent.Buttons = ... # 0x8

        class Modifiers(object):
            NoModifier               : Qt3DInput.QWheelEvent.Modifiers = ... # 0x0
            ShiftModifier            : Qt3DInput.QWheelEvent.Modifiers = ... # 0x2000000
            ControlModifier          : Qt3DInput.QWheelEvent.Modifiers = ... # 0x4000000
            AltModifier              : Qt3DInput.QWheelEvent.Modifiers = ... # 0x8000000
            MetaModifier             : Qt3DInput.QWheelEvent.Modifiers = ... # 0x10000000
            KeypadModifier           : Qt3DInput.QWheelEvent.Modifiers = ... # 0x20000000
        def angleDelta(self) -> PySide2.QtCore.QPoint: ...
        def buttons(self) -> int: ...
        def isAccepted(self) -> bool: ...
        def modifiers(self) -> PySide2.Qt3DInput.Qt3DInput.QWheelEvent.Modifiers: ...
        def setAccepted(self, accepted:bool) -> None: ...
        def type(self) -> PySide2.QtCore.QEvent.Type: ...
        def x(self) -> int: ...
        def y(self) -> int: ...

# eof