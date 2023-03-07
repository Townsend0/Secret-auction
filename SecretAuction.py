import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
c=True
a=[]
while c:
    print(f"Welcome to the secret auction program.\n{logo}")
    a.append({
        0: input("\nWhat's your name:? "),
        1: float(input("What's your bid:? $"))
    },)
    e=True
    while e:
        d=input("\nare there any other bidders? type 'yes' or 'no': ").lower()
        if d=='yes' or d=='no':
            e=False
    if d=='no':
        c=False
    else:
        os.system("clear")
d=a[0][1]
for c in range(len(a)):
    if d<a[c][1]:
        d=a[c][1]
        e=a[c][0]
os.system("clear")
print(f"\nthe winner is {e} with a bid of ${d}.")