import unittest
import twi_api as TA

class TestCase(unittest.TestCase):
    def test_numOfTweet(self):
        # number of input tweets should be an integer from 0 to 2000
        print("Test the input of numOfTweet")
        nums = ['abc', '100000', '-1']
        for num in nums:
            input_num = TA.test_numOfTweet(num)
            self.assertEqual(input_num, "input_num_wrong")

    def test_sentiment_analyze(self):
        # if 0 tweet found, program should be stopped
        print()
        print("Test sentiment_analyze")
        keyword = "cnosjvbwpurxncsdjn"
        tweet_list = TA.get_twi_list(keyword, 10)
        tw_list = TA.sentiment_analyze(tweet_list)
        self.assertEqual(tw_list.empty, True)

    def test_search_limit(self):
        # stop searching when search 15 times in 15 minutes
        print()
        print("Test if up to the limit of tweet search")
        alert = TA.search_limit_alert(20, 16)
        self.assertEqual(alert, True)
        alert = TA.search_limit_alert(12, 16)
        self.assertEqual(alert, True)
        alert = TA.search_limit_alert(12, 1)
        self.assertEqual(alert, False)


if __name__ == '__main__':
    print("Start Testing...")
    unittest.main()
