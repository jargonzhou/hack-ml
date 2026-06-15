from llama_index.core.tools import FunctionTool

from app.constants.db_prompt import sql_server_schema_prompt


def get_database_schema_hint() -> str:
  """Returns the pre-defined SQL Server schema definitions, functions, and stored procedures structures."""
  return sql_server_schema_prompt


sql_schema_tool = FunctionTool.from_defaults(
    fn=get_database_schema_hint,
    name="sql_server_schema_tool",
    description="Use this tool FIRST to inspect the database structure, tables, columns, views, functions, and stored procedures before writing any query."
)
