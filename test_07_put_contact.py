from base import Base


class TestPutContact(Base):

    def test_Put_contact(self):

        # Get Bearer token
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
        
        # Call to update contact using "PUT" method with single entity in body
        response_code, response = self.update_contact("PUT", contact_id)

        # Verify that API call get's failed if not passed all the entity in "PUT" method
        assert response_code == 400

        # Call to update contact using "PUT" menthod
        response_code, response = self.update_contact("PUT", contact_id, self.creds_file['Update_contact'])

        # Veirfy that API call was successful
        assert response_code in [200, 201]

        # Verify that correct record was updated
        assert response["_id"] == contact_id

        # Call to get updated contact
        response_code, response = self.get_contact(contact_id)

        # Verify that api call was successful
        assert response_code in [200, 201]

        # Verify that correct contact was retrived
        assert response["_id"] == contact_id

        # Verify that all the enetites are updated
        for key in self.creds_file['Update_contact']:
            assert response[key] == self.creds_file['Update_contact'][key]
