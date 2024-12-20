class Grammar:
    def __init__(self):
        self.rules = {}

    def add_rule(self, non_terminal, rule):
        if non_terminal not in self.rules:
            self.rules[non_terminal] = []
        self.rules[non_terminal].append(rule)

    def is_simple(self):
        """
        Checks if the grammar satisfies the simplicity rules:
        1. No rule is empty ("").
        2. No rule starts with a non-terminal.
        3. Rules for the same non-terminal are disjoint.
        """
        for non_terminal, rules in self.rules.items():
            seen_starts = set()  # To track the starting character of each rule
            for rule in rules:
                # Rule 1: No rule is empty.
                if rule == "":
                    print(f"\nRule '{non_terminal} -> {rule}' is empty.")
                    return False

                # Rule 2: No rule starts with a non-terminal.
                if rule[0] == "B" or rule[0] == "S":  # Non-terminal check
                    print(f"\nRule '{non_terminal} -> {rule}' starts with a non-terminal.")
                    return False

                # Rule 3: Rules for the same non-terminal must be disjoint.
                start = rule[0]
                if start in seen_starts:
                    print(f"\nRules for non-terminal '{non_terminal}' are not disjoint. "
                          f"Multiple rules start with terminal '{start}'.")
                    return False
                seen_starts.add(start)

        return True


class Parser:
    def __init__(self):
        self.grammar = Grammar()

    def parse(self, input_string, start_symbol):
        """
        Parses the input string using recursive descent parsing.
        """
        stack = [start_symbol]
        idx = 0

        while stack:
            current = stack.pop()

            if current in self.grammar.rules:  # Non-terminal
                rule_found = False
                for rule in self.grammar.rules[current]:
                    if idx < len(input_string) and rule and rule[0] == input_string[idx]:
                        stack.extend(reversed(rule))  # Push rule onto stack
                        rule_found = True
                        break
                if not rule_found:
                    return False, stack[::-1], list(input_string[idx:])
            else:  # Terminal
                if idx < len(input_string) and current == input_string[idx]:
                    idx += 1
                else:
                    stack.append(current)  # Re-add the current terminal to the stack if unmatched
                    return False, stack[::-1], list(input_string[idx:])

        return idx == len(input_string) and not stack, stack[::-1], list(input_string[idx:])


if __name__ == "__main__":
    parser = Parser()
    print("Recursive Descent Parsing For Following grammar")
    while True:
        parser.grammar = Grammar()

        # Input for two non-terminals: 'S' and 'B', each with two rules
        print("               ↓ Grammars ↓")
        for non_terminal in ["S", "B"]:
            for i in range(2):  # Two rules for each non-terminal
                rule = input(f"Enter rule number {i + 1} for non-terminal '{non_terminal}': ").strip()
                parser.grammar.add_rule(non_terminal, rule)

        # Check if the grammar is simple
        if parser.grammar.is_simple():
            print("\nThe Grammar is simple.")
            input_string = input("Enter the string want to be checked: ")
            start_symbol = "S"  # Define the start symbol

            # Print input string breakdown
            print(f"The input String: {[char for char in input_string]}")

            accepted, final_stack, remaining_string = parser.parse(input_string, start_symbol)

            print(f"Stack after checking: {final_stack}")
            print(f"The rest of unchecked String: {remaining_string}")

            if accepted:
                print("\nYour input string is Accepted.\n")
            else:
                print("\nYour input string is Rejected.\n")
        else:
            print("The Grammar isn't simple.\nTry again.\n")
            continue  # Restart for simplicity check

        print("===================================================")

        while True:
            print("\n1- Another Grammar\n2- Another String\n3- Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                break  # Restart with a new grammar
            elif choice == "2":
                input_string = input("Enter the string want to be checked: ")
                start_symbol = "S"  # Define the start symbol

                # Print input string breakdown
                print(f"The input String: {[char for char in input_string]}")

                accepted, final_stack, remaining_string = parser.parse(input_string, start_symbol)

                print(f"Stack after checking: {final_stack}")
                print(f"The rest of unchecked String: {remaining_string}")

                if accepted:
                    print("\nYour input string is Accepted.\n")
                else:
                    print("\nYour input string is Rejected.\n")

                print("===================================================")
            elif choice == "3":
                exit()  # Exit the program
            else:
                print("\nInvalid choice. Try again.")
