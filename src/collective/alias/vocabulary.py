from zope.interface import provider
from zope.component.hooks import getSite

from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from Products.CMFCore.utils import getToolByName


@provider(IVocabularyFactory)
def PortalTypesVocabulary(context):
    """Portal types vocabulary that doesn't require the 'context' object to
    be acquisition wrapped.
    """

    site = getSite()
    if site is None:
        return SimpleVocabulary.fromValues([])

    ttool = getToolByName(site, 'portal_types', None)
    if ttool is None:
        return SimpleVocabulary.fromValues([])

    items = [(ttool[t].Title(), t) for t in ttool.listContentTypes()]
    items.sort()
    return SimpleVocabulary([SimpleTerm(i[1], i[1], i[0]) for i in items])
