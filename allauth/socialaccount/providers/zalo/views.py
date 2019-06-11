import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import ZaloProvider


class ZaloOAuth2Adapter(OAuth2Adapter):
    provider_id = ZaloProvider.id
    access_token_url = 'https://graph.zalo.me/v2.0/me?access_token={access_token}'

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(self.access_token_url.format(access_token=token))
        extra_data = resp.json()
        if extra_data.get('error', None) is None:
            return self.get_provider().sociallogin_from_response(request,
                                                                 extra_data)
        else:
            raise Exception(extra_data.get('message'))


oauth2_login = OAuth2LoginView.adapter_view(ZaloOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(ZaloOAuth2Adapter)
