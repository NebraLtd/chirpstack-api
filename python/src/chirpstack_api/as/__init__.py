# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: chirpstack-api/as_pb/as_pb.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from .. import (
    common as _common__,
    gw as _gw__,
)


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class RxWindow(betterproto.Enum):
    RX1 = 0
    RX2 = 1


class ErrorType(betterproto.Enum):
    GENERIC = 0
    """Generic error type."""

    OTAA = 1
    """OTAA error."""

    DATA_UP_FCNT_RESET = 2
    """Uplink frame-counter was reset."""

    DATA_UP_MIC = 3
    """Uplink MIC error."""

    DEVICE_QUEUE_ITEM_SIZE = 4
    """Downlink payload size error."""

    DEVICE_QUEUE_ITEM_FCNT = 5
    """Downlink frame-counter error."""

    DATA_UP_FCNT_RETRANSMISSION = 6
    """Uplink frame-counter retransmission."""

    DATA_DOWN_GATEWAY = 7
    """Downlink gateway error."""


@dataclass(eq=False, repr=False)
class DeviceActivationContext(betterproto.Message):
    dev_addr: bytes = betterproto.bytes_field(1)
    """Assigned Device Address."""

    app_s_key: "_common__.KeyEnvelope" = betterproto.message_field(2)
    """Application session key (envelope)."""


@dataclass(eq=False, repr=False)
class HandleUplinkDataRequest(betterproto.Message):
    dev_eui: bytes = betterproto.bytes_field(1)
    """DevEUI EUI (8 bytes)."""

    join_eui: bytes = betterproto.bytes_field(2)
    """Join EUI used for OTAA activation (8 bytes)."""

    f_cnt: int = betterproto.uint32_field(3)
    """Frame-counter."""

    f_port: int = betterproto.uint32_field(4)
    """Frame port."""

    adr: bool = betterproto.bool_field(5)
    """ADR enabled."""

    dr: int = betterproto.uint32_field(6)
    """Data-rate."""

    tx_info: "_gw__.UplinkTxInfo" = betterproto.message_field(7)
    """TX meta-data."""

    rx_info: List["_gw__.UplinkRxInfo"] = betterproto.message_field(8)
    """RX meta-data."""

    data: bytes = betterproto.bytes_field(9)
    """Received data (encrypted)."""

    device_activation_context: "DeviceActivationContext" = betterproto.message_field(10)
    """
    Device activation context. This field is only set on the first uplink frame
    when the security context has changed (e.g. a new OTAA (re)activation).
    """

    confirmed_uplink: bool = betterproto.bool_field(11)
    """Uplink was of type confirmed."""


@dataclass(eq=False, repr=False)
class HandleProprietaryUplinkRequest(betterproto.Message):
    mac_payload: bytes = betterproto.bytes_field(1)
    """MACPayload of the proprietary LoRaWAN frame."""

    mic: bytes = betterproto.bytes_field(2)
    """MIC of the proprietary LoRaWAN frame."""

    tx_info: "_gw__.UplinkTxInfo" = betterproto.message_field(3)
    """TXInfo contains the TX related meta-data."""

    rx_info: List["_gw__.UplinkRxInfo"] = betterproto.message_field(4)
    """RXInfo contains the RX related meta-data."""


@dataclass(eq=False, repr=False)
class HandleErrorRequest(betterproto.Message):
    dev_eui: bytes = betterproto.bytes_field(1)
    """Device EUI (8 bytes)."""

    type: "ErrorType" = betterproto.enum_field(3)
    """Type of the error."""

    error: str = betterproto.string_field(4)
    """Error string describing the error."""

    f_cnt: int = betterproto.uint32_field(5)
    """Frame-counter (if applicable) related to the error."""


@dataclass(eq=False, repr=False)
class HandleDownlinkAckRequest(betterproto.Message):
    dev_eui: bytes = betterproto.bytes_field(1)
    """Device EUI (8 bytes)."""

    f_cnt: int = betterproto.uint32_field(2)
    """Downlink frame-counter."""

    acknowledged: bool = betterproto.bool_field(3)
    """Frame was acknowledged?"""


@dataclass(eq=False, repr=False)
class SetDeviceStatusRequest(betterproto.Message):
    dev_eui: bytes = betterproto.bytes_field(1)
    """Device EUI (8 bytes)."""

    battery: int = betterproto.uint32_field(2)
    """
    Battery level (deprecated, use battery_level). 0:      The end-device is
    connected to an external power source 1..254: The battery level, 1 being at
    minimum and 254 being at maximum 255:    The end-device was not able to
    measure the battery level
    """

    margin: int = betterproto.int32_field(3)
    """The device margin status -32..32: The demodulation SNR ration in dB"""

    external_power_source: bool = betterproto.bool_field(4)
    """Device is connected to an external power source."""

    battery_level_unavailable: bool = betterproto.bool_field(5)
    """Device battery status is not available."""

    battery_level: float = betterproto.float_field(6)
    """Battery level as a percentage."""


