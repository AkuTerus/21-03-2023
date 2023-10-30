def cek_palindrome(kalimat):
    kalimat = kalimat.lower()
    kalimat_bersih=''
    
    for karakter in kalimat:
        if karakter.isalpha():
            kalimat_bersih= kalimat_bersih+karakter

        kalimat_bersih_balik = kalimat_bersih[::-1]

    if kalimat_bersih==kalimat_bersih_balik:
        return True
    else:
        return False

    pass

#program utama
kalimat = input('Masukan Kalimat : ')
hasil = cek_palindrome(kalimat)

if hasil==True:
    print('Palindrome!')
else:
    print('Bukan Palindrome!')


It seems you need help implementing the `get_min` and `pop` functions for your custom Queue class without using lists. Here's the code for both functions:

```python
def get_min(queue):
    if queue.get_length() == 0:
        return None

    min_value = queue.front()
    while queue.get_length() > 0:
        value = queue.dequeue()
        if value < min_value:
            min_value = value
        queue.enqueue(value)

    return min_value

def pop(queue):
    if queue.get_length() == 0:
        return None

    # Create a temporary queue to hold elements except the last one
    temp_queue = Queue()
    popped_value = None

    while queue.get_length() > 1:
        temp_queue.enqueue(queue.dequeue())

    if queue.get_length() == 1:
        popped_value = queue.dequeue()

    # Rebuild the original queue
    while temp_queue.get_length() > 0:
        queue.enqueue(temp_queue.dequeue())

    return popped_value
```

You can add these functions to your code, and they should work as expected, finding the minimum value in the queue and popping the last element without changing the queue's contents.