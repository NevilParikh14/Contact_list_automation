from base import Base


class TestGetUser(Base):

    def test_get_user(self):

        # Get Bearer token
        if not self.token:
            self.create_user()
            self.get_token(
                {"email": self.creds_file['users']['email'], "password": self.creds_file['users']['password']})
            assert self.token

        # API call to get the user
        response_code, response = self.get_user()

        # Verify that user is returned
        assert response_code == 200

        # Verify that returned user data correct
        assert response['email'] == self.creds_file['users']['email'] and response['firstName'] == self.creds_file[
            'users']['firstName'] and response['lastName'] == self.creds_file['users']['lastName']

        # Verify that user password is not retrived in user details
        assert 'password' not in response.keys()
