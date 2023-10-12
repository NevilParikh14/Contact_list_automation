import json
import os
import requests


class Base:
    base_url = "https://thinking-tester-contact-list.herokuapp.com"
    main_file_path = os.getcwd()
    token = ""
    updated_values = {"firstName": "updatedName"}
    
    with open(main_file_path + "/config.json", "r") as file:
        creds_file = json.loads(file.read())

    #  Function to send request and return API response
    def request(self, endpoint, method, header, body):
        response = requests.request(
            method,
            headers=header,
            url=self.base_url + "/" + endpoint,
            data=json.dumps(body)
        )
        try:
            response_json = response.json()
        except:
            response_json = {}
        return response.status_code, response_json

    # Function to login and get API token
    def get_token(self, body = {"email": creds_file['users']['email'], "password": creds_file['users']['password']}):
        endpoint = "users/login"
        method = "POST"
        header = {'Content-Type': 'application/json'}
        response_code, response = self.request(endpoint, method, header, body)
        print(response, response_code)
        if response_code in [200, 201]:
            self.token = response['token']
        else:
            self.token = ""

    # Function to create user
    def create_user(self, body = creds_file['users']):

        endpoint = "users"
        method = "POST"
        header = {'Content-Type': 'application/json'}
        response_code, response = self.request(
            endpoint, method, header, body)
        return response_code, response
    
    # Function to get user
    def get_user(self):

        endpoint = "users/me"
        method = "GET"
        header = {'Authorization': 'Bearer ' + self.token}
        response_code, response = self.request(endpoint, method, header, {})
        return response_code, response
    
    # Function to update user
    def update_user(self):

        endpoint = "users/me"
        method = "PATCH"
        header = {'Authorization': 'Bearer ' + self.token,
                  'Content-Type': 'application/json'}
        response_code, response = self.request(
            endpoint, method, header, self.creds_file['updated_users'])
        return response_code, response

    # Function to reset user details
    def reset_user_details(self):
        endpoint = "users/me"
        method = "PATCH"
        header = {'Authorization': 'Bearer ' + self.token,
                  'Content-Type': 'application/json'}
        response_code, response = self.request(
            endpoint, method, header, self.creds_file['users'])
        if response_code not in [200, 201]:
            raise (f"Not able to update the user details: {response}")
        endpoint = "users/me"
        method = "GET"
        header = {'Authorization': 'Bearer ' + self.token}
        response_code, response = self.request(endpoint, method, header, {})
        if response_code != 200:
            raise (f"Not able to update the user details: {response}")

    # Function to delete user
    def delete_user(self):

        self.get_token()
        endpoint = "users/me"
        method = "DELETE"
        header = {'Authorization': 'Bearer ' + self.token}
        response_code, response = self.request(endpoint, method, header, {})
        if response_code in [200, 201]:
            self.token = ""
        return response_code, response

    # Function to create contact
    def create_contact(self, contact_value):

        endpoint = "contacts"
        method = "POST"
        header = {'Authorization': 'Bearer ' + self.token,
                  'Content-Type': 'application/json'}
        response_code, response = self.request(endpoint, method, header, contact_value)
        return response_code, response

    # Function to get all the contacts
    def get_contacts(self):

        endpoint = "contacts"
        method = "GET"
        header = {'Authorization': 'Bearer ' + self.token}
        response_code, response = self.request(endpoint, method, header, {})
        return response_code, response
    
    # Function to get contact
    def get_contact(self, contact_id):

        endpoint = "contacts"
        method = "GET"
        header = {'Authorization': 'Bearer ' + self.token}
        response_code, response = self.request(
            endpoint + "/" + contact_id, method, header, {})
        return response_code, response

    # Function to delete all the contacts
    def delete_contacts(self):
        
        response_code, response = self.get_contacts()
        if response:
            endpoint = "contacts"
            method = "DELETE"
            header = {'Authorization': 'Bearer ' + self.token}
            for i in range(len(response)):
                self.request(
                    endpoint + "/" + response[i]['_id'], method, header, {})
    
    # Function to delete contact
    def delete_contact(self, contact_id):
        
        endpoint = "contacts"
        method = "DELETE"
        header = {'Authorization': 'Bearer ' + self.token}
        response_code, response = self.request(
            endpoint + "/" + contact_id, method, header, {})
        return response_code, response
    
    # Function to update contact
    def update_contact(self, method, contact_id, updated_values = {}):

        if len(updated_values) == 0:
            updated_values = self.updated_values
        endpoint = "contacts"
        header = {'Authorization': 'Bearer ' + self.token,
                  'Content-Type': 'application/json'}
        response_code, response = self.request(
            endpoint + "/" + contact_id, method, header, updated_values)
        return response_code, response

    # Function to logout
    def logout(self):

        endpoint = "users/logout"
        method = "POST"
        header = {'Authorization': 'Bearer ' + self.token}
        response_code, response = self.request(endpoint, method, header, {})
        return response_code, response
