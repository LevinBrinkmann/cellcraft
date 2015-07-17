class BioObject:
    def __init__(self,pos,type):
        self.pos = pos        #position of Bioobject????
        self.type = type  #type of Bioobject
    #add a Subobject (Bioobject) to the object 
    def add_subobject(self.sub):
    #add discrete model position
    def add_discrete_model(discrete_models):
        self.discrete_models = discrete_models
    #add a continous model
    def add_continous_model():
        self.continous_model = continous_model
        
    #initialise discrete model
    #this means that each instance (each BioObject in the dicrete model will be a new instance of BioObject of given type
    
    #returns all bioobjects contained in bioobject (optional: for bioobject being in given state)
    get_contained_bioobjects(**state)
    #initiate states for the Bioobject given 
    def init_states():


    


class DiscreteModel:
    #the discrete model defines relative position and type of each Object
    def __init__(self,pos,types):
        self.pos = pos        #relative positions of all BioObjects
        self.types = types     #type of each BioObject
    def create_instances(relpos):
        #this creates new instances from BioObject for each position in the DiscreteModel
        return [BioObject(pos+relpos,t) for pos,t in zip(self.pos,self.types)]
    def create_continous_model():
        #this creates a new continous model based on the positions of the BioObjects
        #....
        return ContinousModel()


class ContinousModel:
    def __init__(self):
        pass
    
        
