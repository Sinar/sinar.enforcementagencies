from collective.grok import gs
from sinar.enforcementagencies import MessageFactory as _

@gs.importstep(
    name=u'sinar.enforcementagencies', 
    title=_('sinar.enforcementagencies import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinar.enforcementagencies.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
