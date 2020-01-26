import os

class EnvironmentSetUp:

    def setUpGlobalEnvironmentVariables(self):
        os.environ['INSTANCE'] = 'cricklewood'
        os.environ['ARCHIVE_DESTINATION'] = '/home/shyamali/hariraoarchive'
        os.environ['ARCHIVE_SOURCE'] = '/home/shyamali/archivesource'

