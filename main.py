# Класс Snow
# class Snow:
#     def __init__(self, count):
#         self.count = count
#
#     def __add__(self, n):
#         return Snow(self.count + n)
#
#     def __sub__(self, n):
#         return Snow(self.count - n)
#
#     def __mul__(self, n):
#         return Snow(self.count * n)
#
#     def __truediv__(self, n):
#         if n == 0:
#             raise ValueError("Дел")
#         return Snow(self.count / n)
#
#     def makeSnow(self, n):
#         rows = self.count // n
#         snowflake = '*' * n
#         return '\n'.join([snowflake] * rows)
#
# snowflakes = Snow(15)
# result = snowflakes + 5
# print(result.count)
#
# snowflakes = Snow(20)
# result = snowflakes / 4
# print(result.count)
#
# snowflakes = Snow(17)
# snow_pattern = snowflakes.makeSnow(3)
# print(snow_pattern)

# Класс Robot

# class Robot:
#     def __init__(self, x=0, y=0):
#         self.x = max(0, min(100, x))
#         self.y = max(0, min(100, y))
#         self.path_history = [(self.x, self.y)]
#
#     def move(self, commands):
#         for command in commands:
#             if command == 'N' and self.y < 100:
#                 self.y += 1
#             elif command == 'S' and self.y > 0:
#                 self.y -= 1
#             elif command == 'E' and self.x < 100:
#                 self.x += 1
#             elif command == 'W' and self.x > 0:
#                 self.x -= 1
#             self.path_history.append((self.x, self.y))
#         return (self.x, self.y)
#
#     def path(self):
#         return self.path_history
#
# robot = Robot(50, 50)
# print(robot.move("NNEESW"))
# print(robot.path())

# Класс Talking

# class Talking:
#     def __init__(self, name):
#         self.name = name
#         self.yes_count = 0
#         self.no_count = 0
#         self.is_yes = True
#
#     def to_answer(self):
#         if self.is_yes:
#             self.yes_count += 1
#             self.is_yes = False
#             return "moore-moore"
#         else:
#             self.no_count += 1
#             self.is_yes = True
#             return "meow-meow"
#
#     def number_yes(self):
#         return self.yes_count
#
#     def number_no(self):
#         return self.no_count
#
# tk = Talking('Pussy')
# print(tk.to_answer())
# print(tk.to_answer())
# print(tk.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
#
# tk = Talking('Pussy')
# tk1 = Talking('Barsik')
# print(tk.to_answer())
# print(tk1.to_answer())
# print(tk1.to_answer())
# print(tk1.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
# print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no" {tk1.number_no()} times')



