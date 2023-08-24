t=tuple(1,2,3)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: tuple expected at most 1 argument, got 3
t=(1,2,3)
t
(1, 2, 3)
t[1]
2
t[2]
3
t[3]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: tuple index out of range
t_new=(t[0],0,t[2])
t
(1, 2, 3)
t_new
(1, 0, 3)
l=[1,2,3]
l
[1, 2, 3]
l[1]
2
l[1]=0
l
[1, 0, 3]
l.append(4)
l
[1, 0, 3, 4]
l=l+[5,6]
l
[1, 0, 3, 4, 5, 6]
l.append(9)
l
[1, 0, 3, 4, 5, 6, 9]
l.extend([7,8])
l
[1, 0, 3, 4, 5, 6, 9, 7, 8]
l[0:5]
[1, 0, 3, 4, 5]
t[0:2]
(1, 2)
l[:5]
[1, 0, 3, 4, 5]
t = tuple( l )
l
[1, 0, 3, 4, 5, 6, 9, 7, 8]
t
(1, 0, 3, 4, 5, 6, 9, 7, 8)
l_new=list( t )
l_new
[1, 0, 3, 4, 5, 6, 9, 7, 8]
t
(1, 0, 3, 4, 5, 6, 9, 7, 8)
list(t)[1]=2
t
(1, 0, 3, 4, 5, 6, 9, 7, 8)
t)list(t)
  File "<input>", line 1
    t)list(t)
     ^
SyntaxError: unmatched ')'
t=list(t)
t
[1, 0, 3, 4, 5, 6, 9, 7, 8]
t[1]=2
t
[1, 2, 3, 4, 5, 6, 9, 7, 8]
t=tuple(t)
t
(1, 2, 3, 4, 5, 6, 9, 7, 8)
d={}
d
{}
type( d )
<class 'dict'>
d=dict()
d
{}
d={ "Name": "Berçin","LastName":"Sönmez"}
d["Name"]
'Berçin'
d["LastName"]
'Sönmez'
d={3:5}
d
{3: 5}
d[3]
5
d={"3'";"5'","A":"T"}
  File "<input>", line 1
    d={"3'";"5'","A":"T"}
           ^
SyntaxError: invalid syntax
"hello world" [-1:-1:1-]
"hello world" [-1::-1]
  File "<input>", line 1
    "hello world" [-1:-1:1-]
                           ^
SyntaxError: invalid syntax
"hello world" [-1::-1]
'dlrow olleh'