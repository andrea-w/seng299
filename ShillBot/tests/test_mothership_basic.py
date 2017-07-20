
import unittest

from mothership.base import MothershipServer
from workers.basic_worker import BasicUserParseWorker


class TestMothershipBasic(unittest.TestCase):
    pass

    def test_mothership_host_port(self):
        '''
        Purpose: asserts that mothership is running on localhost and on port 8999
                (as specified in settings.py)
        Expectation: create instance of MothershipServer, assert values of instance's host and port
        
        :return:
        '''
        ship = MothershipServer()
        self.assertEqual(ship.host, 127.0.0.1)
        self.assertEqual(ship.port, 8999)
        
    def test_mothership_socket(self):
        '''
        Purpose: asserts that mothership's socket created successfully
        Expectation: create instance of MothershipServer, assert that mothership's socket is not None
        
        :return:
        '''
        ship = MothershipServer()
        
        self.assertNotEqual(ship.sock, None)
        
    def test_mothership_worker_connectivity(self):
        '''
        Purpose: asserts that mothership can connect with worker
        Expectation: create instance of MothershipServer & instance of worker, send blank data from worker to
                     MothershipServer. If raises ValueError, worker has successfully connected with Mothership.
                     Otherwise, worker failed to connect with Mothership.
                     
        :return:
        '''
        ship = MothershipServer()
        ship.run()
        
        worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")
        worker.run()
       
        self.assertRaises(ValueError, worker.send_to_mother(worker, None, ship))
        
        
