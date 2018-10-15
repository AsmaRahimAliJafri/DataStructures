class queue:
    def __init__(self):
        self.myQueue = ['wake', 'eat', 'sleep']

    def mount(self):
        item = input("Enter the item ")
        self.myQueue.append(item)

    def remove(self):
        print("The item removed is "+self.myQueue[0])
        self.myQueue.remove(self.myQueue[0])

    def view(self):
        print(self.myQueue)

    @staticmethod
    def switcher(arg):
        switch = {'1': queue_obj.view(), '2': queue_obj.mount(), '3': queue_obj.remove()}
        result = switch.get(arg, default="please enter a value")
        return result()

queue_obj = queue()

while True:

    print("Enter values either 1 2 or 3")

    queue_obj.switcher(input())
