alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius > 200:
       return 500
    else:
        return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    global alert_failure_count
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        #global alert_failure_count
        alert_failure_count += 1


alert_in_celcius(400.5)
alert_in_celcius(303.6)
alert_in_celcius(250.0)
assert(network_alert_stub(204.2) == 500)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
# Additional check to validate expectations
expected_failures = 3  # We expect 3 failures based on the above temperatures
if alert_failure_count != expected_failures:
    raise AssertionError(f'Expected {expected_failures} failures but got {alert_failure_count}')
