# coding: utf-8

"""
    Web of Science API Lite

    A responsive API that supports rich searching across the Web of Science Core Collection to retrieve core article metadata.  This service provides a great way to reuse Web of Science data both internally and externally to enhance  institutional repositories and research networking systems with best-in-class data. This API supports searching across the Web of Science to retrieve item-level metadata with limited fields:  - UT (Unique Identifier) - Authors - Author keywords - Document type - Title - Issue - Pages - Publication date - Source title - Volume - DOI - ISBN - ISSN   The API supports JSON and XML responses, and this documentation supports trying both response types.   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Source(object):
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
        'pages': 'list[str]',
        'source_title': 'list[str]',
        'issue': 'list[str]',
        'volume': 'list[str]',
        'special_issue': 'list[str]',
        'book_series_title': 'list[str]',
        'published_biblio_date': 'list[str]',
        'published_biblio_year': 'list[str]'
    }

    attribute_map = {
        'pages': 'Pages',
        'source_title': 'SourceTitle',
        'issue': 'Issue',
        'volume': 'Volume',
        'special_issue': 'SpecialIssue',
        'book_series_title': 'BookSeriesTitle',
        'published_biblio_date': 'Published.BiblioDate',
        'published_biblio_year': 'Published.BiblioYear'
    }

    def __init__(self, pages=None, source_title=None, issue=None, volume=None, special_issue=None, book_series_title=None, published_biblio_date=None, published_biblio_year=None):  # noqa: E501
        """Source - a model defined in Swagger"""  # noqa: E501
        self._pages = None
        self._source_title = None
        self._issue = None
        self._volume = None
        self._special_issue = None
        self._book_series_title = None
        self._published_biblio_date = None
        self._published_biblio_year = None
        self.discriminator = None
        if pages is not None:
            self.pages = pages
        if source_title is not None:
            self.source_title = source_title
        if issue is not None:
            self.issue = issue
        if volume is not None:
            self.volume = volume
        if special_issue is not None:
            self.special_issue = special_issue
        if book_series_title is not None:
            self.book_series_title = book_series_title
        if published_biblio_date is not None:
            self.published_biblio_date = published_biblio_date
        if published_biblio_year is not None:
            self.published_biblio_year = published_biblio_year

    @property
    def pages(self):
        """Gets the pages of this Source.  # noqa: E501

        Pages range in the source  # noqa: E501

        :return: The pages of this Source.  # noqa: E501
        :rtype: list[str]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this Source.

        Pages range in the source  # noqa: E501

        :param pages: The pages of this Source.  # noqa: E501
        :type: list[str]
        """

        self._pages = pages

    @property
    def source_title(self):
        """Gets the source_title of this Source.  # noqa: E501

        The title of the source in which the document was published  # noqa: E501

        :return: The source_title of this Source.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_title

    @source_title.setter
    def source_title(self, source_title):
        """Sets the source_title of this Source.

        The title of the source in which the document was published  # noqa: E501

        :param source_title: The source_title of this Source.  # noqa: E501
        :type: list[str]
        """

        self._source_title = source_title

    @property
    def issue(self):
        """Gets the issue of this Source.  # noqa: E501

        Issue Number  # noqa: E501

        :return: The issue of this Source.  # noqa: E501
        :rtype: list[str]
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this Source.

        Issue Number  # noqa: E501

        :param issue: The issue of this Source.  # noqa: E501
        :type: list[str]
        """

        self._issue = issue

    @property
    def volume(self):
        """Gets the volume of this Source.  # noqa: E501

        Volume number  # noqa: E501

        :return: The volume of this Source.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this Source.

        Volume number  # noqa: E501

        :param volume: The volume of this Source.  # noqa: E501
        :type: list[str]
        """

        self._volume = volume

    @property
    def special_issue(self):
        """Gets the special_issue of this Source.  # noqa: E501

        Special issue, in case was published to a special issue journal  # noqa: E501

        :return: The special_issue of this Source.  # noqa: E501
        :rtype: list[str]
        """
        return self._special_issue

    @special_issue.setter
    def special_issue(self, special_issue):
        """Sets the special_issue of this Source.

        Special issue, in case was published to a special issue journal  # noqa: E501

        :param special_issue: The special_issue of this Source.  # noqa: E501
        :type: list[str]
        """

        self._special_issue = special_issue

    @property
    def book_series_title(self):
        """Gets the book_series_title of this Source.  # noqa: E501

        Book series title - in case the article is published in book series  # noqa: E501

        :return: The book_series_title of this Source.  # noqa: E501
        :rtype: list[str]
        """
        return self._book_series_title

    @book_series_title.setter
    def book_series_title(self, book_series_title):
        """Sets the book_series_title of this Source.

        Book series title - in case the article is published in book series  # noqa: E501

        :param book_series_title: The book_series_title of this Source.  # noqa: E501
        :type: list[str]
        """

        self._book_series_title = book_series_title

    @property
    def published_biblio_date(self):
        """Gets the published_biblio_date of this Source.  # noqa: E501

        Published Date  # noqa: E501

        :return: The published_biblio_date of this Source.  # noqa: E501
        :rtype: list[str]
        """
        return self._published_biblio_date

    @published_biblio_date.setter
    def published_biblio_date(self, published_biblio_date):
        """Sets the published_biblio_date of this Source.

        Published Date  # noqa: E501

        :param published_biblio_date: The published_biblio_date of this Source.  # noqa: E501
        :type: list[str]
        """

        self._published_biblio_date = published_biblio_date

    @property
    def published_biblio_year(self):
        """Gets the published_biblio_year of this Source.  # noqa: E501

        Published Year  # noqa: E501

        :return: The published_biblio_year of this Source.  # noqa: E501
        :rtype: list[str]
        """
        return self._published_biblio_year

    @published_biblio_year.setter
    def published_biblio_year(self, published_biblio_year):
        """Sets the published_biblio_year of this Source.

        Published Year  # noqa: E501

        :param published_biblio_year: The published_biblio_year of this Source.  # noqa: E501
        :type: list[str]
        """

        self._published_biblio_year = published_biblio_year

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
        if issubclass(Source, dict):
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
        if not isinstance(other, Source):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other