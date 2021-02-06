class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_in_array = path.split('/')
        for token in path_in_array:
            if token == '' or token == '.':
                continue
            elif token == '..':
                if stack: stack.pop()
            else:
                stack.append(token)
                
        return '/' + '/'.join(stack)