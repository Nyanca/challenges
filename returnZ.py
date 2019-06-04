def returnZ(lst, min_z_count):
    #initialize arrays 
    oneZ = []   
    twoZ = []   
    minZ = []

    for i in lst:
        #count the occurences of 'z' in each string
        count = (i.count('z'))
        
        #if the z count equals the value given, add the string to the array given
        if count is 1:
            oneZ.append(i)
        if count is 2:
            twoZ.append(i)
        if count >= min_z_count:
            minZ.append(i)
            
            #print the first value within each array and then stop looping
            print 'the first occurence of letter z happens in string ' + oneZ[0]
            print 'the first occurence of 2 z\'s happens in the string ' + twoZ[0]
            print 'the first occurence of a string with at least min_z_count happens in the string ' + minZ[0]
            break
        
        elif min_z_count > 6: 
            #print message if the min_z_count is more than the highest number of z's and stop looping
            print 'no string found with that many z\'s'
            break


returnZ(['abc', 'xyz', 'zda', 'ayz', 'azz', 'zzb', 'bbzz', 'dcdzzdz','abzzz','adzzzzzz','cddc'], 6)