"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn("having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        result = self.client.get('/')
        self.assertIn("Please RSVP", result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)
        self.assertIn("Party Details", result.data)
        self.assertIn("Please RSVP", result.data)
    

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        result = self.client.post("/rsvp", data={"name": 'Mel Melitpolski'})
        self.assertIn("")
        pass
        print "FIXME"


if __name__ == "__main__":
    unittest.main()
