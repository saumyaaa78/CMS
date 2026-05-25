from fastapi import APIRouter, UploadFile, File
from typing import List
from pathlib import Path
import shutil

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

UPLOAD_DIR = BASE_DIR / "temp_uploads"

UPLOAD_DIR.mkdir(exist_ok=True)

print("UPLOAD DIRECTORY:")
print(UPLOAD_DIR)


@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):

    print("UPLOAD REQUEST RECEIVED")

    uploaded_files = []

    for file in files:

        print("FILE:", file.filename)

        filename = file.filename or "unknown_file"
        save_path = UPLOAD_DIR / filename

        print("SAVING TO:")
        print(save_path)

        with open(save_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        uploaded_files.append({
            "filename": filename,
            "path": str(save_path)
        })

    print("UPLOAD COMPLETE")

    return {
        "message": "Files uploaded successfully",
        "total_files": len(uploaded_files),
        "files": uploaded_files
    }
