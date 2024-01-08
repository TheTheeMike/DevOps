import argparse
import requests
import json
import logging

def get_user_ids(url, destination, verbose=False):
    if verbose:
        logging.basicConfig(level=logging.INFO)
    try:
        response = requests.get(url)
        if verbose:
            logging.info(f"Response from {url}: {response.status_code}")
        if response.status_code == 200:
            users_data = response.json()
            user_ids_dict = {f"User {user['id']}": str(user['userId']) for user in users_data}

            with open(destination, 'w') as file:
                json.dump(user_ids_dict, file, indent=2)
            if verbose:
                logging.info("User IDs extracted:")
                for user, user_id in user_ids_dict.items():
                    logging.info(f"{user}: {user_id}")
        else:
            logging.error(f"Failed to retrieve data. Status code: {response.status_code}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve user ids from a given URL and save them to a file.")
    parser.add_argument("url", help="URL of the website")
    parser.add_argument("destination", help="Destination file path")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

    args = parser.parse_args()

    get_user_ids(args.url, args.destination, args.verbose)

