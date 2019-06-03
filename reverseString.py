def reverseString():
    str = True
    
    if str:
        str = 'reverse this string'
        print '1. Here is the sentence in reverse with spaces: ' + (str[::-1])
        
        if str:
            str = ''.join(str.split())
            print '2. Here is the sentence in reverse without spaces: ' + (str[::-1])
        
        if str:
            str = 'reverse this string 4 me'
            new_str = ''.join([i for i in str if not i.isdigit()])
            new_str = ''.join(new_str.split())
            print '3. Here is the sentence in reverse without numbers or spaces: ' + (new_str[::-1])
        
        if str:
            str = 'reverse each word in this sentence'
            words = str.split()
            if words:
                reversewords = words[::-1]
                new_str = ' '.join(reversewords)
                print '4. Here is the sentence with each word reversed: ' + (new_str)

reverseString()