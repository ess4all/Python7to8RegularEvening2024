Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = ("id","name")
>>> y = (101,"rahul")
>>> z = {x:y  for i in zip(x,y)}
>>> z
{('id', 'name'): (101, 'rahul')}
>>> z = {x:y  for x,y in zip(x,y)}
>>> z
{'id': 101, 'name': 'rahul'}
>>> 
>>> x
('id', 'name')
>>> y
(101, 'rahul')
>>> list(zip(x,y))
[('id', 101), ('name', 'rahul')]
>>> 
x = [('id', 101), ('name', 'rahul')]
y,z=x
y
('id', 101)
z
('name', 'rahul')
y,z = list(x)
y
('id', 101)



x
[('id', 101), ('name', 'rahul')]
y
('id', 101)


x
[('id', 101), ('name', 'rahul')]
list(y),list(z)=x
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?

x
[('id', 101), ('name', 'rahul')]
y,z = [],[]

x
[('id', 101), ('name', 'rahul')]
y = [i for i in x[0]]
z = [i for i in x[1]]
y
['id', 101]
z
['name', 'rahul']
