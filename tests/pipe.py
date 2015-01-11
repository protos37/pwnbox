import unittest
import pwnbox

class TestProcessPipe(unittest.TestCase):
    def setUp(self):
        self.pipe = pwnbox.ProcessPipe("cat")

    def test_readwrite(self):
        self.pipe.write("Hello World!\n")
        s = ""
        while len(s) < len("Hello World!\n"):
            s += self.pipe.read()
        self.assertEqual("Hello World!\n", s)

    def test_readline(self):
        self.pipe.write("Hello World!\n")
        self.assertEqual("Hello World!\n", self.pipe.readline())

    def test_readuntil(self):
        self.pipe.write("Hello World!\n")
        self.assertEqual("Hello World!", self.pipe.read(until = "rld!"))
        self.assertEqual("\n", self.pipe.read(until = "\n"))

    def tearDown(self):
        self.pipe.close()
