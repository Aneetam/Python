class Mobile:
    def __init__(self,model,camera):
        self.model=model
        self.camera=camera
        
    def make_call(self,number):
       print("Calling  {}".format(number))
       
mob_obj=Mobile('Galaxy','234MP')
mob_obj.make_call(942245363)