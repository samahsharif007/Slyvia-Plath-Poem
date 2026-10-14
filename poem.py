# Poem using classes and inheritence
# Positive spin of Slyvia Plaths fig tree

class Base:
    def __init__(self, taste: str, experience: str):
        self.taste = taste
        self.experience = experience

    def begin(self):
        print("I'm 23 and I'm hungry.\n"
              "I could starve, but I'm sat below a fig tree.\n\n"
              "I picked one.")

    def eat_fig(self):
        print(
            f"I tried it, it was {self.taste}. I saw myself {self.experience}.")


class NextFig(Base):
    def __init__(self, taste, experience, colour, feeling):
        super().__init__(taste, experience)
        self.colour = colour
        self.feeling = feeling

    def eat_another(self):
        print(f"\nI picked another one. It was {self.colour}.")
        self.eat_fig()
        print(f"I felt {self.feeling}.\n")


class FinalFig(NextFig):
    def __init__(self, taste, experience, colour, feeling, consequence):
        super().__init__(taste, experience, colour, feeling)
        self.consequence = consequence

    def eat_another(self):
        print(f"I picked a final fig. It was {self.colour}.\n"
              f"It tasted {self.taste}. I saw myself {self.experience}.\n"
              f"I realised {self.consequence}")


if __name__ == "__main__":
    f1 = Base("sweet", "reading endless books")
    f1.begin()
    f1.eat_fig()

    possibiliites = [
        NextFig("plump", "dancing with my closest friends",
                "deep purple", "alive"),
        NextFig("honeyed", "living by the sea", "golden", "free"),
        NextFig("rich", "painting in a garden", "tender", "hopeful")
    ]

    for fig in possibiliites:
        fig.eat_another()

    final_fig = FinalFig("rotten", "doing nothing", "brown",
                         "empty", "I don't like rotten fruit, nor do I have to eat any.")

    final_fig.eat_another()
