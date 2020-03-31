README.md

# Contents

These files are meant to accompany a Women Who Code DC Python presentation on debugging and unit testing. https://docs.google.com/presentation/d/1xOST7XJpvihz2KDDtTTw1Pogk0rk7z3g-h2CVKk5S9g/edit?usp=sharing

* debug_examples.py: Some broken code!

* debug_answers.py: Some thoughts about what is wrong in debug_examples.py

* test_example.py: Let's add unit tests to fizz_buzz

* test_debug_examples.py: Add test cases to debug functions. Some of these will be broken until you update the code!

# How to Run

* Execute examples in debug_examples.py by uncommenting/saving and then running `python debug_examples.py`

* Use the pdb interactive debugger by adding this to your code where you want the debugger to start. You will be able to step through the execution. See https://docs.python.org/3/library/pdb.html for details.

```
# don't forget to remove this from your final code!
import pdb; pdb.set_trace()
```

* Run the tests on the command line using `python -m unitttest <name of test file>`

