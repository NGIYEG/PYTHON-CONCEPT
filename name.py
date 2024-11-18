name='GEORGE'
career='ELECTRICIAN'
print('Hello Iam ' +name+ ' and Iam an '+career,type(name))
for n in name:
    print(n)
language=["English","Swahili","Dholuo"]
#indexes    0         1         2
print(language)
for i in language:
    print("Language:", i)
    print(language[1])#printing using index
for i in range(0):
    print(language)

count=9
while count>=3:
    print(count)
    count-=1
# count is initially defined with the value of 9. The conditional statement in the while loop is count >= 3, which is true at the initial iteration of the loop, so the loop body executes.
#Inside the loop body, count is printed and then decremented by 1.
#When the first iteration of the loop has finished, Python returns to the top of the loop and checks the conditional again. After the first iteration, count would be equal to 8 so the conditional still evaluates to True and so the loop continues.
#This continues until the count variable becomes 2. At that point, when the conditional is tested it will no longer be True and the loop will stop.

num=["2","3","4","6"]
triple=[i*3 for i in num]
#for i in num:
    #triple.append(num*2)
print(triple)

def add_num():
    print(10+7)
add_num()