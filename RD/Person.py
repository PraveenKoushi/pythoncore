class Person:
    # first_name: str
    # last_name: str
    dict ={}
    def __init__(self, first_name:str, last_name:str):
            self.first_name = first_name
            self.last_name = last_name
            #super.__init__()



    def __repr__(self):
        return f'Person: {self.first_name} {self.last_name} hash = {hash(self)}'

    def __hash__(self):
        to_hash = (self.first_name , self.last_name)
        return hash(to_hash)

    def __eq__(self, value):
        return type(self) == type(value) and self.first_name == value.first_name and self.last_name == value.last_name

    def is_person_in_dict(self, first_name: str, last_name: str, the_dictionary: dict):
        print("I am into preparing dictinary objects")
        print(f'first_name {first_name} and last_name is {last_name}')
        return Person(first_name,last_name) in the_dictionary


dict = {}
dictmod = {}
#p1 = Person("Hari","krishna")
p2 = Person()
#dictnew=p.is_person_in_dict("praveen","kumar",dict)
#print(p1)
#p.is_person_in_dict("praveen","kumar",dict)

dictmod=p2.is_person_in_dict(first_name="parveen",last_name="kumar",the_dictionary=dict)

print(f'dictmod is {dictmod}')