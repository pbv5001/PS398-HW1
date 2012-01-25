import unittest
import HW1

class TestHW1Code(unittest.TestCase):
  
  def setUp(self):
    return
  
  def test_shoutone(self):
    self.assertEqual(HW1.shout("Hello"), "HELLO!") #One word
  
  def test_shouttwo(self):
    self.assertEqual(HW1.shout("Hello again"), "HELLO AGAIN!") #Sentence
	
  def test_shoutthree(self):
    self.assertEqual(HW1.shout("Exclaimed Hello!!!"), "EXCLAIMED HELLO!!!!") #Punctuation
	
  def test_shoutfour(self):
    self.assertEqual(HW1.shout("CAPS?"), "CAPS!!") #Already in caps, add a different punctuation
	
  def stest_shoutfive(self):
    self.assertEqual(HW1.shout("Multiple periods..."), "MULTIPLE PERIODS!!!") #turn punctuation into exclaimation =
	
  def test_reverseone(self):
    self.assertEqual(HW1.reverse("Test one"), "eno tseT") #basic reversal
  
  def test_reversetwo(self):
    self.assertEqual(HW1.reverse("Punctuation test..."), "...tset noitautcnuP") 
	
  def test_reversewordsone(self):
    self.assertEqual(HW1.reversewords("Test one."), "one Test.") 
  
  def test_reversewordstwo(self):
    self.assertEqual(HW1.reversewords("Punctuation test..."), "test... Punctuation.") 
	
  def test_reversewordlettersone(self):
    self.assertEqual(HW1.reversewordletters("This is a test."), "sihT si a tset.") 
  
  def test_reversewordletterstwo(self):
    self.assertEqual(HW1.reversewordletters("This sentence has a lot of words."), "sihT ecnetnes sah a tol fo sdrow.") 
	
  #def piglatin_test_one(self):
   # self.assertEqual(HW1.piglatin("This is a test."), "isThe ise .") #basic reversal
  
  #def piglatin_test_two(self):
    #self.assertEqual(HW1.piglatin("This sentence has a lot of words."), "sihT ecnetnes sah a tol fo sdrow.") #Sentence
	
  
if __name__ == '__main__':
  unittest.main()