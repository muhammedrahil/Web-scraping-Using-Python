print(__name__)
import pickle

my_list=['hello','how are you ','iam fine']
save_file=open("save.txt",'wb')
pickle.dump(my_list,save_file)
save_file.close()

load=open('save.txt','rb')
load_data=pickle.load(load)
load.close()
print(load_data)



import os
class Contact:

    def __init__(self,name,email,massages):
        self.name =name
        self.email=email
        self.massages=massages

    def save(self,filename):
        file = open(filename,"a")
        file.write("Name :"+self.name+"\n")
        file.write("Email :"+self.email+"\n")
        file.write("Massages :"+self.massages+"\n")
        file.close()

    def read(self,filename):
        file = open(filename,"r")
        read =file.read()
        print(read)
        file.close()

    def deletecontent(self,filename):
        file = open(filename, "w")
        file.write("")
        file.close()

    def delete(self,filename):
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print("this file does'nt exist")


person1=Contact("muhammed Rahil","mrahil7510@gmail.com","nothing")

# person1.save("person1.txt")
# person1.read("person1.txt")
# person1.deletecontent("person1.txt")
# person1.delete("person1.txt")