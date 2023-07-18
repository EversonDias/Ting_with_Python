class generate_word():
    def __init__(self, word, instance):
        self.file = instance.search(0)["linhas_do_arquivo"]
        self.name = instance.search(0)["nome_do_arquivo"]
        self.word = word
        self.data = []

    def create_date(self):
        return [{
            "palavra": self.word,
            "arquivo": self.name,
            "ocorrencias": self.data
        }]

    def add(self, value):
        self.data.append(value)

    def resolve(self):
        if len(self.data) == 0:
            return []
        return self.create_date()


def exists_word(word, instance):
    data = generate_word(word, instance)
    for index, line in enumerate(data.file):
        if word.lower() in line.lower():
            data.add({"linha": index + 1})
    return data.resolve()


def search_by_word(word, instance):
    data = generate_word(word, instance)
    for index, line in enumerate(data.file):
        if word.lower() in line.lower():
            data.add({
                "linha": index + 1,
                "conteudo": line
            })
    return data.resolve()
