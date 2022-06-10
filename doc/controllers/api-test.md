# API TEST

```python
api_test_controller = client.api_test
```

## Class Name

`APITESTController`


# Google Search API

```python
def google_search_api(self,
                     part,
                     max_results,
                     q,
                     key,
                     mtype)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `part` | `string` | Query, Required | description of part |
| `max_results` | `string` | Query, Required | Limit of Max Results |
| `q` | `string` | Query, Required | NA |
| `key` | `string` | Query, Required | Value for api key |
| `mtype` | `string` | Query, Required | Type of resource |

## Response Type

`mixed`

## Example Usage

```python
part = 'part2'
max_results = 'maxResults6'
q = 'q0'
key = 'AIzaSyCYWHyYEQOTA5V_o_DHMIdmXd0wiHzB0ns'
mtype = 'video'

result = api_test_controller.google_search_api(part, max_results, q, key, mtype)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 403 | quotaExceeded | `APIException` |
| 404 | not found | `APIException` |

