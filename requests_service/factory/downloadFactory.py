from factory.qichachaMainImpl import QichachaMainImpl
from factory.qichachaOtherImpl import QichachaOtherImpl

downloadImplList = [
    QichachaMainImpl(),
    QichachaOtherImpl(),
]


def getDownloadImp(mid):
    for downloadImp in downloadImplList:
        if downloadImp.mid() == mid:
            return downloadImp
    return None
