import pandas as pd

def process_dataset(file_path):
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(
                file_path,
                encoding="utf-8"
            )

        elif file_path.endswith((".xlsx", ".xls")):
            df = pd.read_excel(
                file_path,
                engine="openpyxl"
            )
        else:

            return {
                "error": "Unsupported file type"
            }

        return {
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns)
        }

    except Exception as error:
        return {
            "error": str(error)
        }
