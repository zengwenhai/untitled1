import os
import unittest


def alltest():
    suite = unittest.TestLoader().discover(
        start_dir = os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite


def run(suite):
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    suite = alltest()
    run(suite)