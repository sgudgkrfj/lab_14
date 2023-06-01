class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"ім'я студента: {self.name}, вік студента: {self.age}")

st=Student("vasia", 12)
st.get_info()



