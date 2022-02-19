"""
We have m completely wet clothes out under sunshine waiting to become dry. we are now at second and it's raining. It's going to rain again on seconds t2 ... tn and after each rain clothes will be completely wet again. Cloth number i needs a(i) seconds to become dry. We can go out and collect all dry clothes at any moment but can't do this more than g times. What is the maximum number of clothes we can collect until second t(n)? Note that the duration of each rain is almost zero, so we can ignore it. Also collecting clothes does not take any time from us.

**  Input format    **
First line of input contains three integers n, m, g(2 <=n <= 100, 1 <= m, g <= 100) respectively. In the second line will be n increasing numbers denoting t1 ... tn (0 <= t1 < ... < tn < 10^4). In the Last line will have m numbers denoting a1 ... a(m) (1 <= a(i) <= 10000 ).

**  Output format   **
In a single line print maxmimum number of clothes we can collect.

SAMPLE INPUT
3 3 2
3 5 8
4 1 3

SAMPLE OUTPUT
2

Explanation
In the sample, first we go outside at time 5(exactly before rain) and take second piece of clothes. Then for the second time, at second 8, we go and take third piece.
"""

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))
m = 0
for i in range(1,len(l2)):
  m = max(m,abs(l2[i-1]-l2[i]))
  c=0
  for j in l3:
      if j <=m and l1[2]!=0:
          c = c+1 
print(c) 
