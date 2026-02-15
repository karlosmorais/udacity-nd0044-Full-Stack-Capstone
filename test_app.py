
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgresql://{}/{}".format('postgres:postgres@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            
        self.new_actor = {
            'name': 'Test Actor',
            'age': 25,
            'gender': 'Male'
        }

        self.new_movie = {
            'title': 'Test Movie',
            'release_date': '2023-01-01'
        }
        
        # Define headers for different roles
        self.assistant_header = {'Authorization': os.environ.get('ASSISTANT_TOKEN')}
        self.director_header = {'Authorization': os.environ.get('DIRECTOR_TOKEN')}
        self.producer_header = {'Authorization': os.environ.get('PRODUCER_TOKEN')}

    def tearDown(self):
        """Executed after each test"""
        pass

    # --- PUBLIC ---
    def test_get_greeting(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_request_beyond_valid_page(self):
        res = self.client().get('/unknown')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # --- ACTORS ---
    
    # GET /actors
    def test_get_actors_assistant(self):
        res = self.client().get('/actors', headers=self.assistant_header)
        data = json.loads(res.data)
        # Assuming token is valid or mocked env var allows pass
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) >= 0)

    def test_get_actors_unauthorized(self):
        res = self.client().get('/actors') # No header
        self.assertEqual(res.status_code, 401)

    # POST /actors
    def test_create_actor_director(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.director_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['created'])

    def test_create_actor_assistant_forbidden(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.assistant_header)
        self.assertEqual(res.status_code, 403)

    # PATCH /actors
    def test_update_actor_director(self):
        # Create actor first
        res_create = self.client().post('/actors', json=self.new_actor, headers=self.director_header)
        data_create = json.loads(res_create.data)
        actor_id = data_create['created']

        update_data = {'name': 'Updated Name'}
        res = self.client().patch(f'/actors/{actor_id}', json=update_data, headers=self.director_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor']['name'], 'Updated Name')

    def test_update_actor_assistant_forbidden(self):
         # Create actor first (as director)
        res_create = self.client().post('/actors', json=self.new_actor, headers=self.director_header)
        data_create = json.loads(res_create.data)
        actor_id = data_create['created']

        update_data = {'name': 'Updated Name'}
        res = self.client().patch(f'/actors/{actor_id}', json=update_data, headers=self.assistant_header)
        self.assertEqual(res.status_code, 403)

    # DELETE /actors
    def test_delete_actor_director(self):
         # Create actor first
        res_create = self.client().post('/actors', json=self.new_actor, headers=self.director_header)
        data_create = json.loads(res_create.data)
        actor_id = data_create['created']

        res = self.client().delete(f'/actors/{actor_id}', headers=self.director_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['delete'], actor_id)

    def test_delete_actor_assistant_forbidden(self):
         # Create actor first
        res_create = self.client().post('/actors', json=self.new_actor, headers=self.director_header)
        data_create = json.loads(res_create.data)
        actor_id = data_create['created']

        res = self.client().delete(f'/actors/{actor_id}', headers=self.assistant_header)
        self.assertEqual(res.status_code, 403)


    # --- MOVIES ---

    # GET /movies
    def test_get_movies_assistant(self):
        res = self.client().get('/movies', headers=self.assistant_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    # POST /movies
    def test_create_movie_producer(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_movie_director_forbidden(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.director_header)
        self.assertEqual(res.status_code, 403)

    # PATCH /movies
    def test_update_movie_director(self):
        # Create movie (as producer)
        res_create = self.client().post('/movies', json=self.new_movie, headers=self.producer_header)
        data_create = json.loads(res_create.data)
        movie_id = data_create['created']

        update_data = {'title': 'Updated Title'}
        res = self.client().patch(f'/movies/{movie_id}', json=update_data, headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie']['title'], 'Updated Title')
    
    def test_update_movie_assistant_forbidden(self):
        # Create movie (as producer)
        res_create = self.client().post('/movies', json=self.new_movie, headers=self.producer_header)
        data_create = json.loads(res_create.data)
        movie_id = data_create['created']

        update_data = {'title': 'Updated Title'}
        res = self.client().patch(f'/movies/{movie_id}', json=update_data, headers=self.assistant_header)
        self.assertEqual(res.status_code, 403)

    # DELETE /movies
    def test_delete_movie_producer(self):
        # Create movie
        res_create = self.client().post('/movies', json=self.new_movie, headers=self.producer_header)
        data_create = json.loads(res_create.data)
        movie_id = data_create['created']

        res = self.client().delete(f'/movies/{movie_id}', headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['delete'], movie_id)

    def test_delete_movie_director_forbidden(self):
        # Create movie
        res_create = self.client().post('/movies', json=self.new_movie, headers=self.producer_header)
        data_create = json.loads(res_create.data)
        movie_id = data_create['created']

        res = self.client().delete(f'/movies/{movie_id}', headers=self.director_header)
        self.assertEqual(res.status_code, 403)

# Make the tests executable
if __name__ == "__main__":
    unittest.main()
