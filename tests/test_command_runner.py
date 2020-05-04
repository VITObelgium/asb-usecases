'''
Created on Apr 29, 2020

@author: banyait
'''
import unittest
from asb_usecases.wrappers.command_runner import process_wrapper

class Test(unittest.TestCase):

    def testCommandRunner(self):
        output=process_wrapper.execute('','cd ~ ; pwd ; echo $USER')
        print(output)
        self.assertEqual(
            output['cmdoutput'].split('\n')[0].split('/')[-1],
            output['cmdoutput'].split('\n')[1]
        )

