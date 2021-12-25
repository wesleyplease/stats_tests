def which_test():
    num_y = int(input("How many dependent variables do you have?"))

    print("stored...")
        
        
        
    print("what is the nature of your independent variables?")

    nat_x_options = ["0 independent variables (1 population)",
            "1 IV with 2 levels (independent groups)",
            "1 IV with 2 or more levels (independent groups)",
            "1 IV with 2 levels (dependent/matched groups)",
            "1 IV with 2 or more levels (dependent/matched groups)",
            "1 interval IV",
            "1 or more interval IV's and 1 or more categorical IV's",
            "1 IV with 2 or more levels (independent groups)"
            ]

    # Print out your options
    for i in range(len(nat_x_options)):
        print(str(i+1) + ":", nat_x_options[i])
        
    # Take user input and get the corresponding item from the list
    nat_x = int(input("Enter a number: "))
    if nat_x in range(1, len(nat_x_options)+1):
        nat_x = nat_x_options[nat_x-1]
    else:
        print("Invalid input!")

    print("stored...")




    print("What is the nature of your dependent vaiables?")

    nat_y_options = ["interval and normal",
                    "ordinal or interval",
                    "categorical with 2 categories",
                    "categorical"    
                ]    
        
    # Print out your options
    for i in range(len(nat_y_options)):
        print(str(i+1) + ":", nat_y_options[i])
        
    # Take user input and get the corresponding item from the list
    nat_y = int(input("Enter a number: "))
    if nat_y in range(1, len(nat_y_options)+1):
        nat_y = nat_y_options[nat_y-1]
    else:
        print("Invalid input!")

    print("stored...")

    print("processing...")
    
    print(f" you have {num_y} independent variable(s), with their nature being {nat_y}, and your dependent variables are {nat_x}")
    
    if num_y < 2:
        
        
        if nat_x == nat_x[0]:
            
            if nat_y == nat_y[0]:
                print("one-sample t-test")
            elif nat_y == nat_y[1]:
                print("one-sample median")
            elif nat_y == nat_y[2]:
                print("binomial test")
            elif nat_y == nat_y[3]:
                print("Chi-sq goodness of fit")
                
        elif nat_x == nat_x[1]:
            
            if nat_y == nat_y[0]:
                print("2 independent sample t-test")
            elif nat_y == nat_y[1]:
                print("Wilcoxon-Mann-Whitney")
            elif nat_y == nat_y[2] or nat_y[3]:
                print("Chi-sq test or Fisher Exact test")
        
        elif nat_x == nat_x[2]:
            
            if nat_y == nat_y[0]:
                print("One-way ANOVA")
            elif nat_y == nat_y[1]:
                print("Krusjal Walis")
            elif nat_y == nat_y[2] or nat_y[3]:
                print("Chi-sq test")
                
        elif nat_x == nat_x[3]:
            
            if nat_y == nat_y[0]:
                print("paired t-test")
            elif nat_y == nat_y[1]:
                print("Wilcoxon SR test")
            elif nat_y == nat_y[2] or nat_y[3]:
                print("McNemar")    
            
        elif nat_x == nat_x[4]:
            
            if nat_y == nat_y[0]:
                print("one-way repeated measures ANOVA")
            elif nat_y == nat_y[1]:
                print("Friedman test")
            elif nat_y == nat_y[2]:
                print("factorial logistic regression")
            elif nat_y == nat_y[3]:
                print("factorial logistic regression")
        
        elif nat_x == nat_x[5]:
            
            if nat_y == nat_y[0]:
                print("correlation or SLR")
            elif nat_y == nat_y[1]:
                print("non-parametric correlation")
            elif nat_y == nat_y[2] or nat_y[3]:
                print("simple logistic regression")
                
        elif nat_x == nat_x[6]:
            
            if nat_y == nat_y[0]:
                print("Multiple regression or ANCOVA")
            elif nat_y == nat_y[2] or nat_y[3]:
                print("multiple logistic regression or discriminant analysis")
    
    elif num_y >= 2:
        
        print("Your options: \n one-way MANOVA \n multivariate multiple linear regerssion \n factor analysis \n canonical correlation for 2 sets of 2+")
                  
which_test()    
