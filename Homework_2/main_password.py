# Charlotte Carbaugh, Student ID 1815532

weak_pass = str(input())
end = 'q*s'
password_parts = []


weak_pass = weak_pass.replace('i', '!')
weak_pass = weak_pass.replace('a', '@')
weak_pass = weak_pass.replace('m', 'M')
weak_pass = weak_pass.replace('B', '8')
weak_pass = weak_pass.replace('o', '.')

password_parts.append(weak_pass)
password_parts.append(end)

password = ''.join(password_parts)

print(password)
