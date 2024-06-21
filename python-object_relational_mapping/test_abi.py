import unittest
import mysql.connector # type: ignore
from mysql.connector import errorcode # type: ignore
from subprocess import run, PIPE

class TestOutput(unittest.TestCase):
    script_name = "0-select_states.py"
    db_user = "root"
    db_password = "abimael12!"
    db_name = "hbtn_0e_0_usa"
    expected_output = """(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')"""

    def run_script(self, db_user, db_password, db_name):
        """Run the student's script and return its output."""
        command = ["python3", self.script_name, db_user, db_password, db_name]
        result = run(command, stdout=PIPE, stderr=PIPE, text=True)
        return result.stdout, result.stderr

    def setUp(self):
        """Set up the database for testing."""
        try:
            self.cnx = mysql.connector.connect(user=self.db_user, password=self.db_password)
            self.cursor = self.cnx.cursor()
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
            self.cursor.execute(f"USE {self.db_name}")
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL)"
            )
            self.cursor.execute("DELETE FROM states")
            states = [
                (1, 'California'), (2, 'Arizona'), (3, 'Texas'),
                (4, 'New York'), (5, 'Nevada')
            ]
            self.cursor.executemany("INSERT INTO states (id, name) VALUES (%s, %s)", states)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.cnx.close()

    def tearDown(self):
        """Clean up the database after testing."""
        try:
            self.cnx = mysql.connector.connect(user=self.db_user, password=self.db_password)
            self.cursor = self.cnx.cursor()
            self.cursor.execute(f"DROP DATABASE IF EXISTS {self.db_name}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.cnx.close()

    def test_output(self):
        """Run the student's script and compare the output to the expected output."""
        stdout, stderr = self.run_script(self.db_user, self.db_password, self.db_name)
        self.assertEqual(stdout.strip(), self.expected_output.strip(), f"Actual output: {stdout.strip()}")

    def test_database_connection_error(self):
        """Test handling of database connection errors."""
        stdout, stderr = self.run_script("wrong_user", "wrong_password", self.db_name)
        self.assertIn("Error connecting to the database", stdout, "Database connection error not handled properly!")

    def test_empty_table(self):
        """Test handling of an empty table."""
        empty_db_name = "hbtn_0e_0_usa_empty"
        try:
            self.cnx = mysql.connector.connect(user=self.db_user, password=self.db_password)
            self.cursor = self.cnx.cursor()
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {empty_db_name}")
            self.cursor.execute(f"USE {empty_db_name}")
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL)"
            )
            self.cursor.execute("DELETE FROM states")
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.cnx.close()

        stdout, stderr = self.run_script(self.db_user, self.db_password, empty_db_name)
        self.assertEqual(stdout.strip(), "", "The script should handle empty tables correctly.")

    def test_large_number_of_rows(self):
        """Test handling of a large number of rows in the table."""
        large_db_name = "hbtn_0e_0_usa_large"
        try:
            self.cnx = mysql.connector.connect(user=self.db_user, password=self.db_password)
            self.cursor = self.cnx.cursor()
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {large_db_name}")
            self.cursor.execute(f"USE {large_db_name}")
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL)"
            )
            self.cursor.execute("DELETE FROM states")
            states = [(f'State{i}',) for i in range(1000)]
            self.cursor.executemany("INSERT INTO states (name) VALUES (%s)", states)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.cnx.close()

        stdout, stderr = self.run_script(self.db_user, self.db_password, large_db_name)
        self.assertGreaterEqual(len(stdout.splitlines()), 1000, "Large number of rows handling issue detected!")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
