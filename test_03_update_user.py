from base import Base


class TestUpdateUser(Base):

    def test_update_user(self):

        # Get Bearer token
        if not self.token:
            self.create_user()
            self.get_token(
                {"email": self.creds_file['users']['email'], "password": self.creds_file['users']['password']})
            assert self.token

        # API call to update user details
        response_code, response = self.update_user()

        # Verify that user details was updated
        assert response_code == 200

        # Verify that user id is returned in respoonse
        assert response['_id']

        # Veriify that user password is not retrived in response
        assert 'password' not in response.keys()

        # API call to fetch the user details
        response_code, response = self.get_user()

        # Veirfy that user inf was retrived
        assert response_code == 200

        # Verify that user data is updated
        assert response['email'] == self.creds_file['updated_users']['email'] and response['firstName'] == self.creds_file[
            'updated_users']['firstName'] and response['lastName'] == self.creds_file['updated_users']['lastName']

        self.reset_user_details()
