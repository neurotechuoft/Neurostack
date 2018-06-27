from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self):
        pass

    @abstractmethod
    @staticmethod
    def available_devices(self) -> []:
        """
        Return a list of devices available to connect to on particular computer.

        :return:
        """
        pass

    @abstractmethod
    def connect(self, device_id=None) -> None:
        """
        Connect to EEG device with id specified. If id is not specified,
        connect to randomly selected EEG device.

        :param device_id:
        :return:
        """
        pass

    @abstractmethod
    def start(self) -> None:
        """
        Start streaming EEG from device, and publish data to subscribers.

        :return:
        """
        pass

    @abstractmethod
    def stop(self) -> None:
        """
        Stop streaming EEG data from device, and stop publishing data to
        subscribers. Connection to device remains intact, and device is not
        turned off.

        :return:
        """
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """
        Close connection to device, WebSocket connections to publishers, and tag
        sources.

        :return:
        """
        pass