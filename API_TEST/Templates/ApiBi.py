class ApiBi(object):

    def __init__(self):
        self.biClientLoginoutReport = self.biClientLoginoutReport()
        self.biHeartclientUserHeart = self.biHeartclientUserHeart()
        self.biUserReport = self.biUserReport()
        self.biVideoOperationReport = self.biVideoOperationReport()
        self.biHeartVideoHeart = self.biHeartVideoHeart()
        self.biVideoPlayVideoHistory = self.biVideoPlayVideoHistory()
        self.historyDeleteHistory = self.historyDeleteHistory()
        self.historyVideoContinuation = self.historyVideoContinuation()
        self.biPanoramaReport = self.biPanoramaReport()
        self.biPageReport = self.biPageReport()


    def biClientLoginoutReport(self):
        biClientLoginoutReport = {}
        biClientLoginoutReport["path"] = "/biClient/biClientLoginout/report"
        biClientLoginoutReport["header"] = {'Content-Type': 'application/json'}
        biClientLoginoutReport["method"] = "POST"
        return biClientLoginoutReport

    def biHeartclientUserHeart(self):
        biHeartclientUserHeart = {}
        biHeartclientUserHeart["path"] = "/biClient/biHeart/clientUserHeart"
        biHeartclientUserHeart["header"] = {'Content-Type': 'application/json'}
        biHeartclientUserHeart["method"] = "POST"
        return biHeartclientUserHeart

    def biUserReport(self):
        biUserReport = {}
        biUserReport["path"] = "/biClient/biUser/report"
        biUserReport["header"] = {'Content-Type': 'application/json'}
        biUserReport["method"] = "POST"
        return biUserReport

    def biVideoOperationReport(self):
        biVideoOperationReport = {}
        biVideoOperationReport["path"] = "/biClient/biVideoOperation/report"
        biVideoOperationReport["header"] = {'Content-Type': 'application/json'}
        biVideoOperationReport["method"] = "POST"
        return biVideoOperationReport

    def biHeartVideoHeart(self):
        biHeartvideoHeart = {}
        biHeartvideoHeart["path"] = "/biClient/biHeart/videoHeart"
        biHeartvideoHeart["header"] = {'Content-Type': 'application/json'}
        biHeartvideoHeart["method"] = "POST"
        return biHeartvideoHeart

    def biVideoPlayVideoHistory(self):
        biVideoPlayVideoHistory = {}
        biVideoPlayVideoHistory["path"] = "/biClient/biVideoPlay/videoHistory"
        biVideoPlayVideoHistory["header"] = {'Content-Type': 'application/json'}
        biVideoPlayVideoHistory["method"] = "GET"
        return biVideoPlayVideoHistory

    def historyDeleteHistory(self):
        historyDeleteHistory = {}
        historyDeleteHistory["path"] = "/biClient/history/deleteHistory"
        historyDeleteHistory["header"] = {'Content-Type': 'application/json'}
        historyDeleteHistory["method"] = "POST"
        return historyDeleteHistory

    def historyVideoContinuation(self):
        historyVideoContinuation = {}
        historyVideoContinuation["path"] = "/biClient/history/videoContinuation"
        historyVideoContinuation["header"] = {'Content-Type': 'application/json'}
        historyVideoContinuation["method"] = "GET"
        return historyVideoContinuation

    def biPanoramaReport(self):
        biPanoramaReport = {}
        biPanoramaReport["path"] = "/biClient/biPanorama/report"
        biPanoramaReport["header"] = {'Content-Type': 'application/json'}
        biPanoramaReport["method"] = "POST"
        return biPanoramaReport

    def biPageReport(self):
        biPageReport = {}
        biPageReport["path"] = "/biClient/biPage/report"
        biPageReport["header"] = {'Content-Type': 'application/json'}
        biPageReport["method"] = "POST"
        return biPageReport
