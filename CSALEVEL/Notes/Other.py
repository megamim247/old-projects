#DECLARE carproc : PROCEDURE <add this too
def carproc():
    global car #Global here as well
    print(car)

#MAIN
global car #Globals like this
car="altima"

#GLOBAL AT BOTH LOCATIONS IS REQUIRED

#Question will mention what to name the file as, eg Question1_J2023

class CLASS:
    def __init__(self,Pstudents:list): #no need for Parameter to have seprate declaration statement
        #DECLARE Pstudents : ARRAY(0,10) of STRING PRIVATE  < note PRIVATE
        self.__students=Pstudents

#READING FROM FILE
#ONLY USE FOR LOOP PLS PLS PLS