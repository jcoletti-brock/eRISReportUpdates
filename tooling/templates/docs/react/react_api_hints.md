# API Integration

- Evaluate the API and Slice for the specific model being used

**API Pattern**

- Fetching data that will be managed by the Redux store should be done with a _Thunk_
- CRUD operations that don't require store interaction should follow the Async API Call pattern detailed below
- CRUD operations that require immediate verification to perform a subsequent step should follow the Sync API Call pattern detailed below

## Thunks

- Dispatch the appropriate action
- Errors should be triggered off of the appropriate error state in found in the redux store (associated selector).

## Async API Calls

- API calls with no Redux integration as results are not stateful or do not require state management.
- Function signature follows callGrpcEndpoint( params, successCallback, errorCallback )
- Use errorHandler found in genericError.js

### Definition of an Async API Call

```javascript
/**
 * javascript docs here
 */
export async function apiCall(params, successCallback, errorCallback) {
	let client = await createClient(<servicename>ServicePromiseClient);
	const request = new ApiRequestObject();

    // Logic here

	client.apiCall(request, {}).then(response => successCallback(response.toObject()), errorCallback);
}
```

### Usage of Async API Calls

```javascript
if (requiredParam) {
  apiFunction(
    /* param1: */ param1,
    /* param2: */ param2,
    successCallback, // Callback for successful API response
    (reason) => errorHandler(reason, dispatch)
  );
}
```

### Sync API Calls

- API calls with no Redux integration that require immediate validation for subsequent steps in the same call.
- Function signature follows callGrpcEndpoint(params)
- Awaits the response and returns the object directly.

### Definition of a Sync API Call

```javascript

/**
 * Creates a new measurement record for a quality recipe.
 * @param {Object} params - our list of params here
 * @returns {Object} Our return object
 */
export async function apiMethodNameSync(param1, param2) {
	let client = await createClient(<servicename>ServicePromiseClient);
	const request = new apiCallRequest();

    /**
     * logic to set params
     * /

	const response = await client.apiCall(request, {});
	return response.getResults.toObject();
}
```

### Usage of Sync API Calls

```javascript
let result = await apiCall(params);
```
