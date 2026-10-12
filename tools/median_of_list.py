# tool: median_of_list
# description: Median of comma-separated numbers
# author: @00200200
# example: median_of_list "3,1,2" -> "2"

from decimal import Decimal, InvalidOperation, localcontext


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Requires exactly one argument"
    try:
        numbers = [Decimal(value.strip()) for value in args[0].split(",")]
    except InvalidOperation:
        return "Error: Expected comma-separated numbers"
    if not all(value.is_finite() for value in numbers):
        return "Error: Numbers must be finite"
    numbers.sort()
    middle = len(numbers) // 2
    if len(numbers) % 2:
        result = numbers[middle]
    else:
        lower, upper = numbers[middle - 1:middle + 1]
        # Align both coefficients and leave room for a carry and a half digit.
        precision = max(lower.adjusted(), upper.adjusted()) - min(
            lower.as_tuple().exponent, upper.as_tuple().exponent
        ) + 2
        with localcontext() as context:
            context.prec = max(context.prec, precision)
            result = (lower + upper) / 2
    if result == result.to_integral_value():
        return str(int(result))
    return format(result, "f").rstrip("0").rstrip(".")
