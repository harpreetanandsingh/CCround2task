from prettytable import PrettyTable



class Course_Planner :
    
    
    def __init__(self):
        hello = True
        subjects = []
        links_for_notes = []
        meetlinks = []
        units = []
        self.n = len(subjects)
    
        def add_subject():
        
            self.subject = input("Enter the subject that you want to add : ")
            subjects.append(self.subject)
            if self.subject =='BioLab' or self.subject == 'ChemLab' or self.subject == 'PhyLab':
                units.append(1)
            elif self.subject =='Mathematics' or self.subject == 'Thermodynamics' or self.subject == 'GenBio':
                units.append(3)
            elif self.subject =='TRW' or self.subject == 'Workshop' :
                units.append(2)
            elif self.subject =='ComputerProg.':
                units.append(4)
                
        

        def add_notes():
            self.notes = input("Give the link for notes : ")
            links_for_notes.append(self.notes)
            self.n = len(subjects)
            
        

        def add_meetlinks():
            self.meet_links = input("Give the link for Gmeet : ")
            meetlinks.append(self.meet_links)


        def remove_sub():
            self.subject_del = input("Enter the subject to be removed : ")
            for i in range(0, len(subjects)):
                if self.subject_del != subjects[i]:
                    print("..")
                
                elif self.subject_del == subjects[i]:
                    del subjects[i]
                    del links_for_notes[i]
                    del units[i]
                    del meetlinks[i]
                    print("Subject deleted")
                    break
            
            
        def get_subinfo():
            self.n = len(subjects)
            myTable = PrettyTable(["Subject", "Units", "Notes link", "Meet link"])
            for i in range(0,self.n):
                myTable.add_row([subjects[i], units[i], links_for_notes[i], meetlinks[i]])
            print(myTable)
            
       
        def add_units():
            print("Sum of all units of subjects added : ", sum(units))


        def update_subinfo():
            for a in range (self.n):
                print(f"Subject{a+1} :" , subjects[a])
            i = int(input("Enter the subject no. for which you want to update information : "))
            z= int(input('''Enter the information that you want to update(1 or 2): 
                        1. Notes
                        2. Link for Gmeet
                        '''))
            if z == 1:
                links_for_notes[i-1] = input("Enter the updated link for notes : ")
            elif z == 2:
                meetlinks[i-1] = input("Enter the updated link for gmeet : ")
    
        self.hello = True
        self.links_for_notes = links_for_notes
        
        
        while self.hello:
        
    
            print('''Kindly tell what you want to do by entering the interger corresponding to your choice:
           1. Add Subject
           2. Remove Subject
           3. Update Subject information
           4. Get info regarding courses
           5. Total units
           6. Exit the program
            ''')
            x = int(input())
            if x == 1:
                print('''Following are the subjects that are available for this semester :
                    Subject                Units
                    1. BioLab                 1
                    2. GenBio                 3
                    3. Thermodynamics         3
                    4. TRW                    2
                    5. ChemLab                1
                    6. ComputerProg.          4
                    7. Mathematics            3
                    8. Workshop               2
                    9. PhyLab                 1      ''')
                
                add_subject()
                self.n = len(subjects)
                y = input('''Do you want to add notes link for the course?(y/n)''' )
                if y == 'y':
                    add_notes()
                    
                elif y == 'n':
                    links_for_notes.append("NA")
                
                q = input('''Do you want to add google meet link for the course?(y/n)''' )
                if q == 'y':
                    add_meetlinks()
                    
                elif q == 'n':
                    meetlinks.append("NA")
               
        

            elif x == 2:
                remove_sub()

            elif x == 3:
                update_subinfo()
                
            elif x == 4:
                get_subinfo()
            
            elif x== 5:
                add_units()
    
            elif x == 6:
                print("Thanks for accessing the course planner.Have a nice day!!!")
                self.hello = False
            
h = input('''Welcome to the Course Planner!!! Do you want to enter? (y/n)''' )

if h == 'y':
    Course_Planner()
elif h == 'n':
    print("Have a nice day!!!")
else:
    print("Invalid response!!! Kindly restart the application...")