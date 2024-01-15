# coding: utf-8

"""
    Speech Services API v3.1

    Speech Services API v3.1.  # noqa: E501

    OpenAPI spec version: v3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class CustomModelLinks(object):
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
        'copy_to': 'str',
        'files': 'str',
        'manifest': 'str'
    }

    attribute_map = {
        'copy_to': 'copyTo',
        'files': 'files',
        'manifest': 'manifest'
    }

    def __init__(self, copy_to=None, files=None, manifest=None, _configuration=None):  # noqa: E501
        """CustomModelLinks - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._copy_to = None
        self._files = None
        self._manifest = None
        self.discriminator = None

        if copy_to is not None:
            self.copy_to = copy_to
        if files is not None:
            self.files = files
        if manifest is not None:
            self.manifest = manifest

    @property
    def copy_to(self):
        """Gets the copy_to of this CustomModelLinks.  # noqa: E501

        The location to the model copy action. See operation \"Models_CopyTo\" for more details.  # noqa: E501

        :return: The copy_to of this CustomModelLinks.  # noqa: E501
        :rtype: str
        """
        return self._copy_to

    @copy_to.setter
    def copy_to(self, copy_to):
        """Sets the copy_to of this CustomModelLinks.

        The location to the model copy action. See operation \"Models_CopyTo\" for more details.  # noqa: E501

        :param copy_to: The copy_to of this CustomModelLinks.  # noqa: E501
        :type: str
        """

        self._copy_to = copy_to

    @property
    def files(self):
        """Gets the files of this CustomModelLinks.  # noqa: E501

        The location to get all files of this entity. See operation \"Models_ListFiles\" for more details.  # noqa: E501

        :return: The files of this CustomModelLinks.  # noqa: E501
        :rtype: str
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this CustomModelLinks.

        The location to get all files of this entity. See operation \"Models_ListFiles\" for more details.  # noqa: E501

        :param files: The files of this CustomModelLinks.  # noqa: E501
        :type: str
        """

        self._files = files

    @property
    def manifest(self):
        """Gets the manifest of this CustomModelLinks.  # noqa: E501

        The location to get a manifest for this model to be used in the on-prem container. See operation \"Models_GetCustomModelManifest\" for more details.  # noqa: E501

        :return: The manifest of this CustomModelLinks.  # noqa: E501
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this CustomModelLinks.

        The location to get a manifest for this model to be used in the on-prem container. See operation \"Models_GetCustomModelManifest\" for more details.  # noqa: E501

        :param manifest: The manifest of this CustomModelLinks.  # noqa: E501
        :type: str
        """

        self._manifest = manifest

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
        if issubclass(CustomModelLinks, dict):
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
        if not isinstance(other, CustomModelLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomModelLinks):
            return True

        return self.to_dict() != other.to_dict()