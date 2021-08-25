import unittest


class SesTestCase(unittest.TestCase):
    def test_sendmail(self):
        from we_pyutils.amazonaws.ses import SesMail
        mail = SesMail('zenkr@qq.com', 'Hello World!')
        request_id = mail.send()
        self.assertIsInstance(request_id, str)


if __name__ == '__main__':
    unittest.main()
