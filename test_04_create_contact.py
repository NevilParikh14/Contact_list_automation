from base import Base


class TestCreateContact(Base):

    def test_create_contact(self):

        # Get Bearer token
        if not self.token:
            self.create_user()
            self.get_token()
            assert self.token

        # Call to add contacts
        for i in range(len(self.creds_file['contacts'])):
            response_code, response = self.create_contact(
                self.creds_file['contacts'][i])

            # Verify that contact was created
            assert response_code == 201

            # Verify that contact id is retrived in the respnse
            assert response['_id']

        # Call to add contacts withh missing entities
        response_code, response = self.create_contact(
            self.creds_file['contacts'][0]["firstName"])

        # Verify that contact was not created and received an error
        assert response_code != 201
