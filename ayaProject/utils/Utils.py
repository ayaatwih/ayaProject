class Constants:
    Full_time = 0
    Part_time = 1
    Available = "Available"
    Not_available = "Not Available"
    Active = "Active"
    Inactive = "Inactive"
    Canceled = "Canceled"


class Methods_Utils:
    @staticmethod
    def check_value_is_empty(*value: str):
        for item in value:
            if item.isspace() or item == "":
                return True
