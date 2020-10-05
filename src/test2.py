def validParenthesesSequence(s):
    s = list(s)
    close_paren = 0
    open_paren = 0
    for i in s:
        if i == "(":
            open_paren += 1
        if i == ")":
            close_paren += 1
    if s[0] == "(" and s[len(s) - 1] == ")":
        if open_paren == close_paren:
            print(s[0])
            print(len(s) - 1)
            return True
        else:
            return False


print(validParenthesesSequence("()()(())"))
