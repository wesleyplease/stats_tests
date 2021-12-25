from scipy.stats import f_oneway, ttest_1samp, ttest_ind


# anova (f_oneway) to test difference in multiple group means
def quick_anova(*args, alpha=0.05):

    test = f_oneway(*args)

    if test.pvalue < alpha:
        print(f"p={test.pvalue} is lower than our level of significance of {alpha}, there is evidence that the mean values across groups are not equal")
    else:
        print(f"There is no evidence to suggest that there are any differences in mean across groups, pvalue = {test.pvalue} > alpha = {alpha}")
       
## Z-test

# T-test to compare 1 sample to a population mean
def quick_t(sample, population_mean, alpha=0.05):
    
    test = ttest_1samp(sample, population_mean, axis=0, nan_policy='propagate', alternative='two-sided')

    if test.pvalue < alpha:
        print(f"p={test.pvalue} is lower than our level of significance of {alpha}, there is evidence that the sample mean does not resemble the population mean")
    else:
        print(f"There is evidence to suggest that the sample mean resembles the population mean, pvalue = {test.pvalue} > alpha = {alpha}") 

# T-test to compare two independent sample means STUDENTS T-TEST
def quick_t_2sample(group_1, group_2, alpha=0.05):
    
    
    test = ttest_ind(group_1, group_2, axis=0, equal_var=True, nan_policy='propagate', permutations=None, random_state=None, alternative='two-sided', trim=0)
    
    if test.pvalue < alpha:
        print(f"p={test.pvalue} is lower than our level of significance of {alpha}, there is evidence that the mean values across groups are not equal")
    else:
        print(f"There is no evidence to suggest that there are any differences in mean across groups, pvalue = {test.pvalue} > alpha = {alpha}")
        
## Paired T-test for (pre and post test score)      
       
    
