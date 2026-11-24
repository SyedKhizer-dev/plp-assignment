from typing import Optional
import logging


def safe_divide(divident: float, divisor: float) -> Optional[float]:
    """
    The function returns the Quotient by dividing two numbers(divident and divisor).

    Args:
        divident (float): Divident
        divisor (float): Divisor

    Returns:
        Optional[float]: Quotient

    Raises:
        ZeroDivisionError: If the divisor is zero.
        TypeError: If the input is not a integer value.
    """
    try:
        return divident / divisor
    except ZeroDivisionError:
        print("Divisor cannot be zero.")
        return None
    except TypeError:
        print("The input must be an integer value.")
        return None


def batch_divide(pairs: list[tuple]) -> list[float]:
    """
    Performs division on multiple numbers.

    Args:
        pairs (list[tuple]): A list of tuples containing dividend and divisor.

    Returns:
        list[float]: A list of successful division results.
    """

    results = []

    for divident, divisor in pairs:
        result = safe_divide(divident, divisor)

        if result is not None:
            results.append(result)
        else:
            logging.warning("Skipping invalid division: %s/%s", divident, divisor)

    return results


pairs = [(10, 2), (6, 0), (9, 3), ("hello", 43)]

print(batch_divide(pairs))
