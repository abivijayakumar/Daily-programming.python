def is_palindrome(s):
  s = s.replace(" " , " ").lower()
  if s == s[: : -1]:
    return "Palindrome"
  else:
    return "Not Palindrome"
    s = input().strip()
    print(is_palindrome(s))
