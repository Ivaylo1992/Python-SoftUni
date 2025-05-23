class DVD:
    def __init__(
            self, name: str,
            dvd_id: int,
            creation_year: int,
            creation_month: str,
            age_restriction: int
    ) -> None:
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        months = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }

        creation_year = int(date.split('.')[2])
        creation_month = months[int(date.split('.')[1])]

        return cls(name, dvd_id, creation_year, creation_month, age_restriction)

    def __repr__(self) -> str:
        rented_info = 'not rented' if not self.is_rented else 'rented'

        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})"
                f" has age restriction {self.age_restriction}."
                f" Status: {rented_info}")


dvd = DVD.from_date(1, "A", "16.10.1997", 18)
print(dvd)