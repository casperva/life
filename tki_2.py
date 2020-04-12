from tkinter import *
import numpy as np
import random

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.init_menu()

        #Creation of init_window


    def init_window(self):

        # changing the title of our master widget
        self.master.title("Life")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


    def init_menu(self):
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Settings", command=self.client_exit)
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="Menu", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="About")

        #added "file" to our menu
        menu.add_cascade(label="About", menu=edit)

    def client_exit(self):
        exit()

class Life:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.organism =np.zeros((i,j), dtype=int)


    def random_organism(self, probability):
        for i in range(1,len(self.organism[:,1])-1):
            for j in range(1,len(self.organism[1,:])-1):
                if (random.randint(0,100) < probability):
                    self.organism[i,j] = 1

    def out(self, print_method):
        print(self.organism)

    def count_living_cells(self):
        living_cells = 0
        for i in range(0,len(self.organism[:,1])):
            for j in range(0,len(self.organism[1,:])):
                if self.organism[j,i] > 0:
                    living_cells += 1
        return living_cells

    def calc_next_generation(self):
        old_organism = np.copy(self.organism)
        neig =np.zeros((self.x,self.y), dtype=int)
        test = np.zeros((self.x,self.y), dtype=int)


        for j in range(1,len(old_organism[:,1])-1):
            for i in range(1,len(old_organism[1,:])-1):
                neighbours = 0
                if old_organism[i-1,j-1] > 0: neighbours += 1
                if old_organism[i+1,j-1] > 0: neighbours += 1
                if old_organism[i  ,j-1] > 0: neighbours += 1
                # print(neighbours)
                if old_organism[i,j-1]   > 0: neighbours += 1
                if old_organism[i,j+1]   > 0: neighbours += 1

                if old_organism[i-1,j+1] > 0: neighbours += 1
                if old_organism[i,  j+1] > 0: neighbours += 1
                if old_organism[i+1,j+1] > 0: neighbours += 1
                # print(neighbours)
                # print('['+str(i)+']'+'['+str(j)+']:'+ str(neighbours_up) + '+' + str(neighbours_line) + '+' + str(neighbours_down))   #str(old_organism[i,j]))
                neig[i,j] = neighbours
                test[i,j] = i # (5*i) + j
                # print(i,j, neighbours)
                if (neighbours == 2) and (self.organism[i,j] > 1):
                    self.organism[i,j] = 1
                elif neighbours == 3:
                    self.organism[i,j] = 1
                else:
                    self.organism[i,j] = 0
        print(' --- neighbours -----------')
        print(neig)
    #    print(test)




root=Tk()
root.geometry("400x300")

app=Window(root)
lf = Life(6,6)
lf.random_organism(50)
print(' --- organism -----------')
print(lf.organism)
print("Number of living cells: " + str(lf.count_living_cells()))
lf.calc_next_generation()
print(' --- organism -----------')
print(lf.organism)
print("Number of living cells: " + str(lf.count_living_cells()))
#print(lf.organism)
#print("Number of living cells: " + str(lf.count_living_cells()))

# root.mainloop()
