def is_palindrome(string):
    if string == string[::-1]:
        return string


lst = input().split()
palindrome = input()
all_palindrome = [x for x in lst if is_palindrome(x)]
with_specified_palindrome = [x for x in all_palindrome if x == palindrome]
print(all_palindrome)
print(f"Found palindrome {with_specified_palindrome.count(palindrome)} times")
