import  datetime
import os
import tarfile

from play.ground.EnvironmentSetUp import EnvironmentSetUp
from play.ground.RandomMethods import RandomMethods


def main():
    globalEnvironmentSetUp = EnvironmentSetUp()
    globalEnvironmentSetUp.setUpGlobalEnvironmentVariables()
    fileList = os.listdir(os.environ['ARCHIVE_SOURCE'])
    archive_tarname = '%s/%s_%s.tar.gz' % (os.environ['ARCHIVE_DESTINATION'], os.environ['INSTANCE'], datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
    print(archive_tarname)
    archive_tarname_open = tarfile.open(archive_tarname, 'w:gz')
    for fileName in fileList:
        filePath = os.path.join(os.environ['ARCHIVE_SOURCE'], fileName)
        print(filePath)
        archive_tarname_open.add(filePath)
    archive_tarname_open.close()

    randomMethods = RandomMethods()
    trade= randomMethods.returnAList()
    print(trade)
main()

