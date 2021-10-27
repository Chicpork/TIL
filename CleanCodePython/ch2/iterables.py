# %%
from datetime import date, timedelta


class DateRangeIterable:
    """An iterable that contains its own iterator object."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class DateRangeContainerIterable:
    """An range that builds its iteration through a generator."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


# %%
for day in DateRangeIterable(date(2019, 1, 1), date(2019, 1, 5)):
    print(day)

# %%
for day in DateRangeContainerIterable(date(2019, 1, 1), date(2019, 1, 5)):
    print(day)

# %%
r1 = DateRangeContainerIterable(date(2019, 1, 1), date(2019, 1, 5))
print(", ".join(map(str, r1)))
print(max(r1))
