# The Python library for the Web of Science API Lite
A responsive API that supports rich searching across the Web of Science Core Collection to retrieve core article metadata.  This service provides a great way to reuse Web of Science data both internally and externally to enhance  institutional repositories and research networking systems with best-in-class data. This API supports searching across the Web of Science to retrieve item-level metadata with limited fields:  
- UT (Unique Identifier) 
- Authors - Author keywords 
- Document type 
- Title 
- Issue 
- Pages 
- Publication date 
- Source title 
- Volume 
- DOI 
- ISBN 
- ISSN   
  
The API supports JSON and XML responses, but this client works with JSON responses only. 

- API version: 1.0
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

You can install directly from Github

```sh
pip install git+https://github.com/Clarivate-SAR/woslite_py_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Clarivate-SAR/woslite_py_client.git`)

Then import the package:

```python
import woslite_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import woslite_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import woslite_client
from woslite_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: key
configuration = woslite_client.Configuration()
configuration.api_key['X-ApiKey'] = 'YOUR_API_KEY'

# create an instance of the API class
integration_api_instance = woslite_client.IntegrationApi(woslite_client.ApiClient(configuration))
search_api_instance = woslite_client.SearchApi(woslite_client.ApiClient(configuration))
database_id = 'WOS'  # str | Database to search. Must be a valid database ID, one of the following: BCI/BIOABS/BIOSIS/CCC/DCI/DIIDW/MEDLINE/WOK/WOS/ZOOREC. WOK represents all databases.
unique_id = 'WOS:000270372400005'  # str | Primary item(s) id to be searched, ex: WOS:000270372400005. Cannot be null or an empty string. Multiple values are separated by comma.
usr_query = 'TS=(cadmium)'  # str | User query for requesting data, ex: TS=(cadmium). The query parser will return errors for invalid queries.
count = 1  # int | Number of records returned in the request
first_record = 1  # int | Specific record, if any within the result set to return. Cannot be less than 1 and greater than 100000.
lang = 'en'  # str | Language of search. This element can take only one value: en for English. If no language is specified, English is passed by default. (optional)
sort_field = 'PY+D'  # str | Order by field(s). Field name and order by clause separated by '+', use A for ASC and D for DESC, ex: PY+D. Multiple values are separated by comma. (optional)

try:
    # Find record(s) by specific id
    api_response = integration_api_instance.id_unique_id_get(database_id, unique_id, count, first_record, lang=lang,
                                                             sort_field=sort_field)
    # for more details look at the models
    firstAuthor = api_response.data[0].author.authors[0]
    print("Response: ")
    pprint(api_response)
    pprint("First author: " + firstAuthor)
except ApiException as e:
    print("Exception when calling IntegrationApi->id_unique_id_get: %s\\n" % e)

try:
    # Find record(s) by user query
    api_response = search_api_instance.root_get(database_id, usr_query, count, first_record, lang=lang,
                                                             sort_field=sort_field)
    # for more details look at the models
    firstAuthor = api_response.data[0].author.authors[0]
    print("Response: ")
    pprint(api_response)
    pprint("First author: " + firstAuthor)
except ApiException as e:
    print("Exception when calling SearchApi->root_get: %s\\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.clarivate.com/api/woslite*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IntegrationApi* | [**id_unique_id_get**](docs/IntegrationApi.md#id_unique_id_get) | **GET** /id/{uniqueId} | Find record(s) by specific id
*SearchApi* | [**query_query_id_get**](docs/SearchApi.md#query_query_id_get) | **GET** /query/{queryId} | Fetch record(s) by query identifier
*SearchApi* | [**root_get**](docs/SearchApi.md#root_get) | **GET** / | Submits a user query and returns results

## Documentation For Models

 - [Author](docs/Author.md)
 - [Doctype](docs/Doctype.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Keyword](docs/Keyword.md)
 - [Other](docs/Other.md)
 - [QueryResult](docs/QueryResult.md)
 - [Source](docs/Source.md)
 - [WosLiteRecord](docs/WosLiteRecord.md)
 - [WosLiteRecordTitle](docs/WosLiteRecordTitle.md)
 - [WosLiteResponse](docs/WosLiteResponse.md)

## Documentation For Authorization


## key

- **Type**: API key
- **API key parameter name**: X-ApiKey
- **Location**: HTTP header


## Licence
MIT


