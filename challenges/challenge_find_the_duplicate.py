def find_duplicate(nums):
    numeros_vistos = set()

    for number in nums:
        if isinstance(number, str):
            return False
        if number < 1:
            return False
        if number in numeros_vistos:
            return number
        else:
            numeros_vistos.add(number)

    return False
