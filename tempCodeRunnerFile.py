import random
import matplotlib.pyplot as plt

class ConditionalProbabilitySimulator:
    def __init__(self):
        self.events = {}

    def add_event(self, name, probability):
        self.events[name] = probability

    def calculate_conditional_probability(self, event_a, event_b):
        probability_a = self.events[event_a]
        probability_b = self.events[event_b]
        probability_a_and_b = probability_a * probability_b
        return probability_a_and_b / probability_b

    def simulate(self, event_a, event_b, num_trials):
        num_successes = 0
        for _ in range(num_trials):
            if random.random() < self.events[event_a] and random.random() < self.events[event_b]:
                num_successes += 1
        return num_successes / num_trials

    def visualize_probabilities(self, event_a, event_b, conditional_probability):
        event_names = [event_a, event_b, f'P({event_a}|{event_b})']
        probabilities = [self.events[event_a], self.events[event_b], conditional_probability]

        plt.bar(event_names, probabilities, color=['blue', 'orange', 'green'])
        plt.ylabel('Probability')
        plt.title('Event Probabilities and Conditional Probability')
        plt.ylim(0, 1)
        plt.axhline(0, color='black', linewidth=0.8)
        plt.grid(axis='y')
        plt.show()

def main():
    simulator = ConditionalProbabilitySimulator()

    print("Welcome to the Conditional Probability Simulator!")
    print("-----------------------------------------------")

    while True:
        print("\nOptions:")
        print("1. Add an event")
        print("2. Calculate conditional probability")
        print("3. Simulate conditional probability")
        print("4. Visualize probabilities")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter event name: ")
            probability = float(input("Enter event probability (0-1): "))
            simulator.add_event(name, probability)
            print(f"Event '{name}' added with probability {probability:.2f}")
        elif choice == "2":
            event_a = input("Enter event A name: ")
            event_b = input("Enter event B name: ")
            if event_a in simulator.events and event_b in simulator.events:
                probability = simulator.calculate_conditional_probability(event_a, event_b)
                print(f"P({event_a}|{event_b}) = {probability:.4f}")
            else:
                print("One or both events not found.")
        elif choice == "3":
            event_a = input("Enter event A name: ")
            event_b = input("Enter event B name: ")
            num_trials = int(input("Enter number of trials: "))
            if event_a in simulator.events and event_b in simulator.events:
                probability = simulator.simulate(event_a, event_b, num_trials)
                print(f"Simulated P({event_a}|{event_b}) = {probability:.4f}")
            else:
                print("One or both events not found.")
        elif choice == "4":
            event_a = input("Enter event A name: ")
            event_b = input("Enter event B name: ")
            if event_a in simulator.events and event_b in simulator.events:
                conditional_probability = simulator.calculate_conditional_probability(event_a, event_b)
                simulator.visualize_probabilities(event_a, event_b, conditional_probability)
            else:
                print("One or both events not found.")
        elif choice == "5":
            print("Exiting simulator.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()