from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data.pop(0)

    def search(self, index):
        if (index >= len(self.data) or index < 0):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]
