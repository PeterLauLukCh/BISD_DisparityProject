# Calculation Result of Ranking-based BISD Model

The project is primarily based on the result from Dr. Philip Greengard and Dr. Andrew Gelman's research *BISG: When inferring race or ethnicity, does it matter that people often live near their relatives?* (https://arxiv.org/pdf/2304.09126.pdf). 

The objective of this project is to calculate disparity using the results from Bayesian Geocoding (BISD). Through BISD, given the surname and geological information of a specific person, we can determine the probability that this person belongs to a specific race. To estimate the number people in certain race, $N$, we need to find the probability of $Pr(N=n)$ using the result above. Considering following example, given voters set ${x_{1},x_{2},x_{3},...,x_{n}}$, where $x_{i}$ represents the $i^{th}$ voter, we denote the probability that the $i^{th}$ voter belongs to white as $Pr(x_{i} = W)$. $Pr(N=n)$ can be modelled via the poisson binomial distribution. 

However, due to the time complexity, poisson binomial distribution cannot be used to deal with the high-volume dataset, which makes us to approximate it into a easy-dealing continuous distribution. 
