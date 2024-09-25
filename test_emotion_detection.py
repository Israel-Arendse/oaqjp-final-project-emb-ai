# Import unititest library.
import unittest

# Import emotion_detector from the EmotionDetection package.
from EmotionDetection.emotion_detection import emotion_detector

# Define the unit test for emotions, joy, anger, disgust, sadness, and fear.
class test_emotion_detection(unittest.TestCase):

  def test_emotion_detector(self):
      # Test case for dominant emotion: joy
      # The dominant emotion is joy when "I am glad this happend' is sent as input.
      test_1 = emotion_detector('I am glad this happend')
      self.assertEqual(test_1['emotion'], 'joy')
      
      # Test case for dominant emotion: anger
      # The dominant emotion is anger when 'I am really mad about this' is sent as input.
      test_2 = emotion_detector('I am really mad about this')
      self.assertEqual(test_2['emotion'], 'anger')

      # Test case for dominant emotion: disgust
      # The dominant emotion is disgust when 'I feel disgusted just about this' is sent as input.
      test_3 = emotion_detector('I feel disgusted just hearing about this')
      self.assertEqual(test_3['emotion'], 'disgust')

      # Test case for dominant emotion: sadness
      # The dominant emotion is sadness when 'I feel so sad about this' is sent as input.
      test_4 = emotion_detector('I am so sad about this')
      self.assertEqual(test_4['emotion'], 'sadness')

      # Test case for dominant emotion: fear
      # The dominant emotion is fear when 'I am really afraid that this will happen' is sent as input.
      test_5 = emotion_detector('I am really afraid this will happend')
      self.assertEqual(test_5['emotion'], 'fear')


# Run all the test casess in the module upon script execution
unittest.main()
