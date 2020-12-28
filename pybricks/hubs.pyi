# SPDX-License-Identifier: MIT
# Copyright (c) 2020 The Pybricks Authors

from ._common import Speaker, Battery, ColorLight, LightMatrix, Keypad
from .media.ev3dev import Image

class EV3Brick:
    screen: Image
    speaker: Speaker
    battery: Battery
    light: ColorLight
    buttons = Keypad

class MoveHub:
    battery: Battery
    light: ColorLight


class CityHub:
    battery: Battery
    light: ColorLight


class TechnicHub:
    battery: Battery
    light: ColorLight


class PrimeHub:
    battery: Battery
    light: ColorLight
    display: LightMatrix
    buttons: Keypad
    speaker: Speaker


class InventorHub(PrimeHub): ...
 