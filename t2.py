class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        return value

    def max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


# Чтение количества запросов
num_queries = int(input())

stack = MaxStack()

# Обработка запросов
for _ in range(num_queries):
    query = input().split()

    if query[0] == 'push':
        value = int(query[1])
        stack.push(value)
    elif query[0] == 'pop':
        stack.pop()
    elif query[0] == 'max':
        print(stack.max())