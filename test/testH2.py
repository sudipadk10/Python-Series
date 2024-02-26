from hello import hello

def test_default():
   assert hello() == "Hello , World"

def test_argument():
   assert hello("Kitty") == "Hello , Kitty"

