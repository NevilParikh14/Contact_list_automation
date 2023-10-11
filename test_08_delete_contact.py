from base import Base


class TestDeleteContact(Base):

    def test_delete_contact(self):

        if not self.token:
            self.create_user()
            self.get_token(
                {"email": self.creds_file['users']['email'], "password": self.creds_file['users']['password']})
            assert self.token

            self.create_contact(self.creds_file['contacts'][0])

        # Get Contact id
        response_code, response = self.get_contacts()

        # Verify that contact id is receieved
        assert response_code in [200, 201]

        contact_id = response[0]['_id']

        # Call to delete contact
        response_code, response = self.delete_contact(contact_id)

        # Verify that API call was successful
        assert response_code in [200, 201]

        # Call to get contact
        response_code, response = self.get_contact(contact_id)
        
        # Verify that API throws an error for deleted contact
        assert response_code == 404
