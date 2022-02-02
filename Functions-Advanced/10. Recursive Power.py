def recursive_power(base, exponent):
    if exponent == 1:
        print(f'base={base}', f'exponent={exponent}', f'result={base}')
        return base
    result = base * recursive_power(base, exponent - 1)
    print(f'base={base}', f'exponent={exponent}', f'result{result}')
    return result


print(recursive_power(2, 3))
