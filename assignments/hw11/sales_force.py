from sales_person import SalesPerson


class SalesForce:

    def __init__(self):
        self.sales_person = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        line = infile.readlines()

        for data in line:
            data_split = data.split(",")
            employee_id = data_split[0]
            name = data_split[1] + " " + data_split[2]
            person = SalesPerson(employee_id, name)

            for i in range(3, len(data_split)):
                sales_amount = eval(data_split[i])
                person.enter_sale(sales_amount)
            i = 0
            self.sales_person.append(person)

        file_name.close()

    def quota_report(self, quota):
        report = []
        for person in self.sales_person:
            if person.total_sale() >= quota:
                report.append([person.get_id(), person.get_name(), person.total_sales(), True])
            report.append([person.get_id(), person.get_name(), person.total_sales(), False])
        return report

    def top_seller(self):
        """
        top_seller() -> list[SalesPerson] - returns a list of SalesPerson objects with the highest sales amount.
        If there are no ties, the list should contain one record. In the case of a tie, the list should include
        all of the top sales people.
        """
        top_seller_list = []
        top_sales = 0
        for i in self.sales_person:
            if i.total_sales() > top_sales:
                top_sales = i.total_sales()
                top_seller_list = [i]
            elif i.total_sales() == top_sales:
                top_seller_list.append(i)
        return top_seller_list

    def individual_sales(self, employee_id):
        """
        individual_sales(employee_id) -> SalesPerson - returns the SalesPerson with the given
        employee_id or None if the id does not exist.
        """
        for i in self.sales_person:
            if i.get_id() == employee_id:
                return i
        return None

    def get_sales_frequency(self):
        """
        get_sale_frequencies() -> dict{sale amount: frequency} -
        returns a dictionary where the keys are sale amounts and
        the values are the frequency of that sale amount (how many
        sales have been for that amount amongst the entire sales force).
        """
        frequencies = {}
        for person in self.sales_person:
            for sale in person.get_sales():
                if sale in frequencies:
                    frequencies[sale] += 1
                else:
                    frequencies = 1
            return frequencies



