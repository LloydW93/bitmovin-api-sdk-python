# coding: utf-8

from bitmovin.models.audio_configuration import AudioConfiguration
from bitmovin.models.channel_layout import ChannelLayout
import pprint
import six
from datetime import datetime
from enum import Enum


class Mp3AudioConfiguration(AudioConfiguration):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Mp3AudioConfiguration, self).openapi_types
        types.update({
            'channel_layout': 'ChannelLayout'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Mp3AudioConfiguration, self).attribute_map
        attributes.update({
            'channel_layout': 'channelLayout'
        })
        return attributes

    def __init__(self, channel_layout=None, *args, **kwargs):
        super(Mp3AudioConfiguration, self).__init__(*args, **kwargs)

        self._channel_layout = None
        self.discriminator = None

        if channel_layout is not None:
            self.channel_layout = channel_layout

    @property
    def channel_layout(self):
        """Gets the channel_layout of this Mp3AudioConfiguration.

        Channel layout of the audio codec configuration

        :return: The channel_layout of this Mp3AudioConfiguration.
        :rtype: ChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        """Sets the channel_layout of this Mp3AudioConfiguration.

        Channel layout of the audio codec configuration

        :param channel_layout: The channel_layout of this Mp3AudioConfiguration.
        :type: ChannelLayout
        """

        if channel_layout is not None:
            if not isinstance(channel_layout, ChannelLayout):
                raise TypeError("Invalid type for `channel_layout`, type has to be `ChannelLayout`")

            self._channel_layout = channel_layout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Mp3AudioConfiguration, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(Mp3AudioConfiguration, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Mp3AudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
