from requests_service.factory.qichachaMainImpl import QichachaMainImpl
from requests_service.factory.qichachaOtherImpl import QichachaOtherImpl
from requests_service.factory.commonImpl import CommonImpl

downloadImplList = [
    QichachaMainImpl(),
    QichachaOtherImpl(),
    CommonImpl()
]


def getDownloadImp(mid):
    for downloadImp in downloadImplList:
        if downloadImp.mid() == mid:
            return downloadImp
    return None
