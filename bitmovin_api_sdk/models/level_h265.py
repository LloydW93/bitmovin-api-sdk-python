# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class LevelH265(Enum):
    L1 = "1"
    L2 = "2"
    L2_1 = "2.1"
    L3 = "3"
    L3_1 = "3.1"
    L4 = "4"
    L4_1 = "4.1"
    L5 = "5"
    L5_1 = "5.1"
    L5_2 = "5.2"
    L6 = "6"
    L6_1 = "6.1"
    L6_2 = "6.2"
