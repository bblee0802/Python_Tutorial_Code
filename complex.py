
f= open('note.txt', 'a+')
f.write("Hi")
print(f.read())

users = {'kim':'password', 'sun80':'qwrt1234', 'hjwik': '90123qw'}

f = open('users.txt','r')
wf = open("tete.txt","wb")
import pickle as pk
pk.dump(users,wf)
f.close()
wf.close()