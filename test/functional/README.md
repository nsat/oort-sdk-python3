# Python 3 SDK Functional Tests

Functional tests for `oort_sdk_client`. Each test spins up a real `oort-agent` and talks to it over HTTP.

## Quick start

Build the agent first (needs Docker + cmake):

    make -C agent

Then run the tests (builds the SDK client automatically):

    cd SDK && make python3-test

Or manually:

    cd SDK && make python3
    cd samples/python3-functional
    poetry install
    poetry run pip install ../../python3-sdk-client
    poetry run pytest . -v

## Custom agent binary

    OORT_AGENT=/path/to/oort-agent make python3-test
