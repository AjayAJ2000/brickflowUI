# JobTrigger

## What It Does

Starts a Databricks job run from the UI.

## Signature

```python
db.JobTrigger(job_id: 'str', label: 'str' = 'Run Job', on_complete: 'Optional[Callable[[Dict[str, Any]], None]]' = None) -> 'VNode'
```

## Parameters

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `job_id` | `str` | `required` | |
| `label` | `str` | `'Run Job'` | |
| `on_complete` | `Optional[Callable[[Dict[str, Any]], None]]` | `None` | |

## Example

```python
import brickflowui as db

node = db.JobTrigger(job_id="job_id", label="Pipeline health")
```

## Integration Notes

- This component composes cleanly with layout primitives such as `Card`, `Grid`, `Row`, and `Column`.
- Prefer controlled state from Python when the value matters to your business logic or backend query layer.
