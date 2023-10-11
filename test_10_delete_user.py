from base import Base


class TestDeleteUser(Base):

    def test_delete_user(self):
        # Get Bearer Token
        if not self.token:
            self.create_user()
            self.get_token(
                {"email": self.creds_file['users']['email'], "password": self.creds_file['users']['password']})
            assert self.token

        # Call to delete the user
        response_code, response = self.delete_user()

        # Verify that user was deleted successfuly
        assert response_code == 200

        # Call to get user details
        response_code, response = self.get_user()

        # Verify that api returns error when tried to call deleted user
        assert response_code == 401

        self.token = ""

        # Veirfy that deleted user is not able to login
        self.get_token(
            {"email": self.creds_file['users']['email'], "password": self.creds_file['users']['password']})
        assert not self.token
