class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = str(name)
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        """
        enter_sale(sale) -> void - adds the value of sale
        to the sales list

        """
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for num in self.sales:
            total += num
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        self_total_sales = self.total_sales()
        other_total_sales = other.total_sales()

        if other_total_sales > self_total_sales:
            return -1
        if other_total_sales < self_total_sales:
            return 1
        if other_total_sales == self_total_sales:
            return 0

    def __str__(self):
        rtn_str = "ID: " + str(self.employee_id)
        rtn_str += "\nName: " + str(self.name)
        rtn_str += "\nTotal Sales: " + str(self.total_sales())
        return rtn_str

