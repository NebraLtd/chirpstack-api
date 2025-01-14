# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: chirpstack-api/common/common.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class Modulation(betterproto.Enum):
    LORA = 0
    """LoRa"""

    FSK = 1
    """FSK"""

    LR_FHSS = 2
    """LR-FHSS"""


class Region(betterproto.Enum):
    EU868 = 0
    """EU868"""

    US915 = 2
    """US915"""

    CN779 = 3
    """CN779"""

    EU433 = 4
    """EU433"""

    AU915 = 5
    """AU915"""

    CN470 = 6
    """CN470"""

    AS923 = 7
    """AS923"""

    AS923_2 = 12
    """AS923 with -1.80 MHz frequency offset"""

    AS923_3 = 13
    """AS923 with -6.60 MHz frequency offset"""

    AS923_4 = 14
    """AS923 with -5.90 MHz frequency offset"""

    KR920 = 8
    """KR920"""

    IN865 = 9
    """IN865"""

    RU864 = 10
    """RU864"""

    ISM2400 = 11
    """ISM2400 (LoRaWAN 2.4 GHz)"""


class MType(betterproto.Enum):
    JoinRequest = 0
    """JoinRequest."""

    JoinAccept = 1
    """JoinAccept."""

    UnconfirmedDataUp = 2
    """UnconfirmedDataUp."""

    UnconfirmedDataDown = 3
    """UnconfirmedDataDown."""

    ConfirmedDataUp = 4
    """ConfirmedDataUp."""

    ConfirmedDataDown = 5
    """ConfirmedDataDown."""

    RejoinRequest = 6
    """RejoinRequest."""

    Proprietary = 7
    """Proprietary."""


class LocationSource(betterproto.Enum):
    UNKNOWN = 0
    """Unknown."""

    GPS = 1
    """GPS."""

    CONFIG = 2
    """Manually configured."""

    GEO_RESOLVER_TDOA = 3
    """Geo resolver (TDOA)."""

    GEO_RESOLVER_RSSI = 4
    """Geo resolver (RSSI)."""

    GEO_RESOLVER_GNSS = 5
    """Geo resolver (GNSS)."""

    GEO_RESOLVER_WIFI = 6
    """Geo resolver (WIFI)."""


@dataclass(eq=False, repr=False)
class KeyEnvelope(betterproto.Message):
    kek_label: str = betterproto.string_field(1)
    """KEK label."""

    aes_key: bytes = betterproto.bytes_field(2)
    """
    AES key (when the kek_label is set, this key is encrypted using a key known
    to the join-server and application-server. For more information please
    refer to the LoRaWAN Backend Interface 'Key Transport Security' section.
    """


@dataclass(eq=False, repr=False)
class Location(betterproto.Message):
    latitude: float = betterproto.double_field(1)
    """Latitude."""

    longitude: float = betterproto.double_field(2)
    """Longitude."""

    altitude: float = betterproto.double_field(3)
    """Altitude."""

    source: "LocationSource" = betterproto.enum_field(4)
    """Location source."""

    accuracy: int = betterproto.uint32_field(5)
    """Accuracy (in meters)."""
