class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score
        print("My name is ", name, ", I'm ", age, "years old. \n" "I'm a",
              track[0], "dev. student and scored", score, "in my accessment.")

    def change_name(self, name):
        print("My name is", name)

    def change_age(self, age):
        print("I am", age, "years old")

    def add_track(self, track):
        print("I am a ", track, "trainee")

    def get_score(self, score):
        print("I scored ", score, "in my accessment")


Bob = Student(name="Bob", age=26, track=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(89)
