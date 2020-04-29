# -*- coding: utf-8 -*-
import os

from social_core.backends.open_id_connect import OpenIdConnectAuth


class VendastaOpenIdConnect(OpenIdConnectAuth):
    """Vendasta OpenID authentication Backend."""

    name = "vendasta"
    OIDC_ENDPOINT = "http://iam-prod.vendasta-internal.com"
    ACCESS_TOKEN_METHOD = "POST"
    EXTRA_DATA = [("sub", "id"), "namespace", "roles"]
    USERNAME_KEY = "sub"
