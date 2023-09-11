class Date(object):
    @staticmethod
    def get_date() -> str:
        return '2020-01-02'


class Time(Date):
    @staticmethod
    def get_time() -> str:
        return '08:01:12'

    @staticmethod
    def get_date() -> str:
        return '1966-01-01'


dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())