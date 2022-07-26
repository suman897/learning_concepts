class pattern:
    def __init__(self,name):
        self.name=name
        pass

    def rect(self,length, breath):
        self.length=length
        self.breath=breath
        i,j=0,0
        
        while i<length :
            while j<breath :
                print("*",end='')
                j+=1
            print("")
            i+=1
            j=0
            
    def rect1(self,length,breath):
        self.length=length
        self.breath=breath
        for i in range(length):
            for i in range(breath):
                print("*",end='')
            print("")



    def triangle(self,height,base):
        self.height=height
        self.base=base
        i,j,k=0,0,0
        while k<height:
            while int(j/2)<base:
                while i<j:
                    print("*",end='')
                    i=i+1
                j=j+2
                i=0
                print("")
            k=k+1
        print('')

if __name__ == '__main__':   
    p1=pattern('design1')    


    p1.rect1(4,8)  
    p1.triangle(4,8)  
    pattern(1).rect(6,10)
    
