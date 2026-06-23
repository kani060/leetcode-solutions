# There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.
    c=0
        for h in hours:
            if h>=target:
                c+=1
        return c
