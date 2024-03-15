# When more than one operator appears in an expression, the order of evaluation depends on the rules of precedence.
# Python follows the same precedence rules for its mathematical operators that mathematics does.
# Parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want.
# Since expressions in parentheses are evaluated first, 2 * (3-1) is 4, and (1+1)**(5-2) is 8. You can also use
# parentheses to make an expression easier to read, as in (minute * 100) / 60: in this case, the parentheses don’t
# change the result, but they reinforce that the expression in parentheses will be evaluated first.
# Exponentiation has the next highest precedence, so 2**1+1 is 3 and not 4, and 3*1**3 is 3 and not 27. Can you
# explain why?
# Multiplication and both division operators have the same precedence, which is higher than addition and subtraction,
# which also have the same precedence. So 2*3-1 yields 5 rather than 4, and 5-2*2 is 1, not 6.
#
# Operators with the same precedence are evaluated from left-to-right. In algebra, we say they are left-associative.
# So in the expression 6-3+2, the subtraction happens first, yielding 3. We then add 2 to get the result 5. If the
# operations had been evaluated from right to left, the result would have been 6-(3+2), which is 1.


print(2 ** 3 ** 2)  # the right-most ** operator gets done first! 2^(3^2)=2^9=512
print((2 ** 3) ** 2)  # use parentheses to force the order you want! (2^3)^2=(8)^2=64

print(16 - 2 * 5 // 3 + 1)
# Following order Below
# 16 - 2 * 5 // 3 + 1
# 16 - 10 // 3 + 1
# 16 - 3 + 1
# 13 + 1 =14
# 14 is the answer

