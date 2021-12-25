'''
Frequency Distribution ***
QQ Plot ***
Kolmogorov-Smirnov test *
Lilliefors corrected K-S
Shapiro-Wilk test ***
Ansderson Darling test
Cramer-von Mises test
D'Agostino skewness test
Anscomb-Glynn kurtosis test
D'Agostino Pearson omnibus test
Jaque-Bera test
'''

from numpy import histogram, random
from scipy.stats import shapiro, probplot
import pylab

def normality(sample, alpha=0.05):
    
    '''
    This function takes a sample -> shows the pp-plot -> then notifies you of the shapiro test results
    '''
    
    probplot(sample, dist="norm", plot=pylab)
    pylab.show()
    
    test = shapiro(sample)
    
    if test.pvalue > alpha:
        print(f"We fail reject the Shapiro null hypothesis. There is evidence to suggest that that data is normal given that our pvalue = {test.pvalue} > alpha = {alpha}")
    else:
        print(f"We reject the Shapiro null hypothesis. There is evidence to suggest that that data is non-normal given that our pvalue = {test.pvalue} < alpha = {alpha}")


x = random.randn(100)
    
normality(x)
