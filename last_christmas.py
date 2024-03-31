class Calculator:
    def __init__(self, operation: str) -> str:
        self.operation = operation.replace(" ", "")

    def solve(self):
        result = self.separate_brackets(self.operation)
        return result
    
    def separate_brackets(self, operation: str):
        opening_brackets = operation.count("(")
        closing_brackets = operation.count(")")
        if opening_brackets > closing_brackets:
            raise ValueError("Too many opening brackets")
        
        elif opening_brackets < closing_brackets:
            raise ValueError("Too many closing brackets")
        
        else:
            result = operation
            for i in range(closing_brackets):
                before_first_closing_bracket = result.split(")", 1)[0]
                brackets_to_solve = before_first_closing_bracket.split("(")[-1]
                brackets_result = self.solve_substring(brackets_to_solve)
                result= result.replace(f"({brackets_to_solve})", brackets_result)

            result = self.solve_substring(result)

        return result
    
    def solve_substring(self, substring):
        while "*" in substring:
            substring = self.operate_two_operands(substring, self.multiply, "*")

        while "/" in substring:
            substring = self.operate_two_operands(substring, self.divide, "/")

        while "+" in substring:
            substring = self.operate_two_operands(substring, self.sum, "+")

        while "-" in substring and substring[0] != "-":
            substring = self.operate_two_operands(substring, self.substract, "-")

        while "%" in substring:
            substring = self.operate_two_operands(substring, self.module, "%")
        
        return substring
    
    def operate_two_operands(self, substring, func, operator):
        first_part, second_part = substring.split(operator, 1)
        first_part_inverse = first_part[::-1]

        a_inverse_beginning = self.recognize_non_digit_position(first_part_inverse)
        a_beginning = len(first_part ) - a_inverse_beginning
        b_end = self.recognize_non_digit_position(second_part)

        a = int(first_part[a_beginning:])
        b = int(second_part[:b_end])

        operation_result = func(a, b)
        result = substring[:a_beginning] + str(operation_result) + substring[len(first_part)+1+b_end:]

        return result

    
    def recognize_non_digit_position(self, substring):
        for i in range(0, len(substring)):
            character = substring[i]
            if character.isdigit():
                continue

            if i == 0 and character == "-":
                continue

            else:
                return i
            
        return len(substring)
    
    def sum(self, a, b):
        return a + b
    
    def substract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
    def module(self, a, b):
        return a % b
    
if __name__ == "__main__":
    operation = input("Enter the operation: ")
    calculator = Calculator(operation)
    print(calculator.solve())