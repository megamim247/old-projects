class Picture:
    def __init__(self,PDescription:str,PWidth:int,PHeight:int,PFrameColour:str):
        #DECLARE Width, Height : INTEGER PRIVATE
        #DECLARE Description, FrameColour : STRING PRIVATE
        self.__Description=PDescription
        self.__Width=PWidth
        self.__Height=PHeight
        self.__FrameColour=PFrameColour
    
    def Getdescription(self):
        return self.__description
    
    def GetHeight(self):
        return self.__Height
    
    def GetWidth(self):
        return self.__Width
    
    def GetColour(self):
        return self.__Colour
    
    def SetDescription(self,PDescription:str):
        self.__Description=PDescription

def ReadData():
    #DECLARE Line : STRING
    #DECLARE Count : INTEGER
    #DECLARE Width, Height : INTEGER 
    #DECLARE Description, FrameColour : STRING 
    global PictureArray #BYREF
    Count=0
    try:
        file=open("Pictures.txt")
        while Line!="":
            Line=file.readline()
            if Count%4==0:
                Description=Line.strip()
            if Count%4==1:
                Width=Line.strip()
            if Count%4==2:
                Height=Line.strip()
            if Count%4==3:
                PictureArray[Count//4]=Picture(Description,Width,Height,Line.strip())
    except IOError:
        print("file not real")

#MAIN
#DECLARE PictureArray : ARRAY(0,99) of Picture
global PictureArray #BYREF
PictureArray=[Picture("",0,0,"") for n in range(0,100)]
ReadData()
#DECLARE UserColour : STRING
#DECLARE UserWidth,UserHeight :INTEGER
UserColour=str(input("enter colour"))
UserColour=UserColour.lower()
