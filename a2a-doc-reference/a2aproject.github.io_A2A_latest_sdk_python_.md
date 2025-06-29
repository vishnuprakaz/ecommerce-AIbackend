---
url: "https://a2aproject.github.io/A2A/latest/sdk/python/"
title: "Python - Agent2Agent (A2A) Protocol"
---

[Skip to content](https://a2aproject.github.io/A2A/latest/sdk/python/#python-sdk-reference)

# Python SDK Reference [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#python-sdk-reference "Permanent link")

This page contains SDK documentation for the [`a2a-sdk`](https://github.com/google-a2a/a2a-python) Python package.

```md-code__content
pip install a2a-sdk

```

The A2A Python SDK.

## `auth` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.auth "Permanent link")

### `user` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.auth.user "Permanent link")

Authenticated user information.

#### `UnauthenticatedUser` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.auth.user.UnauthenticatedUser "Permanent link")

Bases: `User`

A representation that no user has been authenticated in the request.

##### `is_authenticated``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.auth.user.UnauthenticatedUser.is_authenticated "Permanent link")

Returns whether the current user is authenticated.

##### `user_name``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.auth.user.UnauthenticatedUser.user_name "Permanent link")

Returns the user name of the current user.

#### `User` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.auth.user.User "Permanent link")

Bases: `ABC`

A representation of an authenticated user.

##### `is_authenticated``abstractmethod``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.auth.user.User.is_authenticated "Permanent link")

Returns whether the current user is authenticated.

##### `user_name``abstractmethod``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.auth.user.User.user_name "Permanent link")

Returns the user name of the current user.

## `client` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client "Permanent link")

Client-side components for interacting with an A2A agent.

### `A2ACardResolver` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2ACardResolver "Permanent link")

Agent Card resolver.

#### `agent_card_path = agent_card_path.lstrip('/')``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2ACardResolver.agent_card_path "Permanent link")

#### `base_url = base_url.rstrip('/')``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2ACardResolver.base_url "Permanent link")

#### `httpx_client = httpx_client``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2ACardResolver.httpx_client "Permanent link")

#### `get_agent_card(relative_card_path=None, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2ACardResolver.get_agent_card "Permanent link")

Fetches an agent card from a specified path relative to the base\_url.

If relative\_card\_path is None, it defaults to the resolver's configured
agent\_card\_path (for the public agent card).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `relative_card_path` | `str | None` | Optional path to the agent card endpoint,<br>relative to the base URL. If None, uses the default public<br>agent card path. | `None` |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.get request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `AgentCard` | An `AgentCard` object representing the agent's capabilities. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON<br>or validated against the AgentCard schema. |

### `A2AClient` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient "Permanent link")

A2A Client for interacting with an A2A agent.

#### `httpx_client = httpx_client``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient.httpx_client "Permanent link")

#### `url = agent_card.url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient.url "Permanent link")

#### `cancel_task(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient.cancel_task "Permanent link")

Requests the agent to cancel a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `CancelTaskRequest` | The `CancelTaskRequest` object specifying the task ID. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `CancelTaskResponse` | A `CancelTaskResponse` object containing the updated Task with canceled status or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

#### `get_client_from_agent_card_url(httpx_client, base_url, agent_card_path='/.well-known/agent.json', http_kwargs=None)``async``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient.get_client_from_agent_card_url "Permanent link")

Fetches the public AgentCard and initializes an A2A client.

This method will always fetch the public agent card. If an authenticated
or extended agent card is required, the A2ACardResolver should be used
directly to fetch the specific card, and then the A2AClient should be
instantiated with it.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `httpx_client` | `AsyncClient` | An async HTTP client instance (e.g., httpx.AsyncClient). | _required_ |
| `base_url` | `str` | The base URL of the agent's host. | _required_ |
| `agent_card_path` | `str` | The path to the agent card endpoint, relative to the base URL. | `'/.well-known/agent.json'` |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.get request when fetching the agent card. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `A2AClient` | An initialized `A2AClient` instance. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs fetching the agent card. |
| `A2AClientJSONError` | If the agent card response is invalid. |

#### `get_task(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient.get_task "Permanent link")

Retrieves the current state and history of a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `GetTaskRequest` | The `GetTaskRequest` object specifying the task ID and history length. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `GetTaskResponse` | A `GetTaskResponse` object containing the Task or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

#### `get_task_callback(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient.get_task_callback "Permanent link")

Retrieves the push notification configuration for a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `GetTaskPushNotificationConfigRequest` | The `GetTaskPushNotificationConfigRequest` object specifying the task ID. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `GetTaskPushNotificationConfigResponse` | A `GetTaskPushNotificationConfigResponse` object containing the configuration or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

#### `send_message(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient.send_message "Permanent link")

Sends a non-streaming message request to the agent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `SendMessageRequest` | The `SendMessageRequest` object containing the message and configuration. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `SendMessageResponse` | A `SendMessageResponse` object containing the agent's response (Task or Message) or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

#### `send_message_streaming(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient.send_message_streaming "Permanent link")

Sends a streaming message request to the agent and yields responses as they arrive.

This method uses Server-Sent Events (SSE) to receive a stream of updates from the agent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `SendStreamingMessageRequest` | The `SendStreamingMessageRequest` object containing the message and configuration. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. A default `timeout=None` is set but can be overridden. | `None` |

Yields:

| Type | Description |
| --- | --- |
| `AsyncGenerator[SendStreamingMessageResponse]` | `SendStreamingMessageResponse` objects as they are received in the SSE stream. |
| `AsyncGenerator[SendStreamingMessageResponse]` | These can be Task, Message, TaskStatusUpdateEvent, or TaskArtifactUpdateEvent. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP or SSE protocol error occurs during the request. |
| `A2AClientJSONError` | If an SSE event data cannot be decoded as JSON or validated. |

#### `set_task_callback(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClient.set_task_callback "Permanent link")

Sets or updates the push notification configuration for a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `SetTaskPushNotificationConfigRequest` | The `SetTaskPushNotificationConfigRequest` object specifying the task ID and configuration. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `SetTaskPushNotificationConfigResponse` | A `SetTaskPushNotificationConfigResponse` object containing the confirmation or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

### `A2AClientError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClientError "Permanent link")

Bases: `Exception`

Base exception for A2A Client errors.

### `A2AClientHTTPError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClientHTTPError "Permanent link")

Bases: `A2AClientError`

Client exception for HTTP errors received from the server.

#### `message = message``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClientHTTPError.message "Permanent link")

#### `status_code = status_code``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClientHTTPError.status_code "Permanent link")

### `A2AClientJSONError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClientJSONError "Permanent link")

Bases: `A2AClientError`

Client exception for JSON errors during response parsing or validation.

#### `message = message``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AClientJSONError.message "Permanent link")

### `A2AGrpcClient` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AGrpcClient "Permanent link")

A2A Client for interacting with an A2A agent via gRPC.

#### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AGrpcClient.agent_card "Permanent link")

#### `stub = grpc_stub``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AGrpcClient.stub "Permanent link")

#### `cancel_task(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AGrpcClient.cancel_task "Permanent link")

Requests the agent to cancel a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `TaskIdParams` | The `TaskIdParams` object specifying the task ID. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `Task` | A `Task` object containing the updated Task |

#### `get_task(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AGrpcClient.get_task "Permanent link")

Retrieves the current state and history of a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `TaskQueryParams` | The `TaskQueryParams` object specifying the task ID | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `Task` | A `Task` object containing the Task or None. |

#### `get_task_callback(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AGrpcClient.get_task_callback "Permanent link")

Retrieves the push notification configuration for a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `TaskIdParams` | The `TaskIdParams` object specifying the task ID. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `TaskPushNotificationConfig` | A `TaskPushNotificationConfig` object containing the configuration. |

#### `send_message(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AGrpcClient.send_message "Permanent link")

Sends a non-streaming message request to the agent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `MessageSendParams` | The `MessageSendParams` object containing the message and configuration. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `Task | Message` | A `Task` or `Message` object containing the agent's response. |

#### `send_message_streaming(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AGrpcClient.send_message_streaming "Permanent link")

Sends a streaming message request to the agent and yields responses as they arrive.

This method uses gRPC streams to receive a stream of updates from the
agent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `MessageSendParams` | The `MessageSendParams` object containing the message and configuration. | _required_ |

Yields:

| Type | Description |
| --- | --- |
| `AsyncGenerator[Message | Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent]` | `Message` or `Task` or `TaskStatusUpdateEvent` or |
| `AsyncGenerator[Message | Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent]` | `TaskArtifactUpdateEvent` objects as they are received in the |
| `AsyncGenerator[Message | Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent]` | stream. |

#### `set_task_callback(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.A2AGrpcClient.set_task_callback "Permanent link")

Sets or updates the push notification configuration for a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `TaskPushNotificationConfig` | The `TaskPushNotificationConfig` object specifying the task ID and configuration. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `TaskPushNotificationConfig` | A `TaskPushNotificationConfig` object containing the config. |

### `create_text_message_object(role=Role.user, content='')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.create_text_message_object "Permanent link")

Create a Message object containing a single TextPart.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `role` | `Role` | The role of the message sender (user or agent). Defaults to Role.user. | `user` |
| `content` | `str` | The text content of the message. Defaults to an empty string. | `''` |

Returns:

| Type | Description |
| --- | --- |
| `Message` | A `Message` object with a new UUID messageId. |

### `client` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client "Permanent link")

#### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.logger "Permanent link")

#### `A2ACardResolver` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2ACardResolver "Permanent link")

Agent Card resolver.

##### `agent_card_path = agent_card_path.lstrip('/')``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2ACardResolver.agent_card_path "Permanent link")

##### `base_url = base_url.rstrip('/')``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2ACardResolver.base_url "Permanent link")

##### `httpx_client = httpx_client``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2ACardResolver.httpx_client "Permanent link")

##### `get_agent_card(relative_card_path=None, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2ACardResolver.get_agent_card "Permanent link")

Fetches an agent card from a specified path relative to the base\_url.

If relative\_card\_path is None, it defaults to the resolver's configured
agent\_card\_path (for the public agent card).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `relative_card_path` | `str | None` | Optional path to the agent card endpoint,<br>relative to the base URL. If None, uses the default public<br>agent card path. | `None` |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.get request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `AgentCard` | An `AgentCard` object representing the agent's capabilities. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON<br>or validated against the AgentCard schema. |

#### `A2AClient` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient "Permanent link")

A2A Client for interacting with an A2A agent.

##### `httpx_client = httpx_client``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient.httpx_client "Permanent link")

##### `url = agent_card.url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient.url "Permanent link")

##### `cancel_task(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient.cancel_task "Permanent link")

Requests the agent to cancel a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `CancelTaskRequest` | The `CancelTaskRequest` object specifying the task ID. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `CancelTaskResponse` | A `CancelTaskResponse` object containing the updated Task with canceled status or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

##### `get_client_from_agent_card_url(httpx_client, base_url, agent_card_path='/.well-known/agent.json', http_kwargs=None)``async``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient.get_client_from_agent_card_url "Permanent link")

Fetches the public AgentCard and initializes an A2A client.

This method will always fetch the public agent card. If an authenticated
or extended agent card is required, the A2ACardResolver should be used
directly to fetch the specific card, and then the A2AClient should be
instantiated with it.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `httpx_client` | `AsyncClient` | An async HTTP client instance (e.g., httpx.AsyncClient). | _required_ |
| `base_url` | `str` | The base URL of the agent's host. | _required_ |
| `agent_card_path` | `str` | The path to the agent card endpoint, relative to the base URL. | `'/.well-known/agent.json'` |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.get request when fetching the agent card. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `A2AClient` | An initialized `A2AClient` instance. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs fetching the agent card. |
| `A2AClientJSONError` | If the agent card response is invalid. |

##### `get_task(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient.get_task "Permanent link")

Retrieves the current state and history of a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `GetTaskRequest` | The `GetTaskRequest` object specifying the task ID and history length. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `GetTaskResponse` | A `GetTaskResponse` object containing the Task or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

##### `get_task_callback(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient.get_task_callback "Permanent link")

Retrieves the push notification configuration for a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `GetTaskPushNotificationConfigRequest` | The `GetTaskPushNotificationConfigRequest` object specifying the task ID. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `GetTaskPushNotificationConfigResponse` | A `GetTaskPushNotificationConfigResponse` object containing the configuration or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

##### `send_message(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient.send_message "Permanent link")

Sends a non-streaming message request to the agent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `SendMessageRequest` | The `SendMessageRequest` object containing the message and configuration. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `SendMessageResponse` | A `SendMessageResponse` object containing the agent's response (Task or Message) or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

##### `send_message_streaming(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient.send_message_streaming "Permanent link")

Sends a streaming message request to the agent and yields responses as they arrive.

This method uses Server-Sent Events (SSE) to receive a stream of updates from the agent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `SendStreamingMessageRequest` | The `SendStreamingMessageRequest` object containing the message and configuration. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. A default `timeout=None` is set but can be overridden. | `None` |

Yields:

| Type | Description |
| --- | --- |
| `AsyncGenerator[SendStreamingMessageResponse]` | `SendStreamingMessageResponse` objects as they are received in the SSE stream. |
| `AsyncGenerator[SendStreamingMessageResponse]` | These can be Task, Message, TaskStatusUpdateEvent, or TaskArtifactUpdateEvent. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP or SSE protocol error occurs during the request. |
| `A2AClientJSONError` | If an SSE event data cannot be decoded as JSON or validated. |

##### `set_task_callback(request, *, http_kwargs=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.client.A2AClient.set_task_callback "Permanent link")

Sets or updates the push notification configuration for a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `SetTaskPushNotificationConfigRequest` | The `SetTaskPushNotificationConfigRequest` object specifying the task ID and configuration. | _required_ |
| `http_kwargs` | `dict[str, Any] | None` | Optional dictionary of keyword arguments to pass to the<br>underlying httpx.post request. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `SetTaskPushNotificationConfigResponse` | A `SetTaskPushNotificationConfigResponse` object containing the confirmation or an error. |

Raises:

| Type | Description |
| --- | --- |
| `A2AClientHTTPError` | If an HTTP error occurs during the request. |
| `A2AClientJSONError` | If the response body cannot be decoded as JSON or validated. |

### `errors` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.errors "Permanent link")

Custom exceptions for the A2A client.

#### `A2AClientError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.errors.A2AClientError "Permanent link")

Bases: `Exception`

Base exception for A2A Client errors.

#### `A2AClientHTTPError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.errors.A2AClientHTTPError "Permanent link")

Bases: `A2AClientError`

Client exception for HTTP errors received from the server.

##### `message = message``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.errors.A2AClientHTTPError.message "Permanent link")

##### `status_code = status_code``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.errors.A2AClientHTTPError.status_code "Permanent link")

#### `A2AClientJSONError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.errors.A2AClientJSONError "Permanent link")

Bases: `A2AClientError`

Client exception for JSON errors during response parsing or validation.

##### `message = message``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.errors.A2AClientJSONError.message "Permanent link")

### `grpc_client` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client "Permanent link")

#### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.logger "Permanent link")

#### `A2AGrpcClient` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.A2AGrpcClient "Permanent link")

A2A Client for interacting with an A2A agent via gRPC.

##### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.A2AGrpcClient.agent_card "Permanent link")

##### `stub = grpc_stub``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.A2AGrpcClient.stub "Permanent link")

##### `cancel_task(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.A2AGrpcClient.cancel_task "Permanent link")

Requests the agent to cancel a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `TaskIdParams` | The `TaskIdParams` object specifying the task ID. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `Task` | A `Task` object containing the updated Task |

##### `get_task(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.A2AGrpcClient.get_task "Permanent link")

Retrieves the current state and history of a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `TaskQueryParams` | The `TaskQueryParams` object specifying the task ID | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `Task` | A `Task` object containing the Task or None. |

##### `get_task_callback(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.A2AGrpcClient.get_task_callback "Permanent link")

Retrieves the push notification configuration for a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `TaskIdParams` | The `TaskIdParams` object specifying the task ID. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `TaskPushNotificationConfig` | A `TaskPushNotificationConfig` object containing the configuration. |

##### `send_message(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.A2AGrpcClient.send_message "Permanent link")

Sends a non-streaming message request to the agent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `MessageSendParams` | The `MessageSendParams` object containing the message and configuration. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `Task | Message` | A `Task` or `Message` object containing the agent's response. |

##### `send_message_streaming(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.A2AGrpcClient.send_message_streaming "Permanent link")

Sends a streaming message request to the agent and yields responses as they arrive.

This method uses gRPC streams to receive a stream of updates from the
agent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `MessageSendParams` | The `MessageSendParams` object containing the message and configuration. | _required_ |

Yields:

| Type | Description |
| --- | --- |
| `AsyncGenerator[Message | Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent]` | `Message` or `Task` or `TaskStatusUpdateEvent` or |
| `AsyncGenerator[Message | Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent]` | `TaskArtifactUpdateEvent` objects as they are received in the |
| `AsyncGenerator[Message | Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent]` | stream. |

##### `set_task_callback(request)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.grpc_client.A2AGrpcClient.set_task_callback "Permanent link")

Sets or updates the push notification configuration for a specific task.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `request` | `TaskPushNotificationConfig` | The `TaskPushNotificationConfig` object specifying the task ID and configuration. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `TaskPushNotificationConfig` | A `TaskPushNotificationConfig` object containing the config. |

### `helpers` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.helpers "Permanent link")

Helper functions for the A2A client.

#### `create_text_message_object(role=Role.user, content='')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.client.helpers.create_text_message_object "Permanent link")

Create a Message object containing a single TextPart.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `role` | `Role` | The role of the message sender (user or agent). Defaults to Role.user. | `user` |
| `content` | `str` | The text content of the message. Defaults to an empty string. | `''` |

Returns:

| Type | Description |
| --- | --- |
| `Message` | A `Message` object with a new UUID messageId. |

## `grpc` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc "Permanent link")

### `a2a_pb2` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2 "Permanent link")

Generated protocol buffer code.

#### `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ta2a.proto\x12\x06a2a.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xde\x01\n\x18SendMessageConfiguration\x122\n\x15accepted_output_modes\x18\x01 \x03(\tR\x13acceptedOutputModes\x12K\n\x11push_notification\x18\x02 \x01(\x0b2\x1e.a2a.v1.PushNotificationConfigR\x10pushNotification\x12%\n\x0ehistory_length\x18\x03 \x01(\x05R\rhistoryLength\x12\x1a\n\x08blocking\x18\x04 \x01(\x08R\x08blocking"\xf1\x01\n\x04Task\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\ncontext_id\x18\x02 \x01(\tR\tcontextId\x12*\n\x06status\x18\x03 \x01(\x0b2\x12.a2a.v1.TaskStatusR\x06status\x12.\n\tartifacts\x18\x04 \x03(\x0b2\x10.a2a.v1.ArtifactR\tartifacts\x12)\n\x07history\x18\x05 \x03(\x0b2\x0f.a2a.v1.MessageR\x07history\x123\n\x08metadata\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x08metadata"\x98\x01\n\nTaskStatus\x12\'\n\x05state\x18\x01 \x01(\x0e2\x11.a2a.v1.TaskStateR\x05state\x12\'\n\x06update\x18\x02 \x01(\x0b2\x0f.a2a.v1.MessageR\x06update\x128\n\ttimestamp\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\ttimestamp"t\n\x04Part\x12\x14\n\x04text\x18\x01 \x01(\tH\x00R\x04text\x12&\n\x04file\x18\x02 \x01(\x0b2\x10.a2a.v1.FilePartH\x00R\x04file\x12&\n\x04data\x18\x03 \x01(\x0b2\x10.a2a.v1.DataPartH\x00R\x04dataB\x06\n\x04part"\x7f\n\x08FilePart\x12$\n\rfile_with_uri\x18\x01 \x01(\tH\x00R\x0bfileWithUri\x12(\n\x0ffile_with_bytes\x18\x02 \x01(\x0cH\x00R\rfileWithBytes\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeTypeB\x06\n\x04file"7\n\x08DataPart\x12+\n\x04data\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x04data"\xff\x01\n\x07Message\x12\x1d\n\nmessage_id\x18\x01 \x01(\tR\tmessageId\x12\x1d\n\ncontext_id\x18\x02 \x01(\tR\tcontextId\x12\x17\n\x07task_id\x18\x03 \x01(\tR\x06taskId\x12 \n\x04role\x18\x04 \x01(\x0e2\x0c.a2a.v1.RoleR\x04role\x12&\n\x07content\x18\x05 \x03(\x0b2\x0c.a2a.v1.PartR\x07content\x123\n\x08metadata\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x08metadata\x12\x1e\n\nextensions\x18\x07 \x03(\tR\nextensions"\xda\x01\n\x08Artifact\x12\x1f\n\x0bartifact_id\x18\x01 \x01(\tR\nartifactId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x04 \x01(\tR\x0bdescription\x12"\n\x05parts\x18\x05 \x03(\x0b2\x0c.a2a.v1.PartR\x05parts\x123\n\x08metadata\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x08metadata\x12\x1e\n\nextensions\x18\x07 \x03(\tR\nextensions"\xc6\x01\n\x15TaskStatusUpdateEvent\x12\x17\n\x07task_id\x18\x01 \x01(\tR\x06taskId\x12\x1d\n\ncontext_id\x18\x02 \x01(\tR\tcontextId\x12*\n\x06status\x18\x03 \x01(\x0b2\x12.a2a.v1.TaskStatusR\x06status\x12\x14\n\x05final\x18\x04 \x01(\x08R\x05final\x123\n\x08metadata\x18\x05 \x01(\x0b2\x17.google.protobuf.StructR\x08metadata"\xeb\x01\n\x17TaskArtifactUpdateEvent\x12\x17\n\x07task_id\x18\x01 \x01(\tR\x06taskId\x12\x1d\n\ncontext_id\x18\x02 \x01(\tR\tcontextId\x12,\n\x08artifact\x18\x03 \x01(\x0b2\x10.a2a.v1.ArtifactR\x08artifact\x12\x16\n\x06append\x18\x04 \x01(\x08R\x06append\x12\x1d\n\nlast_chunk\x18\x05 \x01(\x08R\tlastChunk\x123\n\x08metadata\x18\x06 \x01(\x0b2\x17.google.protobuf.StructR\x08metadata"\x94\x01\n\x16PushNotificationConfig\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12\x14\n\x05token\x18\x03 \x01(\tR\x05token\x12B\n\x0eauthentication\x18\x04 \x01(\x0b2\x1a.a2a.v1.AuthenticationInfoR\x0eauthentication"P\n\x12AuthenticationInfo\x12\x18\n\x07schemes\x18\x01 \x03(\tR\x07schemes\x12 \n\x0bcredentials\x18\x02 \x01(\tR\x0bcredentials"\xc8\x05\n\tAgentCard\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12\x10\n\x03url\x18\x03 \x01(\tR\x03url\x121\n\x08provider\x18\x04 \x01(\x0b2\x15.a2a.v1.AgentProviderR\x08provider\x12\x18\n\x07version\x18\x05 \x01(\tR\x07version\x12+\n\x11documentation_url\x18\x06 \x01(\tR\x10documentationUrl\x12=\n\x0ccapabilities\x18\x07 \x01(\x0b2\x19.a2a.v1.AgentCapabilitiesR\x0ccapabilities\x12Q\n\x10security_schemes\x18\x08 \x03(\x0b2&.a2a.v1.AgentCard.SecuritySchemesEntryR\x0fsecuritySchemes\x12,\n\x08security\x18\t \x03(\x0b2\x10.a2a.v1.SecurityR\x08security\x12.\n\x13default_input_modes\x18\n \x03(\tR\x11defaultInputModes\x120\n\x14default_output_modes\x18\x0b \x03(\tR\x12defaultOutputModes\x12*\n\x06skills\x18\x0c \x03(\x0b2\x12.a2a.v1.AgentSkillR\x06skills\x12O\n$supports_authenticated_extended_card\x18\r \x01(\x08R!supportsAuthenticatedExtendedCard\x1aZ\n\x14SecuritySchemesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b2\x16.a2a.v1.SecuritySchemeR\x05value:\x028\x01"E\n\rAgentProvider\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12"\n\x0corganization\x18\x02 \x01(\tR\x0corganization"\x98\x01\n\x11AgentCapabilities\x12\x1c\n\tstreaming\x18\x01 \x01(\x08R\tstreaming\x12-\n\x12push_notifications\x18\x02 \x01(\x08R\x11pushNotifications\x126\n\nextensions\x18\x03 \x03(\x0b2\x16.a2a.v1.AgentExtensionR\nextensions"\x91\x01\n\x0eAgentExtension\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri\x12 \n\x0bdescription\x18\x02 \x01(\tR\x0bdescription\x12\x1a\n\x08required\x18\x03 \x01(\x08R\x08required\x12/\n\x06params\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\x06params"\xc6\x01\n\nAgentSkill\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0bdescription\x18\x03 \x01(\tR\x0bdescription\x12\x12\n\x04tags\x18\x04 \x03(\tR\x04tags\x12\x1a\n\x08examples\x18\x05 \x03(\tR\x08examples\x12\x1f\n\x0binput_modes\x18\x06 \x03(\tR\ninputModes\x12!\n\x0coutput_modes\x18\x07 \x03(\tR\x0boutputModes"\x8a\x01\n\x1aTaskPushNotificationConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12X\n\x18push_notification_config\x18\x02 \x01(\x0b2\x1e.a2a.v1.PushNotificationConfigR\x16pushNotificationConfig" \n\nStringList\x12\x12\n\x04list\x18\x01 \x03(\tR\x04list"\x93\x01\n\x08Security\x127\n\x07schemes\x18\x01 \x03(\x0b2\x1d.a2a.v1.Security.SchemesEntryR\x07schemes\x1aN\n\x0cSchemesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12(\n\x05value\x18\x02 \x01(\x0b2\x12.a2a.v1.StringListR\x05value:\x028\x01"\x91\x03\n\x0eSecurityScheme\x12U\n\x17api_key_security_scheme\x18\x01 \x01(\x0b2\x1c.a2a.v1.APIKeySecuritySchemeH\x00R\x14apiKeySecurityScheme\x12[\n\x19http_auth_security_scheme\x18\x02 \x01(\x0b2\x1e.a2a.v1.HTTPAuthSecuritySchemeH\x00R\x16httpAuthSecurityScheme\x12T\n\x16oauth2_security_scheme\x18\x03 \x01(\x0b2\x1c.a2a.v1.OAuth2SecuritySchemeH\x00R\x14oauth2SecurityScheme\x12k\n\x1fopen_id_connect_security_scheme\x18\x04 \x01(\x0b2\#.a2a.v1.OpenIdConnectSecuritySchemeH\x00R\x1bopenIdConnectSecuritySchemeB\x08\n\x06scheme"h\n\x14APIKeySecurityScheme\x12 \n\x0bdescription\x18\x01 \x01(\tR\x0bdescription\x12\x1a\n\x08location\x18\x02 \x01(\tR\x08location\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name"w\n\x16HTTPAuthSecurityScheme\x12 \n\x0bdescription\x18\x01 \x01(\tR\x0bdescription\x12\x16\n\x06scheme\x18\x02 \x01(\tR\x06scheme\x12\#\n\rbearer_format\x18\x03 \x01(\tR\x0cbearerFormat"b\n\x14OAuth2SecurityScheme\x12 \n\x0bdescription\x18\x01 \x01(\tR\x0bdescription\x12(\n\x05flows\x18\x02 \x01(\x0b2\x12.a2a.v1.OAuthFlowsR\x05flows"n\n\x1bOpenIdConnectSecurityScheme\x12 \n\x0bdescription\x18\x01 \x01(\tR\x0bdescription\x12-\n\x13open_id_connect_url\x18\x02 \x01(\tR\x10openIdConnectUrl"\xb0\x02\n\nOAuthFlows\x12S\n\x12authorization_code\x18\x01 \x01(\x0b2".a2a.v1.AuthorizationCodeOAuthFlowH\x00R\x11authorizationCode\x12S\n\x12client_credentials\x18\x02 \x01(\x0b2".a2a.v1.ClientCredentialsOAuthFlowH\x00R\x11clientCredentials\x127\n\x08implicit\x18\x03 \x01(\x0b2\x19.a2a.v1.ImplicitOAuthFlowH\x00R\x08implicit\x127\n\x08password\x18\x04 \x01(\x0b2\x19.a2a.v1.PasswordOAuthFlowH\x00R\x08passwordB\x06\n\x04flow"\x8a\x02\n\x1aAuthorizationCodeOAuthFlow\x12+\n\x11authorization_url\x18\x01 \x01(\tR\x10authorizationUrl\x12\x1b\n\ttoken_url\x18\x02 \x01(\tR\x08tokenUrl\x12\x1f\n\x0brefresh_url\x18\x03 \x01(\tR\nrefreshUrl\x12F\n\x06scopes\x18\x04 \x03(\x0b2..a2a.v1.AuthorizationCodeOAuthFlow.ScopesEntryR\x06scopes\x1a9\n\x0bScopesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xdd\x01\n\x1aClientCredentialsOAuthFlow\x12\x1b\n\ttoken_url\x18\x01 \x01(\tR\x08tokenUrl\x12\x1f\n\x0brefresh_url\x18\x02 \x01(\tR\nrefreshUrl\x12F\n\x06scopes\x18\x03 \x03(\x0b2..a2a.v1.ClientCredentialsOAuthFlow.ScopesEntryR\x06scopes\x1a9\n\x0bScopesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xdb\x01\n\x11ImplicitOAuthFlow\x12+\n\x11authorization_url\x18\x01 \x01(\tR\x10authorizationUrl\x12\x1f\n\x0brefresh_url\x18\x02 \x01(\tR\nrefreshUrl\x12=\n\x06scopes\x18\x03 \x03(\x0b2%.a2a.v1.ImplicitOAuthFlow.ScopesEntryR\x06scopes\x1a9\n\x0bScopesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xcb\x01\n\x11PasswordOAuthFlow\x12\x1b\n\ttoken_url\x18\x01 \x01(\tR\x08tokenUrl\x12\x1f\n\x0brefresh_url\x18\x02 \x01(\tR\nrefreshUrl\x12=\n\x06scopes\x18\x03 \x03(\x0b2%.a2a.v1.PasswordOAuthFlow.ScopesEntryR\x06scopes\x1a9\n\x0bScopesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x028\x01"\xc1\x01\n\x12SendMessageRequest\x12.\n\x07request\x18\x01 \x01(\x0b2\x0f.a2a.v1.MessageB\x03\xe0A\x02R\x07request\x12F\n\rconfiguration\x18\x02 \x01(\x0b2 .a2a.v1.SendMessageConfigurationR\rconfiguration\x123\n\x08metadata\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x08metadata"P\n\x0eGetTaskRequest\x12\x17\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02R\x04name\x12%\n\x0ehistory_length\x18\x02 \x01(\x05R\rhistoryLength"\'\n\x11CancelTaskRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"4\n\x1eGetTaskPushNotificationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\xa3\x01\n!CreateTaskPushNotificationRequest\x12\x1b\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02R\x06parent\x12 \n\tconfig_id\x18\x02 \x01(\tB\x03\xe0A\x02R\x08configId\x12?\n\x06config\x18\x03 \x01(\x0b2".a2a.v1.TaskPushNotificationConfigB\x03\xe0A\x02R\x06config"-\n\x17TaskSubscriptionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"u\n\x1fListTaskPushNotificationRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken"\x15\n\x13GetAgentCardRequest"i\n\x13SendMessageResponse\x12"\n\x04task\x18\x01 \x01(\x0b2\x0c.a2a.v1.TaskH\x00R\x04task\x12\#\n\x03msg\x18\x02 \x01(\x0b2\x0f.a2a.v1.MessageH\x00R\x03msgB\t\n\x07payload"\xf6\x01\n\x0eStreamResponse\x12"\n\x04task\x18\x01 \x01(\x0b2\x0c.a2a.v1.TaskH\x00R\x04task\x12\#\n\x03msg\x18\x02 \x01(\x0b2\x0f.a2a.v1.MessageH\x00R\x03msg\x12D\n\rstatus_update\x18\x03 \x01(\x0b2\x1d.a2a.v1.TaskStatusUpdateEventH\x00R\x0cstatusUpdate\x12J\n\x0fartifact_update\x18\x04 \x01(\x0b2\x1f.a2a.v1.TaskArtifactUpdateEventH\x00R\x0eartifactUpdateB\t\n\x07payload"\x88\x01\n ListTaskPushNotificationResponse\x12<\n\x07configs\x18\x01 \x03(\x0b2".a2a.v1.TaskPushNotificationConfigR\x07configs\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken*\xfa\x01\n\tTaskState\x12\x1a\n\x16TASK_STATE_UNSPECIFIED\x10\x00\x12\x18\n\x14TASK_STATE_SUBMITTED\x10\x01\x12\x16\n\x12TASK_STATE_WORKING\x10\x02\x12\x18\n\x14TASK_STATE_COMPLETED\x10\x03\x12\x15\n\x11TASK_STATE_FAILED\x10\x04\x12\x18\n\x14TASK_STATE_CANCELLED\x10\x05\x12\x1d\n\x19TASK_STATE_INPUT_REQUIRED\x10\x06\x12\x17\n\x13TASK_STATE_REJECTED\x10\x07\x12\x1c\n\x18TASK_STATE_AUTH_REQUIRED\x10\x08*;\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\r\n\tROLE_USER\x10\x01\x12\x0e\n\nROLE_AGENT\x10\x022\xd3\x08\n\nA2AService\x12c\n\x0bSendMessage\x12\x1a.a2a.v1.SendMessageRequest\x1a\x1b.a2a.v1.SendMessageResponse"\x1b\x82\xd3\xe4\x93\x02\x15"\x10/v1/message:send:\x01*\x12k\n\x14SendStreamingMessage\x12\x1a.a2a.v1.SendMessageRequest\x1a\x16.a2a.v1.StreamResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x12/v1/message:stream:\x01*0\x01\x12R\n\x07GetTask\x12\x16.a2a.v1.GetTaskRequest\x1a\x0c.a2a.v1.Task"!\xdaA\x04name\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/{name=tasks/*}\x12[\n\nCancelTask\x12\x19.a2a.v1.CancelTaskRequest\x1a\x0c.a2a.v1.Task"$\x82\xd3\xe4\x93\x02\x1e"\x19/v1/{name=tasks/*}:cancel:\x01*\x12s\n\x10TaskSubscription\x12\x1f.a2a.v1.TaskSubscriptionRequest\x1a\x16.a2a.v1.StreamResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{name=tasks/*}:subscribe0\x01\x12\xb2\x01\n\x1aCreateTaskPushNotification\x12).a2a.v1.CreateTaskPushNotificationRequest\x1a".a2a.v1.TaskPushNotificationConfig"E\xdaA\rparent,config\x82\xd3\xe4\x93\x02/"%/v1/{parent=task/*/pushNotifications}:\x06config\x12\x9c\x01\n\x17GetTaskPushNotification\x12&.a2a.v1.GetTaskPushNotificationRequest\x1a".a2a.v1.TaskPushNotificationConfig"5\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v1/{name=tasks/*/pushNotifications/*}\x12\xa6\x01\n\x18ListTaskPushNotification\x12\'.a2a.v1.ListTaskPushNotificationRequest\x1a(.a2a.v1.ListTaskPushNotificationResponse"7\xdaA\x06parent\x82\xd3\xe4\x93\x02(\x12&/v1/{parent=tasks/*}/pushNotifications\x12P\n\x0cGetAgentCard\x12\x1b.a2a.v1.GetAgentCardRequest\x1a\x11.a2a.v1.AgentCard"\x10\x82\xd3\xe4\x93\x02\n\x12\x08/v1/cardBi\n\ncom.a2a.v1B\x08A2aProtoP\x01Z\x18google.golang.org/a2a/v1\xa2\x02\x03AXX\xaa\x02\x06A2a.V1\xca\x02\x06A2a\\V1\xe2\x02\x12A2a\\V1\\GPBMetadata\xea\x02\x07A2a::V1b\x06proto3')``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.DESCRIPTOR "Permanent link")\
\
#### `ROLE_AGENT``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ROLE_AGENT "Permanent link")\
\
#### `ROLE_UNSPECIFIED``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ROLE_UNSPECIFIED "Permanent link")\
\
#### `ROLE_USER``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ROLE_USER "Permanent link")\
\
#### `TASK_STATE_AUTH_REQUIRED``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TASK_STATE_AUTH_REQUIRED "Permanent link")\
\
#### `TASK_STATE_CANCELLED``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TASK_STATE_CANCELLED "Permanent link")\
\
#### `TASK_STATE_COMPLETED``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TASK_STATE_COMPLETED "Permanent link")\
\
#### `TASK_STATE_FAILED``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TASK_STATE_FAILED "Permanent link")\
\
#### `TASK_STATE_INPUT_REQUIRED``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TASK_STATE_INPUT_REQUIRED "Permanent link")\
\
#### `TASK_STATE_REJECTED``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TASK_STATE_REJECTED "Permanent link")\
\
#### `TASK_STATE_SUBMITTED``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TASK_STATE_SUBMITTED "Permanent link")\
\
#### `TASK_STATE_UNSPECIFIED``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TASK_STATE_UNSPECIFIED "Permanent link")\
\
#### `TASK_STATE_WORKING``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TASK_STATE_WORKING "Permanent link")\
\
#### `APIKeySecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.APIKeySecurityScheme "Permanent link")\
\
Bases: `Message`\
\
##### `DESCRIPTION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.APIKeySecurityScheme.DESCRIPTION_FIELD_NUMBER "Permanent link")\
\
##### `LOCATION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.APIKeySecurityScheme.LOCATION_FIELD_NUMBER "Permanent link")\
\
##### `NAME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.APIKeySecurityScheme.NAME_FIELD_NUMBER "Permanent link")\
\
##### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.APIKeySecurityScheme.description "Permanent link")\
\
##### `location``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.APIKeySecurityScheme.location "Permanent link")\
\
##### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.APIKeySecurityScheme.name "Permanent link")\
\
#### `AgentCapabilities` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCapabilities "Permanent link")\
\
Bases: `Message`\
\
##### `EXTENSIONS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCapabilities.EXTENSIONS_FIELD_NUMBER "Permanent link")\
\
##### `PUSH_NOTIFICATIONS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCapabilities.PUSH_NOTIFICATIONS_FIELD_NUMBER "Permanent link")\
\
##### `STREAMING_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCapabilities.STREAMING_FIELD_NUMBER "Permanent link")\
\
##### `extensions``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCapabilities.extensions "Permanent link")\
\
##### `push_notifications``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCapabilities.push_notifications "Permanent link")\
\
##### `streaming``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCapabilities.streaming "Permanent link")\
\
#### `AgentCard` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard "Permanent link")\
\
Bases: `Message`\
\
##### `CAPABILITIES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.CAPABILITIES_FIELD_NUMBER "Permanent link")\
\
##### `DEFAULT_INPUT_MODES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.DEFAULT_INPUT_MODES_FIELD_NUMBER "Permanent link")\
\
##### `DEFAULT_OUTPUT_MODES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.DEFAULT_OUTPUT_MODES_FIELD_NUMBER "Permanent link")\
\
##### `DESCRIPTION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.DESCRIPTION_FIELD_NUMBER "Permanent link")\
\
##### `DOCUMENTATION_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.DOCUMENTATION_URL_FIELD_NUMBER "Permanent link")\
\
##### `NAME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.NAME_FIELD_NUMBER "Permanent link")\
\
##### `PROVIDER_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.PROVIDER_FIELD_NUMBER "Permanent link")\
\
##### `SECURITY_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.SECURITY_FIELD_NUMBER "Permanent link")\
\
##### `SECURITY_SCHEMES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.SECURITY_SCHEMES_FIELD_NUMBER "Permanent link")\
\
##### `SKILLS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.SKILLS_FIELD_NUMBER "Permanent link")\
\
##### `SUPPORTS_AUTHENTICATED_EXTENDED_CARD_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.SUPPORTS_AUTHENTICATED_EXTENDED_CARD_FIELD_NUMBER "Permanent link")\
\
##### `URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.URL_FIELD_NUMBER "Permanent link")\
\
##### `VERSION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.VERSION_FIELD_NUMBER "Permanent link")\
\
##### `capabilities``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.capabilities "Permanent link")\
\
##### `default_input_modes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.default_input_modes "Permanent link")\
\
##### `default_output_modes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.default_output_modes "Permanent link")\
\
##### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.description "Permanent link")\
\
##### `documentation_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.documentation_url "Permanent link")\
\
##### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.name "Permanent link")\
\
##### `provider``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.provider "Permanent link")\
\
##### `security``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.security "Permanent link")\
\
##### `security_schemes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.security_schemes "Permanent link")\
\
##### `skills``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.skills "Permanent link")\
\
##### `supports_authenticated_extended_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.supports_authenticated_extended_card "Permanent link")\
\
##### `url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.url "Permanent link")\
\
##### `version``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.version "Permanent link")\
\
##### `SecuritySchemesEntry` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.SecuritySchemesEntry "Permanent link")\
\
Bases: `Message`\
\
###### `KEY_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.SecuritySchemesEntry.KEY_FIELD_NUMBER "Permanent link")\
\
###### `VALUE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.SecuritySchemesEntry.VALUE_FIELD_NUMBER "Permanent link")\
\
###### `key``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.SecuritySchemesEntry.key "Permanent link")\
\
###### `value``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentCard.SecuritySchemesEntry.value "Permanent link")\
\
#### `AgentExtension` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentExtension "Permanent link")\
\
Bases: `Message`\
\
##### `DESCRIPTION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentExtension.DESCRIPTION_FIELD_NUMBER "Permanent link")\
\
##### `PARAMS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentExtension.PARAMS_FIELD_NUMBER "Permanent link")\
\
##### `REQUIRED_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentExtension.REQUIRED_FIELD_NUMBER "Permanent link")\
\
##### `URI_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentExtension.URI_FIELD_NUMBER "Permanent link")\
\
##### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentExtension.description "Permanent link")\
\
##### `params``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentExtension.params "Permanent link")\
\
##### `required``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentExtension.required "Permanent link")\
\
##### `uri``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentExtension.uri "Permanent link")\
\
#### `AgentProvider` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentProvider "Permanent link")\
\
Bases: `Message`\
\
##### `ORGANIZATION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentProvider.ORGANIZATION_FIELD_NUMBER "Permanent link")\
\
##### `URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentProvider.URL_FIELD_NUMBER "Permanent link")\
\
##### `organization``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentProvider.organization "Permanent link")\
\
##### `url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentProvider.url "Permanent link")\
\
#### `AgentSkill` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill "Permanent link")\
\
Bases: `Message`\
\
##### `DESCRIPTION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.DESCRIPTION_FIELD_NUMBER "Permanent link")\
\
##### `EXAMPLES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.EXAMPLES_FIELD_NUMBER "Permanent link")\
\
##### `ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.ID_FIELD_NUMBER "Permanent link")\
\
##### `INPUT_MODES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.INPUT_MODES_FIELD_NUMBER "Permanent link")\
\
##### `NAME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.NAME_FIELD_NUMBER "Permanent link")\
\
##### `OUTPUT_MODES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.OUTPUT_MODES_FIELD_NUMBER "Permanent link")\
\
##### `TAGS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.TAGS_FIELD_NUMBER "Permanent link")\
\
##### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.description "Permanent link")\
\
##### `examples``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.examples "Permanent link")\
\
##### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.id "Permanent link")\
\
##### `input_modes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.input_modes "Permanent link")\
\
##### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.name "Permanent link")\
\
##### `output_modes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.output_modes "Permanent link")\
\
##### `tags``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AgentSkill.tags "Permanent link")\
\
#### `Artifact` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact "Permanent link")\
\
Bases: `Message`\
\
##### `ARTIFACT_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.ARTIFACT_ID_FIELD_NUMBER "Permanent link")\
\
##### `DESCRIPTION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.DESCRIPTION_FIELD_NUMBER "Permanent link")\
\
##### `EXTENSIONS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.EXTENSIONS_FIELD_NUMBER "Permanent link")\
\
##### `METADATA_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.METADATA_FIELD_NUMBER "Permanent link")\
\
##### `NAME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.NAME_FIELD_NUMBER "Permanent link")\
\
##### `PARTS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.PARTS_FIELD_NUMBER "Permanent link")\
\
##### `artifact_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.artifact_id "Permanent link")\
\
##### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.description "Permanent link")\
\
##### `extensions``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.extensions "Permanent link")\
\
##### `metadata``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.metadata "Permanent link")\
\
##### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.name "Permanent link")\
\
##### `parts``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Artifact.parts "Permanent link")\
\
#### `AuthenticationInfo` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthenticationInfo "Permanent link")\
\
Bases: `Message`\
\
##### `CREDENTIALS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthenticationInfo.CREDENTIALS_FIELD_NUMBER "Permanent link")\
\
##### `SCHEMES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthenticationInfo.SCHEMES_FIELD_NUMBER "Permanent link")\
\
##### `credentials``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthenticationInfo.credentials "Permanent link")\
\
##### `schemes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthenticationInfo.schemes "Permanent link")\
\
#### `AuthorizationCodeOAuthFlow` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow "Permanent link")\
\
Bases: `Message`\
\
##### `AUTHORIZATION_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.AUTHORIZATION_URL_FIELD_NUMBER "Permanent link")\
\
##### `REFRESH_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.REFRESH_URL_FIELD_NUMBER "Permanent link")\
\
##### `SCOPES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.SCOPES_FIELD_NUMBER "Permanent link")\
\
##### `TOKEN_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.TOKEN_URL_FIELD_NUMBER "Permanent link")\
\
##### `authorization_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.authorization_url "Permanent link")\
\
##### `refresh_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.refresh_url "Permanent link")\
\
##### `scopes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.scopes "Permanent link")\
\
##### `token_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.token_url "Permanent link")\
\
##### `ScopesEntry` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.ScopesEntry "Permanent link")\
\
Bases: `Message`\
\
###### `KEY_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.ScopesEntry.KEY_FIELD_NUMBER "Permanent link")\
\
###### `VALUE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.ScopesEntry.VALUE_FIELD_NUMBER "Permanent link")\
\
###### `key``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.ScopesEntry.key "Permanent link")\
\
###### `value``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.AuthorizationCodeOAuthFlow.ScopesEntry.value "Permanent link")\
\
#### `CancelTaskRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CancelTaskRequest "Permanent link")\
\
Bases: `Message`\
\
##### `NAME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CancelTaskRequest.NAME_FIELD_NUMBER "Permanent link")\
\
##### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CancelTaskRequest.name "Permanent link")\
\
#### `ClientCredentialsOAuthFlow` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow "Permanent link")\
\
Bases: `Message`\
\
##### `REFRESH_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.REFRESH_URL_FIELD_NUMBER "Permanent link")\
\
##### `SCOPES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.SCOPES_FIELD_NUMBER "Permanent link")\
\
##### `TOKEN_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.TOKEN_URL_FIELD_NUMBER "Permanent link")\
\
##### `refresh_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.refresh_url "Permanent link")\
\
##### `scopes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.scopes "Permanent link")\
\
##### `token_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.token_url "Permanent link")\
\
##### `ScopesEntry` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.ScopesEntry "Permanent link")\
\
Bases: `Message`\
\
###### `KEY_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.ScopesEntry.KEY_FIELD_NUMBER "Permanent link")\
\
###### `VALUE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.ScopesEntry.VALUE_FIELD_NUMBER "Permanent link")\
\
###### `key``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.ScopesEntry.key "Permanent link")\
\
###### `value``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ClientCredentialsOAuthFlow.ScopesEntry.value "Permanent link")\
\
#### `CreateTaskPushNotificationRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CreateTaskPushNotificationRequest "Permanent link")\
\
Bases: `Message`\
\
##### `CONFIG_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CreateTaskPushNotificationRequest.CONFIG_FIELD_NUMBER "Permanent link")\
\
##### `CONFIG_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CreateTaskPushNotificationRequest.CONFIG_ID_FIELD_NUMBER "Permanent link")\
\
##### `PARENT_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CreateTaskPushNotificationRequest.PARENT_FIELD_NUMBER "Permanent link")\
\
##### `config``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CreateTaskPushNotificationRequest.config "Permanent link")\
\
##### `config_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CreateTaskPushNotificationRequest.config_id "Permanent link")\
\
##### `parent``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.CreateTaskPushNotificationRequest.parent "Permanent link")\
\
#### `DataPart` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.DataPart "Permanent link")\
\
Bases: `Message`\
\
##### `DATA_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.DataPart.DATA_FIELD_NUMBER "Permanent link")\
\
##### `data``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.DataPart.data "Permanent link")\
\
#### `FilePart` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.FilePart "Permanent link")\
\
Bases: `Message`\
\
##### `FILE_WITH_BYTES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.FilePart.FILE_WITH_BYTES_FIELD_NUMBER "Permanent link")\
\
##### `FILE_WITH_URI_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.FilePart.FILE_WITH_URI_FIELD_NUMBER "Permanent link")\
\
##### `MIME_TYPE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.FilePart.MIME_TYPE_FIELD_NUMBER "Permanent link")\
\
##### `file_with_bytes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.FilePart.file_with_bytes "Permanent link")\
\
##### `file_with_uri``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.FilePart.file_with_uri "Permanent link")\
\
##### `mime_type``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.FilePart.mime_type "Permanent link")\
\
#### `GetAgentCardRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.GetAgentCardRequest "Permanent link")\
\
Bases: `Message`\
\
#### `GetTaskPushNotificationRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.GetTaskPushNotificationRequest "Permanent link")\
\
Bases: `Message`\
\
##### `NAME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.GetTaskPushNotificationRequest.NAME_FIELD_NUMBER "Permanent link")\
\
##### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.GetTaskPushNotificationRequest.name "Permanent link")\
\
#### `GetTaskRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.GetTaskRequest "Permanent link")\
\
Bases: `Message`\
\
##### `HISTORY_LENGTH_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.GetTaskRequest.HISTORY_LENGTH_FIELD_NUMBER "Permanent link")\
\
##### `NAME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.GetTaskRequest.NAME_FIELD_NUMBER "Permanent link")\
\
##### `history_length``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.GetTaskRequest.history_length "Permanent link")\
\
##### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.GetTaskRequest.name "Permanent link")\
\
#### `HTTPAuthSecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.HTTPAuthSecurityScheme "Permanent link")\
\
Bases: `Message`\
\
##### `BEARER_FORMAT_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.HTTPAuthSecurityScheme.BEARER_FORMAT_FIELD_NUMBER "Permanent link")\
\
##### `DESCRIPTION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.HTTPAuthSecurityScheme.DESCRIPTION_FIELD_NUMBER "Permanent link")\
\
##### `SCHEME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.HTTPAuthSecurityScheme.SCHEME_FIELD_NUMBER "Permanent link")\
\
##### `bearer_format``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.HTTPAuthSecurityScheme.bearer_format "Permanent link")\
\
##### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.HTTPAuthSecurityScheme.description "Permanent link")\
\
##### `scheme``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.HTTPAuthSecurityScheme.scheme "Permanent link")\
\
#### `ImplicitOAuthFlow` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow "Permanent link")\
\
Bases: `Message`\
\
##### `AUTHORIZATION_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.AUTHORIZATION_URL_FIELD_NUMBER "Permanent link")\
\
##### `REFRESH_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.REFRESH_URL_FIELD_NUMBER "Permanent link")\
\
##### `SCOPES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.SCOPES_FIELD_NUMBER "Permanent link")\
\
##### `authorization_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.authorization_url "Permanent link")\
\
##### `refresh_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.refresh_url "Permanent link")\
\
##### `scopes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.scopes "Permanent link")\
\
##### `ScopesEntry` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.ScopesEntry "Permanent link")\
\
Bases: `Message`\
\
###### `KEY_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.ScopesEntry.KEY_FIELD_NUMBER "Permanent link")\
\
###### `VALUE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.ScopesEntry.VALUE_FIELD_NUMBER "Permanent link")\
\
###### `key``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.ScopesEntry.key "Permanent link")\
\
###### `value``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ImplicitOAuthFlow.ScopesEntry.value "Permanent link")\
\
#### `ListTaskPushNotificationRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationRequest "Permanent link")\
\
Bases: `Message`\
\
##### `PAGE_SIZE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationRequest.PAGE_SIZE_FIELD_NUMBER "Permanent link")\
\
##### `PAGE_TOKEN_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationRequest.PAGE_TOKEN_FIELD_NUMBER "Permanent link")\
\
##### `PARENT_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationRequest.PARENT_FIELD_NUMBER "Permanent link")\
\
##### `page_size``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationRequest.page_size "Permanent link")\
\
##### `page_token``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationRequest.page_token "Permanent link")\
\
##### `parent``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationRequest.parent "Permanent link")\
\
#### `ListTaskPushNotificationResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationResponse "Permanent link")\
\
Bases: `Message`\
\
##### `CONFIGS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationResponse.CONFIGS_FIELD_NUMBER "Permanent link")\
\
##### `NEXT_PAGE_TOKEN_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationResponse.NEXT_PAGE_TOKEN_FIELD_NUMBER "Permanent link")\
\
##### `configs``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationResponse.configs "Permanent link")\
\
##### `next_page_token``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.ListTaskPushNotificationResponse.next_page_token "Permanent link")\
\
#### `Message` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message "Permanent link")\
\
Bases: `Message`\
\
##### `CONTENT_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.CONTENT_FIELD_NUMBER "Permanent link")\
\
##### `CONTEXT_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.CONTEXT_ID_FIELD_NUMBER "Permanent link")\
\
##### `EXTENSIONS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.EXTENSIONS_FIELD_NUMBER "Permanent link")\
\
##### `MESSAGE_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.MESSAGE_ID_FIELD_NUMBER "Permanent link")\
\
##### `METADATA_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.METADATA_FIELD_NUMBER "Permanent link")\
\
##### `ROLE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.ROLE_FIELD_NUMBER "Permanent link")\
\
##### `TASK_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.TASK_ID_FIELD_NUMBER "Permanent link")\
\
##### `content``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.content "Permanent link")\
\
##### `context_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.context_id "Permanent link")\
\
##### `extensions``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.extensions "Permanent link")\
\
##### `message_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.message_id "Permanent link")\
\
##### `metadata``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.metadata "Permanent link")\
\
##### `role``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.role "Permanent link")\
\
##### `task_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Message.task_id "Permanent link")\
\
#### `OAuth2SecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuth2SecurityScheme "Permanent link")\
\
Bases: `Message`\
\
##### `DESCRIPTION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuth2SecurityScheme.DESCRIPTION_FIELD_NUMBER "Permanent link")\
\
##### `FLOWS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuth2SecurityScheme.FLOWS_FIELD_NUMBER "Permanent link")\
\
##### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuth2SecurityScheme.description "Permanent link")\
\
##### `flows``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuth2SecurityScheme.flows "Permanent link")\
\
#### `OAuthFlows` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuthFlows "Permanent link")\
\
Bases: `Message`\
\
##### `AUTHORIZATION_CODE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuthFlows.AUTHORIZATION_CODE_FIELD_NUMBER "Permanent link")\
\
##### `CLIENT_CREDENTIALS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuthFlows.CLIENT_CREDENTIALS_FIELD_NUMBER "Permanent link")\
\
##### `IMPLICIT_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuthFlows.IMPLICIT_FIELD_NUMBER "Permanent link")\
\
##### `PASSWORD_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuthFlows.PASSWORD_FIELD_NUMBER "Permanent link")\
\
##### `authorization_code``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuthFlows.authorization_code "Permanent link")\
\
##### `client_credentials``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuthFlows.client_credentials "Permanent link")\
\
##### `implicit``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuthFlows.implicit "Permanent link")\
\
##### `password``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OAuthFlows.password "Permanent link")\
\
#### `OpenIdConnectSecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OpenIdConnectSecurityScheme "Permanent link")\
\
Bases: `Message`\
\
##### `DESCRIPTION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OpenIdConnectSecurityScheme.DESCRIPTION_FIELD_NUMBER "Permanent link")\
\
##### `OPEN_ID_CONNECT_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OpenIdConnectSecurityScheme.OPEN_ID_CONNECT_URL_FIELD_NUMBER "Permanent link")\
\
##### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OpenIdConnectSecurityScheme.description "Permanent link")\
\
##### `open_id_connect_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.OpenIdConnectSecurityScheme.open_id_connect_url "Permanent link")\
\
#### `Part` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Part "Permanent link")\
\
Bases: `Message`\
\
##### `DATA_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Part.DATA_FIELD_NUMBER "Permanent link")\
\
##### `FILE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Part.FILE_FIELD_NUMBER "Permanent link")\
\
##### `TEXT_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Part.TEXT_FIELD_NUMBER "Permanent link")\
\
##### `data``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Part.data "Permanent link")\
\
##### `file``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Part.file "Permanent link")\
\
##### `text``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Part.text "Permanent link")\
\
#### `PasswordOAuthFlow` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow "Permanent link")\
\
Bases: `Message`\
\
##### `REFRESH_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.REFRESH_URL_FIELD_NUMBER "Permanent link")\
\
##### `SCOPES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.SCOPES_FIELD_NUMBER "Permanent link")\
\
##### `TOKEN_URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.TOKEN_URL_FIELD_NUMBER "Permanent link")\
\
##### `refresh_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.refresh_url "Permanent link")\
\
##### `scopes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.scopes "Permanent link")\
\
##### `token_url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.token_url "Permanent link")\
\
##### `ScopesEntry` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.ScopesEntry "Permanent link")\
\
Bases: `Message`\
\
###### `KEY_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.ScopesEntry.KEY_FIELD_NUMBER "Permanent link")\
\
###### `VALUE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.ScopesEntry.VALUE_FIELD_NUMBER "Permanent link")\
\
###### `key``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.ScopesEntry.key "Permanent link")\
\
###### `value``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PasswordOAuthFlow.ScopesEntry.value "Permanent link")\
\
#### `PushNotificationConfig` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PushNotificationConfig "Permanent link")\
\
Bases: `Message`\
\
##### `AUTHENTICATION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PushNotificationConfig.AUTHENTICATION_FIELD_NUMBER "Permanent link")\
\
##### `ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PushNotificationConfig.ID_FIELD_NUMBER "Permanent link")\
\
##### `TOKEN_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PushNotificationConfig.TOKEN_FIELD_NUMBER "Permanent link")\
\
##### `URL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PushNotificationConfig.URL_FIELD_NUMBER "Permanent link")\
\
##### `authentication``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PushNotificationConfig.authentication "Permanent link")\
\
##### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PushNotificationConfig.id "Permanent link")\
\
##### `token``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PushNotificationConfig.token "Permanent link")\
\
##### `url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.PushNotificationConfig.url "Permanent link")\
\
#### `Role` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Role "Permanent link")\
\
Bases: `int`\
\
##### `ROLE_AGENT``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Role.ROLE_AGENT "Permanent link")\
\
##### `ROLE_UNSPECIFIED``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Role.ROLE_UNSPECIFIED "Permanent link")\
\
##### `ROLE_USER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Role.ROLE_USER "Permanent link")\
\
#### `Security` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Security "Permanent link")\
\
Bases: `Message`\
\
##### `SCHEMES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Security.SCHEMES_FIELD_NUMBER "Permanent link")\
\
##### `schemes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Security.schemes "Permanent link")\
\
##### `SchemesEntry` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Security.SchemesEntry "Permanent link")\
\
Bases: `Message`\
\
###### `KEY_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Security.SchemesEntry.KEY_FIELD_NUMBER "Permanent link")\
\
###### `VALUE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Security.SchemesEntry.VALUE_FIELD_NUMBER "Permanent link")\
\
###### `key``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Security.SchemesEntry.key "Permanent link")\
\
###### `value``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Security.SchemesEntry.value "Permanent link")\
\
#### `SecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SecurityScheme "Permanent link")\
\
Bases: `Message`\
\
##### `API_KEY_SECURITY_SCHEME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SecurityScheme.API_KEY_SECURITY_SCHEME_FIELD_NUMBER "Permanent link")\
\
##### `HTTP_AUTH_SECURITY_SCHEME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SecurityScheme.HTTP_AUTH_SECURITY_SCHEME_FIELD_NUMBER "Permanent link")\
\
##### `OAUTH2_SECURITY_SCHEME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SecurityScheme.OAUTH2_SECURITY_SCHEME_FIELD_NUMBER "Permanent link")\
\
##### `OPEN_ID_CONNECT_SECURITY_SCHEME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SecurityScheme.OPEN_ID_CONNECT_SECURITY_SCHEME_FIELD_NUMBER "Permanent link")\
\
##### `api_key_security_scheme``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SecurityScheme.api_key_security_scheme "Permanent link")\
\
##### `http_auth_security_scheme``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SecurityScheme.http_auth_security_scheme "Permanent link")\
\
##### `oauth2_security_scheme``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SecurityScheme.oauth2_security_scheme "Permanent link")\
\
##### `open_id_connect_security_scheme``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SecurityScheme.open_id_connect_security_scheme "Permanent link")\
\
#### `SendMessageConfiguration` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageConfiguration "Permanent link")\
\
Bases: `Message`\
\
##### `ACCEPTED_OUTPUT_MODES_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageConfiguration.ACCEPTED_OUTPUT_MODES_FIELD_NUMBER "Permanent link")\
\
##### `BLOCKING_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageConfiguration.BLOCKING_FIELD_NUMBER "Permanent link")\
\
##### `HISTORY_LENGTH_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageConfiguration.HISTORY_LENGTH_FIELD_NUMBER "Permanent link")\
\
##### `PUSH_NOTIFICATION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageConfiguration.PUSH_NOTIFICATION_FIELD_NUMBER "Permanent link")\
\
##### `accepted_output_modes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageConfiguration.accepted_output_modes "Permanent link")\
\
##### `blocking``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageConfiguration.blocking "Permanent link")\
\
##### `history_length``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageConfiguration.history_length "Permanent link")\
\
##### `push_notification``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageConfiguration.push_notification "Permanent link")\
\
#### `SendMessageRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageRequest "Permanent link")\
\
Bases: `Message`\
\
##### `CONFIGURATION_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageRequest.CONFIGURATION_FIELD_NUMBER "Permanent link")\
\
##### `METADATA_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageRequest.METADATA_FIELD_NUMBER "Permanent link")\
\
##### `REQUEST_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageRequest.REQUEST_FIELD_NUMBER "Permanent link")\
\
##### `configuration``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageRequest.configuration "Permanent link")\
\
##### `metadata``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageRequest.metadata "Permanent link")\
\
##### `request``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageRequest.request "Permanent link")\
\
#### `SendMessageResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageResponse "Permanent link")\
\
Bases: `Message`\
\
##### `MSG_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageResponse.MSG_FIELD_NUMBER "Permanent link")\
\
##### `TASK_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageResponse.TASK_FIELD_NUMBER "Permanent link")\
\
##### `msg``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageResponse.msg "Permanent link")\
\
##### `task``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.SendMessageResponse.task "Permanent link")\
\
#### `StreamResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StreamResponse "Permanent link")\
\
Bases: `Message`\
\
##### `ARTIFACT_UPDATE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StreamResponse.ARTIFACT_UPDATE_FIELD_NUMBER "Permanent link")\
\
##### `MSG_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StreamResponse.MSG_FIELD_NUMBER "Permanent link")\
\
##### `STATUS_UPDATE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StreamResponse.STATUS_UPDATE_FIELD_NUMBER "Permanent link")\
\
##### `TASK_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StreamResponse.TASK_FIELD_NUMBER "Permanent link")\
\
##### `artifact_update``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StreamResponse.artifact_update "Permanent link")\
\
##### `msg``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StreamResponse.msg "Permanent link")\
\
##### `status_update``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StreamResponse.status_update "Permanent link")\
\
##### `task``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StreamResponse.task "Permanent link")\
\
#### `StringList` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StringList "Permanent link")\
\
Bases: `Message`\
\
##### `LIST_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StringList.LIST_FIELD_NUMBER "Permanent link")\
\
##### `list``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.StringList.list "Permanent link")\
\
#### `Task` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task "Permanent link")\
\
Bases: `Message`\
\
##### `ARTIFACTS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.ARTIFACTS_FIELD_NUMBER "Permanent link")\
\
##### `CONTEXT_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.CONTEXT_ID_FIELD_NUMBER "Permanent link")\
\
##### `HISTORY_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.HISTORY_FIELD_NUMBER "Permanent link")\
\
##### `ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.ID_FIELD_NUMBER "Permanent link")\
\
##### `METADATA_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.METADATA_FIELD_NUMBER "Permanent link")\
\
##### `STATUS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.STATUS_FIELD_NUMBER "Permanent link")\
\
##### `artifacts``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.artifacts "Permanent link")\
\
##### `context_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.context_id "Permanent link")\
\
##### `history``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.history "Permanent link")\
\
##### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.id "Permanent link")\
\
##### `metadata``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.metadata "Permanent link")\
\
##### `status``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.Task.status "Permanent link")\
\
#### `TaskArtifactUpdateEvent` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent "Permanent link")\
\
Bases: `Message`\
\
##### `APPEND_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.APPEND_FIELD_NUMBER "Permanent link")\
\
##### `ARTIFACT_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.ARTIFACT_FIELD_NUMBER "Permanent link")\
\
##### `CONTEXT_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.CONTEXT_ID_FIELD_NUMBER "Permanent link")\
\
##### `LAST_CHUNK_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.LAST_CHUNK_FIELD_NUMBER "Permanent link")\
\
##### `METADATA_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.METADATA_FIELD_NUMBER "Permanent link")\
\
##### `TASK_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.TASK_ID_FIELD_NUMBER "Permanent link")\
\
##### `append``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.append "Permanent link")\
\
##### `artifact``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.artifact "Permanent link")\
\
##### `context_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.context_id "Permanent link")\
\
##### `last_chunk``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.last_chunk "Permanent link")\
\
##### `metadata``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.metadata "Permanent link")\
\
##### `task_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskArtifactUpdateEvent.task_id "Permanent link")\
\
#### `TaskPushNotificationConfig` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskPushNotificationConfig "Permanent link")\
\
Bases: `Message`\
\
##### `NAME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskPushNotificationConfig.NAME_FIELD_NUMBER "Permanent link")\
\
##### `PUSH_NOTIFICATION_CONFIG_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskPushNotificationConfig.PUSH_NOTIFICATION_CONFIG_FIELD_NUMBER "Permanent link")\
\
##### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskPushNotificationConfig.name "Permanent link")\
\
##### `push_notification_config``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskPushNotificationConfig.push_notification_config "Permanent link")\
\
#### `TaskState` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState "Permanent link")\
\
Bases: `int`\
\
##### `TASK_STATE_AUTH_REQUIRED``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState.TASK_STATE_AUTH_REQUIRED "Permanent link")\
\
##### `TASK_STATE_CANCELLED``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState.TASK_STATE_CANCELLED "Permanent link")\
\
##### `TASK_STATE_COMPLETED``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState.TASK_STATE_COMPLETED "Permanent link")\
\
##### `TASK_STATE_FAILED``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState.TASK_STATE_FAILED "Permanent link")\
\
##### `TASK_STATE_INPUT_REQUIRED``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState.TASK_STATE_INPUT_REQUIRED "Permanent link")\
\
##### `TASK_STATE_REJECTED``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState.TASK_STATE_REJECTED "Permanent link")\
\
##### `TASK_STATE_SUBMITTED``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState.TASK_STATE_SUBMITTED "Permanent link")\
\
##### `TASK_STATE_UNSPECIFIED``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState.TASK_STATE_UNSPECIFIED "Permanent link")\
\
##### `TASK_STATE_WORKING``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskState.TASK_STATE_WORKING "Permanent link")\
\
#### `TaskStatus` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatus "Permanent link")\
\
Bases: `Message`\
\
##### `STATE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatus.STATE_FIELD_NUMBER "Permanent link")\
\
##### `TIMESTAMP_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatus.TIMESTAMP_FIELD_NUMBER "Permanent link")\
\
##### `UPDATE_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatus.UPDATE_FIELD_NUMBER "Permanent link")\
\
##### `state``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatus.state "Permanent link")\
\
##### `timestamp``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatus.timestamp "Permanent link")\
\
##### `update``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatus.update "Permanent link")\
\
#### `TaskStatusUpdateEvent` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent "Permanent link")\
\
Bases: `Message`\
\
##### `CONTEXT_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.CONTEXT_ID_FIELD_NUMBER "Permanent link")\
\
##### `FINAL_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.FINAL_FIELD_NUMBER "Permanent link")\
\
##### `METADATA_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.METADATA_FIELD_NUMBER "Permanent link")\
\
##### `STATUS_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.STATUS_FIELD_NUMBER "Permanent link")\
\
##### `TASK_ID_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.TASK_ID_FIELD_NUMBER "Permanent link")\
\
##### `context_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.context_id "Permanent link")\
\
##### `final``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.final "Permanent link")\
\
##### `metadata``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.metadata "Permanent link")\
\
##### `status``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.status "Permanent link")\
\
##### `task_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskStatusUpdateEvent.task_id "Permanent link")\
\
#### `TaskSubscriptionRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskSubscriptionRequest "Permanent link")\
\
Bases: `Message`\
\
##### `NAME_FIELD_NUMBER``class-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskSubscriptionRequest.NAME_FIELD_NUMBER "Permanent link")\
\
##### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2.TaskSubscriptionRequest.name "Permanent link")\
\
### `a2a_pb2_grpc` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc "Permanent link")\
\
Client and server classes corresponding to protobuf-defined services.\
\
#### `A2AService` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService "Permanent link")\
\
Bases: `object`\
\
A2AService defines the gRPC version of the A2A protocol. This has a slightly\
different shape than the JSONRPC version to better conform to AIP-127,\
where appropriate. The nouns are AgentCard, Message, Task and\
TaskPushNotification.\
\- Messages are not a standard resource so there is no get/delete/update/list\
interface, only a send and stream custom methods.\
\- Tasks have a get interface and custom cancel and subscribe methods.\
\- TaskPushNotification are a resource whose parent is a task. They have get,\
list and create methods.\
\- AgentCard is a static resource with only a get method.\
fields are not present as they don't comply with AIP rules, and the\
optional history\_length on the get task method is not present as it also\
violates AIP-127 and AIP-131.\
\
##### `CancelTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService.CancelTask "Permanent link")\
\
##### `CreateTaskPushNotification(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService.CreateTaskPushNotification "Permanent link")\
\
##### `GetAgentCard(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService.GetAgentCard "Permanent link")\
\
##### `GetTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService.GetTask "Permanent link")\
\
##### `GetTaskPushNotification(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService.GetTaskPushNotification "Permanent link")\
\
##### `ListTaskPushNotification(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService.ListTaskPushNotification "Permanent link")\
\
##### `SendMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService.SendMessage "Permanent link")\
\
##### `SendStreamingMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService.SendStreamingMessage "Permanent link")\
\
##### `TaskSubscription(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)``staticmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AService.TaskSubscription "Permanent link")\
\
#### `A2AServiceServicer` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer "Permanent link")\
\
Bases: `object`\
\
A2AService defines the gRPC version of the A2A protocol. This has a slightly\
different shape than the JSONRPC version to better conform to AIP-127,\
where appropriate. The nouns are AgentCard, Message, Task and\
TaskPushNotification.\
\- Messages are not a standard resource so there is no get/delete/update/list\
interface, only a send and stream custom methods.\
\- Tasks have a get interface and custom cancel and subscribe methods.\
\- TaskPushNotification are a resource whose parent is a task. They have get,\
list and create methods.\
\- AgentCard is a static resource with only a get method.\
fields are not present as they don't comply with AIP rules, and the\
optional history\_length on the get task method is not present as it also\
violates AIP-127 and AIP-131.\
\
##### `CancelTask(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer.CancelTask "Permanent link")\
\
Cancel a task from the agent. If supported one should expect no\
more task updates for the task.\
\
##### `CreateTaskPushNotification(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer.CreateTaskPushNotification "Permanent link")\
\
Set a push notification config for a task.\
\
##### `GetAgentCard(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer.GetAgentCard "Permanent link")\
\
GetAgentCard returns the agent card for the agent.\
\
##### `GetTask(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer.GetTask "Permanent link")\
\
Get the current state of a task from the agent.\
\
##### `GetTaskPushNotification(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer.GetTaskPushNotification "Permanent link")\
\
Get a push notification config for a task.\
\
##### `ListTaskPushNotification(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer.ListTaskPushNotification "Permanent link")\
\
Get a list of push notifications configured for a task.\
\
##### `SendMessage(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer.SendMessage "Permanent link")\
\
Send a message to the agent. This is a blocking call that will return the\
task once it is completed, or a LRO if requested.\
\
##### `SendStreamingMessage(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer.SendStreamingMessage "Permanent link")\
\
SendStreamingMessage is a streaming call that will return a stream of\
task update events until the Task is in an interrupted or terminal state.\
\
##### `TaskSubscription(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceServicer.TaskSubscription "Permanent link")\
\
TaskSubscription is a streaming call that will return a stream of task\
update events. This attaches the stream to an existing in process task.\
If the task is complete the stream will return the completed task (like\
GetTask) and close the stream.\
\
#### `A2AServiceStub` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub "Permanent link")\
\
Bases: `object`\
\
A2AService defines the gRPC version of the A2A protocol. This has a slightly\
different shape than the JSONRPC version to better conform to AIP-127,\
where appropriate. The nouns are AgentCard, Message, Task and\
TaskPushNotification.\
\- Messages are not a standard resource so there is no get/delete/update/list\
interface, only a send and stream custom methods.\
\- Tasks have a get interface and custom cancel and subscribe methods.\
\- TaskPushNotification are a resource whose parent is a task. They have get,\
list and create methods.\
\- AgentCard is a static resource with only a get method.\
fields are not present as they don't comply with AIP rules, and the\
optional history\_length on the get task method is not present as it also\
violates AIP-127 and AIP-131.\
\
##### `CancelTask = channel.unary_unary('/a2a.v1.A2AService/CancelTask', request_serializer=a2a__pb2.CancelTaskRequest.SerializeToString, response_deserializer=a2a__pb2.Task.FromString, _registered_method=True)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub.CancelTask "Permanent link")\
\
##### `CreateTaskPushNotification = channel.unary_unary('/a2a.v1.A2AService/CreateTaskPushNotification', request_serializer=a2a__pb2.CreateTaskPushNotificationRequest.SerializeToString, response_deserializer=a2a__pb2.TaskPushNotificationConfig.FromString, _registered_method=True)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub.CreateTaskPushNotification "Permanent link")\
\
##### `GetAgentCard = channel.unary_unary('/a2a.v1.A2AService/GetAgentCard', request_serializer=a2a__pb2.GetAgentCardRequest.SerializeToString, response_deserializer=a2a__pb2.AgentCard.FromString, _registered_method=True)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub.GetAgentCard "Permanent link")\
\
##### `GetTask = channel.unary_unary('/a2a.v1.A2AService/GetTask', request_serializer=a2a__pb2.GetTaskRequest.SerializeToString, response_deserializer=a2a__pb2.Task.FromString, _registered_method=True)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub.GetTask "Permanent link")\
\
##### `GetTaskPushNotification = channel.unary_unary('/a2a.v1.A2AService/GetTaskPushNotification', request_serializer=a2a__pb2.GetTaskPushNotificationRequest.SerializeToString, response_deserializer=a2a__pb2.TaskPushNotificationConfig.FromString, _registered_method=True)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub.GetTaskPushNotification "Permanent link")\
\
##### `ListTaskPushNotification = channel.unary_unary('/a2a.v1.A2AService/ListTaskPushNotification', request_serializer=a2a__pb2.ListTaskPushNotificationRequest.SerializeToString, response_deserializer=a2a__pb2.ListTaskPushNotificationResponse.FromString, _registered_method=True)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub.ListTaskPushNotification "Permanent link")\
\
##### `SendMessage = channel.unary_unary('/a2a.v1.A2AService/SendMessage', request_serializer=a2a__pb2.SendMessageRequest.SerializeToString, response_deserializer=a2a__pb2.SendMessageResponse.FromString, _registered_method=True)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub.SendMessage "Permanent link")\
\
##### `SendStreamingMessage = channel.unary_stream('/a2a.v1.A2AService/SendStreamingMessage', request_serializer=a2a__pb2.SendMessageRequest.SerializeToString, response_deserializer=a2a__pb2.StreamResponse.FromString, _registered_method=True)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub.SendStreamingMessage "Permanent link")\
\
##### `TaskSubscription = channel.unary_stream('/a2a.v1.A2AService/TaskSubscription', request_serializer=a2a__pb2.TaskSubscriptionRequest.SerializeToString, response_deserializer=a2a__pb2.StreamResponse.FromString, _registered_method=True)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.A2AServiceStub.TaskSubscription "Permanent link")\
\
#### `add_A2AServiceServicer_to_server(servicer, server)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.grpc.a2a_pb2_grpc.add_A2AServiceServicer_to_server "Permanent link")\
\
## `server` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server "Permanent link")\
\
Server-side components for implementing an A2A agent.\
\
### `agent_execution` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution "Permanent link")\
\
Components for executing agent logic within the A2A server.\
\
#### `AgentExecutor` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.AgentExecutor "Permanent link")\
\
Bases: `ABC`\
\
Agent Executor interface.\
\
Implementations of this interface contain the core logic of the agent,\
executing tasks based on requests and publishing updates to an event queue.\
\
##### `cancel(context, event_queue)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.AgentExecutor.cancel "Permanent link")\
\
Request the agent to cancel an ongoing task.\
\
The agent should attempt to stop the task identified by the task\_id\
in the context and publish a `TaskStatusUpdateEvent` with state\
`TaskState.canceled` to the `event_queue`.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `context` | `RequestContext` | The request context containing the task ID to cancel. | _required_ |\
| `event_queue` | `EventQueue` | The queue to publish the cancellation status update to. | _required_ |\
\
##### `execute(context, event_queue)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.AgentExecutor.execute "Permanent link")\
\
Execute the agent's logic for a given request context.\
\
The agent should read necessary information from the `context` and\
publish `Task` or `Message` events, or `TaskStatusUpdateEvent` /\
`TaskArtifactUpdateEvent` to the `event_queue`. This method should\
return once the agent's execution for this request is complete or\
yields control (e.g., enters an input-required state).\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `context` | `RequestContext` | The request context containing the message, task ID, etc. | _required_ |\
| `event_queue` | `EventQueue` | The queue to publish events to. | _required_ |\
\
#### `RequestContext` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext "Permanent link")\
\
Request Context.\
\
Holds information about the current request being processed by the server,\
including the incoming message, task and context identifiers, and related\
tasks.\
\
##### `call_context``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext.call_context "Permanent link")\
\
The server call context associated with this request.\
\
##### `configuration``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext.configuration "Permanent link")\
\
The `MessageSendConfiguration` from the request, if available.\
\
##### `context_id``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext.context_id "Permanent link")\
\
The ID of the conversation context associated with this task.\
\
##### `current_task``property``writable`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext.current_task "Permanent link")\
\
The current `Task` object being processed.\
\
##### `message``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext.message "Permanent link")\
\
The incoming `Message` object from the request, if available.\
\
##### `related_tasks``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext.related_tasks "Permanent link")\
\
A list of tasks related to the current request.\
\
##### `task_id``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext.task_id "Permanent link")\
\
The ID of the task associated with this context.\
\
##### `attach_related_task(task)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext.attach_related_task "Permanent link")\
\
Attaches a related task to the context.\
\
This is useful for scenarios like tool execution where a new task\
might be spawned.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `task` | `Task` | The `Task` object to attach. | _required_ |\
\
##### `get_user_input(delimiter='\n')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContext.get_user_input "Permanent link")\
\
Extracts text content from the user's message parts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `delimiter` | `str` | The string to use when joining multiple text parts. | `'\n'` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `str` | A single string containing all text content from the user message, |\
| `str` | joined by the specified delimiter. Returns an empty string if no |\
| `str` | user message is present or if it contains no text parts. |\
\
#### `RequestContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContextBuilder "Permanent link")\
\
Bases: `ABC`\
\
Builds request context to be supplied to agent executor.\
\
##### `build(params=None, task_id=None, context_id=None, task=None, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.RequestContextBuilder.build "Permanent link")\
\
#### `SimpleRequestContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.SimpleRequestContextBuilder "Permanent link")\
\
Bases: `RequestContextBuilder`\
\
Builds request context and populates referred tasks.\
\
##### `build(params=None, task_id=None, context_id=None, task=None, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.SimpleRequestContextBuilder.build "Permanent link")\
\
Builds the request context for an agent execution.\
\
This method assembles the RequestContext object. If the builder was\
initialized with `should_populate_referred_tasks=True`, it fetches all tasks\
referenced in `params.message.referenceTaskIds` from the `task_store`.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `MessageSendParams | None` | The parameters of the incoming message send request. | `None` |\
| `task_id` | `str | None` | The ID of the task being executed. | `None` |\
| `context_id` | `str | None` | The ID of the current execution context. | `None` |\
| `task` | `Task | None` | The primary task object associated with the request. | `None` |\
| `context` | `ServerCallContext | None` | The server call context, containing metadata about the call. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `RequestContext` | An instance of RequestContext populated with the provided information |\
| `RequestContext` | and potentially a list of related tasks. |\
\
#### `agent_executor` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.agent_executor "Permanent link")\
\
##### `AgentExecutor` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.agent_executor.AgentExecutor "Permanent link")\
\
Bases: `ABC`\
\
Agent Executor interface.\
\
Implementations of this interface contain the core logic of the agent,\
executing tasks based on requests and publishing updates to an event queue.\
\
###### `cancel(context, event_queue)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.agent_executor.AgentExecutor.cancel "Permanent link")\
\
Request the agent to cancel an ongoing task.\
\
The agent should attempt to stop the task identified by the task\_id\
in the context and publish a `TaskStatusUpdateEvent` with state\
`TaskState.canceled` to the `event_queue`.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `context` | `RequestContext` | The request context containing the task ID to cancel. | _required_ |\
| `event_queue` | `EventQueue` | The queue to publish the cancellation status update to. | _required_ |\
\
###### `execute(context, event_queue)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.agent_executor.AgentExecutor.execute "Permanent link")\
\
Execute the agent's logic for a given request context.\
\
The agent should read necessary information from the `context` and\
publish `Task` or `Message` events, or `TaskStatusUpdateEvent` /\
`TaskArtifactUpdateEvent` to the `event_queue`. This method should\
return once the agent's execution for this request is complete or\
yields control (e.g., enters an input-required state).\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `context` | `RequestContext` | The request context containing the message, task ID, etc. | _required_ |\
| `event_queue` | `EventQueue` | The queue to publish events to. | _required_ |\
\
#### `context` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context "Permanent link")\
\
##### `RequestContext` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext "Permanent link")\
\
Request Context.\
\
Holds information about the current request being processed by the server,\
including the incoming message, task and context identifiers, and related\
tasks.\
\
###### `call_context``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext.call_context "Permanent link")\
\
The server call context associated with this request.\
\
###### `configuration``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext.configuration "Permanent link")\
\
The `MessageSendConfiguration` from the request, if available.\
\
###### `context_id``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext.context_id "Permanent link")\
\
The ID of the conversation context associated with this task.\
\
###### `current_task``property``writable`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext.current_task "Permanent link")\
\
The current `Task` object being processed.\
\
###### `message``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext.message "Permanent link")\
\
The incoming `Message` object from the request, if available.\
\
###### `related_tasks``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext.related_tasks "Permanent link")\
\
A list of tasks related to the current request.\
\
###### `task_id``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext.task_id "Permanent link")\
\
The ID of the task associated with this context.\
\
###### `attach_related_task(task)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext.attach_related_task "Permanent link")\
\
Attaches a related task to the context.\
\
This is useful for scenarios like tool execution where a new task\
might be spawned.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `task` | `Task` | The `Task` object to attach. | _required_ |\
\
###### `get_user_input(delimiter='\n')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.context.RequestContext.get_user_input "Permanent link")\
\
Extracts text content from the user's message parts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `delimiter` | `str` | The string to use when joining multiple text parts. | `'\n'` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `str` | A single string containing all text content from the user message, |\
| `str` | joined by the specified delimiter. Returns an empty string if no |\
| `str` | user message is present or if it contains no text parts. |\
\
#### `request_context_builder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.request_context_builder "Permanent link")\
\
##### `RequestContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.request_context_builder.RequestContextBuilder "Permanent link")\
\
Bases: `ABC`\
\
Builds request context to be supplied to agent executor.\
\
###### `build(params=None, task_id=None, context_id=None, task=None, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.request_context_builder.RequestContextBuilder.build "Permanent link")\
\
#### `simple_request_context_builder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.simple_request_context_builder "Permanent link")\
\
##### `SimpleRequestContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.simple_request_context_builder.SimpleRequestContextBuilder "Permanent link")\
\
Bases: `RequestContextBuilder`\
\
Builds request context and populates referred tasks.\
\
###### `build(params=None, task_id=None, context_id=None, task=None, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.agent_execution.simple_request_context_builder.SimpleRequestContextBuilder.build "Permanent link")\
\
Builds the request context for an agent execution.\
\
This method assembles the RequestContext object. If the builder was\
initialized with `should_populate_referred_tasks=True`, it fetches all tasks\
referenced in `params.message.referenceTaskIds` from the `task_store`.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `MessageSendParams | None` | The parameters of the incoming message send request. | `None` |\
| `task_id` | `str | None` | The ID of the task being executed. | `None` |\
| `context_id` | `str | None` | The ID of the current execution context. | `None` |\
| `task` | `Task | None` | The primary task object associated with the request. | `None` |\
| `context` | `ServerCallContext | None` | The server call context, containing metadata about the call. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `RequestContext` | An instance of RequestContext populated with the provided information |\
| `RequestContext` | and potentially a list of related tasks. |\
\
### `apps` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps "Permanent link")\
\
HTTP application components for the A2A server.\
\
#### `A2AFastAPIApplication` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AFastAPIApplication "Permanent link")\
\
Bases: `JSONRPCApplication`\
\
A FastAPI application implementing the A2A protocol server endpoints.\
\
Handles incoming JSON-RPC requests, routes them to the appropriate\
handler methods, and manages response generation including Server-Sent Events\
(SSE).\
\
##### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AFastAPIApplication.agent_card "Permanent link")\
\
##### `extended_agent_card = extended_agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AFastAPIApplication.extended_agent_card "Permanent link")\
\
##### `handler = JSONRPCHandler(agent_card=agent_card, request_handler=http_handler)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AFastAPIApplication.handler "Permanent link")\
\
##### `build(agent_card_url='/.well-known/agent.json', rpc_url='/', extended_agent_card_url='/agent/authenticatedExtendedCard', **kwargs)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AFastAPIApplication.build "Permanent link")\
\
Builds and returns the FastAPI application instance.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL for the A2A JSON-RPC endpoint. | `'/'` |\
| `extended_agent_card_url` | `str` | The URL for the authenticated extended agent card endpoint. | `'/agent/authenticatedExtendedCard'` |\
| `**kwargs` | `Any` | Additional keyword arguments to pass to the FastAPI constructor. | `{}` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `FastAPI` | A configured FastAPI application instance. |\
\
#### `A2AStarletteApplication` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AStarletteApplication "Permanent link")\
\
Bases: `JSONRPCApplication`\
\
A Starlette application implementing the A2A protocol server endpoints.\
\
Handles incoming JSON-RPC requests, routes them to the appropriate\
handler methods, and manages response generation including Server-Sent Events\
(SSE).\
\
##### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AStarletteApplication.agent_card "Permanent link")\
\
##### `extended_agent_card = extended_agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AStarletteApplication.extended_agent_card "Permanent link")\
\
##### `handler = JSONRPCHandler(agent_card=agent_card, request_handler=http_handler)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AStarletteApplication.handler "Permanent link")\
\
##### `build(agent_card_url='/.well-known/agent.json', rpc_url='/', extended_agent_card_url='/agent/authenticatedExtendedCard', **kwargs)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AStarletteApplication.build "Permanent link")\
\
Builds and returns the Starlette application instance.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL path for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL path for the A2A JSON-RPC endpoint (POST requests). | `'/'` |\
| `extended_agent_card_url` | `str` | The URL for the authenticated extended agent card endpoint. | `'/agent/authenticatedExtendedCard'` |\
| `**kwargs` | `Any` | Additional keyword arguments to pass to the Starlette constructor. | `{}` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Starlette` | A configured Starlette application instance. |\
\
##### `routes(agent_card_url='/.well-known/agent.json', rpc_url='/', extended_agent_card_url='/agent/authenticatedExtendedCard')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.A2AStarletteApplication.routes "Permanent link")\
\
Returns the Starlette Routes for handling A2A requests.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL path for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL path for the A2A JSON-RPC endpoint (POST requests). | `'/'` |\
| `extended_agent_card_url` | `str` | The URL for the authenticated extended agent card endpoint. | `'/agent/authenticatedExtendedCard'` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `list[Route]` | A list of Starlette Route objects. |\
\
#### `CallContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.CallContextBuilder "Permanent link")\
\
Bases: `ABC`\
\
A class for building ServerCallContexts using the Starlette Request.\
\
##### `build(request)``abstractmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.CallContextBuilder.build "Permanent link")\
\
Builds a ServerCallContext from a Starlette Request.\
\
#### `JSONRPCApplication` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.JSONRPCApplication "Permanent link")\
\
Bases: `ABC`\
\
Base class for A2A JSONRPC applications.\
\
Handles incoming JSON-RPC requests, routes them to the appropriate\
handler methods, and manages response generation including Server-Sent Events\
(SSE).\
\
##### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.JSONRPCApplication.agent_card "Permanent link")\
\
##### `extended_agent_card = extended_agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.JSONRPCApplication.extended_agent_card "Permanent link")\
\
##### `handler = JSONRPCHandler(agent_card=agent_card, request_handler=http_handler)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.JSONRPCApplication.handler "Permanent link")\
\
##### `build(agent_card_url='/.well-known/agent.json', rpc_url='/', **kwargs)``abstractmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.JSONRPCApplication.build "Permanent link")\
\
Builds and returns the JSONRPC application instance.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL for the A2A JSON-RPC endpoint | `'/'` |\
| `**kwargs` | `Any` | Additional keyword arguments to pass to the FastAPI constructor. | `{}` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `FastAPI | Starlette` | A configured JSONRPC application instance. |\
\
#### `jsonrpc` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc "Permanent link")\
\
A2A JSON-RPC Applications.\
\
##### `A2AFastAPIApplication` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AFastAPIApplication "Permanent link")\
\
Bases: `JSONRPCApplication`\
\
A FastAPI application implementing the A2A protocol server endpoints.\
\
Handles incoming JSON-RPC requests, routes them to the appropriate\
handler methods, and manages response generation including Server-Sent Events\
(SSE).\
\
###### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AFastAPIApplication.agent_card "Permanent link")\
\
###### `extended_agent_card = extended_agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AFastAPIApplication.extended_agent_card "Permanent link")\
\
###### `handler = JSONRPCHandler(agent_card=agent_card, request_handler=http_handler)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AFastAPIApplication.handler "Permanent link")\
\
###### `build(agent_card_url='/.well-known/agent.json', rpc_url='/', extended_agent_card_url='/agent/authenticatedExtendedCard', **kwargs)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AFastAPIApplication.build "Permanent link")\
\
Builds and returns the FastAPI application instance.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL for the A2A JSON-RPC endpoint. | `'/'` |\
| `extended_agent_card_url` | `str` | The URL for the authenticated extended agent card endpoint. | `'/agent/authenticatedExtendedCard'` |\
| `**kwargs` | `Any` | Additional keyword arguments to pass to the FastAPI constructor. | `{}` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `FastAPI` | A configured FastAPI application instance. |\
\
##### `A2AStarletteApplication` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AStarletteApplication "Permanent link")\
\
Bases: `JSONRPCApplication`\
\
A Starlette application implementing the A2A protocol server endpoints.\
\
Handles incoming JSON-RPC requests, routes them to the appropriate\
handler methods, and manages response generation including Server-Sent Events\
(SSE).\
\
###### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AStarletteApplication.agent_card "Permanent link")\
\
###### `extended_agent_card = extended_agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AStarletteApplication.extended_agent_card "Permanent link")\
\
###### `handler = JSONRPCHandler(agent_card=agent_card, request_handler=http_handler)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AStarletteApplication.handler "Permanent link")\
\
###### `build(agent_card_url='/.well-known/agent.json', rpc_url='/', extended_agent_card_url='/agent/authenticatedExtendedCard', **kwargs)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AStarletteApplication.build "Permanent link")\
\
Builds and returns the Starlette application instance.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL path for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL path for the A2A JSON-RPC endpoint (POST requests). | `'/'` |\
| `extended_agent_card_url` | `str` | The URL for the authenticated extended agent card endpoint. | `'/agent/authenticatedExtendedCard'` |\
| `**kwargs` | `Any` | Additional keyword arguments to pass to the Starlette constructor. | `{}` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Starlette` | A configured Starlette application instance. |\
\
###### `routes(agent_card_url='/.well-known/agent.json', rpc_url='/', extended_agent_card_url='/agent/authenticatedExtendedCard')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.A2AStarletteApplication.routes "Permanent link")\
\
Returns the Starlette Routes for handling A2A requests.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL path for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL path for the A2A JSON-RPC endpoint (POST requests). | `'/'` |\
| `extended_agent_card_url` | `str` | The URL for the authenticated extended agent card endpoint. | `'/agent/authenticatedExtendedCard'` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `list[Route]` | A list of Starlette Route objects. |\
\
##### `CallContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.CallContextBuilder "Permanent link")\
\
Bases: `ABC`\
\
A class for building ServerCallContexts using the Starlette Request.\
\
###### `build(request)``abstractmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.CallContextBuilder.build "Permanent link")\
\
Builds a ServerCallContext from a Starlette Request.\
\
##### `JSONRPCApplication` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.JSONRPCApplication "Permanent link")\
\
Bases: `ABC`\
\
Base class for A2A JSONRPC applications.\
\
Handles incoming JSON-RPC requests, routes them to the appropriate\
handler methods, and manages response generation including Server-Sent Events\
(SSE).\
\
###### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.JSONRPCApplication.agent_card "Permanent link")\
\
###### `extended_agent_card = extended_agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.JSONRPCApplication.extended_agent_card "Permanent link")\
\
###### `handler = JSONRPCHandler(agent_card=agent_card, request_handler=http_handler)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.JSONRPCApplication.handler "Permanent link")\
\
###### `build(agent_card_url='/.well-known/agent.json', rpc_url='/', **kwargs)``abstractmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.JSONRPCApplication.build "Permanent link")\
\
Builds and returns the JSONRPC application instance.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL for the A2A JSON-RPC endpoint | `'/'` |\
| `**kwargs` | `Any` | Additional keyword arguments to pass to the FastAPI constructor. | `{}` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `FastAPI | Starlette` | A configured JSONRPC application instance. |\
\
##### `fastapi_app` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.fastapi_app "Permanent link")\
\
###### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.fastapi_app.logger "Permanent link")\
\
###### `A2AFastAPIApplication` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.fastapi_app.A2AFastAPIApplication "Permanent link")\
\
Bases: `JSONRPCApplication`\
\
A FastAPI application implementing the A2A protocol server endpoints.\
\
Handles incoming JSON-RPC requests, routes them to the appropriate\
handler methods, and manages response generation including Server-Sent Events\
(SSE).\
\
`agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.fastapi_app.A2AFastAPIApplication.agent_card "Permanent link")\
\
`extended_agent_card = extended_agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.fastapi_app.A2AFastAPIApplication.extended_agent_card "Permanent link")\
\
`handler = JSONRPCHandler(agent_card=agent_card, request_handler=http_handler)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.fastapi_app.A2AFastAPIApplication.handler "Permanent link")\
\
`build(agent_card_url='/.well-known/agent.json', rpc_url='/', extended_agent_card_url='/agent/authenticatedExtendedCard', **kwargs)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.fastapi_app.A2AFastAPIApplication.build "Permanent link")\
\
Builds and returns the FastAPI application instance.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL for the A2A JSON-RPC endpoint. | `'/'` |\
| `extended_agent_card_url` | `str` | The URL for the authenticated extended agent card endpoint. | `'/agent/authenticatedExtendedCard'` |\
| `**kwargs` | `Any` | Additional keyword arguments to pass to the FastAPI constructor. | `{}` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `FastAPI` | A configured FastAPI application instance. |\
\
##### `jsonrpc_app` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.jsonrpc_app "Permanent link")\
\
###### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.jsonrpc_app.logger "Permanent link")\
\
###### `CallContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.jsonrpc_app.CallContextBuilder "Permanent link")\
\
Bases: `ABC`\
\
A class for building ServerCallContexts using the Starlette Request.\
\
`build(request)``abstractmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.jsonrpc_app.CallContextBuilder.build "Permanent link")\
\
Builds a ServerCallContext from a Starlette Request.\
\
###### `DefaultCallContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.jsonrpc_app.DefaultCallContextBuilder "Permanent link")\
\
Bases: `CallContextBuilder`\
\
A default implementation of CallContextBuilder.\
\
`build(request)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.jsonrpc_app.DefaultCallContextBuilder.build "Permanent link")\
\
Builds a ServerCallContext from a Starlette Request.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `Request` | The incoming Starlette Request object. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `ServerCallContext` | A ServerCallContext instance populated with user and state |\
| `ServerCallContext` | information from the request. |\
\
###### `JSONRPCApplication` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.jsonrpc_app.JSONRPCApplication "Permanent link")\
\
Bases: `ABC`\
\
Base class for A2A JSONRPC applications.\
\
Handles incoming JSON-RPC requests, routes them to the appropriate\
handler methods, and manages response generation including Server-Sent Events\
(SSE).\
\
`agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.jsonrpc_app.JSONRPCApplication.agent_card "Permanent link")\
\
`extended_agent_card = extended_agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.jsonrpc_app.JSONRPCApplication.extended_agent_card "Permanent link")\
\
`handler = JSONRPCHandler(agent_card=agent_card, request_handler=http_handler)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.jsonrpc_app.JSONRPCApplication.handler "Permanent link")\
\
`build(agent_card_url='/.well-known/agent.json', rpc_url='/', **kwargs)``abstractmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.jsonrpc_app.JSONRPCApplication.build "Permanent link")\
\
Builds and returns the JSONRPC application instance.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL for the A2A JSON-RPC endpoint | `'/'` |\
| `**kwargs` | `Any` | Additional keyword arguments to pass to the FastAPI constructor. | `{}` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `FastAPI | Starlette` | A configured JSONRPC application instance. |\
\
###### `StarletteUserProxy` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.jsonrpc_app.StarletteUserProxy "Permanent link")\
\
Bases: `User`\
\
Adapts the Starlette User class to the A2A user representation.\
\
`is_authenticated``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.jsonrpc_app.StarletteUserProxy.is_authenticated "Permanent link")\
\
Returns whether the current user is authenticated.\
\
`user_name``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.jsonrpc_app.StarletteUserProxy.user_name "Permanent link")\
\
Returns the user name of the current user.\
\
##### `starlette_app` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.starlette_app "Permanent link")\
\
###### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.starlette_app.logger "Permanent link")\
\
###### `A2AStarletteApplication` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.apps.jsonrpc.starlette_app.A2AStarletteApplication "Permanent link")\
\
Bases: `JSONRPCApplication`\
\
A Starlette application implementing the A2A protocol server endpoints.\
\
Handles incoming JSON-RPC requests, routes them to the appropriate\
handler methods, and manages response generation including Server-Sent Events\
(SSE).\
\
`agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.starlette_app.A2AStarletteApplication.agent_card "Permanent link")\
\
`extended_agent_card = extended_agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.starlette_app.A2AStarletteApplication.extended_agent_card "Permanent link")\
\
`handler = JSONRPCHandler(agent_card=agent_card, request_handler=http_handler)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.starlette_app.A2AStarletteApplication.handler "Permanent link")\
\
`build(agent_card_url='/.well-known/agent.json', rpc_url='/', extended_agent_card_url='/agent/authenticatedExtendedCard', **kwargs)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.starlette_app.A2AStarletteApplication.build "Permanent link")\
\
Builds and returns the Starlette application instance.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL path for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL path for the A2A JSON-RPC endpoint (POST requests). | `'/'` |\
| `extended_agent_card_url` | `str` | The URL for the authenticated extended agent card endpoint. | `'/agent/authenticatedExtendedCard'` |\
| `**kwargs` | `Any` | Additional keyword arguments to pass to the Starlette constructor. | `{}` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Starlette` | A configured Starlette application instance. |\
\
`routes(agent_card_url='/.well-known/agent.json', rpc_url='/', extended_agent_card_url='/agent/authenticatedExtendedCard')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/#a2a.server.apps.jsonrpc.starlette_app.A2AStarletteApplication.routes "Permanent link")\
\
Returns the Starlette Routes for handling A2A requests.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_card_url` | `str` | The URL path for the agent card endpoint. | `'/.well-known/agent.json'` |\
| `rpc_url` | `str` | The URL path for the A2A JSON-RPC endpoint (POST requests). | `'/'` |\
| `extended_agent_card_url` | `str` | The URL for the authenticated extended agent card endpoint. | `'/agent/authenticatedExtendedCard'` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `list[Route]` | A list of Starlette Route objects. |\
\
### `context` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.context "Permanent link")\
\
Defines the ServerCallContext class.\
\
#### `State = collections.abc.MutableMapping[str, typing.Any]``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.context.State "Permanent link")\
\
#### `ServerCallContext` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.context.ServerCallContext "Permanent link")\
\
Bases: `BaseModel`\
\
A context passed when calling a server method.\
\
This class allows storing arbitrary user data in the state attribute.\
\
##### `model_config = ConfigDict(arbitrary_types_allowed=True)``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.context.ServerCallContext.model_config "Permanent link")\
\
##### `state = Field(default={})``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.context.ServerCallContext.state "Permanent link")\
\
##### `user = Field(default=UnauthenticatedUser())``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.context.ServerCallContext.user "Permanent link")\
\
### `events` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events "Permanent link")\
\
Event handling components for the A2A server.\
\
#### `Event = Message | Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.Event "Permanent link")\
\
Type alias for events that can be enqueued.\
\
#### `EventConsumer` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventConsumer "Permanent link")\
\
Consumer to read events from the agent event queue.\
\
##### `queue = queue``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventConsumer.queue "Permanent link")\
\
##### `agent_task_callback(agent_task)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventConsumer.agent_task_callback "Permanent link")\
\
Callback to handle exceptions from the agent's execution task.\
\
If the agent's asyncio task raises an exception, this callback is\
invoked, and the exception is stored to be re-raised by the consumer loop.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_task` | `Task[None]` | The asyncio.Task that completed. | _required_ |\
\
##### `consume_all()``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventConsumer.consume_all "Permanent link")\
\
Consume all the generated streaming events from the agent.\
\
This method yields events as they become available from the queue\
until a final event is received or the queue is closed. It also\
monitors for exceptions set by the `agent_task_callback`.\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncGenerator[Event]` | Events dequeued from the queue. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `BaseException` | If an exception was set by the `agent_task_callback`. |\
\
##### `consume_one()``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventConsumer.consume_one "Permanent link")\
\
Consume one event from the agent event queue non-blocking.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Event` | The next event from the queue. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError` | If the queue is empty when attempting to dequeue<br>immediately. |\
\
#### `EventQueue` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventQueue "Permanent link")\
\
Event queue for A2A responses from agent.\
\
Acts as a buffer between the agent's asynchronous execution and the\
server's response handling (e.g., streaming via SSE). Supports tapping\
to create child queues that receive the same events.\
\
##### `queue = asyncio.Queue(maxsize=max_queue_size)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventQueue.queue "Permanent link")\
\
##### `close()``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventQueue.close "Permanent link")\
\
Closes the queue for future push events.\
\
Once closed, `dequeue_event` will eventually raise `asyncio.QueueShutDown`\
when the queue is empty. Also closes all child queues.\
\
##### `dequeue_event(no_wait=False)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventQueue.dequeue_event "Permanent link")\
\
Dequeues an event from the queue.\
\
This implementation expects that dequeue to raise an exception when\
the queue has been closed. In python 3.13+ this is naturally provided\
by the QueueShutDown exception generated when the queue has closed and\
the user is awaiting the queue.get method. Python<=3.12 this needs to\
manage this lifecycle itself. The current implementation can lead to\
blocking if the dequeue\_event is called before the EventQueue has been\
closed but when there are no events on the queue. Two ways to avoid this\
are to call this with no\_wait = True which won't block, but is the\
callers responsibility to retry as appropriate. Alternatively, one can\
use a async Task management solution to cancel the get task if the queue\
has closed or some other condition is met. The implementation of the\
EventConsumer uses an async.wait with a timeout to abort the\
dequeue\_event call and retry, when it will return with a closed error.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `no_wait` | `bool` | If True, retrieve an event immediately or raise `asyncio.QueueEmpty`.<br>If False (default), wait until an event is available. | `False` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Event` | The next event from the queue. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `QueueEmpty` | If `no_wait` is True and the queue is empty. |\
| `QueueShutDown` | If the queue has been closed and is empty. |\
\
##### `enqueue_event(event)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventQueue.enqueue_event "Permanent link")\
\
Enqueues an event to this queue and all its children.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `event` | `Event` | The event object to enqueue. | _required_ |\
\
##### `is_closed()` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventQueue.is_closed "Permanent link")\
\
Checks if the queue is closed.\
\
##### `tap()` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventQueue.tap "Permanent link")\
\
Taps the event queue to create a new child queue that receives all future events.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `EventQueue` | A new `EventQueue` instance that will receive all events enqueued |\
| `EventQueue` | to this parent queue from this point forward. |\
\
##### `task_done()` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.EventQueue.task_done "Permanent link")\
\
Signals that a formerly enqueued task is complete.\
\
Used in conjunction with `dequeue_event` to track processed items.\
\
#### `InMemoryQueueManager` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.InMemoryQueueManager "Permanent link")\
\
Bases: `QueueManager`\
\
InMemoryQueueManager is used for a single binary management.\
\
This implements the `QueueManager` interface using in-memory storage for event\
queues. It requires all incoming interactions for a given task ID to hit the\
same binary instance.\
\
This implementation is suitable for single-instance deployments but needs\
a distributed approach for scalable deployments.\
\
##### `add(task_id, queue)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.InMemoryQueueManager.add "Permanent link")\
\
Adds a new event queue for a task ID.\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `TaskQueueExists` | If a queue for the given `task_id` already exists. |\
\
##### `close(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.InMemoryQueueManager.close "Permanent link")\
\
Closes and removes the event queue for a task ID.\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `NoTaskQueue` | If no queue exists for the given `task_id`. |\
\
##### `create_or_tap(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.InMemoryQueueManager.create_or_tap "Permanent link")\
\
Creates a new event queue for a task ID if one doesn't exist, otherwise taps the existing one.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `EventQueue` | A new or child `EventQueue` instance for the `task_id`. |\
\
##### `get(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.InMemoryQueueManager.get "Permanent link")\
\
Retrieves the event queue for a task ID.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `EventQueue | None` | The `EventQueue` instance for the `task_id`, or `None` if not found. |\
\
##### `tap(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.InMemoryQueueManager.tap "Permanent link")\
\
Taps the event queue for a task ID to create a child queue.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `EventQueue | None` | A new child `EventQueue` instance, or `None` if the task ID is not found. |\
\
#### `NoTaskQueue` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.NoTaskQueue "Permanent link")\
\
Bases: `Exception`\
\
Exception raised when attempting to access or close a queue for a task ID that does not exist.\
\
#### `QueueManager` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.QueueManager "Permanent link")\
\
Bases: `ABC`\
\
Interface for managing the event queue lifecycles per task.\
\
##### `add(task_id, queue)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.QueueManager.add "Permanent link")\
\
Adds a new event queue associated with a task ID.\
\
##### `close(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.QueueManager.close "Permanent link")\
\
Closes and removes the event queue for a task ID.\
\
##### `create_or_tap(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.QueueManager.create_or_tap "Permanent link")\
\
Creates a queue if one doesn't exist, otherwise taps the existing one.\
\
##### `get(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.QueueManager.get "Permanent link")\
\
Retrieves the event queue for a task ID.\
\
##### `tap(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.QueueManager.tap "Permanent link")\
\
Creates a child event queue (tap) for an existing task ID.\
\
#### `TaskQueueExists` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.TaskQueueExists "Permanent link")\
\
Bases: `Exception`\
\
Exception raised when attempting to add a queue for a task ID that already exists.\
\
#### `event_consumer` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_consumer "Permanent link")\
\
##### `QueueClosed = asyncio.QueueEmpty``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_consumer.QueueClosed "Permanent link")\
\
##### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_consumer.logger "Permanent link")\
\
##### `EventConsumer` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_consumer.EventConsumer "Permanent link")\
\
Consumer to read events from the agent event queue.\
\
###### `queue = queue``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_consumer.EventConsumer.queue "Permanent link")\
\
###### `agent_task_callback(agent_task)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_consumer.EventConsumer.agent_task_callback "Permanent link")\
\
Callback to handle exceptions from the agent's execution task.\
\
If the agent's asyncio task raises an exception, this callback is\
invoked, and the exception is stored to be re-raised by the consumer loop.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `agent_task` | `Task[None]` | The asyncio.Task that completed. | _required_ |\
\
###### `consume_all()``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_consumer.EventConsumer.consume_all "Permanent link")\
\
Consume all the generated streaming events from the agent.\
\
This method yields events as they become available from the queue\
until a final event is received or the queue is closed. It also\
monitors for exceptions set by the `agent_task_callback`.\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncGenerator[Event]` | Events dequeued from the queue. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `BaseException` | If an exception was set by the `agent_task_callback`. |\
\
###### `consume_one()``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_consumer.EventConsumer.consume_one "Permanent link")\
\
Consume one event from the agent event queue non-blocking.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Event` | The next event from the queue. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError` | If the queue is empty when attempting to dequeue<br>immediately. |\
\
#### `event_queue` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue "Permanent link")\
\
##### `DEFAULT_MAX_QUEUE_SIZE = 1024``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.DEFAULT_MAX_QUEUE_SIZE "Permanent link")\
\
##### `Event = Message | Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.Event "Permanent link")\
\
Type alias for events that can be enqueued.\
\
##### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.logger "Permanent link")\
\
##### `EventQueue` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.EventQueue "Permanent link")\
\
Event queue for A2A responses from agent.\
\
Acts as a buffer between the agent's asynchronous execution and the\
server's response handling (e.g., streaming via SSE). Supports tapping\
to create child queues that receive the same events.\
\
###### `queue = asyncio.Queue(maxsize=max_queue_size)``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.EventQueue.queue "Permanent link")\
\
###### `close()``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.EventQueue.close "Permanent link")\
\
Closes the queue for future push events.\
\
Once closed, `dequeue_event` will eventually raise `asyncio.QueueShutDown`\
when the queue is empty. Also closes all child queues.\
\
###### `dequeue_event(no_wait=False)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.EventQueue.dequeue_event "Permanent link")\
\
Dequeues an event from the queue.\
\
This implementation expects that dequeue to raise an exception when\
the queue has been closed. In python 3.13+ this is naturally provided\
by the QueueShutDown exception generated when the queue has closed and\
the user is awaiting the queue.get method. Python<=3.12 this needs to\
manage this lifecycle itself. The current implementation can lead to\
blocking if the dequeue\_event is called before the EventQueue has been\
closed but when there are no events on the queue. Two ways to avoid this\
are to call this with no\_wait = True which won't block, but is the\
callers responsibility to retry as appropriate. Alternatively, one can\
use a async Task management solution to cancel the get task if the queue\
has closed or some other condition is met. The implementation of the\
EventConsumer uses an async.wait with a timeout to abort the\
dequeue\_event call and retry, when it will return with a closed error.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `no_wait` | `bool` | If True, retrieve an event immediately or raise `asyncio.QueueEmpty`.<br>If False (default), wait until an event is available. | `False` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Event` | The next event from the queue. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `QueueEmpty` | If `no_wait` is True and the queue is empty. |\
| `QueueShutDown` | If the queue has been closed and is empty. |\
\
###### `enqueue_event(event)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.EventQueue.enqueue_event "Permanent link")\
\
Enqueues an event to this queue and all its children.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `event` | `Event` | The event object to enqueue. | _required_ |\
\
###### `is_closed()` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.EventQueue.is_closed "Permanent link")\
\
Checks if the queue is closed.\
\
###### `tap()` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.EventQueue.tap "Permanent link")\
\
Taps the event queue to create a new child queue that receives all future events.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `EventQueue` | A new `EventQueue` instance that will receive all events enqueued |\
| `EventQueue` | to this parent queue from this point forward. |\
\
###### `task_done()` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.event_queue.EventQueue.task_done "Permanent link")\
\
Signals that a formerly enqueued task is complete.\
\
Used in conjunction with `dequeue_event` to track processed items.\
\
#### `in_memory_queue_manager` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.in_memory_queue_manager "Permanent link")\
\
##### `InMemoryQueueManager` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.in_memory_queue_manager.InMemoryQueueManager "Permanent link")\
\
Bases: `QueueManager`\
\
InMemoryQueueManager is used for a single binary management.\
\
This implements the `QueueManager` interface using in-memory storage for event\
queues. It requires all incoming interactions for a given task ID to hit the\
same binary instance.\
\
This implementation is suitable for single-instance deployments but needs\
a distributed approach for scalable deployments.\
\
###### `add(task_id, queue)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.in_memory_queue_manager.InMemoryQueueManager.add "Permanent link")\
\
Adds a new event queue for a task ID.\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `TaskQueueExists` | If a queue for the given `task_id` already exists. |\
\
###### `close(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.in_memory_queue_manager.InMemoryQueueManager.close "Permanent link")\
\
Closes and removes the event queue for a task ID.\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `NoTaskQueue` | If no queue exists for the given `task_id`. |\
\
###### `create_or_tap(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.in_memory_queue_manager.InMemoryQueueManager.create_or_tap "Permanent link")\
\
Creates a new event queue for a task ID if one doesn't exist, otherwise taps the existing one.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `EventQueue` | A new or child `EventQueue` instance for the `task_id`. |\
\
###### `get(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.in_memory_queue_manager.InMemoryQueueManager.get "Permanent link")\
\
Retrieves the event queue for a task ID.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `EventQueue | None` | The `EventQueue` instance for the `task_id`, or `None` if not found. |\
\
###### `tap(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.in_memory_queue_manager.InMemoryQueueManager.tap "Permanent link")\
\
Taps the event queue for a task ID to create a child queue.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `EventQueue | None` | A new child `EventQueue` instance, or `None` if the task ID is not found. |\
\
#### `queue_manager` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.queue_manager "Permanent link")\
\
##### `NoTaskQueue` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.queue_manager.NoTaskQueue "Permanent link")\
\
Bases: `Exception`\
\
Exception raised when attempting to access or close a queue for a task ID that does not exist.\
\
##### `QueueManager` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.queue_manager.QueueManager "Permanent link")\
\
Bases: `ABC`\
\
Interface for managing the event queue lifecycles per task.\
\
###### `add(task_id, queue)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.queue_manager.QueueManager.add "Permanent link")\
\
Adds a new event queue associated with a task ID.\
\
###### `close(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.queue_manager.QueueManager.close "Permanent link")\
\
Closes and removes the event queue for a task ID.\
\
###### `create_or_tap(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.queue_manager.QueueManager.create_or_tap "Permanent link")\
\
Creates a queue if one doesn't exist, otherwise taps the existing one.\
\
###### `get(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.queue_manager.QueueManager.get "Permanent link")\
\
Retrieves the event queue for a task ID.\
\
###### `tap(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.queue_manager.QueueManager.tap "Permanent link")\
\
Creates a child event queue (tap) for an existing task ID.\
\
##### `TaskQueueExists` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.events.queue_manager.TaskQueueExists "Permanent link")\
\
Bases: `Exception`\
\
Exception raised when attempting to add a queue for a task ID that already exists.\
\
### `request_handlers` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers "Permanent link")\
\
Request handler components for the A2A server.\
\
#### `DefaultRequestHandler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler "Permanent link")\
\
Bases: `RequestHandler`\
\
Default request handler for all incoming requests.\
\
This handler provides default implementations for all A2A JSON-RPC methods,\
coordinating between the `AgentExecutor`, `TaskStore`, `QueueManager`,\
and optional `PushNotifier`.\
\
##### `agent_executor = agent_executor``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.agent_executor "Permanent link")\
\
##### `task_store = task_store``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.task_store "Permanent link")\
\
##### `on_cancel_task(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.on_cancel_task "Permanent link")\
\
Default handler for 'tasks/cancel'.\
\
Attempts to cancel the task managed by the `AgentExecutor`.\
\
##### `on_get_task(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.on_get_task "Permanent link")\
\
Default handler for 'tasks/get'.\
\
##### `on_get_task_push_notification_config(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.on_get_task_push_notification_config "Permanent link")\
\
Default handler for 'tasks/pushNotificationConfig/get'.\
\
Requires a `PushNotifier` to be configured.\
\
##### `on_message_send(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.on_message_send "Permanent link")\
\
Default handler for 'message/send' interface (non-streaming).\
\
Starts the agent execution for the message and waits for the final\
result (Task or Message).\
\
##### `on_message_send_stream(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.on_message_send_stream "Permanent link")\
\
Default handler for 'message/stream' (streaming).\
\
Starts the agent execution and yields events as they are produced\
by the agent.\
\
##### `on_resubscribe_to_task(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.on_resubscribe_to_task "Permanent link")\
\
Default handler for 'tasks/resubscribe'.\
\
Allows a client to re-attach to a running streaming task's event stream.\
Requires the task and its queue to still be active.\
\
##### `on_set_task_push_notification_config(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.on_set_task_push_notification_config "Permanent link")\
\
Default handler for 'tasks/pushNotificationConfig/set'.\
\
Requires a `PushNotifier` to be configured.\
\
##### `should_add_push_info(params)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.DefaultRequestHandler.should_add_push_info "Permanent link")\
\
Determines if push notification info should be set for a task.\
\
#### `GrpcHandler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler "Permanent link")\
\
Bases: `A2AServiceServicer`\
\
Maps incoming gRPC requests to the appropriate request handler method.\
\
##### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.agent_card "Permanent link")\
\
##### `context_builder = context_builder or DefaultCallContextBuilder()``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.context_builder "Permanent link")\
\
##### `request_handler = request_handler``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.request_handler "Permanent link")\
\
##### `CancelTask(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.CancelTask "Permanent link")\
\
Handles the 'CancelTask' gRPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `CancelTaskRequest` | The incoming `CancelTaskRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A `Task` object containing the updated Task or a gRPC error. |\
\
##### `CreateTaskPushNotification(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.CreateTaskPushNotification "Permanent link")\
\
Handles the 'CreateTaskPushNotification' gRPC method.\
\
Requires the agent to support push notifications.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `CreateTaskPushNotificationRequest` | The incoming `CreateTaskPushNotificationRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `TaskPushNotificationConfig` | A `TaskPushNotificationConfig` object |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError` | If push notifications are not supported by the agent<br>(due to the `@validate` decorator). |\
\
##### `GetAgentCard(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.GetAgentCard "Permanent link")\
\
Get the agent card for the agent served.\
\
##### `GetTask(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.GetTask "Permanent link")\
\
Handles the 'GetTask' gRPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `GetTaskRequest` | The incoming `GetTaskRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A `Task` object. |\
\
##### `GetTaskPushNotification(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.GetTaskPushNotification "Permanent link")\
\
Handles the 'GetTaskPushNotification' gRPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `GetTaskPushNotificationRequest` | The incoming `GetTaskPushNotificationConfigRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `TaskPushNotificationConfig` | A `TaskPushNotificationConfig` object containing the config. |\
\
##### `ListTaskPushNotification(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.ListTaskPushNotification "Permanent link")\
\
Get a list of push notifications configured for a task.\
\
##### `SendMessage(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.SendMessage "Permanent link")\
\
Handles the 'SendMessage' gRPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SendMessageRequest` | The incoming `SendMessageRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `SendMessageResponse` | A `SendMessageResponse` object containing the result (Task or |\
| `SendMessageResponse` | Message) or throws an error response if a `ServerError` is raised |\
| `SendMessageResponse` | by the handler. |\
\
##### `SendStreamingMessage(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.SendStreamingMessage "Permanent link")\
\
Handles the 'StreamMessage' gRPC method.\
\
Yields response objects as they are produced by the underlying handler's\
stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SendMessageRequest` | The incoming `SendMessageRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncIterable[StreamResponse]` | `StreamResponse` objects containing streaming events |\
| `AsyncIterable[StreamResponse]` | (Task, Message, TaskStatusUpdateEvent, TaskArtifactUpdateEvent) |\
| `AsyncIterable[StreamResponse]` | or gRPC error responses if a `ServerError` is raised. |\
\
##### `TaskSubscription(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.TaskSubscription "Permanent link")\
\
Handles the 'TaskSubscription' gRPC method.\
\
Yields response objects as they are produced by the underlying handler's\
stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `TaskSubscriptionRequest` | The incoming `TaskSubscriptionRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncIterable[StreamResponse]` | `StreamResponse` objects containing streaming events |\
\
##### `abort_context(error, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.GrpcHandler.abort_context "Permanent link")\
\
Sets the grpc errors appropriately in the context.\
\
#### `JSONRPCHandler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler "Permanent link")\
\
Maps incoming JSON-RPC requests to the appropriate request handler method and formats responses.\
\
##### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler.agent_card "Permanent link")\
\
##### `request_handler = request_handler``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler.request_handler "Permanent link")\
\
##### `get_push_notification(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler.get_push_notification "Permanent link")\
\
Handles the 'tasks/pushNotificationConfig/get' JSON-RPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `GetTaskPushNotificationConfigRequest` | The incoming `GetTaskPushNotificationConfigRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `GetTaskPushNotificationConfigResponse` | A `GetTaskPushNotificationConfigResponse` object containing the config or a JSON-RPC error. |\
\
##### `on_cancel_task(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler.on_cancel_task "Permanent link")\
\
Handles the 'tasks/cancel' JSON-RPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `CancelTaskRequest` | The incoming `CancelTaskRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `CancelTaskResponse` | A `CancelTaskResponse` object containing the updated Task or a JSON-RPC error. |\
\
##### `on_get_task(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler.on_get_task "Permanent link")\
\
Handles the 'tasks/get' JSON-RPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `GetTaskRequest` | The incoming `GetTaskRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `GetTaskResponse` | A `GetTaskResponse` object containing the Task or a JSON-RPC error. |\
\
##### `on_message_send(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler.on_message_send "Permanent link")\
\
Handles the 'message/send' JSON-RPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SendMessageRequest` | The incoming `SendMessageRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `SendMessageResponse` | A `SendMessageResponse` object containing the result (Task or Message) |\
| `SendMessageResponse` | or a JSON-RPC error response if a `ServerError` is raised by the handler. |\
\
##### `on_message_send_stream(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler.on_message_send_stream "Permanent link")\
\
Handles the 'message/stream' JSON-RPC method.\
\
Yields response objects as they are produced by the underlying handler's stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SendStreamingMessageRequest` | The incoming `SendStreamingMessageRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncIterable[SendStreamingMessageResponse]` | `SendStreamingMessageResponse` objects containing streaming events |\
| `AsyncIterable[SendStreamingMessageResponse]` | (Task, Message, TaskStatusUpdateEvent, TaskArtifactUpdateEvent) |\
| `AsyncIterable[SendStreamingMessageResponse]` | or JSON-RPC error responses if a `ServerError` is raised. |\
\
##### `on_resubscribe_to_task(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler.on_resubscribe_to_task "Permanent link")\
\
Handles the 'tasks/resubscribe' JSON-RPC method.\
\
Yields response objects as they are produced by the underlying handler's stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `TaskResubscriptionRequest` | The incoming `TaskResubscriptionRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncIterable[SendStreamingMessageResponse]` | `SendStreamingMessageResponse` objects containing streaming events |\
| `AsyncIterable[SendStreamingMessageResponse]` | or JSON-RPC error responses if a `ServerError` is raised. |\
\
##### `set_push_notification(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.JSONRPCHandler.set_push_notification "Permanent link")\
\
Handles the 'tasks/pushNotificationConfig/set' JSON-RPC method.\
\
Requires the agent to support push notifications.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SetTaskPushNotificationConfigRequest` | The incoming `SetTaskPushNotificationConfigRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `SetTaskPushNotificationConfigResponse` | A `SetTaskPushNotificationConfigResponse` object containing the config or a JSON-RPC error. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError` | If push notifications are not supported by the agent<br>(due to the `@validate` decorator). |\
\
#### `RequestHandler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.RequestHandler "Permanent link")\
\
Bases: `ABC`\
\
A2A request handler interface.\
\
This interface defines the methods that an A2A server implementation must\
provide to handle incoming JSON-RPC requests.\
\
##### `on_cancel_task(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.RequestHandler.on_cancel_task "Permanent link")\
\
Handles the 'tasks/cancel' method.\
\
Requests the agent to cancel an ongoing task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskIdParams` | Parameters specifying the task ID. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | None` | The `Task` object with its status updated to canceled, or `None` if the task was not found. |\
\
##### `on_get_task(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.RequestHandler.on_get_task "Permanent link")\
\
Handles the 'tasks/get' method.\
\
Retrieves the state and history of a specific task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskQueryParams` | Parameters specifying the task ID and optionally history length. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | None` | The `Task` object if found, otherwise `None`. |\
\
##### `on_get_task_push_notification_config(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.RequestHandler.on_get_task_push_notification_config "Permanent link")\
\
Handles the 'tasks/pushNotificationConfig/get' method.\
\
Retrieves the current push notification configuration for a task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskIdParams` | Parameters including the task ID. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `TaskPushNotificationConfig` | The `TaskPushNotificationConfig` for the task. |\
\
##### `on_message_send(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.RequestHandler.on_message_send "Permanent link")\
\
Handles the 'message/send' method (non-streaming).\
\
Sends a message to the agent to create, continue, or restart a task,\
and waits for the final result (Task or Message).\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `MessageSendParams` | Parameters including the message and configuration. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | Message` | The final `Task` object or a final `Message` object. |\
\
##### `on_message_send_stream(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.RequestHandler.on_message_send_stream "Permanent link")\
\
Handles the 'message/stream' method (streaming).\
\
Sends a message to the agent and yields stream events as they are\
produced (Task updates, Message chunks, Artifact updates).\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `MessageSendParams` | Parameters including the message and configuration. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncGenerator[Event]` | `Event` objects from the agent's execution. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError(UnsupportedOperationError)` | By default, if not implemented. |\
\
##### `on_resubscribe_to_task(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.RequestHandler.on_resubscribe_to_task "Permanent link")\
\
Handles the 'tasks/resubscribe' method.\
\
Allows a client to re-subscribe to a running streaming task's event stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskIdParams` | Parameters including the task ID. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncGenerator[Event]` | `Event` objects from the agent's ongoing execution for the specified task. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError(UnsupportedOperationError)` | By default, if not implemented. |\
\
##### `on_set_task_push_notification_config(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.RequestHandler.on_set_task_push_notification_config "Permanent link")\
\
Handles the 'tasks/pushNotificationConfig/set' method.\
\
Sets or updates the push notification configuration for a task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskPushNotificationConfig` | Parameters including the task ID and push notification configuration. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `TaskPushNotificationConfig` | The provided `TaskPushNotificationConfig` upon success. |\
\
#### `build_error_response(request_id, error, response_wrapper_type)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.build_error_response "Permanent link")\
\
Helper method to build a JSONRPCErrorResponse wrapped in the appropriate response type.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request_id` | `str | int | None` | The ID of the request that caused the error. | _required_ |\
| `error` | `A2AError | JSONRPCError` | The A2AError or JSONRPCError object. | _required_ |\
| `response_wrapper_type` | `type[RT]` | The Pydantic RootModel type that wraps the response<br>for the specific RPC method (e.g., `SendMessageResponse`). | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `RT` | A Pydantic model representing the JSON-RPC error response, |\
| `RT` | wrapped in the specified response type. |\
\
#### `prepare_response_object(request_id, response, success_response_types, success_payload_type, response_type)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.prepare_response_object "Permanent link")\
\
Helper method to build appropriate JSONRPCResponse object for RPC methods.\
\
Based on the type of the `response` object received from the handler,\
it constructs either a success response wrapped in the appropriate payload type\
or an error response.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request_id` | `str | int | None` | The ID of the request. | _required_ |\
| `response` | `EventTypes` | The object received from the request handler. | _required_ |\
| `success_response_types` | `tuple[type, ...]` | A tuple of expected Pydantic model types for a successful result. | _required_ |\
| `success_payload_type` | `type[SPT]` | The Pydantic model type for the success payload<br>(e.g., `SendMessageSuccessResponse`). | _required_ |\
| `response_type` | `type[RT]` | The Pydantic RootModel type that wraps the final response<br>(e.g., `SendMessageResponse`). | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `RT` | A Pydantic model representing the final JSON-RPC response (success or error). |\
\
#### `default_request_handler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler "Permanent link")\
\
##### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.logger "Permanent link")\
\
##### `DefaultRequestHandler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler "Permanent link")\
\
Bases: `RequestHandler`\
\
Default request handler for all incoming requests.\
\
This handler provides default implementations for all A2A JSON-RPC methods,\
coordinating between the `AgentExecutor`, `TaskStore`, `QueueManager`,\
and optional `PushNotifier`.\
\
###### `agent_executor = agent_executor``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.agent_executor "Permanent link")\
\
###### `task_store = task_store``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.task_store "Permanent link")\
\
###### `on_cancel_task(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.on_cancel_task "Permanent link")\
\
Default handler for 'tasks/cancel'.\
\
Attempts to cancel the task managed by the `AgentExecutor`.\
\
###### `on_get_task(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.on_get_task "Permanent link")\
\
Default handler for 'tasks/get'.\
\
###### `on_get_task_push_notification_config(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.on_get_task_push_notification_config "Permanent link")\
\
Default handler for 'tasks/pushNotificationConfig/get'.\
\
Requires a `PushNotifier` to be configured.\
\
###### `on_message_send(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.on_message_send "Permanent link")\
\
Default handler for 'message/send' interface (non-streaming).\
\
Starts the agent execution for the message and waits for the final\
result (Task or Message).\
\
###### `on_message_send_stream(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.on_message_send_stream "Permanent link")\
\
Default handler for 'message/stream' (streaming).\
\
Starts the agent execution and yields events as they are produced\
by the agent.\
\
###### `on_resubscribe_to_task(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.on_resubscribe_to_task "Permanent link")\
\
Default handler for 'tasks/resubscribe'.\
\
Allows a client to re-attach to a running streaming task's event stream.\
Requires the task and its queue to still be active.\
\
###### `on_set_task_push_notification_config(params, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.on_set_task_push_notification_config "Permanent link")\
\
Default handler for 'tasks/pushNotificationConfig/set'.\
\
Requires a `PushNotifier` to be configured.\
\
###### `should_add_push_info(params)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.default_request_handler.DefaultRequestHandler.should_add_push_info "Permanent link")\
\
Determines if push notification info should be set for a task.\
\
#### `grpc_handler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler "Permanent link")\
\
##### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.logger "Permanent link")\
\
##### `CallContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.CallContextBuilder "Permanent link")\
\
Bases: `ABC`\
\
A class for building ServerCallContexts using the Starlette Request.\
\
###### `build(context)``abstractmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.CallContextBuilder.build "Permanent link")\
\
Builds a ServerCallContext from a gRPC Request.\
\
##### `DefaultCallContextBuilder` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.DefaultCallContextBuilder "Permanent link")\
\
Bases: `CallContextBuilder`\
\
A default implementation of CallContextBuilder.\
\
###### `build(context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.DefaultCallContextBuilder.build "Permanent link")\
\
Builds the ServerCallContext.\
\
##### `GrpcHandler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler "Permanent link")\
\
Bases: `A2AServiceServicer`\
\
Maps incoming gRPC requests to the appropriate request handler method.\
\
###### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.agent_card "Permanent link")\
\
###### `context_builder = context_builder or DefaultCallContextBuilder()``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.context_builder "Permanent link")\
\
###### `request_handler = request_handler``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.request_handler "Permanent link")\
\
###### `CancelTask(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.CancelTask "Permanent link")\
\
Handles the 'CancelTask' gRPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `CancelTaskRequest` | The incoming `CancelTaskRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A `Task` object containing the updated Task or a gRPC error. |\
\
###### `CreateTaskPushNotification(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.CreateTaskPushNotification "Permanent link")\
\
Handles the 'CreateTaskPushNotification' gRPC method.\
\
Requires the agent to support push notifications.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `CreateTaskPushNotificationRequest` | The incoming `CreateTaskPushNotificationRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `TaskPushNotificationConfig` | A `TaskPushNotificationConfig` object |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError` | If push notifications are not supported by the agent<br>(due to the `@validate` decorator). |\
\
###### `GetAgentCard(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.GetAgentCard "Permanent link")\
\
Get the agent card for the agent served.\
\
###### `GetTask(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.GetTask "Permanent link")\
\
Handles the 'GetTask' gRPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `GetTaskRequest` | The incoming `GetTaskRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A `Task` object. |\
\
###### `GetTaskPushNotification(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.GetTaskPushNotification "Permanent link")\
\
Handles the 'GetTaskPushNotification' gRPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `GetTaskPushNotificationRequest` | The incoming `GetTaskPushNotificationConfigRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `TaskPushNotificationConfig` | A `TaskPushNotificationConfig` object containing the config. |\
\
###### `ListTaskPushNotification(request, context)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.ListTaskPushNotification "Permanent link")\
\
Get a list of push notifications configured for a task.\
\
###### `SendMessage(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.SendMessage "Permanent link")\
\
Handles the 'SendMessage' gRPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SendMessageRequest` | The incoming `SendMessageRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `SendMessageResponse` | A `SendMessageResponse` object containing the result (Task or |\
| `SendMessageResponse` | Message) or throws an error response if a `ServerError` is raised |\
| `SendMessageResponse` | by the handler. |\
\
###### `SendStreamingMessage(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.SendStreamingMessage "Permanent link")\
\
Handles the 'StreamMessage' gRPC method.\
\
Yields response objects as they are produced by the underlying handler's\
stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SendMessageRequest` | The incoming `SendMessageRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncIterable[StreamResponse]` | `StreamResponse` objects containing streaming events |\
| `AsyncIterable[StreamResponse]` | (Task, Message, TaskStatusUpdateEvent, TaskArtifactUpdateEvent) |\
| `AsyncIterable[StreamResponse]` | or gRPC error responses if a `ServerError` is raised. |\
\
###### `TaskSubscription(request, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.TaskSubscription "Permanent link")\
\
Handles the 'TaskSubscription' gRPC method.\
\
Yields response objects as they are produced by the underlying handler's\
stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `TaskSubscriptionRequest` | The incoming `TaskSubscriptionRequest` object. | _required_ |\
| `context` | `ServicerContext` | Context provided by the server. | _required_ |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncIterable[StreamResponse]` | `StreamResponse` objects containing streaming events |\
\
###### `abort_context(error, context)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.grpc_handler.GrpcHandler.abort_context "Permanent link")\
\
Sets the grpc errors appropriately in the context.\
\
#### `jsonrpc_handler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler "Permanent link")\
\
##### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.logger "Permanent link")\
\
##### `JSONRPCHandler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler "Permanent link")\
\
Maps incoming JSON-RPC requests to the appropriate request handler method and formats responses.\
\
###### `agent_card = agent_card``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler.agent_card "Permanent link")\
\
###### `request_handler = request_handler``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler.request_handler "Permanent link")\
\
###### `get_push_notification(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler.get_push_notification "Permanent link")\
\
Handles the 'tasks/pushNotificationConfig/get' JSON-RPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `GetTaskPushNotificationConfigRequest` | The incoming `GetTaskPushNotificationConfigRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `GetTaskPushNotificationConfigResponse` | A `GetTaskPushNotificationConfigResponse` object containing the config or a JSON-RPC error. |\
\
###### `on_cancel_task(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler.on_cancel_task "Permanent link")\
\
Handles the 'tasks/cancel' JSON-RPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `CancelTaskRequest` | The incoming `CancelTaskRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `CancelTaskResponse` | A `CancelTaskResponse` object containing the updated Task or a JSON-RPC error. |\
\
###### `on_get_task(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler.on_get_task "Permanent link")\
\
Handles the 'tasks/get' JSON-RPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `GetTaskRequest` | The incoming `GetTaskRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `GetTaskResponse` | A `GetTaskResponse` object containing the Task or a JSON-RPC error. |\
\
###### `on_message_send(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler.on_message_send "Permanent link")\
\
Handles the 'message/send' JSON-RPC method.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SendMessageRequest` | The incoming `SendMessageRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `SendMessageResponse` | A `SendMessageResponse` object containing the result (Task or Message) |\
| `SendMessageResponse` | or a JSON-RPC error response if a `ServerError` is raised by the handler. |\
\
###### `on_message_send_stream(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler.on_message_send_stream "Permanent link")\
\
Handles the 'message/stream' JSON-RPC method.\
\
Yields response objects as they are produced by the underlying handler's stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SendStreamingMessageRequest` | The incoming `SendStreamingMessageRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncIterable[SendStreamingMessageResponse]` | `SendStreamingMessageResponse` objects containing streaming events |\
| `AsyncIterable[SendStreamingMessageResponse]` | (Task, Message, TaskStatusUpdateEvent, TaskArtifactUpdateEvent) |\
| `AsyncIterable[SendStreamingMessageResponse]` | or JSON-RPC error responses if a `ServerError` is raised. |\
\
###### `on_resubscribe_to_task(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler.on_resubscribe_to_task "Permanent link")\
\
Handles the 'tasks/resubscribe' JSON-RPC method.\
\
Yields response objects as they are produced by the underlying handler's stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `TaskResubscriptionRequest` | The incoming `TaskResubscriptionRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncIterable[SendStreamingMessageResponse]` | `SendStreamingMessageResponse` objects containing streaming events |\
| `AsyncIterable[SendStreamingMessageResponse]` | or JSON-RPC error responses if a `ServerError` is raised. |\
\
###### `set_push_notification(request, context=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.jsonrpc_handler.JSONRPCHandler.set_push_notification "Permanent link")\
\
Handles the 'tasks/pushNotificationConfig/set' JSON-RPC method.\
\
Requires the agent to support push notifications.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `SetTaskPushNotificationConfigRequest` | The incoming `SetTaskPushNotificationConfigRequest` object. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `SetTaskPushNotificationConfigResponse` | A `SetTaskPushNotificationConfigResponse` object containing the config or a JSON-RPC error. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError` | If push notifications are not supported by the agent<br>(due to the `@validate` decorator). |\
\
#### `request_handler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.request_handler "Permanent link")\
\
##### `RequestHandler` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.request_handler.RequestHandler "Permanent link")\
\
Bases: `ABC`\
\
A2A request handler interface.\
\
This interface defines the methods that an A2A server implementation must\
provide to handle incoming JSON-RPC requests.\
\
###### `on_cancel_task(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.request_handler.RequestHandler.on_cancel_task "Permanent link")\
\
Handles the 'tasks/cancel' method.\
\
Requests the agent to cancel an ongoing task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskIdParams` | Parameters specifying the task ID. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | None` | The `Task` object with its status updated to canceled, or `None` if the task was not found. |\
\
###### `on_get_task(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.request_handler.RequestHandler.on_get_task "Permanent link")\
\
Handles the 'tasks/get' method.\
\
Retrieves the state and history of a specific task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskQueryParams` | Parameters specifying the task ID and optionally history length. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | None` | The `Task` object if found, otherwise `None`. |\
\
###### `on_get_task_push_notification_config(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.request_handler.RequestHandler.on_get_task_push_notification_config "Permanent link")\
\
Handles the 'tasks/pushNotificationConfig/get' method.\
\
Retrieves the current push notification configuration for a task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskIdParams` | Parameters including the task ID. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `TaskPushNotificationConfig` | The `TaskPushNotificationConfig` for the task. |\
\
###### `on_message_send(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.request_handler.RequestHandler.on_message_send "Permanent link")\
\
Handles the 'message/send' method (non-streaming).\
\
Sends a message to the agent to create, continue, or restart a task,\
and waits for the final result (Task or Message).\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `MessageSendParams` | Parameters including the message and configuration. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | Message` | The final `Task` object or a final `Message` object. |\
\
###### `on_message_send_stream(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.request_handler.RequestHandler.on_message_send_stream "Permanent link")\
\
Handles the 'message/stream' method (streaming).\
\
Sends a message to the agent and yields stream events as they are\
produced (Task updates, Message chunks, Artifact updates).\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `MessageSendParams` | Parameters including the message and configuration. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncGenerator[Event]` | `Event` objects from the agent's execution. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError(UnsupportedOperationError)` | By default, if not implemented. |\
\
###### `on_resubscribe_to_task(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.request_handler.RequestHandler.on_resubscribe_to_task "Permanent link")\
\
Handles the 'tasks/resubscribe' method.\
\
Allows a client to re-subscribe to a running streaming task's event stream.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskIdParams` | Parameters including the task ID. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncGenerator[Event]` | `Event` objects from the agent's ongoing execution for the specified task. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError(UnsupportedOperationError)` | By default, if not implemented. |\
\
###### `on_set_task_push_notification_config(params, context=None)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.request_handler.RequestHandler.on_set_task_push_notification_config "Permanent link")\
\
Handles the 'tasks/pushNotificationConfig/set' method.\
\
Sets or updates the push notification configuration for a task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `params` | `TaskPushNotificationConfig` | Parameters including the task ID and push notification configuration. | _required_ |\
| `context` | `ServerCallContext | None` | Context provided by the server. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `TaskPushNotificationConfig` | The provided `TaskPushNotificationConfig` upon success. |\
\
#### `response_helpers` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.response_helpers "Permanent link")\
\
Helper functions for building A2A JSON-RPC responses.\
\
##### `EventTypes = Task | Message | TaskArtifactUpdateEvent | TaskStatusUpdateEvent | TaskPushNotificationConfig | A2AError | JSONRPCError``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.response_helpers.EventTypes "Permanent link")\
\
Type alias for possible event types produced by handlers.\
\
##### `RT = TypeVar('RT', GetTaskResponse, CancelTaskResponse, SendMessageResponse, SetTaskPushNotificationConfigResponse, GetTaskPushNotificationConfigResponse, SendStreamingMessageResponse)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.response_helpers.RT "Permanent link")\
\
Type variable for RootModel response types.\
\
##### `SPT = TypeVar('SPT', GetTaskSuccessResponse, CancelTaskSuccessResponse, SendMessageSuccessResponse, SetTaskPushNotificationConfigSuccessResponse, GetTaskPushNotificationConfigSuccessResponse, SendStreamingMessageSuccessResponse)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.response_helpers.SPT "Permanent link")\
\
Type variable for SuccessResponse types.\
\
##### `build_error_response(request_id, error, response_wrapper_type)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.response_helpers.build_error_response "Permanent link")\
\
Helper method to build a JSONRPCErrorResponse wrapped in the appropriate response type.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request_id` | `str | int | None` | The ID of the request that caused the error. | _required_ |\
| `error` | `A2AError | JSONRPCError` | The A2AError or JSONRPCError object. | _required_ |\
| `response_wrapper_type` | `type[RT]` | The Pydantic RootModel type that wraps the response<br>for the specific RPC method (e.g., `SendMessageResponse`). | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `RT` | A Pydantic model representing the JSON-RPC error response, |\
| `RT` | wrapped in the specified response type. |\
\
##### `prepare_response_object(request_id, response, success_response_types, success_payload_type, response_type)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.request_handlers.response_helpers.prepare_response_object "Permanent link")\
\
Helper method to build appropriate JSONRPCResponse object for RPC methods.\
\
Based on the type of the `response` object received from the handler,\
it constructs either a success response wrapped in the appropriate payload type\
or an error response.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request_id` | `str | int | None` | The ID of the request. | _required_ |\
| `response` | `EventTypes` | The object received from the request handler. | _required_ |\
| `success_response_types` | `tuple[type, ...]` | A tuple of expected Pydantic model types for a successful result. | _required_ |\
| `success_payload_type` | `type[SPT]` | The Pydantic model type for the success payload<br>(e.g., `SendMessageSuccessResponse`). | _required_ |\
| `response_type` | `type[RT]` | The Pydantic RootModel type that wraps the final response<br>(e.g., `SendMessageResponse`). | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `RT` | A Pydantic model representing the final JSON-RPC response (success or error). |\
\
### `tasks` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks "Permanent link")\
\
Components for managing tasks within the A2A server.\
\
#### `InMemoryPushNotifier` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryPushNotifier "Permanent link")\
\
Bases: `PushNotifier`\
\
In-memory implementation of PushNotifier interface.\
\
Stores push notification configurations in memory and uses an httpx client\
to send notifications.\
\
##### `lock = asyncio.Lock()``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryPushNotifier.lock "Permanent link")\
\
##### `delete_info(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryPushNotifier.delete_info "Permanent link")\
\
Deletes the push notification configuration for a task from memory.\
\
##### `get_info(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryPushNotifier.get_info "Permanent link")\
\
Retrieves the push notification configuration for a task from memory.\
\
##### `send_notification(task)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryPushNotifier.send_notification "Permanent link")\
\
Sends a push notification for a task if configuration exists.\
\
##### `set_info(task_id, notification_config)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryPushNotifier.set_info "Permanent link")\
\
Sets or updates the push notification configuration for a task in memory.\
\
#### `InMemoryTaskStore` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryTaskStore "Permanent link")\
\
Bases: `TaskStore`\
\
In-memory implementation of TaskStore.\
\
Stores task objects in a dictionary in memory. Task data is lost when the\
server process stops.\
\
##### `lock = asyncio.Lock()``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryTaskStore.lock "Permanent link")\
\
##### `tasks = {}``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryTaskStore.tasks "Permanent link")\
\
##### `delete(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryTaskStore.delete "Permanent link")\
\
Deletes a task from the in-memory store by ID.\
\
##### `get(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryTaskStore.get "Permanent link")\
\
Retrieves a task from the in-memory store by ID.\
\
##### `save(task)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.InMemoryTaskStore.save "Permanent link")\
\
Saves or updates a task in the in-memory store.\
\
#### `PushNotifier` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.PushNotifier "Permanent link")\
\
Bases: `ABC`\
\
PushNotifier interface to store, retrieve push notification for tasks and send push notifications.\
\
##### `delete_info(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.PushNotifier.delete_info "Permanent link")\
\
Deletes the push notification configuration for a task.\
\
##### `get_info(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.PushNotifier.get_info "Permanent link")\
\
Retrieves the push notification configuration for a task.\
\
##### `send_notification(task)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.PushNotifier.send_notification "Permanent link")\
\
Sends a push notification containing the latest task state.\
\
##### `set_info(task_id, notification_config)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.PushNotifier.set_info "Permanent link")\
\
Sets or updates the push notification configuration for a task.\
\
#### `ResultAggregator` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.ResultAggregator "Permanent link")\
\
ResultAggregator is used to process the event streams from an AgentExecutor.\
\
There are three main ways to use the ResultAggregator:\
1) As part of a processing pipe. consume\_and\_emit will construct the updated\
task as the events arrive, and re-emit those events for another consumer\
2) As part of a blocking call. consume\_all will process the entire stream and\
return the final Task or Message object\
3) As part of a push solution where the latest Task is emitted after processing an event.\
consume\_and\_emit\_task will consume the Event stream, process the events to the current\
Task object and emit that Task object.\
\
##### `current_result``async``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.ResultAggregator.current_result "Permanent link")\
\
Returns the current aggregated result (Task or Message).\
\
This is the latest state processed from the event stream.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | Message | None` | The current `Task` object managed by the `TaskManager`, or the final |\
| `Task | Message | None` | `Message` if one was received, or `None` if no result has been produced yet. |\
\
##### `task_manager = task_manager``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.ResultAggregator.task_manager "Permanent link")\
\
##### `consume_all(consumer)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.ResultAggregator.consume_all "Permanent link")\
\
Processes the entire event stream from the consumer and returns the final result.\
\
Blocks until the event stream ends (queue is closed after final event or exception).\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `consumer` | `EventConsumer` | The `EventConsumer` to read events from. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | Message | None` | The final `Task` object or `Message` object after the stream is exhausted. |\
| `Task | Message | None` | Returns `None` if the stream ends without producing a final result. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `BaseException` | If the `EventConsumer` raises an exception during consumption. |\
\
##### `consume_and_break_on_interrupt(consumer)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.ResultAggregator.consume_and_break_on_interrupt "Permanent link")\
\
Processes the event stream until completion or an interruptable state is encountered.\
\
Interruptable states currently include `TaskState.auth_required`.\
If interrupted, consumption continues in a background task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `consumer` | `EventConsumer` | The `EventConsumer` to read events from. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | Message | None` | A tuple containing: |\
| `bool` | - The current aggregated result ( `Task` or `Message`) at the point of completion or interruption. |\
| `tuple[Task | Message | None, bool]` | - A boolean indicating whether the consumption was interrupted ( `True`) or completed naturally ( `False`). |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `BaseException` | If the `EventConsumer` raises an exception during consumption. |\
\
##### `consume_and_emit(consumer)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.ResultAggregator.consume_and_emit "Permanent link")\
\
Processes the event stream from the consumer, updates the task state, and re-emits the same events.\
\
Useful for streaming scenarios where the server needs to observe and\
process events (e.g., save task state, send push notifications) while\
forwarding them to the client.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `consumer` | `EventConsumer` | The `EventConsumer` to read events from. | _required_ |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncGenerator[Event]` | The `Event` objects consumed from the `EventConsumer`. |\
\
#### `TaskManager` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskManager "Permanent link")\
\
Helps manage a task's lifecycle during execution of a request.\
\
Responsible for retrieving, saving, and updating the `Task` object based on\
events received from the agent.\
\
##### `context_id = context_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskManager.context_id "Permanent link")\
\
##### `task_id = task_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskManager.task_id "Permanent link")\
\
##### `task_store = task_store``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskManager.task_store "Permanent link")\
\
##### `ensure_task(event)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskManager.ensure_task "Permanent link")\
\
Ensures a Task object exists in memory, loading from store or creating new if needed.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `event` | `TaskStatusUpdateEvent | TaskArtifactUpdateEvent` | The task-related event triggering the need for a Task object. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | An existing or newly created `Task` object. |\
\
##### `get_task()``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskManager.get_task "Permanent link")\
\
Retrieves the current task object, either from memory or the store.\
\
If `task_id` is set, it first checks the in-memory `_current_task`,\
then attempts to load it from the `task_store`.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | None` | The `Task` object if found, otherwise `None`. |\
\
##### `process(event)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskManager.process "Permanent link")\
\
Processes an event, updates the task state if applicable, stores it, and returns the event.\
\
If the event is task-related ( `Task`, `TaskStatusUpdateEvent`, `TaskArtifactUpdateEvent`),\
the internal task state is updated and persisted.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `event` | `Event` | The event object received from the agent. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Event` | The same event object that was processed. |\
\
##### `save_task_event(event)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskManager.save_task_event "Permanent link")\
\
Processes a task-related event (Task, Status, Artifact) and saves the updated task state.\
\
Ensures task and context IDs match or are set from the event.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `event` | `Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent` | The task-related event ( `Task`, `TaskStatusUpdateEvent`, or `TaskArtifactUpdateEvent`). | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | None` | The updated `Task` object after processing the event. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError` | If the task ID in the event conflicts with the TaskManager's ID<br>when the TaskManager's ID is already set. |\
\
##### `update_with_message(message, task)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskManager.update_with_message "Permanent link")\
\
Updates a task object in memory by adding a new message to its history.\
\
If the task has a message in its current status, that message is moved\
to the history first.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `message` | `Message` | The new `Message` to add to the history. | _required_ |\
| `task` | `Task` | The `Task` object to update. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | The updated `Task` object (updated in-place). |\
\
#### `TaskStore` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskStore "Permanent link")\
\
Bases: `ABC`\
\
Agent Task Store interface.\
\
Defines the methods for persisting and retrieving `Task` objects.\
\
##### `delete(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskStore.delete "Permanent link")\
\
Deletes a task from the store by ID.\
\
##### `get(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskStore.get "Permanent link")\
\
Retrieves a task from the store by ID.\
\
##### `save(task)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskStore.save "Permanent link")\
\
Saves or updates a task in the store.\
\
#### `TaskUpdater` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater "Permanent link")\
\
Helper class for agents to publish updates to a task's event queue.\
\
Simplifies the process of creating and enqueueing standard task events.\
\
##### `context_id = context_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.context_id "Permanent link")\
\
##### `event_queue = event_queue``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.event_queue "Permanent link")\
\
##### `task_id = task_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.task_id "Permanent link")\
\
##### `add_artifact(parts, artifact_id=None, name=None, metadata=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.add_artifact "Permanent link")\
\
Adds an artifact chunk to the task and publishes a `TaskArtifactUpdateEvent`.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | A list of `Part` objects forming the artifact chunk. | _required_ |\
| `artifact_id` | `str | None` | The ID of the artifact. A new UUID is generated if not provided. | `None` |\
| `name` | `str | None` | Optional name for the artifact. | `None` |\
| `metadata` | `dict[str, Any] | None` | Optional metadata for the artifact. | `None` |\
\
##### `complete(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.complete "Permanent link")\
\
Marks the task as completed and publishes a final status update.\
\
##### `failed(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.failed "Permanent link")\
\
Marks the task as failed and publishes a final status update.\
\
##### `new_agent_message(parts, metadata=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.new_agent_message "Permanent link")\
\
Creates a new message object sent by the agent for this task/context.\
\
This method only _creates_ the message object. It does not\
\
automatically enqueue it.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | A list of `Part` objects for the message content. | _required_ |\
| `metadata` | `dict[str, Any] | None` | Optional metadata for the message. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Message` | A new `Message` object. |\
\
##### `reject(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.reject "Permanent link")\
\
Marks the task as rejected and publishes a final status update.\
\
##### `start_work(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.start_work "Permanent link")\
\
Marks the task as working and publishes a status update.\
\
##### `submit(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.submit "Permanent link")\
\
Marks the task as submitted and publishes a status update.\
\
##### `update_status(state, message=None, final=False, timestamp=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.TaskUpdater.update_status "Permanent link")\
\
Updates the status of the task and publishes a `TaskStatusUpdateEvent`.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `state` | `TaskState` | The new state of the task. | _required_ |\
| `message` | `Message | None` | An optional message associated with the status update. | `None` |\
| `final` | `bool` | If True, indicates this is the final status update for the task. | `False` |\
| `timestamp` | `str | None` | Optional ISO 8601 datetime string. Defaults to current time. | `None` |\
\
#### `inmemory_push_notifier` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_push_notifier "Permanent link")\
\
##### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_push_notifier.logger "Permanent link")\
\
##### `InMemoryPushNotifier` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_push_notifier.InMemoryPushNotifier "Permanent link")\
\
Bases: `PushNotifier`\
\
In-memory implementation of PushNotifier interface.\
\
Stores push notification configurations in memory and uses an httpx client\
to send notifications.\
\
###### `lock = asyncio.Lock()``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_push_notifier.InMemoryPushNotifier.lock "Permanent link")\
\
###### `delete_info(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_push_notifier.InMemoryPushNotifier.delete_info "Permanent link")\
\
Deletes the push notification configuration for a task from memory.\
\
###### `get_info(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_push_notifier.InMemoryPushNotifier.get_info "Permanent link")\
\
Retrieves the push notification configuration for a task from memory.\
\
###### `send_notification(task)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_push_notifier.InMemoryPushNotifier.send_notification "Permanent link")\
\
Sends a push notification for a task if configuration exists.\
\
###### `set_info(task_id, notification_config)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_push_notifier.InMemoryPushNotifier.set_info "Permanent link")\
\
Sets or updates the push notification configuration for a task in memory.\
\
#### `inmemory_task_store` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_task_store "Permanent link")\
\
##### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_task_store.logger "Permanent link")\
\
##### `InMemoryTaskStore` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_task_store.InMemoryTaskStore "Permanent link")\
\
Bases: `TaskStore`\
\
In-memory implementation of TaskStore.\
\
Stores task objects in a dictionary in memory. Task data is lost when the\
server process stops.\
\
###### `lock = asyncio.Lock()``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_task_store.InMemoryTaskStore.lock "Permanent link")\
\
###### `tasks = {}``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_task_store.InMemoryTaskStore.tasks "Permanent link")\
\
###### `delete(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_task_store.InMemoryTaskStore.delete "Permanent link")\
\
Deletes a task from the in-memory store by ID.\
\
###### `get(task_id)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_task_store.InMemoryTaskStore.get "Permanent link")\
\
Retrieves a task from the in-memory store by ID.\
\
###### `save(task)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.inmemory_task_store.InMemoryTaskStore.save "Permanent link")\
\
Saves or updates a task in the in-memory store.\
\
#### `push_notifier` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.push_notifier "Permanent link")\
\
##### `PushNotifier` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.push_notifier.PushNotifier "Permanent link")\
\
Bases: `ABC`\
\
PushNotifier interface to store, retrieve push notification for tasks and send push notifications.\
\
###### `delete_info(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.push_notifier.PushNotifier.delete_info "Permanent link")\
\
Deletes the push notification configuration for a task.\
\
###### `get_info(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.push_notifier.PushNotifier.get_info "Permanent link")\
\
Retrieves the push notification configuration for a task.\
\
###### `send_notification(task)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.push_notifier.PushNotifier.send_notification "Permanent link")\
\
Sends a push notification containing the latest task state.\
\
###### `set_info(task_id, notification_config)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.push_notifier.PushNotifier.set_info "Permanent link")\
\
Sets or updates the push notification configuration for a task.\
\
#### `result_aggregator` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.result_aggregator "Permanent link")\
\
##### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.result_aggregator.logger "Permanent link")\
\
##### `ResultAggregator` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.result_aggregator.ResultAggregator "Permanent link")\
\
ResultAggregator is used to process the event streams from an AgentExecutor.\
\
There are three main ways to use the ResultAggregator:\
1) As part of a processing pipe. consume\_and\_emit will construct the updated\
task as the events arrive, and re-emit those events for another consumer\
2) As part of a blocking call. consume\_all will process the entire stream and\
return the final Task or Message object\
3) As part of a push solution where the latest Task is emitted after processing an event.\
consume\_and\_emit\_task will consume the Event stream, process the events to the current\
Task object and emit that Task object.\
\
###### `current_result``async``property`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.result_aggregator.ResultAggregator.current_result "Permanent link")\
\
Returns the current aggregated result (Task or Message).\
\
This is the latest state processed from the event stream.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | Message | None` | The current `Task` object managed by the `TaskManager`, or the final |\
| `Task | Message | None` | `Message` if one was received, or `None` if no result has been produced yet. |\
\
###### `task_manager = task_manager``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.result_aggregator.ResultAggregator.task_manager "Permanent link")\
\
###### `consume_all(consumer)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.result_aggregator.ResultAggregator.consume_all "Permanent link")\
\
Processes the entire event stream from the consumer and returns the final result.\
\
Blocks until the event stream ends (queue is closed after final event or exception).\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `consumer` | `EventConsumer` | The `EventConsumer` to read events from. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | Message | None` | The final `Task` object or `Message` object after the stream is exhausted. |\
| `Task | Message | None` | Returns `None` if the stream ends without producing a final result. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `BaseException` | If the `EventConsumer` raises an exception during consumption. |\
\
###### `consume_and_break_on_interrupt(consumer)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.result_aggregator.ResultAggregator.consume_and_break_on_interrupt "Permanent link")\
\
Processes the event stream until completion or an interruptable state is encountered.\
\
Interruptable states currently include `TaskState.auth_required`.\
If interrupted, consumption continues in a background task.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `consumer` | `EventConsumer` | The `EventConsumer` to read events from. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | Message | None` | A tuple containing: |\
| `bool` | - The current aggregated result ( `Task` or `Message`) at the point of completion or interruption. |\
| `tuple[Task | Message | None, bool]` | - A boolean indicating whether the consumption was interrupted ( `True`) or completed naturally ( `False`). |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `BaseException` | If the `EventConsumer` raises an exception during consumption. |\
\
###### `consume_and_emit(consumer)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.result_aggregator.ResultAggregator.consume_and_emit "Permanent link")\
\
Processes the event stream from the consumer, updates the task state, and re-emits the same events.\
\
Useful for streaming scenarios where the server needs to observe and\
process events (e.g., save task state, send push notifications) while\
forwarding them to the client.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `consumer` | `EventConsumer` | The `EventConsumer` to read events from. | _required_ |\
\
Yields:\
\
| Type | Description |\
| --- | --- |\
| `AsyncGenerator[Event]` | The `Event` objects consumed from the `EventConsumer`. |\
\
#### `task_manager` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager "Permanent link")\
\
##### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.logger "Permanent link")\
\
##### `TaskManager` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.TaskManager "Permanent link")\
\
Helps manage a task's lifecycle during execution of a request.\
\
Responsible for retrieving, saving, and updating the `Task` object based on\
events received from the agent.\
\
###### `context_id = context_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.TaskManager.context_id "Permanent link")\
\
###### `task_id = task_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.TaskManager.task_id "Permanent link")\
\
###### `task_store = task_store``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.TaskManager.task_store "Permanent link")\
\
###### `ensure_task(event)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.TaskManager.ensure_task "Permanent link")\
\
Ensures a Task object exists in memory, loading from store or creating new if needed.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `event` | `TaskStatusUpdateEvent | TaskArtifactUpdateEvent` | The task-related event triggering the need for a Task object. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | An existing or newly created `Task` object. |\
\
###### `get_task()``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.TaskManager.get_task "Permanent link")\
\
Retrieves the current task object, either from memory or the store.\
\
If `task_id` is set, it first checks the in-memory `_current_task`,\
then attempts to load it from the `task_store`.\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | None` | The `Task` object if found, otherwise `None`. |\
\
###### `process(event)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.TaskManager.process "Permanent link")\
\
Processes an event, updates the task state if applicable, stores it, and returns the event.\
\
If the event is task-related ( `Task`, `TaskStatusUpdateEvent`, `TaskArtifactUpdateEvent`),\
the internal task state is updated and persisted.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `event` | `Event` | The event object received from the agent. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Event` | The same event object that was processed. |\
\
###### `save_task_event(event)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.TaskManager.save_task_event "Permanent link")\
\
Processes a task-related event (Task, Status, Artifact) and saves the updated task state.\
\
Ensures task and context IDs match or are set from the event.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `event` | `Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent` | The task-related event ( `Task`, `TaskStatusUpdateEvent`, or `TaskArtifactUpdateEvent`). | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task | None` | The updated `Task` object after processing the event. |\
\
Raises:\
\
| Type | Description |\
| --- | --- |\
| `ServerError` | If the task ID in the event conflicts with the TaskManager's ID<br>when the TaskManager's ID is already set. |\
\
###### `update_with_message(message, task)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_manager.TaskManager.update_with_message "Permanent link")\
\
Updates a task object in memory by adding a new message to its history.\
\
If the task has a message in its current status, that message is moved\
to the history first.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `message` | `Message` | The new `Message` to add to the history. | _required_ |\
| `task` | `Task` | The `Task` object to update. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | The updated `Task` object (updated in-place). |\
\
#### `task_store` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_store "Permanent link")\
\
##### `TaskStore` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_store.TaskStore "Permanent link")\
\
Bases: `ABC`\
\
Agent Task Store interface.\
\
Defines the methods for persisting and retrieving `Task` objects.\
\
###### `delete(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_store.TaskStore.delete "Permanent link")\
\
Deletes a task from the store by ID.\
\
###### `get(task_id)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_store.TaskStore.get "Permanent link")\
\
Retrieves a task from the store by ID.\
\
###### `save(task)``abstractmethod``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_store.TaskStore.save "Permanent link")\
\
Saves or updates a task in the store.\
\
#### `task_updater` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater "Permanent link")\
\
##### `TaskUpdater` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater "Permanent link")\
\
Helper class for agents to publish updates to a task's event queue.\
\
Simplifies the process of creating and enqueueing standard task events.\
\
###### `context_id = context_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.context_id "Permanent link")\
\
###### `event_queue = event_queue``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.event_queue "Permanent link")\
\
###### `task_id = task_id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.task_id "Permanent link")\
\
###### `add_artifact(parts, artifact_id=None, name=None, metadata=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.add_artifact "Permanent link")\
\
Adds an artifact chunk to the task and publishes a `TaskArtifactUpdateEvent`.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | A list of `Part` objects forming the artifact chunk. | _required_ |\
| `artifact_id` | `str | None` | The ID of the artifact. A new UUID is generated if not provided. | `None` |\
| `name` | `str | None` | Optional name for the artifact. | `None` |\
| `metadata` | `dict[str, Any] | None` | Optional metadata for the artifact. | `None` |\
\
###### `complete(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.complete "Permanent link")\
\
Marks the task as completed and publishes a final status update.\
\
###### `failed(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.failed "Permanent link")\
\
Marks the task as failed and publishes a final status update.\
\
###### `new_agent_message(parts, metadata=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.new_agent_message "Permanent link")\
\
Creates a new message object sent by the agent for this task/context.\
\
This method only _creates_ the message object. It does not\
\
automatically enqueue it.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | A list of `Part` objects for the message content. | _required_ |\
| `metadata` | `dict[str, Any] | None` | Optional metadata for the message. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Message` | A new `Message` object. |\
\
###### `reject(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.reject "Permanent link")\
\
Marks the task as rejected and publishes a final status update.\
\
###### `start_work(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.start_work "Permanent link")\
\
Marks the task as working and publishes a status update.\
\
###### `submit(message=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.submit "Permanent link")\
\
Marks the task as submitted and publishes a status update.\
\
###### `update_status(state, message=None, final=False, timestamp=None)``async`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.server.tasks.task_updater.TaskUpdater.update_status "Permanent link")\
\
Updates the status of the task and publishes a `TaskStatusUpdateEvent`.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `state` | `TaskState` | The new state of the task. | _required_ |\
| `message` | `Message | None` | An optional message associated with the status update. | `None` |\
| `final` | `bool` | If True, indicates this is the final status update for the task. | `False` |\
| `timestamp` | `str | None` | Optional ISO 8601 datetime string. Defaults to current time. | `None` |\
\
## `types` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types "Permanent link")\
\
### `A2A` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.A2A "Permanent link")\
\
Bases: `RootModel[Any]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.A2A.root "Permanent link")\
\
### `A2AError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.A2AError "Permanent link")\
\
Bases: `RootModel[JSONParseError | InvalidRequestError | MethodNotFoundError | InvalidParamsError | InternalError | TaskNotFoundError | TaskNotCancelableError | PushNotificationNotSupportedError | UnsupportedOperationError | ContentTypeNotSupportedError | InvalidAgentResponseError]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.A2AError.root "Permanent link")\
\
### `A2ARequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.A2ARequest "Permanent link")\
\
Bases: `RootModel[SendMessageRequest | SendStreamingMessageRequest | GetTaskRequest | CancelTaskRequest | SetTaskPushNotificationConfigRequest | GetTaskPushNotificationConfigRequest | TaskResubscriptionRequest]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.A2ARequest.root "Permanent link")\
\
A2A supported request types\
\
### `APIKeySecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.APIKeySecurityScheme "Permanent link")\
\
Bases: `BaseModel`\
\
API Key security scheme.\
\
#### `description = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.APIKeySecurityScheme.description "Permanent link")\
\
Description of this security scheme.\
\
#### `in_ = Field(..., alias='in')``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.APIKeySecurityScheme.in_ "Permanent link")\
\
The location of the API key. Valid values are "query", "header", or "cookie".\
\
#### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.APIKeySecurityScheme.name "Permanent link")\
\
The name of the header, query or cookie parameter to be used.\
\
#### `type = 'apiKey'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.APIKeySecurityScheme.type "Permanent link")\
\
### `AgentCapabilities` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCapabilities "Permanent link")\
\
Bases: `BaseModel`\
\
Defines optional capabilities supported by an agent.\
\
#### `extensions = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCapabilities.extensions "Permanent link")\
\
extensions supported by this agent.\
\
#### `pushNotifications = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCapabilities.pushNotifications "Permanent link")\
\
true if the agent can notify updates to client.\
\
#### `stateTransitionHistory = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCapabilities.stateTransitionHistory "Permanent link")\
\
true if the agent exposes status change history for tasks.\
\
#### `streaming = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCapabilities.streaming "Permanent link")\
\
true if the agent supports SSE.\
\
### `AgentCard` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard "Permanent link")\
\
Bases: `BaseModel`\
\
An AgentCard conveys key information:\
\- Overall details (version, name, description, uses)\
\- Skills: A set of capabilities the agent can perform\
\- Default modalities/content types supported by the agent.\
\- Authentication requirements\
\
#### `capabilities``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.capabilities "Permanent link")\
\
Optional capabilities supported by the agent.\
\
#### `defaultInputModes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.defaultInputModes "Permanent link")\
\
The set of interaction modes that the agent supports across all skills. This can be overridden per-skill.\
Supported media types for input.\
\
#### `defaultOutputModes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.defaultOutputModes "Permanent link")\
\
Supported media types for output.\
\
#### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.description "Permanent link")\
\
A human-readable description of the agent. Used to assist users and\
other agents in understanding what the agent can do.\
\
#### `documentationUrl = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.documentationUrl "Permanent link")\
\
A URL to documentation for the agent.\
\
#### `iconUrl = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.iconUrl "Permanent link")\
\
A URL to an icon for the agent.\
\
#### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.name "Permanent link")\
\
Human readable name of the agent.\
\
#### `provider = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.provider "Permanent link")\
\
The service provider of the agent\
\
#### `security = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.security "Permanent link")\
\
Security requirements for contacting the agent.\
\
#### `securitySchemes = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.securitySchemes "Permanent link")\
\
Security scheme details used for authenticating with this agent.\
\
#### `skills``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.skills "Permanent link")\
\
Skills are a unit of capability that an agent can perform.\
\
#### `supportsAuthenticatedExtendedCard = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.supportsAuthenticatedExtendedCard "Permanent link")\
\
true if the agent supports providing an extended agent card when the user is authenticated.\
Defaults to false if not specified.\
\
#### `url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.url "Permanent link")\
\
A URL to the address the agent is hosted at.\
\
#### `version``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentCard.version "Permanent link")\
\
The version of the agent - format is up to the provider.\
\
### `AgentExtension` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentExtension "Permanent link")\
\
Bases: `BaseModel`\
\
A declaration of an extension supported by an Agent.\
\
#### `description = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentExtension.description "Permanent link")\
\
A description of how this agent uses this extension.\
\
#### `params = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentExtension.params "Permanent link")\
\
Optional configuration for the extension.\
\
#### `required = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentExtension.required "Permanent link")\
\
Whether the client must follow specific requirements of the extension.\
\
#### `uri``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentExtension.uri "Permanent link")\
\
The URI of the extension.\
\
### `AgentProvider` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentProvider "Permanent link")\
\
Bases: `BaseModel`\
\
Represents the service provider of an agent.\
\
#### `organization``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentProvider.organization "Permanent link")\
\
Agent provider's organization name.\
\
#### `url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentProvider.url "Permanent link")\
\
Agent provider's URL.\
\
### `AgentSkill` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentSkill "Permanent link")\
\
Bases: `BaseModel`\
\
Represents a unit of capability that an agent can perform.\
\
#### `description``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentSkill.description "Permanent link")\
\
Description of the skill - will be used by the client or a human\
as a hint to understand what the skill does.\
\
#### `examples = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentSkill.examples "Permanent link")\
\
The set of example scenarios that the skill can perform.\
Will be used by the client as a hint to understand how the skill can be used.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentSkill.id "Permanent link")\
\
Unique identifier for the agent's skill.\
\
#### `inputModes = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentSkill.inputModes "Permanent link")\
\
The set of interaction modes that the skill supports\
(if different than the default).\
Supported media types for input.\
\
#### `name``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentSkill.name "Permanent link")\
\
Human readable name of the skill.\
\
#### `outputModes = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentSkill.outputModes "Permanent link")\
\
Supported media types for output.\
\
#### `tags``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AgentSkill.tags "Permanent link")\
\
Set of tagwords describing classes of capabilities for this specific skill.\
\
### `Artifact` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Artifact "Permanent link")\
\
Bases: `BaseModel`\
\
Represents an artifact generated for a task.\
\
#### `artifactId``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Artifact.artifactId "Permanent link")\
\
Unique identifier for the artifact.\
\
#### `description = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Artifact.description "Permanent link")\
\
Optional description for the artifact.\
\
#### `extensions = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Artifact.extensions "Permanent link")\
\
The URIs of extensions that are present or contributed to this Artifact.\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Artifact.metadata "Permanent link")\
\
Extension metadata.\
\
#### `name = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Artifact.name "Permanent link")\
\
Optional name for the artifact.\
\
#### `parts``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Artifact.parts "Permanent link")\
\
Artifact parts.\
\
### `AuthorizationCodeOAuthFlow` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AuthorizationCodeOAuthFlow "Permanent link")\
\
Bases: `BaseModel`\
\
Configuration details for a supported OAuth Flow\
\
#### `authorizationUrl``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AuthorizationCodeOAuthFlow.authorizationUrl "Permanent link")\
\
The authorization URL to be used for this flow. This MUST be in the form of a URL. The OAuth2\
standard requires the use of TLS\
\
#### `refreshUrl = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AuthorizationCodeOAuthFlow.refreshUrl "Permanent link")\
\
The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2\
standard requires the use of TLS.\
\
#### `scopes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AuthorizationCodeOAuthFlow.scopes "Permanent link")\
\
The available scopes for the OAuth2 security scheme. A map between the scope name and a short\
description for it. The map MAY be empty.\
\
#### `tokenUrl``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.AuthorizationCodeOAuthFlow.tokenUrl "Permanent link")\
\
The token URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard\
requires the use of TLS.\
\
### `CancelTaskRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskRequest "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC request model for the 'tasks/cancel' method.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskRequest.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskRequest.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `method = 'tasks/cancel'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskRequest.method "Permanent link")\
\
A String containing the name of the method to be invoked.\
\
#### `params``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskRequest.params "Permanent link")\
\
A Structured value that holds the parameter values to be used during the invocation of the method.\
\
### `CancelTaskResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskResponse "Permanent link")\
\
Bases: `RootModel[JSONRPCErrorResponse | CancelTaskSuccessResponse]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskResponse.root "Permanent link")\
\
JSON-RPC response for the 'tasks/cancel' method.\
\
### `CancelTaskSuccessResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskSuccessResponse "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC success response model for the 'tasks/cancel' method.\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskSuccessResponse.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskSuccessResponse.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `result``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.CancelTaskSuccessResponse.result "Permanent link")\
\
The result object on success.\
\
### `ClientCredentialsOAuthFlow` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ClientCredentialsOAuthFlow "Permanent link")\
\
Bases: `BaseModel`\
\
Configuration details for a supported OAuth Flow\
\
#### `refreshUrl = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ClientCredentialsOAuthFlow.refreshUrl "Permanent link")\
\
The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2\
standard requires the use of TLS.\
\
#### `scopes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ClientCredentialsOAuthFlow.scopes "Permanent link")\
\
The available scopes for the OAuth2 security scheme. A map between the scope name and a short\
description for it. The map MAY be empty.\
\
#### `tokenUrl``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ClientCredentialsOAuthFlow.tokenUrl "Permanent link")\
\
The token URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard\
requires the use of TLS.\
\
### `ContentTypeNotSupportedError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ContentTypeNotSupportedError "Permanent link")\
\
Bases: `BaseModel`\
\
A2A specific error indicating incompatible content types between request and agent capabilities.\
\
#### `code = -32005``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ContentTypeNotSupportedError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ContentTypeNotSupportedError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Incompatible content types'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ContentTypeNotSupportedError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `DataPart` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.DataPart "Permanent link")\
\
Bases: `BaseModel`\
\
Represents a structured data segment within a message part.\
\
#### `data``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.DataPart.data "Permanent link")\
\
Structured data content\
\
#### `kind = 'data'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.DataPart.kind "Permanent link")\
\
Part type - data for DataParts\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.DataPart.metadata "Permanent link")\
\
Optional metadata associated with the part.\
\
### `FileBase` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileBase "Permanent link")\
\
Bases: `BaseModel`\
\
Represents the base entity for FileParts\
\
#### `mimeType = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileBase.mimeType "Permanent link")\
\
Optional mimeType for the file\
\
#### `name = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileBase.name "Permanent link")\
\
Optional name for the file\
\
### `FilePart` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FilePart "Permanent link")\
\
Bases: `BaseModel`\
\
Represents a File segment within parts.\
\
#### `file``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FilePart.file "Permanent link")\
\
File content either as url or bytes\
\
#### `kind = 'file'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FilePart.kind "Permanent link")\
\
Part type - file for FileParts\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FilePart.metadata "Permanent link")\
\
Optional metadata associated with the part.\
\
### `FileWithBytes` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileWithBytes "Permanent link")\
\
Bases: `BaseModel`\
\
Define the variant where 'bytes' is present and 'uri' is absent\
\
#### `bytes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileWithBytes.bytes "Permanent link")\
\
base64 encoded content of the file\
\
#### `mimeType = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileWithBytes.mimeType "Permanent link")\
\
Optional mimeType for the file\
\
#### `name = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileWithBytes.name "Permanent link")\
\
Optional name for the file\
\
### `FileWithUri` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileWithUri "Permanent link")\
\
Bases: `BaseModel`\
\
Define the variant where 'uri' is present and 'bytes' is absent\
\
#### `mimeType = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileWithUri.mimeType "Permanent link")\
\
Optional mimeType for the file\
\
#### `name = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileWithUri.name "Permanent link")\
\
Optional name for the file\
\
#### `uri``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.FileWithUri.uri "Permanent link")\
\
URL for the File content\
\
### `GetTaskPushNotificationConfigRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigRequest "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC request model for the 'tasks/pushNotificationConfig/get' method.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigRequest.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigRequest.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `method = 'tasks/pushNotificationConfig/get'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigRequest.method "Permanent link")\
\
A String containing the name of the method to be invoked.\
\
#### `params``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigRequest.params "Permanent link")\
\
A Structured value that holds the parameter values to be used during the invocation of the method.\
\
### `GetTaskPushNotificationConfigResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigResponse "Permanent link")\
\
Bases: `RootModel[JSONRPCErrorResponse | GetTaskPushNotificationConfigSuccessResponse]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigResponse.root "Permanent link")\
\
JSON-RPC response for the 'tasks/pushNotificationConfig/set' method.\
\
### `GetTaskPushNotificationConfigSuccessResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigSuccessResponse "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC success response model for the 'tasks/pushNotificationConfig/get' method.\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigSuccessResponse.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigSuccessResponse.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `result``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskPushNotificationConfigSuccessResponse.result "Permanent link")\
\
The result object on success.\
\
### `GetTaskRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskRequest "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC request model for the 'tasks/get' method.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskRequest.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskRequest.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `method = 'tasks/get'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskRequest.method "Permanent link")\
\
A String containing the name of the method to be invoked.\
\
#### `params``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskRequest.params "Permanent link")\
\
A Structured value that holds the parameter values to be used during the invocation of the method.\
\
### `GetTaskResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskResponse "Permanent link")\
\
Bases: `RootModel[JSONRPCErrorResponse | GetTaskSuccessResponse]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskResponse.root "Permanent link")\
\
JSON-RPC response for the 'tasks/get' method.\
\
### `GetTaskSuccessResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskSuccessResponse "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC success response for the 'tasks/get' method.\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskSuccessResponse.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskSuccessResponse.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `result``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.GetTaskSuccessResponse.result "Permanent link")\
\
The result object on success.\
\
### `HTTPAuthSecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.HTTPAuthSecurityScheme "Permanent link")\
\
Bases: `BaseModel`\
\
HTTP Authentication security scheme.\
\
#### `bearerFormat = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.HTTPAuthSecurityScheme.bearerFormat "Permanent link")\
\
A hint to the client to identify how the bearer token is formatted. Bearer tokens are usually\
generated by an authorization server, so this information is primarily for documentation\
purposes.\
\
#### `description = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.HTTPAuthSecurityScheme.description "Permanent link")\
\
Description of this security scheme.\
\
#### `scheme``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.HTTPAuthSecurityScheme.scheme "Permanent link")\
\
The name of the HTTP Authentication scheme to be used in the Authorization header as defined\
in RFC7235. The values used SHOULD be registered in the IANA Authentication Scheme registry.\
The value is case-insensitive, as defined in RFC7235.\
\
#### `type = 'http'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.HTTPAuthSecurityScheme.type "Permanent link")\
\
### `ImplicitOAuthFlow` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ImplicitOAuthFlow "Permanent link")\
\
Bases: `BaseModel`\
\
Configuration details for a supported OAuth Flow\
\
#### `authorizationUrl``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ImplicitOAuthFlow.authorizationUrl "Permanent link")\
\
The authorization URL to be used for this flow. This MUST be in the form of a URL. The OAuth2\
standard requires the use of TLS\
\
#### `refreshUrl = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ImplicitOAuthFlow.refreshUrl "Permanent link")\
\
The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2\
standard requires the use of TLS.\
\
#### `scopes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.ImplicitOAuthFlow.scopes "Permanent link")\
\
The available scopes for the OAuth2 security scheme. A map between the scope name and a short\
description for it. The map MAY be empty.\
\
### `In` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.In "Permanent link")\
\
Bases: `str`, `Enum`\
\
The location of the API key. Valid values are "query", "header", or "cookie".\
\
#### `cookie = 'cookie'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.In.cookie "Permanent link")\
\
#### `header = 'header'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.In.header "Permanent link")\
\
#### `query = 'query'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.In.query "Permanent link")\
\
### `InternalError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InternalError "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC error indicating an internal JSON-RPC error on the server.\
\
#### `code = -32603``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InternalError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InternalError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Internal error'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InternalError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `InvalidAgentResponseError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidAgentResponseError "Permanent link")\
\
Bases: `BaseModel`\
\
A2A specific error indicating agent returned invalid response for the current method\
\
#### `code = -32006``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidAgentResponseError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidAgentResponseError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Invalid agent response'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidAgentResponseError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `InvalidParamsError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidParamsError "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC error indicating invalid method parameter(s).\
\
#### `code = -32602``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidParamsError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidParamsError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Invalid parameters'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidParamsError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `InvalidRequestError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidRequestError "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC error indicating the JSON sent is not a valid Request object.\
\
#### `code = -32600``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidRequestError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidRequestError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Request payload validation error'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.InvalidRequestError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `JSONParseError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONParseError "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC error indicating invalid JSON was received by the server.\
\
#### `code = -32700``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONParseError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONParseError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Invalid JSON payload'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONParseError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `JSONRPCError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCError "Permanent link")\
\
Bases: `BaseModel`\
\
Represents a JSON-RPC 2.0 Error object.\
This is typically included in a JSONRPCErrorResponse when an error occurs.\
\
#### `code``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `JSONRPCErrorResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCErrorResponse "Permanent link")\
\
Bases: `BaseModel`\
\
Represents a JSON-RPC 2.0 Error Response object.\
\
#### `error``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCErrorResponse.error "Permanent link")\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCErrorResponse.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCErrorResponse.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
### `JSONRPCMessage` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCMessage "Permanent link")\
\
Bases: `BaseModel`\
\
Base interface for any JSON-RPC 2.0 request or response.\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCMessage.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCMessage.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
### `JSONRPCRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCRequest "Permanent link")\
\
Bases: `BaseModel`\
\
Represents a JSON-RPC 2.0 Request object.\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCRequest.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCRequest.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `method``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCRequest.method "Permanent link")\
\
A String containing the name of the method to be invoked.\
\
#### `params = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCRequest.params "Permanent link")\
\
A Structured value that holds the parameter values to be used during the invocation of the method.\
\
### `JSONRPCResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCResponse "Permanent link")\
\
Bases: `RootModel[JSONRPCErrorResponse | SendMessageSuccessResponse | SendStreamingMessageSuccessResponse | GetTaskSuccessResponse | CancelTaskSuccessResponse | SetTaskPushNotificationConfigSuccessResponse | GetTaskPushNotificationConfigSuccessResponse]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCResponse.root "Permanent link")\
\
Represents a JSON-RPC 2.0 Response object.\
\
### `JSONRPCSuccessResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCSuccessResponse "Permanent link")\
\
Bases: `BaseModel`\
\
Represents a JSON-RPC 2.0 Success Response object.\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCSuccessResponse.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCSuccessResponse.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `result``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.JSONRPCSuccessResponse.result "Permanent link")\
\
The result object on success\
\
### `Message` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message "Permanent link")\
\
Bases: `BaseModel`\
\
Represents a single message exchanged between user and agent.\
\
#### `contextId = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message.contextId "Permanent link")\
\
The context the message is associated with\
\
#### `extensions = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message.extensions "Permanent link")\
\
The URIs of extensions that are present or contributed to this Message.\
\
#### `kind = 'message'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message.kind "Permanent link")\
\
Event type\
\
#### `messageId``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message.messageId "Permanent link")\
\
Identifier created by the message creator\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message.metadata "Permanent link")\
\
Extension metadata.\
\
#### `parts``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message.parts "Permanent link")\
\
Message content\
\
#### `referenceTaskIds = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message.referenceTaskIds "Permanent link")\
\
List of tasks referenced as context by this message.\
\
#### `role``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message.role "Permanent link")\
\
Message sender's role\
\
#### `taskId = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Message.taskId "Permanent link")\
\
Identifier of task the message is related to\
\
### `MessageSendConfiguration` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MessageSendConfiguration "Permanent link")\
\
Bases: `BaseModel`\
\
Configuration for the send message request.\
\
#### `acceptedOutputModes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MessageSendConfiguration.acceptedOutputModes "Permanent link")\
\
Accepted output modalities by the client.\
\
#### `blocking = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MessageSendConfiguration.blocking "Permanent link")\
\
If the server should treat the client as a blocking request.\
\
#### `historyLength = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MessageSendConfiguration.historyLength "Permanent link")\
\
Number of recent messages to be retrieved.\
\
#### `pushNotificationConfig = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MessageSendConfiguration.pushNotificationConfig "Permanent link")\
\
Where the server should send notifications when disconnected.\
\
### `MessageSendParams` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MessageSendParams "Permanent link")\
\
Bases: `BaseModel`\
\
Sent by the client to the agent as a request. May create, continue or restart a task.\
\
#### `configuration = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MessageSendParams.configuration "Permanent link")\
\
Send message configuration.\
\
#### `message``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MessageSendParams.message "Permanent link")\
\
The message being sent to the server.\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MessageSendParams.metadata "Permanent link")\
\
Extension metadata.\
\
### `MethodNotFoundError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MethodNotFoundError "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC error indicating the method does not exist or is not available.\
\
#### `code = -32601``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MethodNotFoundError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MethodNotFoundError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Method not found'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.MethodNotFoundError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `OAuth2SecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OAuth2SecurityScheme "Permanent link")\
\
Bases: `BaseModel`\
\
OAuth2.0 security scheme configuration.\
\
#### `description = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OAuth2SecurityScheme.description "Permanent link")\
\
Description of this security scheme.\
\
#### `flows``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OAuth2SecurityScheme.flows "Permanent link")\
\
An object containing configuration information for the flow types supported.\
\
#### `type = 'oauth2'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OAuth2SecurityScheme.type "Permanent link")\
\
### `OAuthFlows` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OAuthFlows "Permanent link")\
\
Bases: `BaseModel`\
\
Allows configuration of the supported OAuth Flows\
\
#### `authorizationCode = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OAuthFlows.authorizationCode "Permanent link")\
\
Configuration for the OAuth Authorization Code flow. Previously called accessCode in OpenAPI 2.0.\
\
#### `clientCredentials = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OAuthFlows.clientCredentials "Permanent link")\
\
Configuration for the OAuth Client Credentials flow. Previously called application in OpenAPI 2.0\
\
#### `implicit = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OAuthFlows.implicit "Permanent link")\
\
Configuration for the OAuth Implicit flow\
\
#### `password = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OAuthFlows.password "Permanent link")\
\
Configuration for the OAuth Resource Owner Password flow\
\
### `OpenIdConnectSecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OpenIdConnectSecurityScheme "Permanent link")\
\
Bases: `BaseModel`\
\
OpenID Connect security scheme configuration.\
\
#### `description = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OpenIdConnectSecurityScheme.description "Permanent link")\
\
Description of this security scheme.\
\
#### `openIdConnectUrl``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OpenIdConnectSecurityScheme.openIdConnectUrl "Permanent link")\
\
Well-known URL to discover the \[\[OpenID-Connect-Discovery\]\] provider metadata.\
\
#### `type = 'openIdConnect'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.OpenIdConnectSecurityScheme.type "Permanent link")\
\
### `Part` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Part "Permanent link")\
\
Bases: `RootModel[TextPart | FilePart | DataPart]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Part.root "Permanent link")\
\
Represents a part of a message, which can be text, a file, or structured data.\
\
### `PartBase` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PartBase "Permanent link")\
\
Bases: `BaseModel`\
\
Base properties common to all message parts.\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PartBase.metadata "Permanent link")\
\
Optional metadata associated with the part.\
\
### `PasswordOAuthFlow` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PasswordOAuthFlow "Permanent link")\
\
Bases: `BaseModel`\
\
Configuration details for a supported OAuth Flow\
\
#### `refreshUrl = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PasswordOAuthFlow.refreshUrl "Permanent link")\
\
The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL. The OAuth2\
standard requires the use of TLS.\
\
#### `scopes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PasswordOAuthFlow.scopes "Permanent link")\
\
The available scopes for the OAuth2 security scheme. A map between the scope name and a short\
description for it. The map MAY be empty.\
\
#### `tokenUrl``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PasswordOAuthFlow.tokenUrl "Permanent link")\
\
The token URL to be used for this flow. This MUST be in the form of a URL. The OAuth2 standard\
requires the use of TLS.\
\
### `PushNotificationAuthenticationInfo` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationAuthenticationInfo "Permanent link")\
\
Bases: `BaseModel`\
\
Defines authentication details for push notifications.\
\
#### `credentials = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationAuthenticationInfo.credentials "Permanent link")\
\
Optional credentials\
\
#### `schemes``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationAuthenticationInfo.schemes "Permanent link")\
\
Supported authentication schemes - e.g. Basic, Bearer\
\
### `PushNotificationConfig` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationConfig "Permanent link")\
\
Bases: `BaseModel`\
\
Configuration for setting up push notifications for task updates.\
\
#### `authentication = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationConfig.authentication "Permanent link")\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationConfig.id "Permanent link")\
\
Push Notification ID - created by server to support multiple callbacks\
\
#### `token = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationConfig.token "Permanent link")\
\
Token unique to this task/session.\
\
#### `url``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationConfig.url "Permanent link")\
\
URL for sending the push notifications.\
\
### `PushNotificationNotSupportedError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationNotSupportedError "Permanent link")\
\
Bases: `BaseModel`\
\
A2A specific error indicating the agent does not support push notifications.\
\
#### `code = -32003``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationNotSupportedError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationNotSupportedError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Push Notification is not supported'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.PushNotificationNotSupportedError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `Role` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Role "Permanent link")\
\
Bases: `str`, `Enum`\
\
Message sender's role\
\
#### `agent = 'agent'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Role.agent "Permanent link")\
\
#### `user = 'user'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Role.user "Permanent link")\
\
### `SecurityScheme` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SecurityScheme "Permanent link")\
\
Bases: `RootModel[APIKeySecurityScheme | HTTPAuthSecurityScheme | OAuth2SecurityScheme | OpenIdConnectSecurityScheme]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SecurityScheme.root "Permanent link")\
\
Mirrors the OpenAPI Security Scheme Object\
(https://swagger.io/specification/#security-scheme-object)\
\
### `SecuritySchemeBase` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SecuritySchemeBase "Permanent link")\
\
Bases: `BaseModel`\
\
Base properties shared by all security schemes.\
\
#### `description = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SecuritySchemeBase.description "Permanent link")\
\
Description of this security scheme.\
\
### `SendMessageRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageRequest "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC request model for the 'message/send' method.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageRequest.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageRequest.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `method = 'message/send'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageRequest.method "Permanent link")\
\
A String containing the name of the method to be invoked.\
\
#### `params``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageRequest.params "Permanent link")\
\
A Structured value that holds the parameter values to be used during the invocation of the method.\
\
### `SendMessageResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageResponse "Permanent link")\
\
Bases: `RootModel[JSONRPCErrorResponse | SendMessageSuccessResponse]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageResponse.root "Permanent link")\
\
JSON-RPC response model for the 'message/send' method.\
\
### `SendMessageSuccessResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageSuccessResponse "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC success response model for the 'message/send' method.\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageSuccessResponse.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageSuccessResponse.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `result``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendMessageSuccessResponse.result "Permanent link")\
\
The result object on success\
\
### `SendStreamingMessageRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageRequest "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC request model for the 'message/stream' method.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageRequest.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageRequest.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `method = 'message/stream'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageRequest.method "Permanent link")\
\
A String containing the name of the method to be invoked.\
\
#### `params``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageRequest.params "Permanent link")\
\
A Structured value that holds the parameter values to be used during the invocation of the method.\
\
### `SendStreamingMessageResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageResponse "Permanent link")\
\
Bases: `RootModel[JSONRPCErrorResponse | SendStreamingMessageSuccessResponse]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageResponse.root "Permanent link")\
\
JSON-RPC response model for the 'message/stream' method.\
\
### `SendStreamingMessageSuccessResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageSuccessResponse "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC success response model for the 'message/stream' method.\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageSuccessResponse.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageSuccessResponse.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `result``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SendStreamingMessageSuccessResponse.result "Permanent link")\
\
The result object on success\
\
### `SetTaskPushNotificationConfigRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigRequest "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC request model for the 'tasks/pushNotificationConfig/set' method.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigRequest.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigRequest.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `method = 'tasks/pushNotificationConfig/set'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigRequest.method "Permanent link")\
\
A String containing the name of the method to be invoked.\
\
#### `params``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigRequest.params "Permanent link")\
\
A Structured value that holds the parameter values to be used during the invocation of the method.\
\
### `SetTaskPushNotificationConfigResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigResponse "Permanent link")\
\
Bases: `RootModel[JSONRPCErrorResponse | SetTaskPushNotificationConfigSuccessResponse]`\
\
#### `root``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigResponse.root "Permanent link")\
\
JSON-RPC response for the 'tasks/pushNotificationConfig/set' method.\
\
### `SetTaskPushNotificationConfigSuccessResponse` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigSuccessResponse "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC success response model for the 'tasks/pushNotificationConfig/set' method.\
\
#### `id = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigSuccessResponse.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigSuccessResponse.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `result``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.SetTaskPushNotificationConfigSuccessResponse.result "Permanent link")\
\
The result object on success.\
\
### `Task` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Task "Permanent link")\
\
Bases: `BaseModel`\
\
#### `artifacts = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Task.artifacts "Permanent link")\
\
Collection of artifacts created by the agent.\
\
#### `contextId``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Task.contextId "Permanent link")\
\
Server-generated id for contextual alignment across interactions\
\
#### `history = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Task.history "Permanent link")\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Task.id "Permanent link")\
\
Unique identifier for the task\
\
#### `kind = 'task'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Task.kind "Permanent link")\
\
Event type\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Task.metadata "Permanent link")\
\
Extension metadata.\
\
#### `status``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.Task.status "Permanent link")\
\
Current status of the task\
\
### `TaskArtifactUpdateEvent` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskArtifactUpdateEvent "Permanent link")\
\
Bases: `BaseModel`\
\
Sent by server during sendStream or subscribe requests\
\
#### `append = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskArtifactUpdateEvent.append "Permanent link")\
\
Indicates if this artifact appends to a previous one\
\
#### `artifact``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskArtifactUpdateEvent.artifact "Permanent link")\
\
Generated artifact\
\
#### `contextId``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskArtifactUpdateEvent.contextId "Permanent link")\
\
The context the task is associated with\
\
#### `kind = 'artifact-update'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskArtifactUpdateEvent.kind "Permanent link")\
\
Event type\
\
#### `lastChunk = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskArtifactUpdateEvent.lastChunk "Permanent link")\
\
Indicates if this is the last chunk of the artifact\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskArtifactUpdateEvent.metadata "Permanent link")\
\
Extension metadata.\
\
#### `taskId``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskArtifactUpdateEvent.taskId "Permanent link")\
\
Task id\
\
### `TaskIdParams` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskIdParams "Permanent link")\
\
Bases: `BaseModel`\
\
Parameters containing only a task ID, used for simple task operations.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskIdParams.id "Permanent link")\
\
Task id.\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskIdParams.metadata "Permanent link")\
\
### `TaskNotCancelableError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskNotCancelableError "Permanent link")\
\
Bases: `BaseModel`\
\
A2A specific error indicating the task is in a state where it cannot be canceled.\
\
#### `code = -32002``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskNotCancelableError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskNotCancelableError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Task cannot be canceled'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskNotCancelableError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `TaskNotFoundError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskNotFoundError "Permanent link")\
\
Bases: `BaseModel`\
\
A2A specific error indicating the requested task ID was not found.\
\
#### `code = -32001``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskNotFoundError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskNotFoundError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'Task not found'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskNotFoundError.message "Permanent link")\
\
A String providing a short description of the error.\
\
### `TaskPushNotificationConfig` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskPushNotificationConfig "Permanent link")\
\
Bases: `BaseModel`\
\
Parameters for setting or getting push notification configuration for a task\
\
#### `pushNotificationConfig``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskPushNotificationConfig.pushNotificationConfig "Permanent link")\
\
Push notification configuration.\
\
#### `taskId``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskPushNotificationConfig.taskId "Permanent link")\
\
Task id.\
\
### `TaskQueryParams` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskQueryParams "Permanent link")\
\
Bases: `BaseModel`\
\
Parameters for querying a task, including optional history length.\
\
#### `historyLength = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskQueryParams.historyLength "Permanent link")\
\
Number of recent messages to be retrieved.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskQueryParams.id "Permanent link")\
\
Task id.\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskQueryParams.metadata "Permanent link")\
\
### `TaskResubscriptionRequest` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskResubscriptionRequest "Permanent link")\
\
Bases: `BaseModel`\
\
JSON-RPC request model for the 'tasks/resubscribe' method.\
\
#### `id``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskResubscriptionRequest.id "Permanent link")\
\
An identifier established by the Client that MUST contain a String, Number.\
Numbers SHOULD NOT contain fractional parts.\
\
#### `jsonrpc = '2.0'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskResubscriptionRequest.jsonrpc "Permanent link")\
\
Specifies the version of the JSON-RPC protocol. MUST be exactly "2.0".\
\
#### `method = 'tasks/resubscribe'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskResubscriptionRequest.method "Permanent link")\
\
A String containing the name of the method to be invoked.\
\
#### `params``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskResubscriptionRequest.params "Permanent link")\
\
A Structured value that holds the parameter values to be used during the invocation of the method.\
\
### `TaskState` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState "Permanent link")\
\
Bases: `str`, `Enum`\
\
Represents the possible states of a Task.\
\
#### `auth_required = 'auth-required'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState.auth_required "Permanent link")\
\
#### `canceled = 'canceled'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState.canceled "Permanent link")\
\
#### `completed = 'completed'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState.completed "Permanent link")\
\
#### `failed = 'failed'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState.failed "Permanent link")\
\
#### `input_required = 'input-required'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState.input_required "Permanent link")\
\
#### `rejected = 'rejected'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState.rejected "Permanent link")\
\
#### `submitted = 'submitted'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState.submitted "Permanent link")\
\
#### `unknown = 'unknown'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState.unknown "Permanent link")\
\
#### `working = 'working'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskState.working "Permanent link")\
\
### `TaskStatus` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatus "Permanent link")\
\
Bases: `BaseModel`\
\
TaskState and accompanying message.\
\
#### `message = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatus.message "Permanent link")\
\
Additional status updates for client\
\
#### `state``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatus.state "Permanent link")\
\
#### `timestamp = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatus.timestamp "Permanent link")\
\
ISO 8601 datetime string when the status was recorded.\
\
### `TaskStatusUpdateEvent` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatusUpdateEvent "Permanent link")\
\
Bases: `BaseModel`\
\
Sent by server during sendStream or subscribe requests\
\
#### `contextId``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatusUpdateEvent.contextId "Permanent link")\
\
The context the task is associated with\
\
#### `final``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatusUpdateEvent.final "Permanent link")\
\
Indicates the end of the event stream\
\
#### `kind = 'status-update'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatusUpdateEvent.kind "Permanent link")\
\
Event type\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatusUpdateEvent.metadata "Permanent link")\
\
Extension metadata.\
\
#### `status``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatusUpdateEvent.status "Permanent link")\
\
Current status of the task\
\
#### `taskId``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TaskStatusUpdateEvent.taskId "Permanent link")\
\
Task id\
\
### `TextPart` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TextPart "Permanent link")\
\
Bases: `BaseModel`\
\
Represents a text segment within parts.\
\
#### `kind = 'text'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TextPart.kind "Permanent link")\
\
Part type - text for TextParts\
\
#### `metadata = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TextPart.metadata "Permanent link")\
\
Optional metadata associated with the part.\
\
#### `text``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.TextPart.text "Permanent link")\
\
Text content\
\
### `UnsupportedOperationError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.UnsupportedOperationError "Permanent link")\
\
Bases: `BaseModel`\
\
A2A specific error indicating the requested operation is not supported by the agent.\
\
#### `code = -32004``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.UnsupportedOperationError.code "Permanent link")\
\
A Number that indicates the error type that occurred.\
\
#### `data = None``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.UnsupportedOperationError.data "Permanent link")\
\
A Primitive or Structured value that contains additional information about the error.\
This may be omitted.\
\
#### `message = 'This operation is not supported'``class-attribute``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.types.UnsupportedOperationError.message "Permanent link")\
\
A String providing a short description of the error.\
\
## `utils` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils "Permanent link")\
\
Utility functions for the A2A Python SDK.\
\
### `append_artifact_to_task(task, event)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.append_artifact_to_task "Permanent link")\
\
Helper method for updating a Task object with new artifact data from an event.\
\
Handles creating the artifacts list if it doesn't exist, adding new artifacts,\
and appending parts to existing artifacts based on the `append` flag in the event.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `task` | `Task` | The `Task` object to modify. | _required_ |\
| `event` | `TaskArtifactUpdateEvent` | The `TaskArtifactUpdateEvent` containing the artifact data. | _required_ |\
\
### `are_modalities_compatible(server_output_modes, client_output_modes)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.are_modalities_compatible "Permanent link")\
\
Checks if server and client output modalities (MIME types) are compatible.\
\
Modalities are compatible if:\
1\. The client specifies no preferred output modes (client\_output\_modes is None or empty).\
2\. The server specifies no supported output modes (server\_output\_modes is None or empty).\
3\. There is at least one common modality between the server's supported list and the client's preferred list.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `server_output_modes` | `list[str] | None` | A list of MIME types supported by the server/agent for output.<br>Can be None or empty if the server doesn't specify. | _required_ |\
| `client_output_modes` | `list[str] | None` | A list of MIME types preferred by the client for output.<br>Can be None or empty if the client accepts any. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `bool` | True if the modalities are compatible, False otherwise. |\
\
### `build_text_artifact(text, artifact_id)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.build_text_artifact "Permanent link")\
\
Helper to create a text artifact.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `text` | `str` | The text content for the artifact. | _required_ |\
| `artifact_id` | `str` | The ID for the artifact. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Artifact` | An `Artifact` object containing a single `TextPart`. |\
\
### `completed_task(task_id, context_id, artifacts, history=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.completed_task "Permanent link")\
\
Creates a Task object in the 'completed' state.\
\
Useful for constructing a final Task representation when the agent\
finishes and produces artifacts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `task_id` | `str` | The ID of the task. | _required_ |\
| `context_id` | `str` | The context ID of the task. | _required_ |\
| `artifacts` | `list[Artifact]` | A list of `Artifact` objects produced by the task. | _required_ |\
| `history` | `list[Message] | None` | An optional list of `Message` objects representing the task history. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A `Task` object with status set to 'completed'. |\
\
### `create_task_obj(message_send_params)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.create_task_obj "Permanent link")\
\
Create a new task object from message send params.\
\
Generates UUIDs for task and context IDs if they are not already present in the message.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `message_send_params` | `MessageSendParams` | The `MessageSendParams` object containing the initial message. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A new `Task` object initialized with 'submitted' status and the input message in history. |\
\
### `get_message_text(message, delimiter='\n')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.get_message_text "Permanent link")\
\
Extracts and joins all text content from a Message's parts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `message` | `Message` | The `Message` object. | _required_ |\
| `delimiter` | `str` | The string to use when joining text from multiple TextParts. | `'\n'` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `str` | A single string containing all text content, or an empty string if no text parts are found. |\
\
### `get_text_parts(parts)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.get_text_parts "Permanent link")\
\
Extracts text content from all TextPart objects in a list of Parts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | A list of `Part` objects. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `list[str]` | A list of strings containing the text content from any `TextPart` objects found. |\
\
### `new_agent_parts_message(parts, context_id=None, task_id=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.new_agent_parts_message "Permanent link")\
\
Creates a new agent message containing a list of Parts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | The list of `Part` objects for the message content. | _required_ |\
| `context_id` | `str | None` | The context ID for the message. | `None` |\
| `task_id` | `str | None` | The task ID for the message. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Message` | A new `Message` object with role 'agent'. |\
\
### `new_agent_text_message(text, context_id=None, task_id=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.new_agent_text_message "Permanent link")\
\
Creates a new agent message containing a single TextPart.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `text` | `str` | The text content of the message. | _required_ |\
| `context_id` | `str | None` | The context ID for the message. | `None` |\
| `task_id` | `str | None` | The task ID for the message. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Message` | A new `Message` object with role 'agent'. |\
\
### `new_artifact(parts, name, description='')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.new_artifact "Permanent link")\
\
Creates a new Artifact object.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | The list of `Part` objects forming the artifact's content. | _required_ |\
| `name` | `str` | The human-readable name of the artifact. | _required_ |\
| `description` | `str` | An optional description of the artifact. | `''` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Artifact` | A new `Artifact` object with a generated artifactId. |\
\
### `new_data_artifact(name, data, description='')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.new_data_artifact "Permanent link")\
\
Creates a new Artifact object containing only a single DataPart.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `name` | `str` | The human-readable name of the artifact. | _required_ |\
| `data` | `dict[str, Any]` | The structured data content of the artifact. | _required_ |\
| `description` | `str` | An optional description of the artifact. | `''` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Artifact` | A new `Artifact` object with a generated artifactId. |\
\
### `new_task(request)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.new_task "Permanent link")\
\
Creates a new Task object from an initial user message.\
\
Generates task and context IDs if not provided in the message.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `Message` | The initial `Message` object from the user. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A new `Task` object initialized with 'submitted' status and the input message in history. |\
\
### `new_text_artifact(name, text, description='')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.new_text_artifact "Permanent link")\
\
Creates a new Artifact object containing only a single TextPart.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `name` | `str` | The human-readable name of the artifact. | _required_ |\
| `text` | `str` | The text content of the artifact. | _required_ |\
| `description` | `str` | An optional description of the artifact. | `''` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Artifact` | A new `Artifact` object with a generated artifactId. |\
\
### `artifact` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.artifact "Permanent link")\
\
Utility functions for creating A2A Artifact objects.\
\
#### `new_artifact(parts, name, description='')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.artifact.new_artifact "Permanent link")\
\
Creates a new Artifact object.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | The list of `Part` objects forming the artifact's content. | _required_ |\
| `name` | `str` | The human-readable name of the artifact. | _required_ |\
| `description` | `str` | An optional description of the artifact. | `''` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Artifact` | A new `Artifact` object with a generated artifactId. |\
\
#### `new_data_artifact(name, data, description='')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.artifact.new_data_artifact "Permanent link")\
\
Creates a new Artifact object containing only a single DataPart.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `name` | `str` | The human-readable name of the artifact. | _required_ |\
| `data` | `dict[str, Any]` | The structured data content of the artifact. | _required_ |\
| `description` | `str` | An optional description of the artifact. | `''` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Artifact` | A new `Artifact` object with a generated artifactId. |\
\
#### `new_text_artifact(name, text, description='')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.artifact.new_text_artifact "Permanent link")\
\
Creates a new Artifact object containing only a single TextPart.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `name` | `str` | The human-readable name of the artifact. | _required_ |\
| `text` | `str` | The text content of the artifact. | _required_ |\
| `description` | `str` | An optional description of the artifact. | `''` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Artifact` | A new `Artifact` object with a generated artifactId. |\
\
### `errors` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.errors "Permanent link")\
\
Custom exceptions for A2A server-side errors.\
\
#### `A2AServerError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.errors.A2AServerError "Permanent link")\
\
Bases: `Exception`\
\
Base exception for A2A Server errors.\
\
#### `MethodNotImplementedError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.errors.MethodNotImplementedError "Permanent link")\
\
Bases: `A2AServerError`\
\
Exception raised for methods that are not implemented by the server handler.\
\
##### `message = message``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.errors.MethodNotImplementedError.message "Permanent link")\
\
#### `ServerError` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.errors.ServerError "Permanent link")\
\
Bases: `Exception`\
\
Wrapper exception for A2A or JSON-RPC errors originating from the server's logic.\
\
This exception is used internally by request handlers and other server components\
to signal a specific error that should be formatted as a JSON-RPC error response.\
\
##### `error = error``instance-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.errors.ServerError.error "Permanent link")\
\
### `helpers` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.helpers "Permanent link")\
\
General utility functions for the A2A Python SDK.\
\
#### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.helpers.logger "Permanent link")\
\
#### `append_artifact_to_task(task, event)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.helpers.append_artifact_to_task "Permanent link")\
\
Helper method for updating a Task object with new artifact data from an event.\
\
Handles creating the artifacts list if it doesn't exist, adding new artifacts,\
and appending parts to existing artifacts based on the `append` flag in the event.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `task` | `Task` | The `Task` object to modify. | _required_ |\
| `event` | `TaskArtifactUpdateEvent` | The `TaskArtifactUpdateEvent` containing the artifact data. | _required_ |\
\
#### `are_modalities_compatible(server_output_modes, client_output_modes)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.helpers.are_modalities_compatible "Permanent link")\
\
Checks if server and client output modalities (MIME types) are compatible.\
\
Modalities are compatible if:\
1\. The client specifies no preferred output modes (client\_output\_modes is None or empty).\
2\. The server specifies no supported output modes (server\_output\_modes is None or empty).\
3\. There is at least one common modality between the server's supported list and the client's preferred list.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `server_output_modes` | `list[str] | None` | A list of MIME types supported by the server/agent for output.<br>Can be None or empty if the server doesn't specify. | _required_ |\
| `client_output_modes` | `list[str] | None` | A list of MIME types preferred by the client for output.<br>Can be None or empty if the client accepts any. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `bool` | True if the modalities are compatible, False otherwise. |\
\
#### `build_text_artifact(text, artifact_id)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.helpers.build_text_artifact "Permanent link")\
\
Helper to create a text artifact.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `text` | `str` | The text content for the artifact. | _required_ |\
| `artifact_id` | `str` | The ID for the artifact. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Artifact` | An `Artifact` object containing a single `TextPart`. |\
\
#### `create_task_obj(message_send_params)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.helpers.create_task_obj "Permanent link")\
\
Create a new task object from message send params.\
\
Generates UUIDs for task and context IDs if they are not already present in the message.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `message_send_params` | `MessageSendParams` | The `MessageSendParams` object containing the initial message. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A new `Task` object initialized with 'submitted' status and the input message in history. |\
\
#### `validate(expression, error_message=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.helpers.validate "Permanent link")\
\
Decorator that validates if a given expression evaluates to True.\
\
Typically used on class methods to check capabilities or configuration\
before executing the method's logic. If the expression is False,\
a `ServerError` with an `UnsupportedOperationError` is raised.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `expression` | `Callable[[Any], bool]` | A callable that takes the instance ( `self`) as its argument<br>and returns a boolean. | _required_ |\
| `error_message` | `str | None` | An optional custom error message for the `UnsupportedOperationError`.<br>If None, the string representation of the expression will be used. | `None` |\
\
#### `validate_async_generator(expression, error_message=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.helpers.validate_async_generator "Permanent link")\
\
Decorator that validates if a given expression evaluates to True.\
\
Typically used on class methods to check capabilities or configuration\
before executing the method's logic. If the expression is False,\
a `ServerError` with an `UnsupportedOperationError` is raised.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `expression` | `Callable[[Any], bool]` | A callable that takes the instance ( `self`) as its argument<br>and returns a boolean. | _required_ |\
| `error_message` | `str | None` | An optional custom error message for the `UnsupportedOperationError`.<br>If None, the string representation of the expression will be used. | `None` |\
\
### `message` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.message "Permanent link")\
\
Utility functions for creating and handling A2A Message objects.\
\
#### `get_message_text(message, delimiter='\n')` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.message.get_message_text "Permanent link")\
\
Extracts and joins all text content from a Message's parts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `message` | `Message` | The `Message` object. | _required_ |\
| `delimiter` | `str` | The string to use when joining text from multiple TextParts. | `'\n'` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `str` | A single string containing all text content, or an empty string if no text parts are found. |\
\
#### `get_text_parts(parts)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.message.get_text_parts "Permanent link")\
\
Extracts text content from all TextPart objects in a list of Parts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | A list of `Part` objects. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `list[str]` | A list of strings containing the text content from any `TextPart` objects found. |\
\
#### `new_agent_parts_message(parts, context_id=None, task_id=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.message.new_agent_parts_message "Permanent link")\
\
Creates a new agent message containing a list of Parts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `parts` | `list[Part]` | The list of `Part` objects for the message content. | _required_ |\
| `context_id` | `str | None` | The context ID for the message. | `None` |\
| `task_id` | `str | None` | The task ID for the message. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Message` | A new `Message` object with role 'agent'. |\
\
#### `new_agent_text_message(text, context_id=None, task_id=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.message.new_agent_text_message "Permanent link")\
\
Creates a new agent message containing a single TextPart.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `text` | `str` | The text content of the message. | _required_ |\
| `context_id` | `str | None` | The context ID for the message. | `None` |\
| `task_id` | `str | None` | The task ID for the message. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Message` | A new `Message` object with role 'agent'. |\
\
### `proto_utils` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils "Permanent link")\
\
Utils for converting between proto and Python types.\
\
#### `FromProto` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto "Permanent link")\
\
Converts proto types to Python types.\
\
##### `agent_card(card)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.agent_card "Permanent link")\
\
##### `artifact(artifact)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.artifact "Permanent link")\
\
##### `authentication_info(info)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.authentication_info "Permanent link")\
\
##### `capabilities(capabilities)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.capabilities "Permanent link")\
\
##### `data(data)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.data "Permanent link")\
\
##### `file(file)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.file "Permanent link")\
\
##### `message(message)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.message "Permanent link")\
\
##### `message_send_configuration(config)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.message_send_configuration "Permanent link")\
\
##### `message_send_params(request)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.message_send_params "Permanent link")\
\
##### `metadata(metadata)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.metadata "Permanent link")\
\
##### `oauth2_flows(flows)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.oauth2_flows "Permanent link")\
\
##### `part(part)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.part "Permanent link")\
\
##### `provider(provider)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.provider "Permanent link")\
\
##### `push_notification_config(config)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.push_notification_config "Permanent link")\
\
##### `role(role)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.role "Permanent link")\
\
##### `security(security)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.security "Permanent link")\
\
##### `security_scheme(scheme)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.security_scheme "Permanent link")\
\
##### `security_schemes(schemes)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.security_schemes "Permanent link")\
\
##### `skill(skill)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.skill "Permanent link")\
\
##### `task(task)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.task "Permanent link")\
\
##### `task_artifact_update_event(event)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.task_artifact_update_event "Permanent link")\
\
##### `task_id_params(request)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.task_id_params "Permanent link")\
\
##### `task_push_notification_config(request)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.task_push_notification_config "Permanent link")\
\
##### `task_query_params(request)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.task_query_params "Permanent link")\
\
##### `task_state(state)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.task_state "Permanent link")\
\
##### `task_status(status)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.task_status "Permanent link")\
\
##### `task_status_update_event(event)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.FromProto.task_status_update_event "Permanent link")\
\
#### `ToProto` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto "Permanent link")\
\
Converts Python types to proto types.\
\
##### `agent_card(card)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.agent_card "Permanent link")\
\
##### `artifact(artifact)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.artifact "Permanent link")\
\
##### `authentication_info(info)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.authentication_info "Permanent link")\
\
##### `capabilities(capabilities)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.capabilities "Permanent link")\
\
##### `data(data)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.data "Permanent link")\
\
##### `file(file)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.file "Permanent link")\
\
##### `message(message)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.message "Permanent link")\
\
##### `message_send_configuration(config)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.message_send_configuration "Permanent link")\
\
##### `metadata(metadata)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.metadata "Permanent link")\
\
##### `oauth2_flows(flows)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.oauth2_flows "Permanent link")\
\
##### `part(part)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.part "Permanent link")\
\
##### `provider(provider)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.provider "Permanent link")\
\
##### `push_notification_config(config)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.push_notification_config "Permanent link")\
\
##### `role(role)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.role "Permanent link")\
\
##### `security(security)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.security "Permanent link")\
\
##### `security_scheme(scheme)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.security_scheme "Permanent link")\
\
##### `security_schemes(schemes)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.security_schemes "Permanent link")\
\
##### `skill(skill)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.skill "Permanent link")\
\
##### `stream_response(event)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.stream_response "Permanent link")\
\
##### `task(task)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.task "Permanent link")\
\
##### `task_artifact_update_event(event)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.task_artifact_update_event "Permanent link")\
\
##### `task_or_message(event)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.task_or_message "Permanent link")\
\
##### `task_push_notification_config(config)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.task_push_notification_config "Permanent link")\
\
##### `task_state(state)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.task_state "Permanent link")\
\
##### `task_status(status)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.task_status "Permanent link")\
\
##### `task_status_update_event(event)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.task_status_update_event "Permanent link")\
\
##### `update_event(event)``classmethod`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.proto_utils.ToProto.update_event "Permanent link")\
\
Converts a task, message, or task update event to a StreamResponse.\
\
### `task` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.task "Permanent link")\
\
Utility functions for creating A2A Task objects.\
\
#### `completed_task(task_id, context_id, artifacts, history=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.task.completed_task "Permanent link")\
\
Creates a Task object in the 'completed' state.\
\
Useful for constructing a final Task representation when the agent\
finishes and produces artifacts.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `task_id` | `str` | The ID of the task. | _required_ |\
| `context_id` | `str` | The context ID of the task. | _required_ |\
| `artifacts` | `list[Artifact]` | A list of `Artifact` objects produced by the task. | _required_ |\
| `history` | `list[Message] | None` | An optional list of `Message` objects representing the task history. | `None` |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A `Task` object with status set to 'completed'. |\
\
#### `new_task(request)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.task.new_task "Permanent link")\
\
Creates a new Task object from an initial user message.\
\
Generates task and context IDs if not provided in the message.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `request` | `Message` | The initial `Message` object from the user. | _required_ |\
\
Returns:\
\
| Type | Description |\
| --- | --- |\
| `Task` | A new `Task` object initialized with 'submitted' status and the input message in history. |\
\
### `telemetry` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.telemetry "Permanent link")\
\
OpenTelemetry Tracing Utilities for A2A Python SDK.\
\
This module provides decorators to simplify the integration of OpenTelemetry\
tracing into Python applications. It offers `trace_function` for instrumenting\
individual functions (both synchronous and asynchronous) and `trace_class`\
for instrumenting multiple methods within a class.\
\
The tracer is initialized with the module name and version defined by\
`INSTRUMENTING_MODULE_NAME` ('a2a-python-sdk') and\
`INSTRUMENTING_MODULE_VERSION` ('1.0.0').\
\
Features:\
\- Automatic span creation for decorated functions/methods.\
\- Support for both synchronous and asynchronous functions.\
\- Default span naming based on module and function/class/method name.\
\- Customizable span names, kinds, and static attributes.\
\- Dynamic attribute setting via an `attribute_extractor` callback.\
\- Automatic recording of exceptions and setting of span status.\
\- Selective method tracing in classes using include/exclude lists.\
\
Usage\
\
For a single function:\
\
```md-code__content\
from your_module import trace_function\
\
@trace_function\
def my_function():\
    # ...\
    pass\
\
@trace_function(span_name='custom.op', kind=SpanKind.CLIENT)\
async def my_async_function():\
    # ...\
    pass\
\
```\
\
For a class:\
\
```md-code__content\
from your_module import trace_class\
\
@trace_class(exclude_list=['internal_method'])\
class MyService:\
    def public_api(self, user_id):\
        # This method will be traced\
        pass\
\
    def internal_method(self):\
        # This method will not be traced\
        pass\
\
```\
\
#### `INSTRUMENTING_MODULE_NAME = 'a2a-python-sdk'``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.telemetry.INSTRUMENTING_MODULE_NAME "Permanent link")\
\
#### `INSTRUMENTING_MODULE_VERSION = '1.0.0'``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.telemetry.INSTRUMENTING_MODULE_VERSION "Permanent link")\
\
#### `SpanKind = _SpanKind``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.telemetry.SpanKind "Permanent link")\
\
#### `logger = logging.getLogger(__name__)``module-attribute`[¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.telemetry.logger "Permanent link")\
\
#### `trace_class(include_list=None, exclude_list=None, kind=SpanKind.INTERNAL)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.telemetry.trace_class "Permanent link")\
\
A class decorator to automatically trace specified methods of a class.\
\
This decorator iterates over the methods of a class and applies the\
`trace_function` decorator to them, based on the `include_list` and\
`exclude_list` criteria. Methods starting or ending with double underscores\
(dunder methods, e.g., `__init__`, `__call__`) are always excluded by default.\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `include_list` | `list[str]` | A list of method names to<br>explicitly include for tracing. If provided, only methods in this<br>list (that are not dunder methods) will be traced.<br>Defaults to None (trace all non-dunder methods). | `None` |\
| `exclude_list` | `list[str]` | A list of method names to exclude<br>from tracing. This is only considered if `include_list` is not<br>provided. Dunder methods are implicitly excluded.<br>Defaults to an empty list. | `None` |\
| `kind` | `SpanKind` | The `opentelemetry.trace.SpanKind` for the<br>created spans on the methods. Defaults to `SpanKind.INTERNAL`. | `INTERNAL` |\
\
Returns:\
\
| Name | Type | Description |\
| --- | --- | --- |\
| `callable` | `Callable` | A decorator function that, when applied to a class,<br>modifies the class to wrap its specified methods with tracing. |\
\
Example\
\
To trace all methods except 'internal\_method':\
\
```md-code__content\
@trace_class(exclude_list=['internal_method'])\
class MyService:\
    def public_api(self):\
        pass\
\
    def internal_method(self):\
        pass\
\
```\
\
To trace only 'method\_one' and 'method\_two':\
\
```md-code__content\
@trace_class(include_list=['method_one', 'method_two'])\
class AnotherService:\
    def method_one(self):\
        pass\
\
    def method_two(self):\
        pass\
\
    def not_traced_method(self):\
        pass\
\
```\
\
#### `trace_function(func=None, *, span_name=None, kind=SpanKind.INTERNAL, attributes=None, attribute_extractor=None)` [¶](https://a2aproject.github.io/A2A/latest/sdk/python/\#a2a.utils.telemetry.trace_function "Permanent link")\
\
A decorator to automatically trace a function call with OpenTelemetry.\
\
This decorator can be used to wrap both sync and async functions.\
When applied, it creates a new span for each call to the decorated function.\
The span will record the execution time, status (OK or ERROR), and any\
exceptions that occur.\
\
It can be used in two ways:\
\
1. As a direct decorator: `@trace_function`\
2. As a decorator factory to provide arguments: `@trace_function(span_name="custom.name")`\
\
Parameters:\
\
| Name | Type | Description | Default |\
| --- | --- | --- | --- |\
| `func` | `callable` | The function to be decorated. If None,<br>the decorator returns a partial function, allowing it to be called<br>with arguments. Defaults to None. | `None` |\
| `span_name` | `str` | Custom name for the span. If None,<br>it defaults to `f'{func.__module__}.{func.__name__}'`.<br>Defaults to None. | `None` |\
| `kind` | `SpanKind` | The `opentelemetry.trace.SpanKind` for the<br>created span. Defaults to `SpanKind.INTERNAL`. | `INTERNAL` |\
| `attributes` | `dict` | A dictionary of static attributes to be<br>set on the span. Keys are attribute names (str) and values are<br>the corresponding attribute values. Defaults to None. | `None` |\
| `attribute_extractor` | `callable` | A function that can be used<br>to dynamically extract and set attributes on the span.<br>It is called within a `finally` block, ensuring it runs even if<br>the decorated function raises an exception.<br>The function signature should be:<br>`attribute_extractor(span, args, kwargs, result, exception)`<br>where:<br>\- `span` : the OpenTelemetry `Span` object.<br>\- `args` : a tuple of positional arguments passed<br>\- `kwargs` : a dictionary of keyword arguments passed<br>\- `result` : return value (None if an exception occurred)<br>\- `exception` : exception object if raised (None otherwise).<br>Any exception raised by the `attribute_extractor` itself will be<br>caught and logged. Defaults to None. | `None` |\
\
Returns:\
\
| Name | Type | Description |\
| --- | --- | --- |\
| `callable` | `Callable` | The wrapped function that includes tracing, or a partial<br>decorator if `func` is None. |\
\
Back to top