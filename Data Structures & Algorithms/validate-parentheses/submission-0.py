class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in s:

            if i in '{[(':
                stack.append(i)

            elif i in '})]':

                if not stack:
                    return False

                a = stack.pop()

                if (i == ')' and a != '(') or \
                   (i == ']' and a != '[') or \
                   (i == '}' and a != '{'):
                    return False

        return len(stack) == 0
