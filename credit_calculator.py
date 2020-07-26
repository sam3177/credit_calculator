import math


class Credit:
    def ui_input(self):
        a = input()
        self.make(a)

    def __init__(self):
        self.principal = 0
        self.annuity = 0
        self.interest = 0
        self.months = 0
        self.i = 0
        self.first_choice = ''  # save the first option
        self.state = 'action'
        self.ui_input()

    def months_count(self):
        x = self.annuity / (self.annuity - self.i * self.principal)
        n = math.ceil(math.log(x, 1 + self.i))
        years, months = n // 12, n % 12
        if years == 1:
            s = ''
        else:
            s = 's'
        if months == 1:
            s_ = ''
        else:
            s_ = 's'
        if years > 0 and months > 0:
            print('You need {} year{} and {} month{} to repay this credit!'.format(years, s, months, s_))
        elif years == 0:
            print('You need {} month{} to repay this credit!'.format(months, s_))
        elif months == 0:
            print('You need {} year{} repay this credit!'.format(years, s))

    def annuity_count(self):
        ann = math.ceil(self.principal * (self.i * math.pow(self.i + 1, self.months)) / (math.pow(self.i + 1, self.months) - 1))
        print('Your annuity payment = {}!'.format(ann))

    def credit_count(self):
        credit_ = math.floor(self.annuity / ((self.i * math.pow(self.i + 1, self.months)) / (math.pow(self.i + 1, self.months) - 1)))
        print('Your credit principal = {}!'.format(credit_))

    def enter_credit(self):
        print('Enter credit principal:')
        self.state = 'credit_p'
        return self.ui_input()

    def enter_monthly_payment(self):
        print('Enter monthly payment:')
        self.state = 'monthly_p'
        return self.ui_input()

    def enter_interest(self):
        print('Enter credit interest:')
        self.state = 'interest'
        return self.ui_input()

    def enter_months(self):
        print('Enter count of periods:')
        self.state = 'months'
        return self.ui_input()

    def make(self, xxx):
        if self.state == 'action':
            self.first_choice = xxx
            if xxx == 'n':
                return self.enter_credit()
            elif xxx == 'a':
                return self.enter_credit()
            elif xxx == 'p':
                return self.enter_monthly_payment()

        elif self.state == 'credit_p':
            self.principal = int(xxx)
            if self.first_choice == 'n':
                return self.enter_monthly_payment()
            elif self.first_choice == 'a':
                return self.enter_months()

        elif self.state == 'monthly_p':
            self.annuity = float(xxx)
            if self.first_choice == 'n':
                return self.enter_interest()
            elif self.first_choice == 'p':
                return self.enter_months()

        elif self.state == 'months':
            self.months = int(xxx)
            return self.enter_interest()

        elif self.state == 'interest':
            self.interest = float(xxx)
            self.i = float(xxx) / 100 / 12
            if self.first_choice == 'n':
                return self.months_count()
            elif self.first_choice == 'a':
                return self.annuity_count()
            elif self.first_choice == 'p':
                return self.credit_count()


print('What do you want to calculate?\ntype "n" - for count of months,')
print('type "a" - for annuity monthly payment,\ntype "p" - for credit principal:')
credit = Credit()
