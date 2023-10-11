from base import Base


class TestCreateUser(Base):

    def test_create_user(self):

        self.delete_user()

        # Call to create a user
        response_code, response = self.create_user()

        # Verify that API call was successful
        assert response_code in [200, 201]

        # Veirfy that user was created
        assert response['user']

        # Verify that token is received that can be used for performin other actions
        assert response['token']

        # Login and retrive the Bearer token
        self.get_token(
            {"email": self.creds_file['users']['email'], "password": self.creds_file['users']['password']})

        # Verify that token is received
        assert self.token

        # Logout the user
        endpoint = "users/logout"
        method = "POST"
        header = {'Authorization': 'Bearer ' + self.token}
        response_code, response = self.request(endpoint, method, header, {})

        # Verify that user was able to logout successfuly
        assert response_code == 200

        self.token = ""

        # Create duplicate user
        endpoint = "users"
        method = "POST"
        header = {'Content-Type': 'application/json'}
        response_code, response = self.request(
            endpoint, method, header, self.creds_file['users'])

        # Verify that duplicate user cannot be created
        assert response_code == 400
