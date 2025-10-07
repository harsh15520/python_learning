from collections import Counter
import re

class WordFrequencyAnalyzer:
    """Complete word frequency analyzer with multiple features."""
    
    def __init__(self, text=None, filename=None):
        """Initialize with text or file."""
        if filename:
            self.text = self._read_file(filename)
        else:
            self.text = text or ""
        
        self.word_counts = None
    
    def _read_file(self, filename):
        """Read text from file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return ""
    
    def analyze(self, min_length=1, exclude_words=None):
        """Analyze word frequencies."""
        # Clean and tokenize
        words = re.findall(r'\w+', self.text.lower())
        
        # Filter by length
        words = [w for w in words if len(w) >= min_length]
        
        # Exclude specific words (stopwords)
        if exclude_words:
            words = [w for w in words if w not in exclude_words]
        
        # Count
        self.word_counts = Counter(words)
        
        return self.word_counts
    
    def get_top_words(self, n=10):
        """Get top N most common words."""
        if self.word_counts is None:
            self.analyze()
        return self.word_counts.most_common(n)
    
    def get_statistics(self):
        """Get text statistics."""
        if self.word_counts is None:
            self.analyze()
        
        total_words = sum(self.word_counts.values())
        unique_words = len(self.word_counts)
        
        return {
            'total_words': total_words,
            'unique_words': unique_words,
            'avg_word_length': sum(len(w) * c for w, c in self.word_counts.items()) / total_words
        }
    
    def display_report(self, top_n=10):
        """Display comprehensive report."""
        if self.word_counts is None:
            self.analyze()
        
        stats = self.get_statistics()
        
        print("\n" + "=" * 50)
        print("WORD FREQUENCY ANALYSIS REPORT")
        print("=" * 50)
        
        print(f"\nText Statistics:")
        print(f"  Total words: {stats['total_words']}")
        print(f"  Unique words: {stats['unique_words']}")
        print(f"  Average word length: {stats['avg_word_length']:.2f}")
        
        print(f"\nTop {top_n} Most Common Words:")
        print("-" * 50)
        for i, (word, count) in enumerate(self.get_top_words(top_n), 1):
            percentage = (count / stats['total_words']) * 100
            print(f"{i:2}. {word:15} : {count:4} ({percentage:.1f}%)")
        
        print("=" * 50)

# Example usage
text = """
Python is a versatile programming language. Python is easy to learn.
Many developers choose Python for web development. Python is powerful.
Data science and machine learning use Python extensively.
Python has a large community and many libraries.
"""

# Common English stopwords to exclude
stopwords = {'is', 'a', 'to', 'and', 'for', 'has', 'the', 'in'}

# Create analyzer
analyzer = WordFrequencyAnalyzer(text=text)

# Analyze with options
analyzer.analyze(min_length=3, exclude_words=stopwords)

# Display report
analyzer.display_report(top_n=10)

# Get specific results
print("\nWords appearing more than once:")
for word, count in analyzer.word_counts.items():
    if count > 1:
        print(f"  {word}: {count}")
