from plone.app.layout.viewlets import common as base
from redturtle.agidtheme.controlpanel.interfaces import IRedturtleAgidthemeSettings
from plone import api
from ..vocabularies import SHARES
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.utils import getSiteLogo


class SocialViewlet(base.ViewletBase):

    def __init__(self, context, request, view, manager):
        super(SocialViewlet, self).__init__(context, request, view, manager)

    def render(self):
        """
        """
        allowed_types = api.portal.get_registry_record(
            'available_types',
            interface=IRedturtleAgidthemeSettings)
        if self.context.portal_type in allowed_types:
            return self.index()
        return ""

    def get_socials(self):
        socials = api.portal.get_registry_record(
            'available_socials',
            interface=IRedturtleAgidthemeSettings)
        return socials

    def get_sharer_url(self, social_type):
        share_url = SHARES[social_type]['share_url']
        if social_type == 'linkedin':
            return share_url.format(self.context.absolute_url(), self.context.title)
        if social_type == 'twitter':
            return share_url.format(
                self.context.absolute_url(),
                self.context.title,
                '',
                '',
            )
        if social_type == 'pinterest':
            return share_url.format('', self.context.absolute_url(), 'false', self.context.title)
        if social_type == 'pocket':
            return share_url.format(self.context.absolute_url(), self.context.title)
        return share_url.format(self.context.absolute_url())


class LogoViewlet(base.ViewletBase):
    index = ViewPageTemplateFile('templates/logo.pt')

    def update(self):

        super(LogoViewlet, self).update()
        self.site_title = api.portal.get_registry_record(
            'plone.site_title',)

        # TODO: should this be changed to settings.site_title?
        self.navigation_root_title = self.site_title
        self.logo_title = self.site_title
        self.img_src = getSiteLogo()
