from base import Base


class TestCreateUser(Base):

    def test_create_user(self):

        self.delete_user()

        # Call to create a user
        response_code, response = self.create_user()

        # Verify that the API call was successful
        assert response_code in [200, 201]

        # Veirfy that the user was created
        assert response['user']

        # Verify that a token is received that can be used for performing other actions
        assert response['token']

        # Login and retrieve the Bearer token
        self.get_token(
            {"email": self.creds_file['users']['email'], "password": self.creds_file['users']['password']})

        # Verify that the token is received
        assert self.token

        # Logout the user
        response_code, response = self.logout()

        # Verify that the user was able to log out successfully
        assert response_code == 200

        self.token = ""

        # Create duplicate user
        response_code, response = self.create_user()

        # Verify that duplicate user cannot be created
        assert response_code == 400
