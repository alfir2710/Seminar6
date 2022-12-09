#2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

#[12,'sadf',5643] ---> ['sadf'] ,[12,5643]

n = input()
 
new = filter(str.isalpha, n)
print([''.join(list(new))])
new = filter(str.isdigit, n)
print([''.join(list(new))])
