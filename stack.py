''' stack 1'''
def solution(S):
    # Stack to keep track of opening brackets
    stack = []

    # Dictionary to map closing brackets to their corresponding opening brackets
    matching_bracket = {')': '(', '}': '{', ']': '['}

    for char in S:
        if char in matching_bracket.values():
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif stack and stack[-1] == matching_bracket[char]:
            stack.pop()
        else:
            return 0

    # If the stack is empty, all opening brackets were properly matched
    return 1 if not stack else 0


# Example usage
print(solution("{[()()]}"))  # Output: 1
print(solution("([)()]"))  # Output: 0

''' stack 2'''


def solution(A, B):
    # Stack to store the sizes of the downstream fish
    downstream_stack = []
    # Counter for the number of alive fish
    alive_fish_count = 0

    for i in range(len(A)):
        if B[i] == 1:
            # If the fish is moving downstream, push it onto the stack
            downstream_stack.append(A[i])
        else:
            # If the fish is moving upstream
            while downstream_stack:
                # Compare the upstream fish with the top of the downstream stack
                if downstream_stack[-1] < A[i]:
                    # Downstream fish gets eaten
                    downstream_stack.pop()
                else:
                    # Upstream fish gets eaten
                    break
            else:
                # If stack is empty, the upstream fish survives
                alive_fish_count += 1

    # All fish left in the stack will survive as they are all downstream fish
    alive_fish_count += len(downstream_stack)

    return alive_fish_count


# Example usage
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
print(solution(A, B))  # Output: 2

''' stack 3'''
def solution(S):
    stack = []
    for i in S:
        # if ( append
        # if ) pop
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return 0

    return 1 if not stack else 0

