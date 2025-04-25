class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        if not self.data:
            return "No data to retrieve"
        else:
            return self.data[0]

# Example usage
project_group = MyClass()
project_group.add_data(1)
project_group.add_data(2)
print(project_group.get_data())
