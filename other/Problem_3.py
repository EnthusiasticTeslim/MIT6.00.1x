s = 'teslim'
for counter in range(len(s)):
    longest_string = s[counter]                                                            #start of letter iterated 
    counter_duplicate = counter
    while (s[(counter_duplicate + 1)] >= s[counter_duplicate]):
        longest_string = longest_string + s[(counter_duplicate+1)]
        counter_duplicate = counter_duplicate + 1
    #print(longest_string)
    current_longest_string = longest_string
    break

for counter2 in range(1, len(s)):
    comparison_string = s[counter2]                                                    
    counter_duplicate2 = counter2                   
    while (counter_duplicate2 < (len(s)-1)) and (s[(counter_duplicate2 + 1)] >= s[counter_duplicate2]):
        comparison_string = comparison_string + s[counter_duplicate2+1]

        #(counter_duplicate2 < (len(s)-1)) was what I tweaked and apparently
        #solved the index error issue. except for 1 question, where it showed
        #up again. When I ran pythontutor, I found out if value assigned to
        #counter_duplicate >= len(s) , the program would have Index Error.
        
        counter_duplicate2 = counter_duplicate2 + 1
    if len(current_longest_string) < len(comparison_string):
        current_longest_string = comparison_string
print(current_longest_string)
