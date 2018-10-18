class Numerology():
    def __init__(self):
        """ This class is used for Numerology. It generates numbers from name and date of birth """
        self.numbers = {1: 'ajs', 2: 'bkt', 3: 'clu', 4: 'dmv', 5: 'enw', 6: 'fox', 7: 'gpy', 8: 'hqz', 9: 'ir'}

    def name(self, name):
       """ This method will process the name. It takes one input name as string. """ 
        name = name.replace(' ', '').lower()
        name_result = 0
        for letter in name:
            for key, value in self.numbers.items():
                if letter in value:
                    name_result += key
        return self.add(str(name_result))

    def add(self,number):
        """ Addition Logic """
        total = 0
        for n in number:
            total += int(n)
        if len(str(total)) > 1:
            self.add(str(total))
        else:
            # Final result
            return total

    def birth_date(self,date):
        """  Input date with dd/mm/yyyy format  """
        date = date.replace('/','')
        return self.add(date)   
