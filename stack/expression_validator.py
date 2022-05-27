from stack import Stack


class ExpressionValidator:

    @staticmethod
    def validate(expression):
        is_valid = True
        expression_size = len(expression)
        character_stack = Stack(expression_size)

        for i in range(expression_size):
            character = expression[i]
            if character == '{' or character == '[' or character == '(':
                character_stack.stack_up(character)
            elif character == '}' or character == ']' or character == ')':
                if not character_stack.is_empty():
                    open_character = character_stack.unstack()
                    if ((open_character == '{' and character != '}') or
                        (open_character == '[' and character != ']') or
                        (open_character == '(' and character != ')')):
                        print('Error: ', character, ' in the position ', i)
                        is_valid = False
                        break
                else:
                    print('Error: ', character, ' in the position ', i)
                    is_valid = False
        if not character_stack.is_empty():
            print('Error!')
            is_valid = False

        return is_valid
