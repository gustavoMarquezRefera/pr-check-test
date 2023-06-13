import os
import json
import sys

def check_pr_description():
    pull_request_event = os.environ.get('GITHUB_EVENT_PATH')
    with open(pull_request_event) as event_file:
        pr_data = json.load(event_file)
        description = pr_data['pull_request']['body']
        
        if description is None:
            print("Invalid pull request description!")
            print("Description is empty.")
            sys.exit(1)
        
        description_length = len(description)
        
        if description_length < 200 or description_length > 250:
            print("Invalid pull request description!")
            print("Description must be between 200 and 250 characters.")
            sys.exit(1)

check_pr_description()

