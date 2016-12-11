import re

string_to_test = 'I am looking for a number between 2 and 5 but also 12 Main Street.'

def find_address(string_to_test):

    address_regex = r"(\d+) ([a-zA-Z]+) ([Ss]t(reet)?|[Rr]oad|[Bb]oulevard|[Bb]lvd \
                            |[Aa]ve(nue)?|[Ll]ane|[Ll]n|[Cc]ir(cle)?|[Cc](our)?t)"

    if re.search(address_regex, string_to_test):
        match = re.search(address_regex, string_to_test) 

        results = {
            "full_address" : match.group(0),
            "number" : match.group(1),
            "street_name" : match.group(2),
            "street_type" : match.group(3)
        }   

        print "\nMatch found from index %s to %s" % (match.start(), match.end())
        print "Full address:", results["full_address"]

        return results
    else: 
        print '\nNo address found for:', string_to_test
        return None

string_to_test = 'I am looking for a number between 2 and 5 but also 12 Main St.'
find_address(string_to_test)
find_address("55 Furrow Ave")
find_address("55 Furrow Avenue")
find_address("55 Left Court")
find_address("55 Left court")
find_address("55 Left ct")
find_address("55 Left Ct.")
