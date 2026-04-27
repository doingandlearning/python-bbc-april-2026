class Headline:
    """
    A class to represent a news headline with its source.
    
    Attributes:
        text (str): The headline text
        source (str): The news source (e.g., "BBC News")
    """
    
    def __init__(self, text: str, source: str):
        """
        Initialize a new Headline object.
        
        Args:
            text (str): The headline text
            source (str): The news source
        """
        self.text = text
        self.source = source
    
    def __str__(self):
        """
        Return a string representation of the Headline object.
        
        Returns:
            str: A readable representation of the headline
        """
        return f"Headline(text='{self.text}', source='{self.source}')"
    
    def get_word_count(self):
        """
        Get the number of words in the headline text.
        
        Returns:
            int: The word count
        """
        return len(self.text.split())

    def short_headline(self):
        """
        Generate a shortened version of the headline text.
        Returns a truncated headline with a maximum of 8 words followed by an ellipsis.
        If the headline contains fewer than 8 words, returns the original text unchanged.
        Returns:
            str: The original text if it contains fewer than 8 words, otherwise the first 
                 8 words followed by " ...".
        """

        if len(self.text.split()) < 8:
            return self.text
        else:
            short_headline = " ".join(self.text.split()[0:8]) + " ..."
            return short_headline

    def test(self) -> int:
        print("Hello")
        return 1
