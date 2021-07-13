# coding: utf-8

"""
    Flexify.IO User REST API

    + Get API token + Authorize using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.12.6
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class User(object):
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
        'account': 'BillingAccount',
        'actual_limits': 'UserConfig',
        'billing_server_account_id': 'str',
        'delete_requested': 'datetime',
        'external_id': 'str',
        'id': 'int',
        'org': 'Organization',
        'profile': 'UserProfile',
        'registered': 'datetime',
        'require_license_terms': 'bool',
        'roles': 'list[str]',
        'settings': 'UserSettings',
        'sign_up_code': 'str',
        'state': 'str',
        'user_limits': 'UserConfig',
        'username': 'str'
    }

    attribute_map = {
        'account': 'account',
        'actual_limits': 'actualLimits',
        'billing_server_account_id': 'billingServerAccountId',
        'delete_requested': 'deleteRequested',
        'external_id': 'externalId',
        'id': 'id',
        'org': 'org',
        'profile': 'profile',
        'registered': 'registered',
        'require_license_terms': 'requireLicenseTerms',
        'roles': 'roles',
        'settings': 'settings',
        'sign_up_code': 'signUpCode',
        'state': 'state',
        'user_limits': 'userLimits',
        'username': 'username'
    }

    def __init__(self, account=None, actual_limits=None, billing_server_account_id=None, delete_requested=None, external_id=None, id=None, org=None, profile=None, registered=None, require_license_terms=None, roles=None, settings=None, sign_up_code=None, state=None, user_limits=None, username=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._account = None
        self._actual_limits = None
        self._billing_server_account_id = None
        self._delete_requested = None
        self._external_id = None
        self._id = None
        self._org = None
        self._profile = None
        self._registered = None
        self._require_license_terms = None
        self._roles = None
        self._settings = None
        self._sign_up_code = None
        self._state = None
        self._user_limits = None
        self._username = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if actual_limits is not None:
            self.actual_limits = actual_limits
        if billing_server_account_id is not None:
            self.billing_server_account_id = billing_server_account_id
        if delete_requested is not None:
            self.delete_requested = delete_requested
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if org is not None:
            self.org = org
        if profile is not None:
            self.profile = profile
        if registered is not None:
            self.registered = registered
        if require_license_terms is not None:
            self.require_license_terms = require_license_terms
        if roles is not None:
            self.roles = roles
        if settings is not None:
            self.settings = settings
        if sign_up_code is not None:
            self.sign_up_code = sign_up_code
        if state is not None:
            self.state = state
        if user_limits is not None:
            self.user_limits = user_limits
        if username is not None:
            self.username = username

    @property
    def account(self):
        """Gets the account of this User.  # noqa: E501

        Billing Account associated with this user  # noqa: E501

        :return: The account of this User.  # noqa: E501
        :rtype: BillingAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this User.

        Billing Account associated with this user  # noqa: E501

        :param account: The account of this User.  # noqa: E501
        :type: BillingAccount
        """

        self._account = account

    @property
    def actual_limits(self):
        """Gets the actual_limits of this User.  # noqa: E501

        Actual limits thar are currently in force  # noqa: E501

        :return: The actual_limits of this User.  # noqa: E501
        :rtype: UserConfig
        """
        return self._actual_limits

    @actual_limits.setter
    def actual_limits(self, actual_limits):
        """Sets the actual_limits of this User.

        Actual limits thar are currently in force  # noqa: E501

        :param actual_limits: The actual_limits of this User.  # noqa: E501
        :type: UserConfig
        """

        self._actual_limits = actual_limits

    @property
    def billing_server_account_id(self):
        """Gets the billing_server_account_id of this User.  # noqa: E501

        ID of this user's billing account on an external billing server  # noqa: E501

        :return: The billing_server_account_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._billing_server_account_id

    @billing_server_account_id.setter
    def billing_server_account_id(self, billing_server_account_id):
        """Sets the billing_server_account_id of this User.

        ID of this user's billing account on an external billing server  # noqa: E501

        :param billing_server_account_id: The billing_server_account_id of this User.  # noqa: E501
        :type: str
        """

        self._billing_server_account_id = billing_server_account_id

    @property
    def delete_requested(self):
        """Gets the delete_requested of this User.  # noqa: E501

        If not null - time when the user requested to delete his or her account  # noqa: E501

        :return: The delete_requested of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._delete_requested

    @delete_requested.setter
    def delete_requested(self, delete_requested):
        """Sets the delete_requested of this User.

        If not null - time when the user requested to delete his or her account  # noqa: E501

        :param delete_requested: The delete_requested of this User.  # noqa: E501
        :type: datetime
        """

        self._delete_requested = delete_requested

    @property
    def external_id(self):
        """Gets the external_id of this User.  # noqa: E501

        External ID of the user, if specified  # noqa: E501

        :return: The external_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this User.

        External ID of the user, if specified  # noqa: E501

        :param external_id: The external_id of this User.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        User ID in the system  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        User ID in the system  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def org(self):
        """Gets the org of this User.  # noqa: E501

        Organization owning this user  # noqa: E501

        :return: The org of this User.  # noqa: E501
        :rtype: Organization
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this User.

        Organization owning this user  # noqa: E501

        :param org: The org of this User.  # noqa: E501
        :type: Organization
        """

        self._org = org

    @property
    def profile(self):
        """Gets the profile of this User.  # noqa: E501

        User's profile  # noqa: E501

        :return: The profile of this User.  # noqa: E501
        :rtype: UserProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this User.

        User's profile  # noqa: E501

        :param profile: The profile of this User.  # noqa: E501
        :type: UserProfile
        """

        self._profile = profile

    @property
    def registered(self):
        """Gets the registered of this User.  # noqa: E501

        Registration time  # noqa: E501

        :return: The registered of this User.  # noqa: E501
        :rtype: datetime
        """
        return self._registered

    @registered.setter
    def registered(self, registered):
        """Sets the registered of this User.

        Registration time  # noqa: E501

        :param registered: The registered of this User.  # noqa: E501
        :type: datetime
        """

        self._registered = registered

    @property
    def require_license_terms(self):
        """Gets the require_license_terms of this User.  # noqa: E501

        Indicates that this user does not have a password and needs to accept EULA  # noqa: E501

        :return: The require_license_terms of this User.  # noqa: E501
        :rtype: bool
        """
        return self._require_license_terms

    @require_license_terms.setter
    def require_license_terms(self, require_license_terms):
        """Sets the require_license_terms of this User.

        Indicates that this user does not have a password and needs to accept EULA  # noqa: E501

        :param require_license_terms: The require_license_terms of this User.  # noqa: E501
        :type: bool
        """

        self._require_license_terms = require_license_terms

    @property
    def roles(self):
        """Gets the roles of this User.  # noqa: E501

        Roles associated with this user  # noqa: E501

        :return: The roles of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.

        Roles associated with this user  # noqa: E501

        :param roles: The roles of this User.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ROLE_ACTUATOR", "ROLE_ADMIN", "ROLE_BILLING", "ROLE_DISTRIBUTOR", "ROLE_IMPERSONATOR", "ROLE_PARTNER_ADMIN", "ROLE_USER"]  # noqa: E501
        if not set(roles).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles = roles

    @property
    def settings(self):
        """Gets the settings of this User.  # noqa: E501

        User's settings  # noqa: E501

        :return: The settings of this User.  # noqa: E501
        :rtype: UserSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this User.

        User's settings  # noqa: E501

        :param settings: The settings of this User.  # noqa: E501
        :type: UserSettings
        """

        self._settings = settings

    @property
    def sign_up_code(self):
        """Gets the sign_up_code of this User.  # noqa: E501

        Sign up code that the user used when signing up  # noqa: E501

        :return: The sign_up_code of this User.  # noqa: E501
        :rtype: str
        """
        return self._sign_up_code

    @sign_up_code.setter
    def sign_up_code(self, sign_up_code):
        """Sets the sign_up_code of this User.

        Sign up code that the user used when signing up  # noqa: E501

        :param sign_up_code: The sign_up_code of this User.  # noqa: E501
        :type: str
        """

        self._sign_up_code = sign_up_code

    @property
    def state(self):
        """Gets the state of this User.  # noqa: E501

        State of this user  # noqa: E501

        :return: The state of this User.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this User.

        State of this user  # noqa: E501

        :param state: The state of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "DISABLED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def user_limits(self):
        """Gets the user_limits of this User.  # noqa: E501

        Limits defined for this user  # noqa: E501

        :return: The user_limits of this User.  # noqa: E501
        :rtype: UserConfig
        """
        return self._user_limits

    @user_limits.setter
    def user_limits(self, user_limits):
        """Sets the user_limits of this User.

        Limits defined for this user  # noqa: E501

        :param user_limits: The user_limits of this User.  # noqa: E501
        :type: UserConfig
        """

        self._user_limits = user_limits

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501

        Username, always the same as user's email  # noqa: E501

        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

        Username, always the same as user's email  # noqa: E501

        :param username: The username of this User.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
