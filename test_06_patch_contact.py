from base import Base


class TestPatchContact(Base):

    def test_patch_contact(self):
        # Get Bearer token
        if not self.token:
            self.create_user()
            self.get_token()
            assert self.token

            self.create_contact(self.creds_file['contacts'][0])

        # Get Contact id
        response_code, response = self.get_contacts()

        # Verify that contact id is receieved
        assert response_code in [200, 201]

        contact_id = response[0]['_id']

        # Update any single contact entity
        response_code, response = self.update_contact("PATCH", contact_id)

        # Verify that API call was successful
        assert response_code in [200, 201]

        # Verify that the correct contact was updated
        assert response["_id"] == contact_id

        # Call to get contact
        response_code, response = self.get_contact(contact_id)

        # Verify that API call was successful
        assert response_code in [200, 201]

        # Verify that the correct contact details are receieved
        assert response["_id"] == contact_id

        # Verify that the value is updated
        for key in self.updated_values:
            assert response[key] == self.updated_values[key]
