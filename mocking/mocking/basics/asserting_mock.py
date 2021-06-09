from unittest.mock import Mock

json = Mock()
json.loads('{"key": "value"}')

json.loads.assert_called()
json.loads.assert_called_once()
# called with assertions must match the *args, **kwargs
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')

json.loads('{"key2": "value2"}')

# failed assertions will raise an AssertionError
# json.loads.assert_called_once()
# json.loads.assert_called_once_with('{"key": "value"}')
# json.loads.assert_not_called()

print(json.loads.call_count)
# last call
print(json.loads.call_args)
# all calls
print(json.loads.call_args_list)
print(json.method_calls)

