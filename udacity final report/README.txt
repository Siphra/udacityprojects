Dataset : Loan Data from Prosper set from 2007 - 2014

Abstract :

I took a dive into the Loan Data from Prosper set to look for impacts on 
the effective yield, I Identified two variables that had high correlation with it.


Main Findings:

Higher credit risk leads to overall higher expected yield in each loan.
This is of course due directly to the fact that APRs are higher on more risky loans.
What's surprising about this is that these more risky loans are not supported by a robust
number of investors, but rather by relatively few taking on the risk themselves. 
While the more stable loans tend to have more individual backers. Interestingly, a linear
regression shows that that people with No Credit, combRating = NC, are the only group
for which the expected yield is lower when compared to the best credit Rating, combRating = AA
We've seen that the other credit ratings all have a positive correlation, the yields are
expected to get larger with a modest gain in each group, which is almost linear in 
nature.


FeedBack:


Resources:
https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html
https://seaborn.pydata.org/tutorial/categorical.html

