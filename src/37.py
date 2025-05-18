class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        if not self.data:
            return None
        else:
            return self.data[0]

    def delete_data(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]

    def print_data(self):
        for data in self.data:
            print(data)

class DataProcessor:

    @staticmethod
    def process_data(data_list, processor_class, processor_type):
        if not processor_type == "simple":
            return None

        processed_data = []

        for item in data_list:
            if processor_class.process_item(item):
                processed_data.append(processor_class.get_data())

        return processed_data

class ItemProcessor:

    def process_item(self, item):
        # Add your processing logic here
        pass

data_list = [1, 2, 3]
processor_instance = DataProcessor()
processed_data = processor_instance.process_data(data_list, ItemProcessor(), "simple")

print(processed_data)
