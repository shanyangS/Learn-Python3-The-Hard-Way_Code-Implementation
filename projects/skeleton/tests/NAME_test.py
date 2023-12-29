import NAME

def setup_teardown():
    print("SETUP!")
    yield
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")