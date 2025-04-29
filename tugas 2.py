print ("lalu ilham wira sakti  242421121")
inputuser = int(input("masukkan bilangan antara 24 atau lebih dari 21"))

#+++++24------------
#memeriksa angka yang kurang dari 24
iskurangdari = (inputuser <24)

#memeriksa angka yang kurang dari 21
islebihdari = (inputuser <21)

final = iskurangdari or islebihdari
print("angka yang anda masukan", final)