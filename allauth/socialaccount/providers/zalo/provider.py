from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class ZaloAccount(ProviderAccount):

    def get_avatar_url(self):
        return self.account.extra_data.get('picture').get('data').get('url')

    def to_str(self):
        return self.account.extra_data.get('name', self.account.uid)


class ZaloProvider(OAuth2Provider):
    id = 'zalo'
    name = 'Zalo'
    account_class = ZaloAccount

    def get_default_scope(self):
        return []

    def extract_uid(self, data):
        return str(data['id'])


provider_classes = [ZaloProvider]
