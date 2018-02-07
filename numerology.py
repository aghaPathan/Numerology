class Numerology():
    """
            This class takes input as string of a name and output a numerological number
        """
    def __init__(self):
        self.name_result = int()
        self.num_result = int()
        self.numbers = {1: 'ajs', 2: 'bkt', 3: 'clu', 4: 'dmv', 5: 'enw', 6: 'fox', 7: 'gpy', 8: 'hqz', 9: 'ir'}
        self.temp = int()

    def name(self,input):
        name = input.replace(' ', '').lower()

        for letter in name:
            for key, value in self.numbers.iteritems():
                if letter in value:
                    self.name_result += key

        return self.sum(str(self.name_result))

    def sum(self, input):
        i = 0
        self.num_result = 0
        while i <= len(input)-1:
            self.num_result += int(input[i])
            i += 1
            if i > len(input)-1:
                if len(str(self.num_result)) > 1:
                    return self.sum(str(self.num_result))
                if len(str(self.num_result)) == 1:
                    return self.num_result
