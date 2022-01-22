
def search(n1,n2):
    if n2 in n1:
        return "word is found"
    else:
        return "not found"

send=input("enter word")
word=input("enter word")
print(search(send,word))