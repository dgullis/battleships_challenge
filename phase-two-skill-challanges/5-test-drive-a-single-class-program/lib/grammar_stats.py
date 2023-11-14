class GrammarStats:
    def __init__(self):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise

        self.tests = 0
        self.passed = 0


    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise

        self.tests += 1
        if text[0].isupper() and text[-1] in '.!?':
            self.passed += 1
            return True
        return False
    

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        
        return (self.passed/self.tests)*100