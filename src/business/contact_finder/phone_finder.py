from utils import BaseService


class PhoneFinder(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find_from_domain(self, domain: str):
        return
