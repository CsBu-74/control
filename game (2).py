#12.	Классы «Клиент»(Client) и «Банк» (Bank) Класс «Клиент»
# содержит поля: код клиента, ФИО, дата открытия вклада,
# размер вклада, процент по вкладу. Класс «Банк» (class Bank)
# содержит поле clientBase представляющем собой список клиентов и
# методами: –   — принимает обьект клиента и помещает его в base. –
# showByMoney(money) — принимает количество денег и выводит
# информацию о всех клиентах у которых размер вклада больше – showByCode(cod) —
# принимает код и выводит всю информацию клиенте
# с данным кодом. – showByProc(proc) — принимает процент и выводит информацию о
# всех клиентах у которых процент по вкладу больше данного.


class Client:
    def __init__(self, code, fio, date, size, perc):
        self.code = code
        self.fio = fio
        self.date = date
        self.size = size
        self.perc = perc

class Bank:
    def __init__(self):
        self.base = []

    def addClient(self, client):
        self.base.append(client)

    def showByMoney(self, money):
        for client in self.base:
            if client.size > money:
                self.clientinfo(client)

    def showByCode(self, code):
        for client in self.base:
            if client.code == code:
                self.clientinfo(client)
                break

    def showByProc(self, proc):
        for client in self.base:
            if client.perc > proc:
                self.clientinfo(client)

    def clientinfo(self, client):
        print("Код клиента:", client.code)
        print("ФИО:", client.fio)
        print("Дата открытия вклада:", client.date)
        print("Размер вклада:", client.size)
        print("Процент по вкладу:", client.perc)



