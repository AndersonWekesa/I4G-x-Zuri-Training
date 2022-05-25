class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        return

    def change_name(self, new_name):
        self.name = new_name
        return
    
    def change_age(self, new_age):
        self.age = new_age
        return

    def add_track(self, new_track):
        self.tracks.append(new_track)
        return

    def get_score(self):
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.get_score())
