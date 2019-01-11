from requests_service.factory.qichachaMainImpl import QichachaMainImpl
from requests_service.factory.qichachaOtherImpl import QichachaOtherImpl

downloadImplList = [
    QichachaMainImpl(),
    QichachaOtherImpl(),
]


def getDownloadImp(mid):
    for downloadImp in downloadImplList:
        if downloadImp.mid() == mid:
            return downloadImp
    return None
