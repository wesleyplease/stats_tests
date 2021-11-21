## mann-whitney u test is used to identify differences in independent samples
import math
import pandas as pd
import numpy as np

# a = [82,76,99,50,7,84,89,100,96,82,75,72]
# b = [79,88,100,60,35,83,92,100,93,87,70,79]
a = [1, 2, 1, 4, 2]
b = [2, 2, 6, 4, 5]
crit = 2

def mann_whit_u(a, b, m_w_critical=0):
    a = a
    b = b

    a_var = ["a" for i in a] # create a list to keep track of my a's
    b_var = ["b" for i in b] # create a list to keep track of my b's

    n_a = len(a)
    n_b = len(b)
    n = n_a + n_b

    coded_frame = pd.DataFrame(zip(a + b, a_var + b_var))
    ranked_coded_frame = coded_frame.sort_values(by=[0])
    ranked_coded_frame[2] = np.arange(1, n+1)
    print(ranked_coded_frame)

    null_hypothesis = "there is no tendency of the ranks of one method to be systematically" \
                      " different than one another"
    alternative_hypothesis = "the ranks of one method are systematically different from one another"

    ## Now add up all the ranks of each group
    a_frame = ranked_coded_frame[ranked_coded_frame[1]=='a'] # df with only a values and ranks
    b_frame = ranked_coded_frame[ranked_coded_frame[1]=='b'] # df with only b values and ranks

    a_rank_sum = sum(a_frame[2]) # sum of a ranks
    b_rank_sum = sum(b_frame[2]) # sum of b ranks


    U_a = n_a * n_b + (n_a *(n_a + 1))/2 - a_rank_sum
    U_b = n_a * n_b + (n_b *(n_b + 1))/2 - b_rank_sum

    m_w_tstat = min(U_b,U_a)
    print(m_w_tstat)

    ## use mann-whitney table of critical values on the count of 1 sample (not both)
    ## on 7 with alpha at 0,05 = 8 = mann-whitney critical

    mean = (n_a * n_b)/2
    sd = math.sqrt((n_a * n_b * (n_a + n_b + 1))/12)
    z = (m_w_tstat - mean)/sd
    # small: 0.1; medium: 0.3; large: 0.5
    effect_size = abs(z)/n

    ###
    m_w_critical = m_w_critical      # find an easier approach to finding the mann whitney critical value
    ###

    ##  RESPONSE and CONCLUSIONS
    print("######## CONCLUSIONS: #########")
    if m_w_critical >= m_w_tstat:
        print(f"Since {m_w_critical} >= {m_w_tstat}, We must reject the null hypothesis that {null_hypothesis}")
        print(f"There is evidence to support that {alternative_hypothesis}")
    elif m_w_critical == 0:
        print("please look up your critical value")
    else:
        print(f"since {m_w_critical} < {m_w_tstat} there is insufficient evidence to reject the null hypothesis: {null_hypothesis}")

    print("Effect size: " + str(effect_size) + "; (small: 0.1; medium: 0.3; large: 0.5)")

mann_whit_u(a, b, crit)

