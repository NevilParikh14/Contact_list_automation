from base import Base


class TestCreateUser(Base):

    def test_valid_details(self):

        self.delete_user()

        # Call to create a user
        response_code, response = self.create_user()

        # Verify that the API call was successful
        assert response_code == 201

        # Veirfy that the user was created
        assert response['user']

        # Verify that a token is received that can be used for performing other actions
        assert response['token']
    
    def test_user_login(self):

        self.get_token()

        # Verify that user is able to login
        assert self.token

    def test_empty_details(self):

        # Test case for empty user details
        response_code, response = self.create_user({})
        
        # Verify that if provided empty body then api throws error
        assert response_code == 400

    def test_required_fields(self):

        # Loop to check the required fields while creating user
        for i in self.creds_file['users']:
            dup_creds_file = self.creds_file['users'].copy()
            dup_creds_file[i] = ""
            response_code, response = self.create_user(dup_creds_file)
            
            # Verify that if provided empty value in required values then API returns error
            assert response_code == 400
            
            dup_creds_file.pop(i)
            response_code, response = self.create_user(dup_creds_file)
            
            # Verify that if not provided required value then API returns error
            assert response_code == 400

    def test_duplicate_user(self):

        # Create duplicate user
        response_code, response = self.create_user()

        # Verify that duplicate user cannot be created
        assert response_code == 400

        assert response