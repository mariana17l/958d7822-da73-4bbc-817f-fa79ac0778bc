import fire
import json 

from util import InvestmentProject


class Main(object):
    
    @staticmethod
    def describe_investment(filepath, hurdle_rate=None):
        investment_project = InvestmentProject.from_csv(filepath=filepath, hurdle_rate=hurdle_rate)
        description = investment_project.describe()
        print(json.dumps(description, indent=4))
        print(json.dumps(description, indent=4))
        print('When the internal rate of return is greater than ')
        print('the hurdle rate, means that the investment is ')
        print('profitable, IRR overpasses the minimum return rate ')
        print('(hurdle rate).')
        print('')
        print('The net present value cant be negative, since is a ')
        print('sum of positive values, these values are positive ')
        print('because the cashflow is a positive number divided ')
        print('by another positive number elevates to a positive ')
        print('time periods')
    @staticmethod
    def plot_investment(filepath, save="", show=False):
        print('Mariana')
        investment = InvestmentProject.from_csv(filepath=filepath)
        fig = investment.plot(show=show)
        if save:
            fig.savefig("pic.png")
        return
if __name__ == "__main__":
    fire.Fire(Main)