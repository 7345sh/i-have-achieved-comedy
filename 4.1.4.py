str = input()

def palindrome():

    if str == str[::-1]:
        return True
    else: return False

res = palindrome()
print(res)