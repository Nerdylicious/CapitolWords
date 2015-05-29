#Purpose: Search the Congressional Record for the most recent mention of the search term provided
import requests
import pprint

need_result = True 

while need_result:
    try:
        word = raw_input("\nEnter a word to search for: ")

        query_params = { 'apikey': 'f6ab5f2e4f69444b9f2c0a44d9a5223d',
                        'per_page': 1,
                        'phrase' : word,
                        'sort' : 'date desc'}

        endpoint = "http://capitolwords.org/api/text.json"

        response = requests.get(endpoint, params=query_params)
        data = response.json()

        first_result = data['results'][0]
        date = first_result['date']
        name = first_result['speaker_first'] + ' ' + first_result['speaker_last']
        party = first_result['speaker_party']
        chamber = first_result['chamber']
        context = first_result['speaking']

        print "\nOn {0}, {1} ({2}) of the {3} said:\n".format(date, name, party, chamber)

        for paragraph in context:
            print paragraph,

        print "\n"
        need_result = False
    except:
        print "Error, try another word ..."
