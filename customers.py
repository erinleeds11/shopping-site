"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,first_name, last_name, email, pw):
        self.first_name =first_name
        self.last_name = last_name
        self.email = email
        self.pw = pw


    def __repr__(self):
        return "<Customer: {}, {}, {}>".format(self.first_name, self.last_name, 
            self.email)

def read_customer_info(filepath):

    customer_dict = {}

    with open(filepath) as file:
        for line in file:
            (first_name, 
            last_name, 
            email,
            pw)= line.strip().split("|")

            customer_dict[email] = Customer(first_name, last_name, email, pw)

def get_by_email(email):

    return customer_dict[email]


customers = read_customer_info("customers.txt")
