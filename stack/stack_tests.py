from stack import Stack
from expression_validator import ExpressionValidator


def stack_test():
    stack = Stack(5)

    stack.stack_up(1)
    stack.stack_up(2)
    stack.stack_up(3)
    stack.stack_up(4)
    stack.stack_up(5)
    stack.stack_up(6)

    print('---')
    value = stack.unstack()
    print(value)
    stack.unstack()
    stack.unstack()
    value = stack.unstack()
    print(value)
    stack.unstack()
    stack.unstack()


def validate_expression_test():
    expression = 'c[d]'
    print(ExpressionValidator.validate(expression))
    expression = 'a{b[c]d}e'
    print(ExpressionValidator.validate(expression))
    expression = 'a{b[c(d)e]f}g'
    print(ExpressionValidator.validate(expression))
    expression = 'a{b(c]d}e'
    print(ExpressionValidator.validate(expression))
    expression = 'a[b{c}d]e}'
    print(ExpressionValidator.validate(expression))
    expression = 'a{b(c)'
    print(ExpressionValidator.validate(expression))


if __name__ == '__main__':
    # print('STACK TEST')
    # print('------------------------')
    # stack_test()

    print()
    print('VALIDATE EXPRESSION TEST')
    print('------------------------')
    validate_expression_test()
