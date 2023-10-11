from base import Base


class TestLogoutUser(Base):

    def test_logout_user(self):

        # Get Bearer Token
        if not self.token:
            self.create_user()
            self.get_token(
                {"email": self.creds_file['users']['email'], "password": self.creds_file['users']['password']})
            assert self.token

        # Logout the User
        
        response_code, response = self.logout()

        # Verify that user was logout successfully
        assert response_code == 200

        self.token = ""

        # Call Get User API
        response_code, response = self.get_user()

        # Verify that api returns error when try to perform action on loged out user
        assert response_code == 401

        # Call Get Contacts API
        response_code, response = self.get_contacts()

        # Verify that api returns error when try to perform action on loged out user
        assert response_code == 401
