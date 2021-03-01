def count_letters(text):
    results = {}
    for letter in text:
        if letter not in results:
            results[letter] = 0
        results[letter] +=1
    return results
    
print(count_letters("my name is ahmad")) 
