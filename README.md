# Calculation Result of Ranking-based BISD Model

The project is primarily based on the result from Dr. Philip Greengard and Dr. Andrew Gelman's research *BISG: When inferring race or ethnicity, does it matter that people often live near their relatives?* (https://arxiv.org/pdf/2304.09126.pdf), aiming to estimate the specific number of voters in each race.

Through the ranking-based BISD model, given a person's family name and geolocation information, we can calculate the probability of this person's ethnicity. For example, with the information of person $x$'s surname and home location, we can calculate $Pr(x$ is White), $Pr(x$ is Asian), $Pr(x$ is Black), and so on. Consider a set of voters $X$, which contains $x_{1}, x_{2}, ..., x_{n}$, the estimated number of Whites would be:

<p align="center">
$\text{Num of White} = E(x_1 \text{ is white}) + E(x_2 \text{ is white}) + \ldots + E(x_n \text{ is white})$
</p>

<p align="center">
$\text{Num of White} = Pr(x_1 \text{ is white}) + Pr(x_2 \text{ is white}) + \ldots + Pr(x_n \text{ is white})$
</p>

Now, given a set of surnames $Y$, which contains $y_{1}, y_{2}, ..., y_{n}$, each $y_{i}$ contains its frequency, $fr(y_{i})$, and the corresponding probability of being each race. Therefore,

<p align="center">
$\text{Num of White} = fr(y_{1})\cdot Pr(y_1 \text{ is white}) + fr(y_{2})\cdot Pr(y_2 \text{ is white}) + \ldots + fr(y_{n})\cdot Pr(y_n \text{ is white})$
</p>

Calculation procedures are in Calculation.py and results is in results.txt
