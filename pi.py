# Calculating Pi Using an Infinite Series


#1 Use the Gregory-Leibniz series. Mathematicians have found several different mathematical series that, if carried out infinitely, will accurately calculate pi to a great number of decimal places. Some of these are so complex they require supercomputers to process them. One of the simplest, however, is the Gregory-Leibniz series. Though not very efficient, it will get closer and closer to pi with every iteration, accurately producing pi to five decimal places with 500,000 iterations.[4] Here is the formula to apply.
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
# Take 4 and subtract 4 divided by 3. Then add 4 divided by 5. Then subtract 4 divided by 7. Continue alternating between adding and subtracting fractions with a numerator of 4 and a denominator of each subsequent odd number. The more times you do this, the closer you will get to pi.


# 2 Try the Nilakantha series. This is another infinite series to calculate pi that is fairly easy to understand. While somewhat more complicated, it converges on pi much quicker than the Leibniz formula.[5]
# π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14) ...
# For this formula, take three and start alternating between adding and subtracting fractions with numerators of 4 and denominators that are the product of three consecutive integers which increase with every new iteration. Each subsequent fraction begins its set of integers with the highest one used in the previous fraction. Carry this out even a few times and the results get fairly close to pi.

def chi(x):
	return [0, 1, 0, -1][x % 4]

def nilakantha(n):
	return 3 + 4 * sum(chi(n) / ((n + 1) * (n + 2) * (n + 3)) for n in range(1, n + 1))


# The Wallis Formula
# π/2 = (2/1)(2/3)(4/3)(4/5)(6/5)(6/7) = product((2*k)/(2*k-1)*(2*k)/(2*k+1) for k in range(1,inf))



# sin(x) = x - x**3/3! + x**5/5! - x**7/7! + ...
