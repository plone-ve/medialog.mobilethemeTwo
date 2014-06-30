from zope.interface import Interface
from z3c.form import interfaces
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.mobilethemeTwo')


class IMobilethemeTwoLayer(Interface):
    """A layer specific to medialog.mobilethemeTwo
        """


class IMobilethemeTwoSettings(form.Schema):
    """Adds settings to medialog.controlpanel
        """
    
    form.fieldset(
        'mobilethemeTwo',
                  label=_(u'MobilethemeTwo settings'),
                  fields=[
                          'scrape_external_base_url',
                          'scrape_url'
                          ],
                  )
                  
        scrape_external_base_url = schema.TextLine(
                 title=_(u"scrape_external_base_url", default=u"Base URL for external site"),
                 description=_(u"help_scrape_external_base_url",
                 default=u"scrape_external_base_url")
                 )

        scrape_url = schema.TextLine(
                  title=_(u"scrape_url", default=u"URL that should be redirected"),
                   description=_(u"help_scrape_url",
                    default=u"URL that will be redirected to http;//yoursite/scrape?url=originalUrL")
        )


alsoProvides(IMobilethemeTwo, IMedialogControlpanelSettingsProvider)
