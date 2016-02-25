'''Find minimal number of countries, whose names can cover all 26 alphabets from A to Z.'''
import itertools
import math
import random
countries = "Afghanistan; Albania; Algeria; Andorra; Angola; Antigua and Barbuda; Argentina; Armenia; Australia; Austria; Azerbaijan; Bahamas; Bahrain; Bangladesh; Barbados; Belarus; Belgium; Belize; Benin; Bhutan; Bolivia (Plurinational State of); Bosnia and Herzegovina; Botswana; Brazil; Brunei Darussalam; Bulgaria; Burkina Faso; Burundi; Cabo Verde; Cambodia; Cameroon; Canada; Central African Republic; Chad; Chile; China; Colombia; Comoros; Congo; Costa Rica; C'te D'Ivoire; Croatia ; Cuba; Cyprus; Czech Republic; Democratic People's Republic of Korea; Democratic Republic of the Congo  ; Denmark; Djibouti; Dominica; Dominican Republic; Ecuador; Egypt; El Salvador; Equatorial Guinea; Eritrea; Estonia; Ethiopia; Fiji; Finland; France; Gabon; Gambia; Georgia; Germany; Ghana; Greece; Grenada; Guatemala; Guinea; Guinea Bissau; Guyana; Haiti; Honduras; Hungary; Iceland; India; Indonesia; Iran (Islamic Republic of); Iraq; Ireland; Israel; Italy; Jamaica; Japan; Jordan; Kazakhstan; Kenya; Kiribati; Kuwait; Kyrgyzstan; Lao People's Democratic Republic; Latvia; Lebanon; Lesotho; Liberia; Libya; Liechtenstein; Lithuania; Luxembourg; Madagascar; Malawi; Malaysia; Maldives; Mali; Malta; Marshall Islands; Mauritania; Mauritius; Mexico; Micronesia (Federated States of); Monaco; Mongolia; Montenegro; Morocco; Mozambique; Myanmar; Namibia; Nauru; Nepal; Netherlands; New Zealand; Nicaragua; Niger; Nigeria; Norway; Oman; Pakistan; Palau; Panama; Papua New Guinea; Paraguay; Peru; Philippines; Poland; Portugal; Qatar; Republic of Korea; Republic of Moldova; Romania; Russian Federation; Rwanda; Saint Kitts and Nevis; Saint Lucia; Saint Vincent and the Grenadines; Samoa; San Marino; Sao Tome and Principe; Saudi Arabia ; Senegal; Serbia; Seychelles; Sierra Leone; Singapore; Slovakia; Slovenia; Solomon Islands; Somalia; South Africa; South Sudan; Spain; Sri Lanka; Sudan; Suriname; Swaziland; Sweden; Switzerland; Syrian Arab Republic; Tajikistan; Thailand; The former Yugoslav Republic of Macedonia; TimorLeste; Togo; Tonga; Trinidad and Tobago; Tunisia; Turkey; Turkmenistan; Tuvalu; Uganda; Ukraine; United Arab Emirates; United Kingdom of Great Britain and Northern Ireland; United Republic of Tanzania ; United States of America; Uruguay; Uzbekistan; Vanuatu; Venezuela (Bolivarian Republic of); Viet Nam; Yemen; Zambia; Zimbabwe "
countries = countries.replace("(","")
countries = countries.replace(")","")
countries = countries.replace(" ","")
countries = countries.replace("'","")
listOfCountries = countries.split(";")
countriesNum = len(listOfCountries)
completeAlphabet = "".join(map(chr, range(97, 123)))
def checkAlphabetComplete(e):
    flattenedStr = "".join(e)
    flattenedStr = flattenedStr.lower()
    flattenedStr = list(set(list(flattenedStr)))
    flattenedStr.sort(key=lambda x:(not x.islower(), x))
    flattenedStr = "".join(flattenedStr)
        
#    print completeAlphabet,flattenedStr
    if completeAlphabet in flattenedStr: 
        return True
    else:
        return False

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def bruteForce():
    for i in [x+1 for x in range(12)]:
        print countriesNum,i,nCr(countriesNum,i)
        cb = list(itertools.combinations(listOfCountries,i))
        checkAlphabetComplete(cb)

def reduce(seq):
    maxIndex = len(seq) - 1
#    print maxIndex
    firstChoiceIndex = random.randint(0,maxIndex)
    firstChoice = seq[firstChoiceIndex]
    del seq[firstChoiceIndex]
    return firstChoice

def randomMethod():
    combinations = []
    while(True):
        if checkAlphabetComplete(combinations):
#            print len(combinations),combinations
            return [len(combinations),combinations]
        else:
            combinations.append(reduce(listOfCountries))

backup = [x for x in listOfCountries]
while(True):
    [length,combination] = randomMethod()
    if (length<9):
        print length, combination
        
    listOfCountries = [x for x in backup]
#print list(itertools.combinations(listOfCountries,2)))
