import unittest
from backend.db import create_user, get_user_by_email, update_user
from backend.auth import hash_password


class TestDB(unittest.TestCase):
    def test_create_and_get_user(self):
        hashed_password = hash_password('Martin2005')
        user_id = create_user("testuser1234@example.com", "Martin", "Gogulanov", hashed_password)
        self.assertIsInstance(user_id, int)

        user = get_user_by_email("testuser1234@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user["email"], "testuser1234@example.com")

    def test_update_user(self):
        hashed_password = hash_password('Martin2005')
        update_user("testuser1234@example.com", "Martin", "Gogulanov", hashed_password)
        updated_user = get_user_by_email("testuser1234@example.com")
        self.assertEqual(updated_user["first_name"], "Martin")

if __name__ == '__main__':
    unittest.main()
