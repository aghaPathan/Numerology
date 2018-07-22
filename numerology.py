class Numerology:

    def __init__(self):

        self.total = int()
        self.numbers = {1: 'ajs', 2: 'bkt', 3: 'clu', 4: 'dmv', 5: 'enw', 6: 'fox', 7: 'gpy', 8: 'hqz', 9: 'ir'}


    def name(self, name):
       """ This method will process the name """ 
        name = name.replace(' ', '').lower()
        name_result = 0
        for letter in name:
            for key, value in self.numbers.items():
                if letter in value:
                    name_result += key

        self.add(str(name_result))

        return self.total

    def add(self,number):
        """ Addition Logic """
        total = 0
        for n in number:
            total += int(n)
        if len(str(total)) > 1:
            self.add(str(total))
        else:
            # Final result
            self.total = total


    def birth_date(self,date):
        """  Input date with dd/mm/yyyy format  """
        date = date.replace('/','')
        self.add(date)
        return self.total
    
