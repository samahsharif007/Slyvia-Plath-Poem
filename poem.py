# Poem using classes and inheritence
# Positive spin of Slyvia Plaths fig tree

class Base:
    def __init__(self, taste: str, experience: str):
        self.taste = taste
        self.experience = experience

        print("I'm 23 and I'm hungry.\n"
              "I could starve, but I'm sat below a fig tree.\n"
              "I should eat some before they rot.\n\n"
              "I picked one.")

        print(f"I tried it, it was {taste}. I saw {experience}")
        print(f"I picked another one.")


if __name__ == "__main__":

    f1 = Base("sweet", "dancing on a stage")
