class Student:
    def __init__(self,fname,Lname,score):
        self.fname = fname
        self.Lname = Lname
        self.score = score
    
    def state(self,score):
        self.score = score

        if 20 >= self.score > 18:
            return "very good"
        elif 18 >= self.score > 15:
            return "good"
        elif 15 >= self.score > 12:
            return "not bad"
        elif 12 >= self.score > 10:
            return "bad"
        elif 10 >= self.score > 0:
            return "very bad"
        else:
            return "out of range"
