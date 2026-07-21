class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, w1: str, w2: str = None):
        if not w2:
            return w1.upper()
        else:
            return w1 + w2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
