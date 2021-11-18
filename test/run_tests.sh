#!/usr/bin/env bash

# list of test cases you want to run
tests=(
       test/test_UDFunction.py
       test/test_Calculator.py
       test/test_API.py
)


# decide what driver to use (depending on arguments given)
unit='run --source=undefined -m unittest'
if [[ $# -gt 0 && ${1} == 'coverage' ]]; then
       driver="${@} ${unit}"
elif [[ $# -gt 0 && ${1} == 'pytest'* ]]; then
       driver="${@}"
else
       driver="python3 ${@} ${unit}"
fi

# echo ${driver} ${tests[@]}

# we must add the module source path because we use `import cs107_package` in our test suite and we
# want to test from the source directly (not a package that we have (possibly) installed earlier)

export PYTHONPATH="$(pwd -P)/../src/":${PYTHONPATH}
# run the tests
${driver} ${tests[@]}
