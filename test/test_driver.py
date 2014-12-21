from nose.tools import eq_, raises
from nanodb_driver.driver import Driver, ConnectionTimedOut


class TestDriver(object):
    def test_override_settings(self):
        d = Driver()
        eq_(d.settings['db_url'], "127.0.0.1")
        eq_(d.settings['db_port'], 8000)
        eq_(d.settings['method'], "tcp")


        d = Driver(url="localhost", port=3000)
        eq_(d.settings['db_url'], "localhost")
        eq_(d.settings['db_port'], 3000)
        eq_(d.settings['method'], "tcp")

    @raises(ConnectionTimedOut)
    def test_no_server_query(self):
        d = Driver(timeout=100)
        d._send_command("ping")


    def test_is_connected(self):
        d = Driver(timeout=100)
        eq_(d.is_connected, False)