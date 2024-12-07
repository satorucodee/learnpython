# String Formatting

# F-strings
# F-string allows you to format selected parts of a string
# To specify a string as an f-string, simply put an f in front of the string literal

txt = f"The price is 49 dollars"
print(txt)


# Placeholders and modifiers
# To format values in an f-string, add placeholders {}, a placeholder can contain
# variable, operation, functions, and modifiers to format the value.

price = 50
txt = f'The price is {price} dollars'
print(txt)

# a modifier is include by adding a colon : followed by legal formatting type, like
# .2f which means fixed point number with 2 decimals:

txt = f"The price is {price: .2f} dollars"
print(txt)

# You can also format a value directly without keeping it in a vairable

txt = f"The price is {95:.2f} dollars"
print(txt)

# Perform Operations in F-strings
# You can perform python operations inside the placeholders.

txt = f"The price is {20 * 59} dollars"
print(txt)

# You can perform is...else statements inside the placeholders

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

# Execute Function in F-strings

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)


#

# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding Unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format
