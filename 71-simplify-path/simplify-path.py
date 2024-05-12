class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path)==1:
            return "/"
        stack = []
        path_list = path.split("/")
        for i in path_list:
            if i=="..":
                if stack:
                    stack.pop()
            elif i=="." or not i:
                continue
            else:
                stack.append(i)
        final = "/"+"/".join(stack)
        return final
