# Word Frequency Counter: Basic to Advanced

Let's build a comprehensive word frequency counter in Python, progressing from basic concepts to advanced implementations with real-world features.

***

## **Level 1: Basic Dictionary Approach**

Start with a simple dictionary and manual counting.

```python
def basic_word_counter(text):
    """Basic word frequency counter using dictionary."""
    words = text.split()
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

# Example
text = "hello world hello everyone"
result = basic_word_counter(text)
print(result)
# Output: {'hello': 2, 'world': 1, 'everyone': 1}
```

***

## **Level 2: Improved with `setdefault()` and Preprocessing**

Add case normalization and punctuation removal.

```python
import re

def improved_word_counter(text):
    """Word counter with text cleaning."""
    # Normalize case
    text_lower = text.lower()
    
    # Remove punctuation using regex
    cleaned_text = re.sub(r'[^\w\s]', '', text_lower)
    
    # Split into words
    words = cleaned_text.split()
    
    # Count using setdefault
    word_counts = {}
    for word in words:
        word_counts.setdefault(word, 0)
        word_counts[word] += 1
    
    return word_counts

# Example
text = "Hello, World! Hello everyone. HELLO again!"
result = improved_word_counter(text)
print(result)
# Output: {'hello': 3, 'world': 1, 'everyone': 1, 'again': 1}
```

***

## **Level 3: Using `collections.Counter`**

The professional, Pythonic approach.

```python
from collections import Counter
import re

def counter_word_freq(text):
    """Word frequency using Counter."""
    # Clean and tokenize
    words = re.findall(r'\w+', text.lower())
    
    # Count with Counter
    return Counter(words)

# Example
text = "Python is great. Python is powerful. I love Python!"
word_freq = counter_word_freq(text)

print("All words:", dict(word_freq))
print("Top 3:", word_freq.most_common(3))
# Output:
# All words: {'python': 3, 'is': 2, 'great': 1, 'powerful': 1, 'i': 1, 'love': 1}
# Top 3: [('python', 3), ('is', 2), ('great', 1)]
```

***

## **Level 4: Advanced Features**

### A. Sorting and Filtering

```python
from collections import Counter
import re

def advanced_word_counter(text, min_length=3):
    """Advanced counter with filtering and sorting."""
    # Clean and tokenize
    words = re.findall(r'\w+', text.lower())
    
    # Filter short words
    filtered_words = [w for w in words if len(w) >= min_length]
    
    # Count
    word_freq = Counter(filtered_words)
    
    return word_freq

def display_sorted_results(word_freq, sort_by='frequency', top_n=10):
    """Display results with different sorting options."""
    if sort_by == 'frequency':
        # Sort by frequency (descending)
        sorted_words = word_freq.most_common(top_n)
    elif sort_by == 'alphabetical':
        # Sort alphabetically
        sorted_words = sorted(word_freq.items())[:top_n]
    else:
        sorted_words = list(word_freq.items())[:top_n]
    
    print(f"\n--- {sort_by.title()} Order (Top {top_n}) ---")
    for word, count in sorted_words:
        print(f"{word:15} : {count:3}")

# Example
text = """
Python is a high-level programming language. 
Python is easy to learn. Python is versatile.
Many developers love Python for its simplicity.
"""

word_freq = advanced_word_counter(text, min_length=4)
display_sorted_results(word_freq, 'frequency', 5)
display_sorted_results(word_freq, 'alphabetical', 5)
```

### B. Reading from Files

```python
from collections import Counter
import re

def count_words_from_file(filename):
    """Count word frequencies from a text file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Extract words
        words = re.findall(r'\w+', text.lower())
        
        # Count frequencies
        word_counts = Counter(words)
        
        return word_counts
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return Counter()
    except Exception as e:
        print(f"Error: {e}")
        return Counter()

def save_results(word_counts, output_file, top_n=None):
    """Save word frequency results to a file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("Word Frequency Analysis\n")
            file.write("=" * 40 + "\n\n")
            
            items = word_counts.most_common(top_n) if top_n else word_counts.most_common()
            
            for word, count in items:
                file.write(f"{word:20} : {count:5}\n")
        
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")

# Example usage
word_counts = count_words_from_file('sample.txt')
if word_counts:
    print("Top 10 most common words:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")
    
    # Save results
    save_results(word_counts, 'word_frequency_results.txt', top_n=50)
```

***

## **Level 5: Complete Real-World Application**

### Full-Featured Word Analyzer

```python
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
```

***

## **Comparison of Methods**

| Level | Method | Best For | Features |
|-------|--------|----------|----------|
| 1 | Basic Dict | Learning | Manual counting |
| 2 | Dict + `setdefault()` | Simple projects | Text cleaning |
| 3 | `Counter` | Most cases | Built-in methods |
| 4 | Advanced | Production | Sorting, filtering, file I/O |
| 5 | OOP Class | Large projects | Full analysis, reports |

***

## **Key Takeaways**
- Start simple with dictionaries to understand the logic
- Use `collections.Counter` for real-world applications
- Always preprocess text (lowercase, remove punctuation)
- Add filtering for meaningful results (stopwords, min length)
- Consider file I/O for practical use cases
