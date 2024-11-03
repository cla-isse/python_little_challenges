def string_compressor(string):
  count = 1
  result = []
  
  for i in range(0, len(string)): 
    if i+1 < len(string) and string[i] == string[i+1]:
      count += 1
    else:
      if count == 1:
        result.append(f'{string[i]}')
      else: 
        result.append(f'{count}.{string[i]}')
      count = 1

  return result

# Example
string_compressor('AAAABBBCCCDDE')
