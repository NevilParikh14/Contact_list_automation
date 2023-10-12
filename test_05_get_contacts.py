from base import Base


class TestFetchContacts(Base):

    def test_get_contacts(self):

        # Get Bearer token
        if not self.token:
            self.create_user()
            self.get_token()
            assert self.token
            self.delete_contacts()
            for i in range(len(self.creds_file['contacts'])):
                self.create_contact(self.creds_file['contacts'][i])

        # Call to get Contact List
        response_code, response = self.get_contacts()

        # Verify that contact list was retrived
        assert response_code in [200, 201]

        # Verify that contact list count is same as it was created
        assert len(response) == len(self.creds_file['contacts'])

        # Collect all the contact ids from the list
        contact_ids = []
        for i in range(len(response)):
            contact_ids.append(response[i]['_id'])

        # Call to collect single contact
        for id in contact_ids:
            response_code, response = self.get_contact(id)

            # Verify that call was successful
            assert response_code in [200, 201]

            # Verify that received contact id that was passed during API call
            assert response["_id"] == id
