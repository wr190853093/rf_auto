class ApiCms(object):

    def __init__(self):
        self.getCategoryList = self.getCategoryList()
        self.getContentList = self.getContentList()

    def getContentList(self):
        getCategoryList = {}
        getCategoryList["path"] = "/cmsClient/content/getContentList"
        getCategoryList["header"] = {"Content-Type": "application/json"}
        return getCategoryList

    def getCategoryList(self):
        getCategoryList = {}
        getCategoryList["path"] = "/cmsClient/content/getCategoryList"
        getCategoryList["header"] = {'Content-Type': 'application/json', 'mac': 'f98f1bc2846e11ea89a'}
        return getCategoryList
