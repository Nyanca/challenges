def reverseString(str):
    
    #reverse the string passed to the function
    word = str[::-1]
    print '1. Here is the string in reverse: ' + (word)
    
    if str:
        #pass in a value for 'str' & reverse this value
        str = 'reverse this string'
        print '2. Here is the sentence in reverse with spaces: ' + (str[::-1])
        
        if str:
            #pass in a value for 'str' & reverse this value without spaces
            str = ''.join(str.split())
            print '3. Here is the sentence in reverse without spaces: ' + (str[::-1])
        
        if str:
            #pass in a value for 'str' with numbers. Print reverse wihtout numbers or spaces
            str = 'reverse this string 4 me'
            new_str = ''.join([i for i in str if not i.isdigit()])
            new_str = ''.join(new_str.split())
            print '4. Here is the sentence in reverse without numbers or spaces: ' + (new_str[::-1])
        
        if str:
            #pass in a value for 'str' & reverse each word
            str = 'reverse each word in this sentence'
            words = str.split()
            if words:
                reversewords = words[::-1]
                new_str = ' '.join(reversewords)
                print '5. Here is the sentence with each word reversed: ' + (new_str)
    
reverseString('word')
