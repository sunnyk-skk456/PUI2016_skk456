##HW4_1
###CitibikeReview_hc1924 to skk456

##IDEA: Usage of citi bikes goes low during the winter time.


## a) NULL HYPOTHESIS
### There is no difference in the average trip duration of subscribers in summer months as compared to the winter months.

## a)Comments on the  NULL HYPOTHESIS
I believe the NULL Hypothesis responds to the IDEA. In winter people are less likely to use citibikesd than summer time in terms of frequency. The weather is too cold to ride in open air, and the road condition may cause higher risk of accidents, especially in areas of frequent snow. But I am curious about the average duration time you are using to do the research, which makes it even interesting and the results less so obvious.

##The alternative hypothesis is correctly stated for your given Null Hypothesis

## b)The data was correctly proccesed and the columns duration is fine to answer the question.
But I am not sure about using the np.abs(stats.zscore(summer_dur)) < 3) is the right way to do the Z-test. And we don't see a p-value output to do the decision (reject the null hypothesis or not). The data you are using is well chosen, the graph is very intuitive to show the difference between the two groups.

## c) t-Test

##I would recommend t-Test because the indpendent variable (average duration time) is continuous and the dependent variable (time of the year) is dichotomous, and most critically, you are tesing if there is difference between two groups on one DV. That's when you use a t-test.
