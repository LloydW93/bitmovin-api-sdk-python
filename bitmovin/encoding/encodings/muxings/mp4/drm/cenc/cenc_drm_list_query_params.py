
class CencDrmListQueryParams(dict):
    def __init__(self, offset: str = None, limit: str = None, *args, **kwargs):
        super(CencDrmListQueryParams, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
