class DomainException(Exception):
    pass


class BusinessRuleException(DomainException):
    def __init__(self, rule):
        self.rule = rule

    def __str__(self):
        return str(self.rule)
