"""forth.py

Implement an evaluator for a very simple subset of Forth.
"""


class StackUnderflowError(Exception):
    pass


def define_word_evaluate(input_data: list) -> list:
    if len(input_data) < 2:
        raise ValueError("illegal operation")

    define = {}
    operation = input_data.pop().lower()

    # special case
    if "+" in operation:
        line = input_data.pop()[2:-2].split()
        result = operation.replace(line[0], line[1])
        return [result]

    for chunk in input_data:
        # strip ': ... ;'
        line = chunk[2:-2].split()

        key = line[0].lower()
        value = " ".join([v.lower() for v in line[1:]])

        # update dup when key == value
        if value in define:
            define[key] = define[value]
        else:
            if key in define.keys():
                value = value.replace(key, define[key])

            define[key] = value

    # special case - avoid Raise
    result = []

    splitted = operation.split()

    if len(splitted) == 1:
        result.append(define[splitted[0]])
    else:
        if splitted[0].isdigit():
            result.append(splitted[0])
            for op in splitted[1:]:
                result.append(define[op])
        else:
            for op in splitted:
                result.append(define[op])

    r = " ".join(result)
    return [r]


def stack_size_check(num_of_stack_elems: int, needed: int) -> bool:
    """stack_size_check

    Like assert expression
    :param num_of_stack_elems: int - length stack
    :param neede: int - need length
    :return: bool
    """
    if num_of_stack_elems < needed:
        raise StackUnderflowError("Insufficient number of items in stack")
    return True


def calc_list(input_data: list) -> list:
    stack = []

    for chunk in input_data[0].split(" "):
        # operator
        if chunk in ("+", "-", "*", "/"):
            stack_size_check(len(stack), 2)

            right, left = stack.pop(), stack.pop()

            # check division by 0
            if chunk == "/" and right == 0:
                raise ZeroDivisionError("divide by zero")

            res = int(int(eval(f"{left} {chunk} {right}")))
            stack.append(res)

        elif chunk.lower() in ("over", "drop", "dup", "swap"):
            chunk = chunk.lower()

            if chunk == "over":
                stack_size_check(len(stack), 2)
                stack.append(stack[-2])

            elif chunk == "drop":
                stack_size_check(len(stack), 1)
                stack.pop()

            elif chunk == "dup":
                stack_size_check(len(stack), 1)
                stack.append(stack[-1])

            elif chunk == "swap":
                stack_size_check(len(stack), 2)
                right, left = stack.pop(), stack.pop()
                stack.append(right)
                stack.append(left)

        elif chunk.isdigit() or chunk[1:].isdigit():
            stack.append(int(chunk))

        else:
            raise ValueError("undefined operation", chunk)

    return stack


def evaluate(input_data: list) -> list:
    if ":" in input_data[0]:
        input_data = define_word_evaluate(input_data)

    return calc_list(input_data)
