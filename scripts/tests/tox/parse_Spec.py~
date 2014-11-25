import unittest
import random
import subprocess


def call_ff(option):
    return subprocess.Popen("ff "+option, shell=True, stdout=PIPE).stdout.read()


#JUST AN EXAMPLE HERE, REAL BELOW
class Test_Example(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
        
        
class Test_Installed(unittest.TestCase): #look into tox and virtualenv, as that will be used for testing!
    def setUp(self):
        pass
    def test_run(self):
        return_code = subprocess.call("ff --status", shell=True)
        self.assertTrue(return_code > 0)
    def test_parsepy(self):
        self.parsed_py = call_ff('--parse test.py')
        self.assertTrue(len(self.parsed_py) > 5)
    def test_parsec(self):
        self.parsed_c = call_ff('--parse test.c')
        self.assertTrue(len(self.parsed_c) > 5)
    def test_parsejava(self):
        self.parsed_j = call_ff('--parse test.java')
        self.assertTrue(len(self.parsed_java) > 5)
    #Guys please write more tests.

        
if __name__ == '__main__':
    unittest.main()
