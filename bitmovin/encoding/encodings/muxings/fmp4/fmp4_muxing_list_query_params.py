
class Fmp4MuxingListQueryParams(dict):
    def __init__(self, offset: int = None, limit: int = None, *args, **kwargs):
        super(Fmp4MuxingListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit