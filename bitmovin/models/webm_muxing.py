# coding: utf-8

from bitmovin.models.encoding_output import EncodingOutput
from bitmovin.models.ignoring import Ignoring
from bitmovin.models.muxing import Muxing
from bitmovin.models.muxing_stream import MuxingStream
from bitmovin.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six
from datetime import datetime
from enum import Enum


class WebmMuxing(Muxing):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(WebmMuxing, self).openapi_types
        types.update({
            'segment_length': 'float',
            'segment_naming': 'str',
            'segment_naming_template': 'str',
            'init_segment_name': 'str',
            'init_segment_name_template': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(WebmMuxing, self).attribute_map
        attributes.update({
            'segment_length': 'segmentLength',
            'segment_naming': 'segmentNaming',
            'segment_naming_template': 'segmentNamingTemplate',
            'init_segment_name': 'initSegmentName',
            'init_segment_name_template': 'initSegmentNameTemplate'
        })
        return attributes

    def __init__(self, segment_length=None, segment_naming=None, segment_naming_template=None, init_segment_name=None, init_segment_name_template=None, *args, **kwargs):
        super(WebmMuxing, self).__init__(*args, **kwargs)

        self._segment_length = None
        self._segment_naming = None
        self._segment_naming_template = None
        self._init_segment_name = None
        self._init_segment_name_template = None
        self.discriminator = None

        self.segment_length = segment_length
        if segment_naming is not None:
            self.segment_naming = segment_naming
        if segment_naming_template is not None:
            self.segment_naming_template = segment_naming_template
        if init_segment_name is not None:
            self.init_segment_name = init_segment_name
        if init_segment_name_template is not None:
            self.init_segment_name_template = init_segment_name_template

    @property
    def segment_length(self):
        """Gets the segment_length of this WebmMuxing.

        Length of the fragments in seconds

        :return: The segment_length of this WebmMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        """Sets the segment_length of this WebmMuxing.

        Length of the fragments in seconds

        :param segment_length: The segment_length of this WebmMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, float):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

            self._segment_length = segment_length


    @property
    def segment_naming(self):
        """Gets the segment_naming of this WebmMuxing.

        Segment naming policy

        :return: The segment_naming of this WebmMuxing.
        :rtype: str
        """
        return self._segment_naming

    @segment_naming.setter
    def segment_naming(self, segment_naming):
        """Sets the segment_naming of this WebmMuxing.

        Segment naming policy

        :param segment_naming: The segment_naming of this WebmMuxing.
        :type: str
        """

        if segment_naming is not None:
            if not isinstance(segment_naming, str):
                raise TypeError("Invalid type for `segment_naming`, type has to be `str`")

            self._segment_naming = segment_naming


    @property
    def segment_naming_template(self):
        """Gets the segment_naming_template of this WebmMuxing.

        Segment naming policy with placeholders which will be replaced during the encoding. The result will be saved in segmentNaming. {rand:4} gets replaced with an alphanumeric string of length specified after the colon. Defaults to 32. If this field is set, segmentNaming must not be specified.

        :return: The segment_naming_template of this WebmMuxing.
        :rtype: str
        """
        return self._segment_naming_template

    @segment_naming_template.setter
    def segment_naming_template(self, segment_naming_template):
        """Sets the segment_naming_template of this WebmMuxing.

        Segment naming policy with placeholders which will be replaced during the encoding. The result will be saved in segmentNaming. {rand:4} gets replaced with an alphanumeric string of length specified after the colon. Defaults to 32. If this field is set, segmentNaming must not be specified.

        :param segment_naming_template: The segment_naming_template of this WebmMuxing.
        :type: str
        """

        if segment_naming_template is not None:
            if not isinstance(segment_naming_template, str):
                raise TypeError("Invalid type for `segment_naming_template`, type has to be `str`")

            self._segment_naming_template = segment_naming_template


    @property
    def init_segment_name(self):
        """Gets the init_segment_name of this WebmMuxing.

        Init segment name

        :return: The init_segment_name of this WebmMuxing.
        :rtype: str
        """
        return self._init_segment_name

    @init_segment_name.setter
    def init_segment_name(self, init_segment_name):
        """Sets the init_segment_name of this WebmMuxing.

        Init segment name

        :param init_segment_name: The init_segment_name of this WebmMuxing.
        :type: str
        """

        if init_segment_name is not None:
            if not isinstance(init_segment_name, str):
                raise TypeError("Invalid type for `init_segment_name`, type has to be `str`")

            self._init_segment_name = init_segment_name


    @property
    def init_segment_name_template(self):
        """Gets the init_segment_name_template of this WebmMuxing.

        Segment naming policy with placeholders which will be replaced during the encoding, similar to segmentNamingTemplate. The result will be saved in initSegmentName. If this field is set, initSegmentName must not be specified and segmentNamingTemplate should be set. 

        :return: The init_segment_name_template of this WebmMuxing.
        :rtype: str
        """
        return self._init_segment_name_template

    @init_segment_name_template.setter
    def init_segment_name_template(self, init_segment_name_template):
        """Sets the init_segment_name_template of this WebmMuxing.

        Segment naming policy with placeholders which will be replaced during the encoding, similar to segmentNamingTemplate. The result will be saved in initSegmentName. If this field is set, initSegmentName must not be specified and segmentNamingTemplate should be set. 

        :param init_segment_name_template: The init_segment_name_template of this WebmMuxing.
        :type: str
        """

        if init_segment_name_template is not None:
            if not isinstance(init_segment_name_template, str):
                raise TypeError("Invalid type for `init_segment_name_template`, type has to be `str`")

            self._init_segment_name_template = init_segment_name_template

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(WebmMuxing, self).to_dict()

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
            if issubclass(WebmMuxing, dict):
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
        if not isinstance(other, WebmMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other