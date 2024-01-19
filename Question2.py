def evaluate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error: " + str(e)

input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

with open(output_file, "w") as file:
    for line in lines:
        expression = line.strip()
        answer = evaluate_expression(expression)
        file.write(answer + "\n")