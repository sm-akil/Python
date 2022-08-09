from collections import deque

if __name__ == '__main__':

    stack = deque()

    print('Inserting A into the stack…')
    stack.append('A')

    print('Inserting B into the stack…')
    stack.append('B')

    print('Inserting C into the stack…')
    stack.append('C')

    print('Inserting D into the stack…')
    stack.append('D')

    print('Top element is', stack[-1])  # prints the stack's top (D)

    print(f'Removing {stack.pop()} from the stack')  # removing the top element (D)
    print(f'Removing {stack.pop()} from the stack')  # removing the next top (C)

    # returns the total number of elements present in the stack
    print('The stack size is', len(stack))

    print(f'Removing {stack.pop()} from the stack')  # removing the top element (B)
    print(f'Removing {stack.pop()} from the stack')  # removing the next top (A)

    # check if the stack is empty
    if len(stack) == 0:
        print('The stack is empty')
    else:
        print('The stack is not empty')