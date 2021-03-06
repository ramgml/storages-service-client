# coding: utf-8

"""
    Genezis Storages

    Сервис файловых хранилищ  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StorageRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'storage_type': 'str',
        'additional': 'object'
    }

    attribute_map = {
        'storage_type': 'storage_type',
        'additional': 'additional'
    }

    def __init__(self, storage_type=None, additional=None):  # noqa: E501
        """StorageRequest - a model defined in Swagger"""  # noqa: E501
        self._storage_type = None
        self._additional = None
        self.discriminator = None
        if storage_type is not None:
            self.storage_type = storage_type
        if additional is not None:
            self.additional = additional

    @property
    def storage_type(self):
        """Gets the storage_type of this StorageRequest.  # noqa: E501

        Тип хранилища  # noqa: E501

        :return: The storage_type of this StorageRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this StorageRequest.

        Тип хранилища  # noqa: E501

        :param storage_type: The storage_type of this StorageRequest.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

    @property
    def additional(self):
        """Gets the additional of this StorageRequest.  # noqa: E501


        :return: The additional of this StorageRequest.  # noqa: E501
        :rtype: object
        """
        return self._additional

    @additional.setter
    def additional(self, additional):
        """Sets the additional of this StorageRequest.


        :param additional: The additional of this StorageRequest.  # noqa: E501
        :type: object
        """

        self._additional = additional

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StorageRequest, dict):
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
        if not isinstance(other, StorageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
