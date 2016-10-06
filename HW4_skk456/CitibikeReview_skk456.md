Assignment 1: Review classmate's Citibike project proposal

Hello Franz,

Below is my peer review for your CitiBike assignment.

a. You formulated the question - How is the new bus route for X8 improving commute times? From your Null Hypothesis, I understand you are trying to evaluate if the new route for Bus X8 takes less time, on average compared to it's old route. Hence, I would suggest to change your question from How to Does the new bus route for X8 has improved average commute time, compared to it's older route. As I understand we are not trying to identify the reasons i.e. the How part when comparing the commute timing. I see that you have correctly formulated the Null and Alternate Hypothesis and also listed the Confidence level - Alpha to 5% I suggest re-wording the Null Hypothesis to have more clarity -
Null Hypothesis - The mean commute time for the new bus route (TimeNew.mean()) is the same or longer than mean commute time for the old bus route (TimeOld.mean()) for bus number X8.

A minor suggestion to follow the convention for your Null and Alternate Hypothesis equations.

  H0: TimeNew.mean() >= TimeOld.mean()

  Ha: TimeNew.mean() < TimeOld.mean()

These changes are to state the hypothesis with best clarity.

b. The data you chose supports your project and you also chose the correct variables to answer your question. It is useful to see that you have added good comments and markdown statments with mathematical equations to understand the formula used to calculate the Z Score. You have added appropriate comments throughtout the code to make it self explanatory and also followed the PEP8 compliance for coding.

c. For your research project -
  - Independent Variable (IV) is Bus Route, which is categorical in nature and
  - Dependent Variable (DV) is Time, which is continuous in nature. 
  As you have 1 categorical IV and 1 continuous DV, I recommend you to use the ANOVA Inferential Statistical Tests. 
  If a Control Variable is added to your research and data scope, ANCOVA test would be a better fit.

Good Luck!

Best, 
Sunny.