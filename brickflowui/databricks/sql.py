"""
Databricks SQL Connector helpers for BrickflowUI.

Provides a simple interface to execute SQL queries against a Databricks SQL warehouse,
using environment variables set by Databricks Apps or local .env files.
"""

from __future__ import annotations

import logging
import os
from contextlib import contextmanager
from typing import Any, Dict, List, Optional

logger = logging.getLogger("brickflowui.databricks.sql")

_connection = None


def _get_connection():
    """Get or create a cached connection to the Databricks SQL warehouse."""
    global _connection

    if _connection is not None:
        try:
            # Test if connection is still alive
            with _connection.cursor() as cur:
                cur.execute("SELECT 1")
            return _connection
        except Exception:
            _connection = None

    try:
        from databricks import sql as db_sql
    except ImportError:
        raise ImportError(
            "databricks-sql-connector is required for SQL integration. "
            "Install it with: pip install brickflowui[databricks]"
        )

    host = os.getenv("DATABRICKS_HOST", "").lstrip("https://")
    token = os.getenv("DATABRICKS_TOKEN") or os.getenv("DATABRICKS_OAUTH_TOKEN")
    http_path = os.getenv("DATABRICKS_WAREHOUSE_ID")

    if not host:
        raise ValueError("DATABRICKS_HOST environment variable is not set.")
    if not http_path:
        raise ValueError("DATABRICKS_WAREHOUSE_ID environment variable is not set.")

    # Normalize http_path: if it's just a warehouse ID, build the path
    if not http_path.startswith("/sql/"):
        http_path = f"/sql/1.0/warehouses/{http_path}"

    connect_args: Dict[str, Any] = {
        "server_hostname": host,
        "http_path": http_path,
    }

    if token:
        connect_args["access_token"] = token
    else:
        # Try Databricks SDK auth (OAuth, instance profiles, etc.)
        try:
            from databricks.sdk import WorkspaceClient
            w = WorkspaceClient()
            connect_args["credentials_provider"] = lambda: w.config.authenticate
        except Exception:
            raise ValueError(
                "No authentication found. Set DATABRICKS_TOKEN or configure Databricks SDK auth."
            )

    logger.info(f"Connecting to Databricks SQL warehouse at {host}")
    _connection = db_sql.connect(**connect_args)
    return _connection


def query(sql: str, params: Optional[List[Any]] = None) -> "Any":
    """
    Execute a SQL query and return results as a pandas DataFrame.

    Example:
        df = query("SELECT * FROM catalog.schema.table LIMIT 100")
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas is required. Install with: pip install brickflowui[databricks]")

    conn = _get_connection()
    with conn.cursor() as cur:
        cur.execute(sql, parameters=params)
        results = cur.fetchall()
        columns = [desc[0] for desc in cur.description] if cur.description else []
        return pd.DataFrame(results, columns=columns)


def execute(sql: str, params: Optional[List[Any]] = None) -> None:
    """
    Execute a non-returning SQL statement (INSERT, UPDATE, DELETE, etc.)

    Example:
        execute("UPDATE catalog.schema.table SET status = ? WHERE id = ?", ["active", 42])
    """
    conn = _get_connection()
    with conn.cursor() as cur:
        cur.execute(sql, parameters=params)


def query_to_records(sql: str, params: Optional[List[Any]] = None) -> List[Dict[str, Any]]:
    """
    Execute a SQL query and return results as a list of dicts (for Table component).

    Example:
        rows = query_to_records("SELECT id, name, status FROM my_table LIMIT 50")
        return db.Table(data=rows)
    """
    df = query(sql, params)
    return df.to_dict(orient="records")


@contextmanager
def transaction():
    """Context manager for a SQL transaction (commit on success, rollback on error)."""
    conn = _get_connection()
    try:
        yield conn
        conn.cursor().execute("COMMIT")
    except Exception:
        try:
            conn.cursor().execute("ROLLBACK")
        except Exception:
            pass
        raise