@dataclass(eq=False, repr=False)
class SetDeviceLocationRequest(betterproto.Message):
    dev_eui: bytes = betterproto.bytes_field(1)
    """Device EUI (8 bytes)."""

    location: "_common__.Location" = betterproto.message_field(2)
    """The location of the device."""

    uplink_ids: List[bytes] = betterproto.bytes_field(3)
    """Uplink IDs used for geolocation."""


@dataclass(eq=False, repr=False)
class HandleGatewayStatsRequest(betterproto.Message):
    gateway_id: bytes = betterproto.bytes_field(1)
    """Gateway ID (8 bytes)."""

    stats_id: bytes = betterproto.bytes_field(2)
    """Stats ID (UUID)."""

    time: datetime = betterproto.message_field(3)
    """Timestamp."""

    location: "_common__.Location" = betterproto.message_field(4)
    """Gateway location."""

    rx_packets_received: int = betterproto.uint32_field(5)
    """Uplink frames received."""

    rx_packets_received_ok: int = betterproto.uint32_field(6)
    """Uplink frames received OK."""

    tx_packets_received: int = betterproto.uint32_field(7)
    """Downlink transmissions requested."""

    tx_packets_emitted: int = betterproto.uint32_field(8)
    """Downlink emitted."""

    metadata: Dict[str, str] = betterproto.map_field(
        9, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    """Gateway metadata."""

    tx_packets_per_frequency: Dict[int, int] = betterproto.map_field(
        10, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    """Tx packets per frequency."""

    rx_packets_per_frequency: Dict[int, int] = betterproto.map_field(
        11, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    """Rx packets per frequency."""

    tx_packets_per_dr: Dict[int, int] = betterproto.map_field(
        12, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    """Tx packets per DR."""

    rx_packets_per_dr: Dict[int, int] = betterproto.map_field(
        13, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    """Rx packets per DR."""

    tx_packets_per_status: Dict[str, int] = betterproto.map_field(
        14, betterproto.TYPE_STRING, betterproto.TYPE_UINT32
    )
    """Tx packets per status."""


@dataclass(eq=False, repr=False)
class HandleTxAckRequest(betterproto.Message):
    dev_eui: bytes = betterproto.bytes_field(1)
    """Device EUI (8 bytes)."""

    f_cnt: int = betterproto.uint32_field(2)
    """Downlink frame-counter."""

    gateway_id: bytes = betterproto.bytes_field(3)
    """Gateway ID."""

    tx_info: "_gw__.DownlinkTxInfo" = betterproto.message_field(4)
    """TXInfo contains the TX related meta-data."""


@dataclass(eq=False, repr=False)
class ReEncryptDeviceQueueItemsRequest(betterproto.Message):
    dev_eui: bytes = betterproto.bytes_field(1)
    """DevEUI of the device."""

    dev_addr: bytes = betterproto.bytes_field(2)
    """
    Device addres. This is the device address which was used to encrypt the
    given payloads.
    """

    f_cnt_start: int = betterproto.uint32_field(3)
    """
    Downlink frame-counter to start with. The application-server must use this
    value when encrypting the first item, and increment it for each successive
    item.
    """

    items: List["ReEncryptDeviceQueueItem"] = betterproto.message_field(4)
    """Items to re-encrypt."""


@dataclass(eq=False, repr=False)
class ReEncryptDeviceQueueItemsResponse(betterproto.Message):
    items: List["ReEncryptedDeviceQueueItem"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ReEncryptDeviceQueueItem(betterproto.Message):
    frm_payload: bytes = betterproto.bytes_field(1)
    """The encrypted FRMPayload bytes."""

    f_cnt: int = betterproto.uint32_field(2)
    """The original FCnt of the payload."""

    f_port: int = betterproto.uint32_field(3)
    """The FPort of the payload."""

    confirmed: bool = betterproto.bool_field(4)
    """Payload is of type confirmed."""


@dataclass(eq=False, repr=False)
class ReEncryptedDeviceQueueItem(betterproto.Message):
    frm_payload: bytes = betterproto.bytes_field(1)
    """The re-encrypted FRMPayload bytes."""

    f_cnt: int = betterproto.uint32_field(2)
    """The new FCnt of the payload."""

    f_port: int = betterproto.uint32_field(3)
    """The FPort of the payload."""

    confirmed: bool = betterproto.bool_field(4)
    """Payload is of type confirmed."""


class ApplicationServerServiceStub(betterproto.ServiceStub):
    async def handle_uplink_data(
        self,
        handle_uplink_data_request: "HandleUplinkDataRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "betterproto_lib_google_protobuf.Empty":
        return await self._unary_unary(
            "/as.ApplicationServerService/HandleUplinkData",
            handle_uplink_data_request,
            betterproto_lib_google_protobuf.Empty,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def handle_proprietary_uplink(
        self,
        handle_proprietary_uplink_request: "HandleProprietaryUplinkRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "betterproto_lib_google_protobuf.Empty":
        return await self._unary_unary(
            "/as.ApplicationServerService/HandleProprietaryUplink",
            handle_proprietary_uplink_request,
            betterproto_lib_google_protobuf.Empty,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def handle_error(
        self,
        handle_error_request: "HandleErrorRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "betterproto_lib_google_protobuf.Empty":
        return await self._unary_unary(
            "/as.ApplicationServerService/HandleError",
            handle_error_request,
            betterproto_lib_google_protobuf.Empty,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def handle_downlink_ack(
        self,
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "betterproto_lib_google_protobuf.Empty":
        return await self._unary_unary(
            "/as.ApplicationServerService/HandleDownlinkACK",
            handle_downlink_ack_request,
            betterproto_lib_google_protobuf.Empty,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def handle_gateway_stats(
        self,
        handle_gateway_stats_request: "HandleGatewayStatsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "betterproto_lib_google_protobuf.Empty":
        return await self._unary_unary(
            "/as.ApplicationServerService/HandleGatewayStats",
            handle_gateway_stats_request,
            betterproto_lib_google_protobuf.Empty,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def handle_tx_ack(
        self,
        handle_tx_ack_request: "HandleTxAckRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "betterproto_lib_google_protobuf.Empty":
        return await self._unary_unary(
            "/as.ApplicationServerService/HandleTxAck",
            handle_tx_ack_request,
            betterproto_lib_google_protobuf.Empty,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def set_device_status(
        self,
        set_device_status_request: "SetDeviceStatusRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "betterproto_lib_google_protobuf.Empty":
        return await self._unary_unary(
            "/as.ApplicationServerService/SetDeviceStatus",
            set_device_status_request,
            betterproto_lib_google_protobuf.Empty,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def set_device_location(
        self,
        set_device_location_request: "SetDeviceLocationRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "betterproto_lib_google_protobuf.Empty":
        return await self._unary_unary(
            "/as.ApplicationServerService/SetDeviceLocation",
            set_device_location_request,
            betterproto_lib_google_protobuf.Empty,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def re_encrypt_device_queue_items(
        self,
        re_encrypt_device_queue_items_request: "ReEncryptDeviceQueueItemsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ReEncryptDeviceQueueItemsResponse":
        return await self._unary_unary(
            "/as.ApplicationServerService/ReEncryptDeviceQueueItems",
            re_encrypt_device_queue_items_request,
            ReEncryptDeviceQueueItemsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class ApplicationServerServiceBase(ServiceBase):
    async def handle_uplink_data(
        self, handle_uplink_data_request: "HandleUplinkDataRequest"
    ) -> "betterproto_lib_google_protobuf.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def handle_proprietary_uplink(
        self, handle_proprietary_uplink_request: "HandleProprietaryUplinkRequest"
    ) -> "betterproto_lib_google_protobuf.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def handle_error(
        self, handle_error_request: "HandleErrorRequest"
    ) -> "betterproto_lib_google_protobuf.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def handle_downlink_ack(self) -> "betterproto_lib_google_protobuf.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def handle_gateway_stats(
        self, handle_gateway_stats_request: "HandleGatewayStatsRequest"
    ) -> "betterproto_lib_google_protobuf.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def handle_tx_ack(
        self, handle_tx_ack_request: "HandleTxAckRequest"
    ) -> "betterproto_lib_google_protobuf.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set_device_status(
        self, set_device_status_request: "SetDeviceStatusRequest"
    ) -> "betterproto_lib_google_protobuf.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def set_device_location(
        self, set_device_location_request: "SetDeviceLocationRequest"
    ) -> "betterproto_lib_google_protobuf.Empty":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def re_encrypt_device_queue_items(
        self, re_encrypt_device_queue_items_request: "ReEncryptDeviceQueueItemsRequest"
    ) -> "ReEncryptDeviceQueueItemsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_handle_uplink_data(
        self,
        stream: "grpclib.server.Stream[HandleUplinkDataRequest, betterproto_lib_google_protobuf.Empty]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.handle_uplink_data(request)
        await stream.send_message(response)

    async def __rpc_handle_proprietary_uplink(
        self,
        stream: "grpclib.server.Stream[HandleProprietaryUplinkRequest, betterproto_lib_google_protobuf.Empty]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.handle_proprietary_uplink(request)
        await stream.send_message(response)

    async def __rpc_handle_error(
        self,
        stream: "grpclib.server.Stream[HandleErrorRequest, betterproto_lib_google_protobuf.Empty]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.handle_error(request)
        await stream.send_message(response)

    async def __rpc_handle_downlink_ack(
        self,
        stream: "grpclib.server.Stream[HandleDownlinkAckRequest, betterproto_lib_google_protobuf.Empty]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.handle_downlink_ack(request)
        await stream.send_message(response)

    async def __rpc_handle_gateway_stats(
        self,
        stream: "grpclib.server.Stream[HandleGatewayStatsRequest, betterproto_lib_google_protobuf.Empty]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.handle_gateway_stats(request)
        await stream.send_message(response)

    async def __rpc_handle_tx_ack(
        self,
        stream: "grpclib.server.Stream[HandleTxAckRequest, betterproto_lib_google_protobuf.Empty]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.handle_tx_ack(request)
        await stream.send_message(response)

    async def __rpc_set_device_status(
        self,
        stream: "grpclib.server.Stream[SetDeviceStatusRequest, betterproto_lib_google_protobuf.Empty]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.set_device_status(request)
        await stream.send_message(response)

    async def __rpc_set_device_location(
        self,
        stream: "grpclib.server.Stream[SetDeviceLocationRequest, betterproto_lib_google_protobuf.Empty]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.set_device_location(request)
        await stream.send_message(response)

    async def __rpc_re_encrypt_device_queue_items(
        self,
        stream: "grpclib.server.Stream[ReEncryptDeviceQueueItemsRequest, ReEncryptDeviceQueueItemsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.re_encrypt_device_queue_items(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/as.ApplicationServerService/HandleUplinkData": grpclib.const.Handler(
                self.__rpc_handle_uplink_data,
                grpclib.const.Cardinality.UNARY_UNARY,
                HandleUplinkDataRequest,
                betterproto_lib_google_protobuf.Empty,
            ),
            "/as.ApplicationServerService/HandleProprietaryUplink": grpclib.const.Handler(
                self.__rpc_handle_proprietary_uplink,
                grpclib.const.Cardinality.UNARY_UNARY,
                HandleProprietaryUplinkRequest,
                betterproto_lib_google_protobuf.Empty,
            ),
            "/as.ApplicationServerService/HandleError": grpclib.const.Handler(
                self.__rpc_handle_error,
                grpclib.const.Cardinality.UNARY_UNARY,
                HandleErrorRequest,
                betterproto_lib_google_protobuf.Empty,
            ),
            "/as.ApplicationServerService/HandleDownlinkACK": grpclib.const.Handler(
                self.__rpc_handle_downlink_ack,
                grpclib.const.Cardinality.UNARY_UNARY,
                HandleDownlinkAckRequest,
                betterproto_lib_google_protobuf.Empty,
            ),
            "/as.ApplicationServerService/HandleGatewayStats": grpclib.const.Handler(
                self.__rpc_handle_gateway_stats,
                grpclib.const.Cardinality.UNARY_UNARY,
                HandleGatewayStatsRequest,
                betterproto_lib_google_protobuf.Empty,
            ),
            "/as.ApplicationServerService/HandleTxAck": grpclib.const.Handler(
                self.__rpc_handle_tx_ack,
                grpclib.const.Cardinality.UNARY_UNARY,
                HandleTxAckRequest,
                betterproto_lib_google_protobuf.Empty,
            ),
            "/as.ApplicationServerService/SetDeviceStatus": grpclib.const.Handler(
                self.__rpc_set_device_status,
                grpclib.const.Cardinality.UNARY_UNARY,
                SetDeviceStatusRequest,
                betterproto_lib_google_protobuf.Empty,
            ),
            "/as.ApplicationServerService/SetDeviceLocation": grpclib.const.Handler(
                self.__rpc_set_device_location,
                grpclib.const.Cardinality.UNARY_UNARY,
                SetDeviceLocationRequest,
                betterproto_lib_google_protobuf.Empty,
            ),
            "/as.ApplicationServerService/ReEncryptDeviceQueueItems": grpclib.const.Handler(
                self.__rpc_re_encrypt_device_queue_items,
                grpclib.const.Cardinality.UNARY_UNARY,
                ReEncryptDeviceQueueItemsRequest,
                ReEncryptDeviceQueueItemsResponse,
            ),
        }
