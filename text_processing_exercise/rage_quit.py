class RageQuit:

    def __init__(self, string):
        self.string = string.upper()
        self.all_symbols = ""

    def go_through_string(self):
        current_string = ""
        for index in range(len(self.string)):
            element = self.string[index]
            if not element.isdigit():
                current_string += self.string[index]
            else:
                # Check for the number because it can be with length more than 1 / greater than 9
                number = ""
                for indx in range(index, len(self.string)):
                    if not self.string[indx].isdigit():
                        break
                    number += self.string[indx]
                self.all_symbols += (current_string * int(number))
                current_string = ""

    def final(self):
        unique_symbols = ""
        for symbol in self.all_symbols:
            if symbol not in unique_symbols:
                unique_symbols += symbol
        return f"Unique symbols used: {len(unique_symbols)}\n{self.all_symbols}"


text = input()

obj = RageQuit(text)
obj.go_through_string()
print(obj.final())


# Other solution that doesn't get 100/100 in Judge because the number can be greater than 9
# text = input()
# current_string = ""
# unique_symbols = []
# for element in text:
#     if not element.isdigit():
#         current_string += element
#     else:
#         repetitions = int(element)
#         unique_symbols.append(current_string.upper() * repetitions)
#         current_string = ""
#
# all_symbols = "".join(unique_symbols)
# used_symbols = ""
# for symbol in all_symbols:
#     if symbol not in used_symbols:
#         used_symbols += symbol
# print(f"Unique symbols used: {len(used_symbols)}")
# print(all_symbols)
