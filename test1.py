def hitung_vokal(kalimat):
    vokal = 'aiueoAIUEO'#Siapkan daftar huruf vokal
    jumlah = 0
    for karakter in kalimat:
        if karakter in vokal:
            jumlah = jumlah+1
    return jumlah

def hitung_white_space(kalimat):
    jumlah = 0
    for karakter in kalimat:
        if karakter.isspace()==True:
            jumlah=jumlah+1
    return jumlah

def hitung_konsonan(kalimat):
    #konsonan = alfabet(a-z,A-Z) - vokal (aiueo,AIUEO) 
    vokal = 'aiueoAIUEO'
    jumlah = 0
    for karakter in kalimat:
        if karakter in kalimat:
            if karakter not in vokal and karakter.isalpha():
                jumlah=jumlah+1
    return jumlah


#Input
kalimat = input('masukan Sebuah kalimat: ')

#Proses
jumlah_vokal=hitung_vokal(kalimat)
jumlah_whitespace=hitung_white_space(kalimat)
jumlah_huruf_mati=hitung_konsonan(kalimat)

#Output
print(f'Jumlah Huruf vokal : {jumlah_vokal}')
print(f'Jumlah White Space : {jumlah_whitespace}')
print(f'Jumlah Huruf Konsonan : {jumlah_huruf_mati}')



Sure, I can help you implement the missing methods in your Single Linked List Non-Circular (SLNC) class. Here's the complete implementation, including the `getData` and `hapusDuplikasi` methods:

```python
class Node:
    def __init__(self, value):
        self.next = None
        self.data = value

class SLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getLength(self):
        return self.size

    def writeAllData(self):
        if self.size == 0:
            result = 'Linked list kosong'
        else:
            result = 'Linked List: ' + str(self.size) + ' data:\n'
            helper = self.head
            while helper != None:
                result = result + str(helper.data) + ' '
                helper = helper.next
        print(result)

    def insert_head(self, new_data):
        node_baru = Node(new_data)
        if self.size == 0:
            self.head = node_baru
            self.tail = node_baru
        else:
            node_baru.next = self.head
            self.head = node_baru
        self.size = self.size + 1

    def insert_tail(self, new_data):
        node_baru = Node(new_data)
        if self.size == 0:
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru
        self.size = self.size + 1

    def insert_mid(self, new_data, index):
        if self.size == 0 or index <= 0:
            self.insert_head(new_data)
        elif index >= self.size:
            self.insert_tail(new_data)
        else:
            node_baru = Node(new_data)
            helper = self.head
            for i in range(index - 1):
                helper = helper.next
            node_baru.next = helper.next
            helper.next = node_baru
            self.size = self.size + 1

    def delete_head(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None
            self.size = self.size - 1
            return deleted_node
        else:
            hapus = self.head
            deleted_node = self.head
            self.head = self.head.next
            del hapus
            self.size = self.size - 1
            return deleted_node

    def delete_tail(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None
            self.size = self.size - 1
            return deleted_node
        else:
            helper = self.head
            while helper.next != self.tail:
                helper = helper.next
            hapus = self.tail
            deleted_node = self.tail
            self.tail = helper
            self.tail.next = None
            del hapus
            self.size = self.size - 1
            return deleted_node

    def delete_mid(self, index):
        if self.size == 0 or index <= 0:
            return self.delete_head()
        elif index >= self.size - 1:
            return self.delete_tail()
        else:
            helper = self.head
            for i in range(index - 1):
                helper = helper.next
            hapus = helper.next
            helper.next = hapus.next
            deleted_node = hapus
            del hapus
            self.size = self.size - 1
            return deleted_node

    def getData(self, index):
        if index < 0 or index >= self.size:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def hapusDuplikasi(self):
        if self.size <= 1:
            return

        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                    self.size -= 1
                else:
                    runner = runner.next
            current = current.next


if __name__ == "__main__":
    ll = SLNC()
    for i in [1, 1, 1, 1, 1, 2, 3, 4, 2, 2, 2, 5, 6]:
        ll.insert_tail(i)
    ll.writeAllData()
    ll.hapusDuplikasi()
    ll.writeAllData()
```

This code should now include the `getData` and `hapusDuplikasi` methods as per your requirements.