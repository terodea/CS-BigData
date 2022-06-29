from ast import arg
import json
import faker
from dateutil.relativedelta import relativedelta
from datetime import datetime
from faker import Faker
import argparse




class DataGenerator:
    def __init__(self, args):
        try:
            self.faker = Faker("en_IN")
            self.CHARACTERS = ["Mario", "Luigi", "Peach", "Toad"]
            self.DATE_END = datetime.now()
            self.DATE_START = self.DATE_END + relativedelta(months=-1)
            self.MAX_LIVES = 10
            self.MIN_LIVES = 1
            self.NUM_EVENTS = int(args.get("no_of_events", 2))
            self.MIN_SALARY = int(args.get("min_salary", 50000))
            self.MAX_SALARY = int(args.get("max_salary", 700000))
            self._generate_events()
        except Exception as err:
            raise err

    def _generate_events(self):
        """ Generate the metric data """
        # yield {
            #     "character": faker.random_element(self.CHARACTERS),
            #     "lives": faker.random_int(min=self.MIN_LIVES, max=self.MAX_LIVES, step=1),
            #     "time": str(faker.date_between_dates(self.DATE_START, self.DATE_END)),
            # }

        for _ in range(self.NUM_EVENTS):
            _ = self.faker.profile()
            yield {
                "job_profile": _["job"],
                "company": _["company"],
                "aadhar_no": _["ssn"], 
                "blood_group": _["blood_group"],
                "name": _["name"],
                "sex": _["sex"],
                "mail": f"{'.'.join(i.lower() for i in _['name'].split(' '))}@{self.faker.random_element(['hotmail.com', 'gmail.com', 'yahoo.com', 'rediff.com'])}",
                "job_no": self.faker.random_int(min=self.MIN_LIVES, max=self.MAX_LIVES, step=1),
                "salary" : self.faker.random_int(min=self.MIN_SALARY, max=self.MAX_SALARY, step=10)
            }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A data generator utility.",
        usage="python3 client.py --no_of_events 10 --min_salary 500000 --max_salary 700000")
    parser.add_argument("--no_of_events", help="No of data points to generate.", type=int)
    parser.add_argument("--min_salary", help="Min Salary", type=int)
    parser.add_argument("--max_salary", help="Max Salary", type=int)
    _args = vars(parser.parse_args())
    DataGenerator(args=_args)
