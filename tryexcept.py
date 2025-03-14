def divide_vals(num,den):
   '''
   Args:
   numerator: (float) numerator of fraction
   denominator: (float) denominator of fraction

   Returns:
   fraction_val: (float) numerator/denominator
   '''
   try:
    f = num/den
    return f
   except ZeroDivisionError:
    return "denominator cannot be zero"


def num_words(text):
    '''
    Args:
      text: (string) string of words

    Returns:
      num_words: (int) number of words in the string
    '''
    try:
        num_words = len(text.split())
        return num_words
    except AttributeError:
        return "text argument must be a string"
  
print(divide_vals(10,5))
print(divide_vals(10,0))

print(num_words("hello world"))
print(num_words("this is a sentence. this is another sentence"))
print(num_words(846310))

