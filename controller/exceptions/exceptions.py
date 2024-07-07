class CustomerNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Customer Not Found !!!")

class BeautyJobNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Beauty Job Not Found !!!")

class EmployeeNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Employee Not Found !!!")

class ReserveotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Reserve Not Found !!!")

class TimingNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Timing Not Found !!!")