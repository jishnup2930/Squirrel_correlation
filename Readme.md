Overview
This project analyzes a journal kept by Scott, a boy who experiences unexplained squirrel transformations on some nights. The goal is to identify which activities are most correlated with the transformation. The analysis is based on the mathematical concept of correlation.

Journal Data
The journal data is stored in a file named journal.json, containing entries for each day of three months. Each entry looks like this:

json
Copy code
{
  "events": [
    "carrot",
    "exercise",
    "weekend"
  ],
  "squirrel": false
}
This indicates the activities Scott engaged in on a particular day, along with whether or not he transformed into a squirrel.

Mathematical Background
Correlation measures the degree of association between two variables. In this case, let's assume the variables can be either True or False. The correlation (ϕ) ranges from -1 to +1, representing perfect negative and positive correlations respectively.

Formula
The correlation (ϕ) is calculated using the following formula:

scss
Copy code
ϕ = (n₁₁ * n₀₀ - n₁₀ * n₀₁) / sqrt(n₁₊ * n₀₊ * n₊₁ * n₊₀)
Where:

n₁₁: Number of times both variables were True
n₀₀: Number of times both variables were False
n₁₀: Number of times first variable was True, second was False
n₀₁: Number of times first variable was False, second was True
n₁₊: Number of times first variable was True regardless of second variable
n₀₊: Number of times first variable was False regardless of second variable
n₊₁: Number of times second variable was True regardless of first variable
n₊₀: Number of times second variable was False regardless of first variable
Example
Consider the following data:

r
Copy code
| X | Y |
|---|---|
| T | T |
| T | F |
| T | T |
| F | T |
| F | T |
| T | F |
| F | F |
Calculating the correlation:

scss
Copy code
ϕ = (2 * 1 - 2 * 2) / sqrt(4 * 3 * 4 * 3)
   = (2 - 4) / sqrt(144)
   = -2 / 12
   = -0.1667
This indicates a slight negative correlation.




