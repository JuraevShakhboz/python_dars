# 1-masala. CAMELCASE AND SNAKECASE
# def to_case(input_string, target_case):
#     words = input_string.split('_') if '_' in input_string else input_string.split()
    
#     if target_case == 'camel_case':
#         camel_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
#         return ''.join(camel_words)
    
#     if target_case == 'snake_case':
#         return '_'.join(words).lower()

#     return None

# input_str = "is_modal_open"
# camel_result = to_case(input_str, 'camel_case')
# snake_result = to_case(input_str, 'snake_case')

# print("Input:", input_str)
# print("Camel Case:", camel_result)
# print("Snake Case:", snake_result)



# 2-masala. CAESAR_CIPHER
# def caesar_cipher_encrypt(text, key):
#     encrypted_text = ""
#     for char in text:
#         if char.isalpha():
#             is_upper = char.isupper()
#             char_index = ord(char.lower()) - ord('a')
#             encrypted_index = (char_index + key) % 26
#             encrypted_char = chr(encrypted_index + ord('A' if is_upper else 'a'))
#             encrypted_text += encrypted_char
#         else:
#             encrypted_text += char
#     return encrypted_text

# def main():
#     text = input("Enter the text to encrypt: ")
#     key = int(input("Enter the key (shift value): "))
    
#     encrypted_text = caesar_cipher_encrypt(text, key)
#     print("Encrypted Text:", encrypted_text)

# if __name__ == "__main__":
#     main()



# 4-masala. TIMETABLE
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

class TimeTable(Time):
    def __init__(self, hour, minute, second, subject, start_time, classroom):
        super().__init__(hour, minute, second)
        self.subject = subject
        self.start_time = start_time
        self.classroom = classroom

# 5 ta obyekt yaratish
objects = [
    TimeTable(9, 0, 0, "Math", "09:00 AM", "Room 101"),
    TimeTable(10, 30, 0, "History", "10:30 AM", "Room 202"),
    TimeTable(13, 45, 0, "Physics", "01:45 PM", "Room 301"),
    TimeTable(15, 15, 0, "Chemistry", "03:15 PM", "Room 203"),
    TimeTable(16, 45, 0, "English", "04:45 PM", "Room 102")
]

# Foydalanuvchi tomonidan kiritilgan vaqt
user_hour = int(input("Soatni kiriting: "))
user_minute = int(input("Daqiqani kiriting: "))
user_second = int(input("Soniyaning nechi soniyasini kiriting: "))

# Kiruvchi vaqt bo'yicha qaysi fan boshlanishi
for obj in objects:
    if obj.hour == user_hour and obj.minute == user_minute and obj.second == user_second:
        print(f"{obj.start_time} da {obj.subject} fanining boshlanishi.")
        break
else:
    print("Siz kiritgan vaqtda hech qanday fan boshlanmadi.")