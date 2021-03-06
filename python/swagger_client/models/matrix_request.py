# coding: utf-8

"""
    GraphHopper Directions API

    You use the GraphHopper Directions API to add route planning, navigation and route optimization to your software. E.g. the Routing API has turn instructions and elevation data and the Route Optimization API solves your logistic problems and supports various constraints like time window and capacity restrictions. Also it is possible to get all distances between all locations with our fast Matrix API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MatrixRequest(object):
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
        'points': 'list[list[float]]',
        'from_points': 'list[list[float]]',
        'to_points': 'list[list[float]]',
        'point_hints': 'list[str]',
        'from_point_hints': 'list[str]',
        'to_point_hints': 'list[str]',
        'out_arrays': 'list[str]',
        'vehicle': 'str'
    }

    attribute_map = {
        'points': 'points',
        'from_points': 'from_points',
        'to_points': 'to_points',
        'point_hints': 'point_hints',
        'from_point_hints': 'from_point_hints',
        'to_point_hints': 'to_point_hints',
        'out_arrays': 'out_arrays',
        'vehicle': 'vehicle'
    }

    def __init__(self, points=None, from_points=None, to_points=None, point_hints=None, from_point_hints=None, to_point_hints=None, out_arrays=None, vehicle=None):  # noqa: E501
        """MatrixRequest - a model defined in Swagger"""  # noqa: E501

        self._points = None
        self._from_points = None
        self._to_points = None
        self._point_hints = None
        self._from_point_hints = None
        self._to_point_hints = None
        self._out_arrays = None
        self._vehicle = None
        self.discriminator = None

        if points is not None:
            self.points = points
        if from_points is not None:
            self.from_points = from_points
        if to_points is not None:
            self.to_points = to_points
        if point_hints is not None:
            self.point_hints = point_hints
        if from_point_hints is not None:
            self.from_point_hints = from_point_hints
        if to_point_hints is not None:
            self.to_point_hints = to_point_hints
        if out_arrays is not None:
            self.out_arrays = out_arrays
        if vehicle is not None:
            self.vehicle = vehicle

    @property
    def points(self):
        """Gets the points of this MatrixRequest.  # noqa: E501

        Specifiy multiple points for which the weight-, route-, time- or distance-matrix should be calculated. In this case the starts are identical to the destinations. If there are N points, then NxN entries will be calculated. The order of the point parameter is important. Specify at least three points. Cannot be used together with from_point or to_point. Is a string with the format longitude,latitude.  # noqa: E501

        :return: The points of this MatrixRequest.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this MatrixRequest.

        Specifiy multiple points for which the weight-, route-, time- or distance-matrix should be calculated. In this case the starts are identical to the destinations. If there are N points, then NxN entries will be calculated. The order of the point parameter is important. Specify at least three points. Cannot be used together with from_point or to_point. Is a string with the format longitude,latitude.  # noqa: E501

        :param points: The points of this MatrixRequest.  # noqa: E501
        :type: list[list[float]]
        """

        self._points = points

    @property
    def from_points(self):
        """Gets the from_points of this MatrixRequest.  # noqa: E501

        The starting points for the routes. E.g. if you want to calculate the three routes A-&gt;1, A-&gt;2, A-&gt;3 then you have one from_point parameter and three to_point parameters. Is a string with the format longitude,latitude.  # noqa: E501

        :return: The from_points of this MatrixRequest.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._from_points

    @from_points.setter
    def from_points(self, from_points):
        """Sets the from_points of this MatrixRequest.

        The starting points for the routes. E.g. if you want to calculate the three routes A-&gt;1, A-&gt;2, A-&gt;3 then you have one from_point parameter and three to_point parameters. Is a string with the format longitude,latitude.  # noqa: E501

        :param from_points: The from_points of this MatrixRequest.  # noqa: E501
        :type: list[list[float]]
        """

        self._from_points = from_points

    @property
    def to_points(self):
        """Gets the to_points of this MatrixRequest.  # noqa: E501

        The destination points for the routes. Is a string with the format longitude,latitude.  # noqa: E501

        :return: The to_points of this MatrixRequest.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._to_points

    @to_points.setter
    def to_points(self, to_points):
        """Sets the to_points of this MatrixRequest.

        The destination points for the routes. Is a string with the format longitude,latitude.  # noqa: E501

        :param to_points: The to_points of this MatrixRequest.  # noqa: E501
        :type: list[list[float]]
        """

        self._to_points = to_points

    @property
    def point_hints(self):
        """Gets the point_hints of this MatrixRequest.  # noqa: E501

        Optional parameter. Specifies a hint for each point in the `points` array to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up.  # noqa: E501

        :return: The point_hints of this MatrixRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._point_hints

    @point_hints.setter
    def point_hints(self, point_hints):
        """Sets the point_hints of this MatrixRequest.

        Optional parameter. Specifies a hint for each point in the `points` array to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up.  # noqa: E501

        :param point_hints: The point_hints of this MatrixRequest.  # noqa: E501
        :type: list[str]
        """

        self._point_hints = point_hints

    @property
    def from_point_hints(self):
        """Gets the from_point_hints of this MatrixRequest.  # noqa: E501

        More information for the `from_points` array. See `point_hints`  # noqa: E501

        :return: The from_point_hints of this MatrixRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._from_point_hints

    @from_point_hints.setter
    def from_point_hints(self, from_point_hints):
        """Sets the from_point_hints of this MatrixRequest.

        More information for the `from_points` array. See `point_hints`  # noqa: E501

        :param from_point_hints: The from_point_hints of this MatrixRequest.  # noqa: E501
        :type: list[str]
        """

        self._from_point_hints = from_point_hints

    @property
    def to_point_hints(self):
        """Gets the to_point_hints of this MatrixRequest.  # noqa: E501

        More information for the `to_points` array. See `point_hints`  # noqa: E501

        :return: The to_point_hints of this MatrixRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._to_point_hints

    @to_point_hints.setter
    def to_point_hints(self, to_point_hints):
        """Sets the to_point_hints of this MatrixRequest.

        More information for the `to_points` array. See `point_hints`  # noqa: E501

        :param to_point_hints: The to_point_hints of this MatrixRequest.  # noqa: E501
        :type: list[str]
        """

        self._to_point_hints = to_point_hints

    @property
    def out_arrays(self):
        """Gets the out_arrays of this MatrixRequest.  # noqa: E501

        Specifies which arrays should be included in the response. Specify one or more of the following options 'weights', 'times', 'distances'. To specify more than one array use e.g. out_array=times&amp;out_array=distances. The units of the entries of distances are meters, of times are seconds and of weights is arbitrary and it can differ for different vehicles or versions of this API.  # noqa: E501

        :return: The out_arrays of this MatrixRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._out_arrays

    @out_arrays.setter
    def out_arrays(self, out_arrays):
        """Sets the out_arrays of this MatrixRequest.

        Specifies which arrays should be included in the response. Specify one or more of the following options 'weights', 'times', 'distances'. To specify more than one array use e.g. out_array=times&amp;out_array=distances. The units of the entries of distances are meters, of times are seconds and of weights is arbitrary and it can differ for different vehicles or versions of this API.  # noqa: E501

        :param out_arrays: The out_arrays of this MatrixRequest.  # noqa: E501
        :type: list[str]
        """

        self._out_arrays = out_arrays

    @property
    def vehicle(self):
        """Gets the vehicle of this MatrixRequest.  # noqa: E501

        The vehicle for which the route should be calculated. Other vehicles are foot, small_truck etc, see here for the details.  # noqa: E501

        :return: The vehicle of this MatrixRequest.  # noqa: E501
        :rtype: str
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this MatrixRequest.

        The vehicle for which the route should be calculated. Other vehicles are foot, small_truck etc, see here for the details.  # noqa: E501

        :param vehicle: The vehicle of this MatrixRequest.  # noqa: E501
        :type: str
        """

        self._vehicle = vehicle

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MatrixRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
