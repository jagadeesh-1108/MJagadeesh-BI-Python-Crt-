from collections import deque
import matplotlib.pyplot as plt

class Openmic:
    def __init__(self):
        self.performers = []
        self.audience = set()
        self.queue = deque()
        self.votes = {}
        self.voted = {}

    def register(self, name, role):
        role = role.lower()
        if role == "performer" and name not in self.performers:
            self.performers.append(name)
            self.queue.append(name)
            self.votes[name] = 0 
        elif role == 'audience' and name not in self.audience:
            self.audience.add(name)
            self.voted[name] = set()

    def start(self):
        if not self.audience:
            print("No audience registered. No voting will take place.")
            return
        while self.queue:
            p = self.queue.popleft()
            for a in self.audience:
                if p not in self.voted[a]:
                    vote = input(f"{a}, vote for {p}? (y/n): ").strip().lower()
                    if vote == "y":
                        self.votes[p] += 1
                        self.voted[a].add(p)

    def winner(self):
        if not self.votes:
            print("No votes recorded.")
            return
        max_v = max(self.votes.values())
        for p in self.votes:
            if self.votes[p] == max_v:
                print(f"winner {p} with {max_v} votes")

    def save(self, file="results.txt"):
        with open(file, 'w') as f:
            for p in self.performers:
                f.write(f"{p}-{self.votes.get(p, 0)} votes\n")

    def chart(self):
        if not self.votes:
            print("No votes to display.")
            return
        names, counts = zip(*self.votes.items())
        plt.bar(names, counts)
        plt.title("Vote Count")
        plt.ylabel("Votes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

o = Openmic()
o.register("Alice", "performer")
o.register("Bob", "performer")
o.register("Tom", "performer")
o.register("Jerry", "performer")
o.register("Sam", "audience")
o.register("Rita", "audience")
o.start()
o.winner()
o.save()
o.chart()