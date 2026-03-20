"""Created on 20260311_1130"""
from enum import Enum, unique
from myersbriggs.utils.myersbriggs_util import MyersBriggsUtil

@unique
class MyersBriggsPersonalityEnum(Enum):
    """
    The creation of the 16 MBTI values.
    The values were not represented as numbers to avoid simple modifications.
    The values are the results of the sha-1 hash function.
    """
    ISTJ    = '4881eb260e494c40a60d03a2b014cb3a80bd8029'
    ISFJ    = '15150db117f08c44d91080ccebc46de92c8f5edf'
    INFJ    = '585cffcfe7f5e836b19101081108087a37253d86'
    INTJ    = 'ab6399944b8db06e478edf978e05cdd0b9c3463e'
    ISTP    = '7b69d7ee5e015e588d446c1cc603a32bd5888b5a'
    ISFP    = '8157e8216666352b7da1ebeb0cc3719edd0b6200'
    INFP    = 'a44b466401f563f38af73f525addb830b50809ec'
    INTP    = '452c61c906d6f674e4e91a6226435c504851ea33'
    ESTP    = '94f65569ae29ca12ecac4d235659b23b72435c89'
    ESFP    = '4b63860361d6caf8ac2d1b3f2dde1fccb750098a'
    ENFP    = '0f4dbcf37d9a1736c426fb9112dbb4cb9e81094a'
    ENTP    = '2e0f58e75ba06c0db7986bf4647e190c2f704308'
    ESTJ    = 'a23a4ac3f1e7a950bf07d6332c0659c2a72af492'
    ESFJ    = '0c0cedf7f2227c7f553a37ef40dfe9b3866309b8'
    ENFJ    = '54f48f60440d09298d09f1b8866886d17b1b26b7'
    ENTJ    = '20d5a7272744e8e59a15c508e53aa6e77c4df7a7'