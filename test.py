def extractPhonemes2(word, i, arr):
    vowel = ['a','ā','e','i','o','u','ū']
    terminals = ['ṃ']
    exceptions = ['r', 'ḥ', 'm']
    print('entered recursion', i)    
    print(word)
    if len(word) == 0:
        return arr
    if len(word) == i:
        arr.append(word)
        return arr
    if word[i] in vowel:
        #a,e
        if i == 0:
            arr.append(word[:i+1])
            print('first vowel')
            print(arr)
            return extractPhonemes2(word[i+1:], 0,arr)
        # next can be a terminal or exception
        else:
            print('second vowel skipping')
            print(arr)
            return extractPhonemes2(word, i+1,arr)
    #if 'ṃ'
    if word[i] in terminals:
        print('found terminal')
        print(arr)
        arr.append(word[:i+1])
        return extractPhonemes2(word[i+1:], 0,arr)
    #exception is a consonant if first
    if word[i] in exceptions:
        if i == 0:
            print('first exception skipping')
            print(arr)
            return extractPhonemes2(word, i+1, arr)
        else:
            #exceptions are terminals if preceded by a vowel
            print('not first exception')
            print(word, i)
            if word[i-1] in vowel and i+1 < len(word) and word[i+1] in vowel:
                arr.append(word[:i])
                print('previous vowel and next vowel', i, word)
                print(arr)
                return extractPhonemes2(word[i:], 0,arr)
            else:
                if i+1 < len(word) and word[i+1] in vowel:
                    print('next is vowel skipping')
                    print(arr)
                    return extractPhonemes2(word, i+1, arr)
                else: 
                    arr.append(word[:i+1])
                    print('next is not vowel')
                    print(arr)
                    return extractPhonemes2(word[i+1:], 0,arr)
    #finally if it is a consonant
    if i == 0:
        print('first consonant skipping')
        print(arr)
        return extractPhonemes2(word, i+1, arr)
    else:
        if word[i-1] in vowel:
            print('consonant with previous vowel')
            print(arr)
            arr.append(word[:i])
            return extractPhonemes2(word[i:], 0,arr)
        else:
            print('consonant with not previous vowel skippng')
            print(arr)
            return extractPhonemes2(word, i+1, arr)
    return arr

abh = ['tathā' 'hi' 'dūrād' 'rūpaṃ' 'paśyati' 'akṣisthamañjanaṃ' 'na' 'paśyati'
 'dūrācchabdaṃ' 'śṛṇoti' 'sati' 'ca' 'prāptaviṣayatve' 'divyaṃ'
 'cakṣuḥśrotramiha' 'manuṣyeṣu' 'dhyāyināṃ' 'nopajāyeta' 'ghrāṇādivat'
 'yadyaprāptaviṣayaṃ' 'cakṣuḥ' 'kasmānna' 'sarvamaprāptaṃ' 'paśyati'
 'dūraṃ' 'tiraskṛtaṃ' 'ca' 'kathaṃ' 'tāvadayaskānto' 'na' 'sarvamaprāptam'
 'ayaḥ' 'karṣati' "prāptaviṣayatve'pi" 'caitat' 'samānam' 'kasmānna'
 'sarvaṃ' 'prāptaṃ' 'paśyatyañjanaṃ' 'śalākāṃ' 'vā' 'yathā' 'ca'
 'ghrāṇādīnāṃ' 'hi' 'prāpto' 'viṣayo' 'na' 'tu' 'sarvaḥ'
 'sahabhūgandhādyagrahaṇād' 'evaṃ' 'cakṣuṣo' "'pyaprāptaḥ" 'syāt' 'na'
 'tu' 'sarvaḥ' 'manastvarūpitvāt' 'prāptumevāśaktam' 'kecit' 'punaḥ'
 'śrotraṃ' 'prāptāprāptaviṣayaṃ' 'manyante' "karṇābhyantare'pi"
 'śabdaśravaṇāt' 'śeṣaṃ' 'tu' 'ghrāṇajihvākāyākhyam']
#abh = ["śrotraṃ"]
for i in range(len(abh)):
    arr = []
    arr = extractPhonemes2(abh[i], 0, arr)
    print(arr)

#arr = extractPhonemes2(abh[0], 0, arr)
#print(arr)

